#!/usr/bin/env python3
"""
run-analyse — BC Extension Analysis orchestrator (collector → analyst → completeness referee).

Mirrors the run-build family, but there is no compiler and no code is changed: it analyses a
customer's AL extension and writes two documents (WIKI.md, PERFORMANCE_IMPROVEMENTS.md) into
the source folder. The deterministic collector (bc_collect.py) does the tool-loop the local
models fail at; the analyst model only reasons over the resulting facts pack + source.

Backends (ANALYST_BACKEND): `pi` (deepseek-r1 on Larry, read-only reasoning) or `claude`.
Claude is egress-gated via egress_policy — a customer folder defaults to `local-only`, so the
source never leaves for Anthropic unless policy allows. Escalation (ESCALATE_AFTER set) hands a
still-incomplete draft to Claude ONCE, and only where egress is permitted.

Usage:
  run-analyse.py --source <customer-folder>
Env: ANALYST_BACKEND=pi|claude (default pi), ANALYST_MODEL (default ollama/deepseek-r1:14b),
     ESCALATE_AFTER=1 (arm one Claude completion pass), EGRESS_POLICY / <folder>/.anon/config.yml.
"""
import json
import os
import re
import ssl
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bc_collect
import egress_policy

PI_BIN = (os.environ.get("PI_BIN") or __import__("shutil").which("pi")
          or os.path.expanduser("~/.npm-global/bin/pi"))
PI_EXT = os.path.expanduser(os.environ.get("PI_EXT", "~/.pi/ollama-provider.ts"))
CLAUDE_BIN = (os.environ.get("CLAUDE_BIN") or __import__("shutil").which("claude")
              or os.path.expanduser("~/.local/bin/claude"))
ANALYST_BACKEND = os.environ.get("ANALYST_BACKEND", "pi")
ANALYST_MODEL = os.environ.get("ANALYST_MODEL", "ollama/deepseek-r1:14b")
TIMEOUT = int(os.environ.get("ANALYST_TIMEOUT", "1800"))
OLLAMA_WARM_URL = os.environ.get("OLLAMA_WARM_URL",
                                 "https://larry.home.arpa:11443/v1/chat/completions")
PREWARM_KEEP_ALIVE = os.environ.get("PREWARM_KEEP_ALIVE", "2h")
# Soft cap so a big extension doesn't blow the local model's 32k context (chars, ~4/token).
SOURCE_CHAR_CAP = int(os.environ.get("ANALYST_SOURCE_CAP", "90000"))

_esc = os.environ.get("ESCALATE_AFTER", "").strip()
ESCALATE_AFTER = int(_esc) if _esc.isdigit() else None

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_FILE = os.environ.get("BC_ANALYSIS_PROMPT",
                             os.path.join(_REPO, "tooling", "bc-analysis.prompt.md"))


def strip_think(text):
    """Remove deepseek-r1 chain-of-thought so it never lands in the document."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"^.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)  # unclosed open
    text = text.strip()
    # Strip a whole-document markdown fence — leading and trailing handled independently,
    # since the model often emits the opening ```markdown but not a matching close.
    text = re.sub(r"^```(?:markdown|md)?[ \t]*\n", "", text)
    text = re.sub(r"\n```[ \t]*$", "", text)
    return text.strip()


def run_pi(prompt, model=ANALYST_MODEL, timeout=TIMEOUT):
    """One-shot pi, READ-ONLY (`-xt write,edit`) — the model reasons and returns text only."""
    # Prompt over STDIN, never argv. A source bundle is up to ANALYST_SOURCE_CAP (90k)
    # chars, which exceeds the OS argv limit and dies with
    #   OSError: [Errno 7] Argument list too long
    # — seen on a 38-file extension (95,612 chars). run-ingest.py already does it this
    # way; this path had not been run against a large enough extension to hit it.
    cmd = [PI_BIN, "-e", PI_EXT, "--model", model, "-p", "--no-session",
           # Analysis writes documentation, never code — grant read-only tools only.
           # A deny-list left Bash available in a flow whose whole premise is that the
           # customer's source is only READ.
           "--tools", "read,grep,find,ls"]
    print(f"  Running Pi analyst ({model})…")
    t = time.time()
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f"  Pi TIMEOUT after {timeout}s")
        return ""
    print(f"  Pi done in {time.time() - t:.0f}s (exit {r.returncode})")
    return (r.stdout or "").strip()


def run_claude(prompt, timeout=TIMEOUT):
    """One-shot Claude for text output — EGRESS-GATED (customer source stays local by default)."""
    ok, reason = egress_policy.allowed("anthropic")
    if not ok:
        print(f"  ⛔ Claude analyst BLOCKED — {reason}")
        return ""
    cmd = [CLAUDE_BIN, "-p"]          # prompt over stdin — see run_pi above (Errno 7)
    print("  Running Claude analyst…")
    t = time.time()
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f"  Claude TIMEOUT after {timeout}s")
        return ""
    print(f"  Claude done in {time.time() - t:.0f}s (exit {r.returncode})")
    return (r.stdout or "").strip()


def analyst(prompt, backend):
    return run_claude(prompt) if backend == "claude" else run_pi(prompt)


def prewarm(model):
    """Load the reasoner (long keep_alive) so a cold ROCm load doesn't eat the timeout. Fail-open."""
    if ANALYST_BACKEND != "pi":
        return
    m = model.split("/", 1)[-1]
    print(f"\n--- Pre-warming {m} ---")
    body = json.dumps({"model": m, "messages": [{"role": "user", "content": "ok"}],
                       "max_tokens": 1, "keep_alive": PREWARM_KEEP_ALIVE}).encode()
    req = urllib.request.Request(OLLAMA_WARM_URL, data=body, headers={
        "Content-Type": "application/json", "Authorization": "Bearer ollama"})
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    t = time.time()
    try:
        urllib.request.urlopen(req, timeout=480, context=ctx).read()
        print(f"  warm in {time.time() - t:.0f}s")
    except Exception as e:
        print(f"  pre-warm skipped ({e})")


# --- Completeness referee (replaces the compiler; reports gaps, does not change code) ---
# Each requirement is (label, [accepted aliases]) — present if ANY alias appears (case-insensitive).
WIKI_REQUIRED = [
    ("Overview", ["overview"]),
    ("Architecture", ["architecture"]),
    ("Business Process", ["business process", "process flow", "end-to-end"]),
    ("Job Queue", ["job queue"]),
    ("Configuration", ["configuration", "setup"]),
    ("Object Inventory", ["object inventory", "inventory"]),
]
PERF_REQUIRED = [
    ("N+1", ["n+1", "n + 1"]),
    ("Commit", ["commit"]),
    ("SetAutoCalcFields", ["setautocalcfields", "autocalc", "flowfield"]),
    ("Missing Index", ["missing index", "missing key", "setrange", "index"]),
    ("SetCurrentKey", ["setcurrentkey"]),
    ("HTTP Timeout", ["http timeout", "httpclient", "timeout"]),
    ("Job Queue", ["job queue", "onrun"]),
    ("UCI", ["universal code initiative", "uci"]),
    ("Priority Summary", ["priority summary", "priority table", "| severity", "priority"]),
]


def _missing(text, requirements):
    low = (text or "").lower()
    return [label for label, aliases in requirements if not any(a in low for a in aliases)]


def completeness(wiki, perf):
    return {"WIKI.md": _missing(wiki, WIKI_REQUIRED),
            "PERFORMANCE_IMPROVEMENTS.md": _missing(perf, PERF_REQUIRED)}


def build_prompt(instructions, facts, source, doc):
    which = ("WIKI.md — the technical wiki (all 9 required sections)" if doc == "WIKI"
             else "PERFORMANCE_IMPROVEMENTS.md — all 8 checks incl. the UCI compliance costing, "
                  "each finding using the finding template, ending with the Priority Summary table")
    return (
        "You are a Business Central / AL analyst producing a documentation deliverable. Follow the "
        f"ANALYSIS INSTRUCTIONS to produce **only {which}**.\n"
        "STRICT OUTPUT RULES:\n"
        "- Output ONLY the finished document as GitHub-flavoured markdown. No preamble ('Based on…', "
        "'It appears…'), no closing remarks, no fences around the whole document.\n"
        "- This is an ANALYSIS task. **Do NOT write, complete, fix, or continue any AL code** — even "
        "if a SOURCE snippet looks truncated. The SOURCE is provided only for you to read and describe.\n"
        "- Use EVERY required section/heading from the instructions, in order, even if a section is "
        "brief ('none found'). Do not collapse the structure into free-form prose.\n"
        "- Object IDs and the inventory in the FACTS PACK are authoritative — use them, never invent IDs. "
        "The greps in the FACTS PACK are already run; reason over them and the SOURCE.\n\n"
        f"===== ANALYSIS INSTRUCTIONS =====\n{instructions}\n\n"
        f"===== FACTS PACK (deterministic, authoritative) =====\n{facts}\n\n"
        f"===== SOURCE =====\n{source}\n")


def main():
    args = sys.argv[1:]
    if "--source" not in args:
        sys.exit("usage: run-analyse.py --source <customer-folder>")
    source = os.path.abspath(args[args.index("--source") + 1].rstrip("/"))
    if not os.path.isdir(source):
        sys.exit(f"ERROR: source folder not found: {source}")

    backend = ANALYST_BACKEND
    egress_policy.set_policy_for(source)
    egress_ok, egress_reason = egress_policy.allowed("anthropic")
    if backend == "claude" and not egress_ok:
        print(f"ERROR: ANALYST_BACKEND=claude but {egress_reason}. Use pi (Larry).")
        sys.exit(1)

    escalate = ESCALATE_AFTER
    print(f"Source: {source}")
    print(f"Analyst backend: {backend}" + (f" ({ANALYST_MODEL})" if backend == "pi" else " (Claude)"))
    print(f"Egress policy: {egress_policy.policy()}")
    if escalate is not None and backend == "pi":
        if not egress_ok:
            escalate = None
            print(f"Escalation: DISARMED by egress policy — {egress_reason}. Stays on Larry.")
        elif not os.path.exists(CLAUDE_BIN):
            print(f"Escalation: off (claude not found at {CLAUDE_BIN})")
            escalate = None
        else:
            print("Escalation: ARMED — Claude completes any gaps the local draft leaves (billed).")
    else:
        print("Escalation: off")

    if not os.path.exists(PROMPT_FILE):
        sys.exit(f"ERROR: analysis prompt not found: {PROMPT_FILE}")
    instructions = open(PROMPT_FILE, encoding="utf-8").read()

    print("\n--- Collecting (deterministic, no model) ---")
    # Claude has a big context; local models are ~32k → cap the bundle at whole-file boundaries.
    cap = None if backend == "claude" else SOURCE_CHAR_CAP
    data = bc_collect.collect(source, source_char_cap=cap)
    facts = data["facts_md"]
    src_bundle = data["source_bundle"]
    print(f"  {len(data['files'])} AL files, target={data['app'].get('target') or 'absent'}, "
          f"source bundle {len(src_bundle)} chars"
          + (f" (capped at {cap})" if cap else ""))

    if backend == "pi":
        prewarm(ANALYST_MODEL)

    docs = {}
    for doc, fname in [("WIKI", "WIKI.md"), ("PERF", "PERFORMANCE_IMPROVEMENTS.md")]:
        print(f"\n--- Analyst: {fname} ---")
        out = strip_think(analyst(build_prompt(instructions, facts, src_bundle, doc), backend))
        docs[fname] = out
        open(os.path.join(source, fname), "w", encoding="utf-8").write(out)
        print(f"  wrote {fname} ({len(out)} chars)")

    gaps = completeness(docs["WIKI.md"], docs["PERFORMANCE_IMPROVEMENTS.md"])
    _report(gaps)

    total_gaps = sum(len(v) for v in gaps.values())
    if total_gaps and escalate is not None and backend == "pi":
        print("\n=== ESCALATION — Claude completing gaps ===")
        for fname, missing in gaps.items():
            if not missing:
                continue
            doc = "WIKI" if fname == "WIKI.md" else "PERF"
            prompt = (build_prompt(instructions, facts, src_bundle, doc)
                      + f"\n\nThe previous draft was INCOMPLETE — missing: {', '.join(missing)}. "
                      "Produce the COMPLETE document.")
            out = strip_think(run_claude(prompt))
            if out:
                docs[fname] = out
                open(os.path.join(source, fname), "w", encoding="utf-8").write(out)
                print(f"  Claude rewrote {fname} ({len(out)} chars)")
        _report(completeness(docs["WIKI.md"], docs["PERFORMANCE_IMPROVEMENTS.md"]))

    print(f"\nDONE — WIKI.md + PERFORMANCE_IMPROVEMENTS.md in {source}")


def _report(gaps):
    total = sum(len(v) for v in gaps.values())
    if not total:
        print("\n  ✔ completeness: all required sections/checks present")
        return
    print("\n  ⚠ completeness gaps:")
    for fname, missing in gaps.items():
        if missing:
            print(f"    {fname}: missing {', '.join(missing)}")


if __name__ == "__main__":
    main()

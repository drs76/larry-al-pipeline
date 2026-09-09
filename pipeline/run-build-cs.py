#!/usr/bin/env python3
"""
Larry C# build orchestrator — Pi agent harness, local, free.

C#/.NET analogue of run-build-go.py, tuned for Azure Functions (isolated worker).
Same keep-best / no-regress fix loop and pi->Claude escalation; the referee is the
.NET toolchain.

Flow:
  1. Larry (Pi) writes files from the handover (larry-handover.prompt.md)
  2. Per round: dotnet format (apply), then dotnet build -> dotnet format
     --verify-no-changes (format gate) -> dotnet test (only if a test project exists).
     Toolchain = ground truth.
  3. Errors -> Larry (Pi) fixes -> re-run. Keep-best across up to MAX_FIX_ROUNDS.
  4. Escalation: after ESCALATE_AFTER rounds hand the rest to Claude Code (billed).
     OFF unless ESCALATE_AFTER=N is set.

Usage:
  python3 run-build-cs.py --project <root>   # target a .NET project/solution root
  python3 run-build-cs.py --project <root> --skip-larry    # fix existing files only
  python3 run-build-cs.py --project <root> --review-only   # just the referee loop

Model: env PI_CODER_MODEL (default ollama/ornith:35b). C# / Azure Functions rules
live in the handover. Expected files come from an optional 'machine-readable manifest'
block; if absent, "at least one .cs file exists" is the write gate.
"""

import sys
import os
import re
import time
import subprocess

import egress_policy   # deny-by-default Anthropic egress gate (anon hook §0)
import claude_egress   # policy-routed Claude execution (anon hook §5 — mirror under enterprise-anon)
import coder         # shared pi spawn: one implementation, three pipelines
import bonsai_vram   # Mode B GPU time-share: evict the Bonsai chat server before loading the coder

CODER_BACKEND = os.environ.get("CODER_BACKEND", "pi")

PI_BIN      = os.environ.get("PI_BIN") or __import__("shutil").which("pi") or os.path.expanduser("~/.npm-global/bin/pi")
PI_EXT      = os.path.expanduser("~/.pi/ollama-provider.ts")
CODER_MODEL = os.environ.get("PI_CODER_MODEL", "ollama/qwen3-coder:30b")  # ornith:35b broken (ROCm cold-load hang)

CLAUDE_BIN  = os.environ.get("CLAUDE_BIN") or __import__("shutil").which("claude") or os.path.expanduser("~/.local/bin/claude")
# Mid tier — cheap-cloud rung (OpenRouter) between Larry and Claude, egress-gated
# by egress_policy.allowed("openrouter"). See war-plans/mid-tier-routing/.
MID_EXT     = os.path.expanduser(os.environ.get("MID_EXT", "~/.pi/openrouter-provider.ts"))
MID_MODEL   = os.environ.get("MID_MODEL", "openrouter/deepseek/deepseek-chat")

MAX_WRITE_ATTEMPTS = 3
MAX_FIX_ROUNDS     = int(os.environ.get("MAX_FIX_ROUNDS", "8"))

_esc = os.environ.get("ESCALATE_AFTER", "").strip()
ESCALATE_AFTER = int(_esc) if _esc.isdigit() else None
# Mid-tier ladder: pi 0..M-1, mid M..N-1, Claude N+ (both one-way, M<N).
_escm = os.environ.get("ESCALATE_MID_AFTER", "").strip()
ESCALATE_MID_AFTER = int(_escm) if _escm.isdigit() else None
_coder_state = {"backend": CODER_BACKEND}

PROJECT_ROOT   = None
HANDOVER       = None
EXPECTED_FILES = []

PI_TIMEOUT = 3600
# Write phase gets a shorter budget so a stalled/looping coder (e.g. a slow
# reasoning model like ornith) fails fast and retries instead of burning the
# full PI_TIMEOUT × MAX_WRITE_ATTEMPTS. Real ornith writes were <=~700s.
WRITE_TIMEOUT = int(os.environ.get("PI_WRITE_TIMEOUT", "1200"))
_CODER_CFG = coder.CoderConfig(PI_BIN, PI_EXT, ["-p", "--mode", "json", "--no-session", "-a"],
                               include_stderr=False)

# Fix rounds get their own budget. They used to inherit PI_TIMEOUT (3600s) — the same as the
# bench harness RUN_TIMEOUT — so a stalled fix call could never hit its own timeout: the outer
# cap always killed the run first. Measured on the AL pipeline over 2197 fix calls: median 17s,
# p95 56s, p99 120s. 600s is 5x p99. Ported from run-build.py (ee96607).
FIX_TIMEOUT = int(os.environ.get("PI_FIX_TIMEOUT", "600"))
# MAX_FIX_ROUNDS x FIX_TIMEOUT still outlasts a 3600s harness cap, so bounding one call is not
# enough on its own.
MAX_FIX_TIMEOUTS = int(os.environ.get("PI_MAX_FIX_TIMEOUTS", "2"))
# Did the last coder call end on its timeout rather than by finishing? run_pi returns "" for
# both, and the write loop must tell them apart.


def wedged_write(produced, timed_out, attempt, max_attempts=None):
    """Is this write attempt a wedge worth abandoning rather than repeating?

    A wedge is the coder burning its ENTIRE timeout and producing NOTHING. Retrying
    reproduces it exactly: the 2026-08-29 go/cs suite lost b64forward to a full write
    timeout. Narrow on purpose — a timeout WITH partial output is a coder that ran and was
    cut off and does recover; nothing produced WITHOUT a timeout is a fast transient, which
    is the case retries exist for. Only the pair is hopeless. Ported from run-build.py.
    """
    n = MAX_WRITE_ATTEMPTS if max_attempts is None else max_attempts
    return produced == 0 and timed_out and attempt < n


# Review findings can be real but a one-shot fix may regress (a reasoning model's
# fix sometimes doesn't compile). Retry the review-fix a few times (revert-on-regress),
# then optionally escalate the fix to Claude if escalation is armed (ESCALATE_AFTER set).
REVIEW_FIX_ROUNDS = int(os.environ.get("PI_REVIEW_FIX_ROUNDS", "2"))

# Per-build metrics: one JSON line per run, same file the AL runner writes so
# build_leaderboard.py sees all languages. Pure instrumentation — fail-open.
METRICS_LOG = os.environ.get(
    "BUILD_METRICS", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".build-metrics.jsonl"))


def emit_metrics(rec):
    try:
        import json as _json, datetime as _dt
        rec = {"ts": _dt.datetime.now().strftime("%Y-%m-%dT%H:%M"), **rec}
        with open(METRICS_LOG, "a") as f:
            f.write(_json.dumps(rec) + "\n")
    except Exception as _e:
        print(f"  (metrics not written: {_e})")


# Directories excluded from source walks (build output, VCS, packages).
_SKIP_DIRS = {"bin", "obj", ".git", ".vs", "packages", "node_modules"}


def parse_manifest(handover_path):
    try:
        with open(handover_path) as f:
            text = f.read()
    except OSError:
        return []
    idx = text.lower().rfind("machine-readable manifest")
    if idx == -1:
        return []
    block = re.search(r"```[^\n]*\n(.*?)```", text[idx:], re.DOTALL)
    if not block:
        return []
    return [ln.strip() for ln in block.group(1).splitlines() if ln.strip().startswith("/")]


def configure_project(root):
    global PROJECT_ROOT, HANDOVER, EXPECTED_FILES
    PROJECT_ROOT = root.rstrip("/")
    HANDOVER     = PROJECT_ROOT + "/larry-handover.prompt.md"
    EXPECTED_FILES = parse_manifest(HANDOVER)
    print(f"Project: {PROJECT_ROOT}")
    if EXPECTED_FILES:
        print(f"  Expected files from manifest: {len(EXPECTED_FILES)}")
    else:
        print("  No manifest — write gate = '>=1 .cs file exists'.")
    print(f"  Egress policy: {egress_policy.set_policy_for(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Coder harness
# ---------------------------------------------------------------------------

def run_pi(prompt, label="Pi", model=CODER_MODEL, timeout=PI_TIMEOUT, ext=PI_EXT):
    """Delegates to coder.run_pi — one implementation for all three pipelines.

    Three copies of this function drifted apart and the drift cost real runs twice in
    one week (the stdin wedge, then three stall guards the AL pipeline alone had).
    The signature is unchanged so every existing call site still works."""
    return coder.run_pi(prompt, _CODER_CFG, PROJECT_ROOT, label=label,
                        model=model, timeout=timeout, ext=ext)


def run_claude_code(prompt, label="Claude", timeout=PI_TIMEOUT):
    """Run Claude Code headless (one-shot), billed against the subscription.

    Phase 5: routed through claude_egress — under enterprise-anon Claude runs in
    a scrubbed mirror and its diff is reverse-mapped back; local-only blocks."""
    return claude_egress.run_claude(PROJECT_ROOT, prompt, CLAUDE_BIN,
                                    label=label, timeout=timeout)


def run_mid(prompt, label="Mid", timeout=PI_TIMEOUT):
    """Cheap-cloud MID tier (OpenRouter via pi). Gated PER CALL by
    egress_policy.allowed('openrouter') — a blocked policy returns "" and does no
    network I/O, so customer code can never leak even by an unexpected path."""
    ok, reason = egress_policy.allowed("openrouter")
    if not ok:
        print(f"  ⛔ Mid tier BLOCKED ({label}) — {reason}")
        return ""
    print(f"  Running mid tier ({label}, {MID_MODEL})...")
    return run_pi(prompt, label, model=MID_MODEL, timeout=timeout, ext=MID_EXT)


def run_coder(prompt, label, timeout=PI_TIMEOUT):
    # Cleared per call; set only by a backend that detects its own
    # timeout, so a backend that reports none reads as "did not time out".
    coder.LAST["timed_out"] = False
    if _coder_state["backend"] == "mid":
        return run_mid(prompt, label, timeout=timeout)
    if _coder_state["backend"] == "claude":
        return run_claude_code(prompt, label, timeout=timeout)
    return run_pi(prompt, label, timeout=timeout)


# ---------------------------------------------------------------------------
# Project helpers
# ---------------------------------------------------------------------------

def _walk(exts):
    out = []
    for dp, dirs, fs in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in _SKIP_DIRS]
        for fn in fs:
            if fn.endswith(exts):
                out.append(os.path.join(dp, fn))
    return out


def cs_files():
    return _walk((".cs",))


def project_files():
    return _walk((".cs", ".csproj", ".sln", ".fs", ".fsproj"))


def has_test_project():
    """A csproj that references the test SDK, or is named *Test(s)*."""
    for p in _walk((".csproj",)):
        name = os.path.basename(p)
        if re.search(r"tests?", name, re.I):
            return True
        try:
            if "Microsoft.NET.Test.Sdk" in open(p).read():
                return True
        except OSError:
            pass
    return False


def get_project_file_listing():
    rel = sorted(os.path.relpath(f, PROJECT_ROOT) for f in _walk((".cs", ".csproj", ".sln")))
    return "\n".join(f"  {r}" for r in rel) if rel else "  (no source files yet)"


def read_handover():
    with open(HANDOVER) as f:
        return f.read()


def write_gate_met():
    if EXPECTED_FILES:
        written = sum(1 for f in EXPECTED_FILES if os.path.exists(f))
        print(f"  Wrote {written}/{len(EXPECTED_FILES)} expected files.")
        return written >= max(1, len(EXPECTED_FILES) // 2)
    n = len(cs_files())
    print(f"  {n} .cs file(s) present.")
    return n >= 1


# ---------------------------------------------------------------------------
# Toolchain wrappers
# ---------------------------------------------------------------------------

def _dotnet(args, timeout=1200):
    r = subprocess.run(["dotnet"] + args, cwd=PROJECT_ROOT,
                       capture_output=True, text=True, timeout=timeout)
    return (r.stdout + r.stderr).strip(), r.returncode == 0


def normalize_cs():
    """Deterministic pre-referee fix: apply dotnet format (whitespace/style/analyzers)."""
    out, ok = _dotnet(["format", "--no-restore"])
    print("  dotnet format applied" if ok else "  dotnet format deferred (project not yet buildable)")


# ---------------------------------------------------------------------------
# Referee: dotnet build -> format gate -> dotnet test
# ---------------------------------------------------------------------------

def run_referee():
    """dotnet build ; if ok, dotnet format --verify-no-changes (format GATE) ;
    if a test project exists, dotnet test. Returns (report, passed, score)."""
    print("\n--- .NET referee ---")
    normalize_cs()

    build_out, build_ok = _dotnet(["build", "--nologo"])
    print(f"  dotnet build: {'PASS' if build_ok else 'FAIL'}")

    fmt_out, fmt_ok = "", True
    test_out, test_ok, tested = "", True, False
    if build_ok:
        fmt_out, fmt_ok = _dotnet(["format", "--verify-no-changes", "--no-restore"])
        print(f"  format gate:  {'PASS' if fmt_ok else 'FAIL'}")
        if has_test_project():
            tested = True
            test_out, test_ok = _dotnet(["test", "--nologo", "--no-build"])
            if not test_ok:  # --no-build can miss a test-only build; retry building
                test_out, test_ok = _dotnet(["test", "--nologo"])
            print(f"  dotnet test:  {'PASS' if test_ok else 'FAIL'}")

    build_errs = len(re.findall(r":\s*error\s+\w+\d+:", build_out)) or (0 if build_ok else 1)
    test_fails = 0 if test_ok else (len(re.findall(r"Failed!", test_out)) or 1)
    score = build_errs * 1000 + (0 if fmt_ok else 100) + test_fails

    passed = build_ok and fmt_ok and test_ok
    parts = [f"BUILD: {'PASS' if build_ok else 'FAIL'}", build_out]
    if build_ok:
        parts += [f"\nFORMAT GATE: {'PASS' if fmt_ok else 'FAIL'}",
                  "" if fmt_ok else "Run 'dotnet format' — code is not formatting-clean:\n" + fmt_out]
        if tested:
            parts += [f"\nTEST: {'PASS' if test_ok else 'FAIL'}", test_out]
    report = "\n".join(p for p in parts if p.strip())

    if not passed:
        for line in report.splitlines():
            if line.strip():
                print(f"  {line}")
    return report, passed, score


def truncate_referee(text, max_lines=25):
    """Dedupe/cap toolchain output. MSBuild repeats each error once per referencing
    project; collapse identical messages (strip file/line prefix)."""
    seen, order = {}, []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        key = re.sub(r"^.*?[/\\][^/\\]+\.\w+\(\d+,\d+\):\s*", "", s)  # strip path(line,col):
        key = re.sub(r"\s*\[[^\]]*\.csproj\]\s*$", "", key)          # strip [proj.csproj]
        if key not in seen:
            seen[key] = s
            order.append(key)
    head = [seen[k] for k in order[:max_lines]]
    extra = len(order) - len(head)
    if extra > 0:
        head.append(f"... (+{extra} more distinct lines, omitted)")
    return "\n".join(head)


# ---------------------------------------------------------------------------
# Snapshot / restore for no-regress
# ---------------------------------------------------------------------------

def snapshot_src():
    return {f: open(f).read() for f in project_files()}


def restore_src(snap):
    # remove files created after the snapshot, then restore snapshot contents
    current = set(project_files())
    for f in current - set(snap):
        try:
            os.remove(f)
        except OSError:
            pass
    for p, content in snap.items():
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(content)


def build_fix_msg(findings):
    listing = get_project_file_listing()
    return (
        f"Project root: {PROJECT_ROOT}/ (.NET / Azure Functions isolated worker)\n\n"
        f"Current source files:\n{listing}\n\n"
        f"---\n\n"
        f"The .NET toolchain reported these problems that must be fixed:\n\n"
        f"{findings}\n\n"
        f"---\n\n"
        f"Instructions:\n"
        f"- Read the affected file(s) and fix ONLY the listed issues, then write them back.\n"
        f"- 'error CSxxxx' are compile errors; a FORMAT GATE failure means run/obey dotnet format "
        f"(fix whitespace, usings ordering, braces); 'Failed!' lines are failing tests.\n"
        f"- Do NOT delete files or change files with no issues. Do NOT add features beyond the fix.\n"
        f"After editing, the pipeline re-runs dotnet build / format / test."
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass
    t0 = time.time()
    args = sys.argv[1:]
    skip_larry  = "--skip-larry"  in args
    review_only = "--review-only" in args
    review_peer = "--review"      in args   # validator-peer behaviour review after PASS

    if "--project" not in args:
        print("ERROR: --project <root> is required.")
        sys.exit(1)
    i = args.index("--project")
    if i + 1 >= len(args):
        print("ERROR: --project requires a path argument.")
        sys.exit(1)
    configure_project(args[i + 1])

    if not os.path.isdir(PROJECT_ROOT):
        print(f"ERROR: project root not found: {PROJECT_ROOT}")
        sys.exit(1)
    if not _walk((".csproj", ".sln", ".fsproj")):
        print(f"ERROR: no .csproj/.sln in {PROJECT_ROOT} (run 'csw new' first).")
        sys.exit(1)
    if not (skip_larry or review_only) and not os.path.exists(HANDOVER):
        print(f"ERROR: no handover at {HANDOVER}")
        sys.exit(1)

    backend_bin = CLAUDE_BIN if CODER_BACKEND == "claude" else PI_BIN
    if not os.path.exists(backend_bin):
        print(f"ERROR: coder backend '{CODER_BACKEND}' not found at {backend_bin}.")
        sys.exit(1)
    egress_ok, egress_reason = egress_policy.escalation_available()
    if CODER_BACKEND == "claude" and not egress_ok:
        print(f"ERROR: CODER_BACKEND=claude but {egress_reason}. Use CODER_BACKEND=pi (Larry).")
        sys.exit(1)
    print(f"Coder backend: {CODER_BACKEND}" +
          (f" ({CODER_MODEL})" if CODER_BACKEND == "pi" else " (Claude Code)"))
    if CODER_BACKEND == "pi":
        # Mode B: free the GPU from the Bonsai chat server (bonsai-context.md).
        # Falls back to the dashboard API on client boxes, where the Larry-local
        # `bonsai` CLI does not exist and this previously no-opped in silence.
        bonsai_vram.free_bonsai_vram_once()
    if ESCALATE_AFTER is not None and CODER_BACKEND == "pi":
        if not egress_ok:
            globals()["ESCALATE_AFTER"] = None   # policy forbids egress: never latch to Claude
            print(f"Escalation: DISARMED by egress policy — {egress_reason}. Build stays on Larry.")
        elif not os.path.exists(CLAUDE_BIN):
            print(f"ERROR: ESCALATE_AFTER set but Claude bin not found at {CLAUDE_BIN}.")
            sys.exit(1)
        else:
            print(f"Escalation: ARMED — pi does {ESCALATE_AFTER} fix round(s), then Claude Code closes (billed).")
    else:
        print("Escalation: off (set ESCALATE_AFTER=N to auto-hand stalled builds to Claude).")

    # Mid-tier arming — disarmed unless the policy permits openrouter, and requires
    # ESCALATE_MID_AFTER < ESCALATE_AFTER (else the ladder inverts).
    if ESCALATE_MID_AFTER is not None and CODER_BACKEND == "pi":
        mid_ok, mid_reason = egress_policy.mid_available()
        if not mid_ok:
            globals()["ESCALATE_MID_AFTER"] = None
            print(f"Mid tier: DISARMED by egress policy — {mid_reason}. Build stays on Larry.")
        elif ESCALATE_AFTER is not None and ESCALATE_MID_AFTER >= ESCALATE_AFTER:
            globals()["ESCALATE_MID_AFTER"] = None
            print(f"Mid tier: DISARMED — ESCALATE_MID_AFTER ({_escm}) must be < ESCALATE_AFTER ({ESCALATE_AFTER}).")
        else:
            print(f"Mid tier: ARMED — pi does {ESCALATE_MID_AFTER} round(s), then {MID_MODEL} "
                  f"(cloud-billed via OpenRouter)" +
                  (f", then Claude at round {ESCALATE_AFTER}." if ESCALATE_AFTER is not None
                   else " (no Claude rung — pi→mid→stop)."))

    # ---- Write phase -------------------------------------------------------
    if not skip_larry and not review_only:
        handover_text = read_handover()
        ok = False
        for attempt in range(1, MAX_WRITE_ATTEMPTS + 1):
            print(f"\n--- Larry: writing files (attempt {attempt}) ---")
            run_coder(handover_text, label="Larry-write", timeout=WRITE_TIMEOUT)
            if write_gate_met():
                ok = True
                break
            if wedged_write(len([f for f in EXPECTED_FILES if os.path.exists(f)]) if EXPECTED_FILES else len(cs_files()), coder.LAST["timed_out"], attempt):
                print(f"  Coder hit the full {WRITE_TIMEOUT}s timeout and produced "
                      f"nothing — wedged, not slow. Abandoning after attempt {attempt} "
                      f"of {MAX_WRITE_ATTEMPTS} rather than repeating it.")
                break
            print("  Write gate not met. Retrying...")
        if not ok:
            print(f"\nERROR: Larry failed to write files after {MAX_WRITE_ATTEMPTS} attempts.")
            sys.exit(1)

    # ---- Fix loop (keep-best / no-regress) ---------------------------------
    best = {"score": None, "snap": None, "report": "", "findings": "", "passed": False}

    # leaderboard metrics (mirrors run-build.py)
    first_pass_ok = None
    passed_round = None
    escalated = False
    mid_escalated = False
    regressions = 0

    for fix_round in range(MAX_FIX_ROUNDS + 1):
        label = "initial build" if fix_round == 0 else f"fix round {fix_round}"
        print(f"\n=== {label.upper()} ===")

        report, passed, score = run_referee()
        if fix_round == 0:
            first_pass_ok = passed
        elif best["score"] is not None and score > best["score"]:
            regressions += 1
        print(f"  score: {score}" + (f"  (best: {best['score']})" if best["score"] is not None else ""))
        findings = truncate_referee(report) if not passed else ""

        if best["score"] is None or score < best["score"]:
            best = {"score": score, "snap": snapshot_src(), "report": report,
                    "findings": findings, "passed": passed}
            print(f"  ★ new best (score {score})")

        if passed:
            passed_round = fix_round
            break
        if fix_round >= MAX_FIX_ROUNDS:
            print(f"\n  Max fix rounds ({MAX_FIX_ROUNDS}) reached.")
            break
        if coder.FIX_TIMEOUT_STREAK["n"] >= MAX_FIX_TIMEOUTS:
            print(f"\n  {coder.FIX_TIMEOUT_STREAK['n']} consecutive fix calls hit the full "
                  f"{FIX_TIMEOUT}s timeout — abandoning the fix loop; best is kept.")
            break

        if score > best["score"]:
            print(f"  Round regressed ({score} > best {best['score']}) — reverting before fixing.")
            restore_src(best["snap"])
            fix_findings = best["findings"]
        else:
            fix_findings = findings

        if (ESCALATE_AFTER is not None and _coder_state["backend"] in ("pi", "mid")
                and fix_round >= ESCALATE_AFTER):
            _coder_state["backend"] = "claude"
            escalated = True
            print(f"\n  ⚠ ESCALATION: {fix_round} round(s) without a pass — Claude Code closes (billed).")
        elif (ESCALATE_MID_AFTER is not None and _coder_state["backend"] == "pi"
                and fix_round >= ESCALATE_MID_AFTER):
            _coder_state["backend"] = "mid"
            mid_escalated = True
            print(f"\n  ⚠ MID ESCALATION: {fix_round} pi round(s) without a pass — "
                  f"mid tier ({MID_MODEL}, cloud-billed) closes next.")

        who = "Claude" if _coder_state["backend"] == "claude" else "Larry (Pi)"
        print(f"\n--- {who}: fixing issues (round {fix_round + 1}) ---")
        run_coder(build_fix_msg(fix_findings), label=f"{who}-fix", timeout=FIX_TIMEOUT)

    if best["snap"]:
        restore_src(best["snap"])

    # ---- Validator-peer review (optional; only meaningful once referee passes) ---
    if review_peer and best["passed"]:
        print("\n=== VALIDATOR-PEER REVIEW (coms) ===")
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import coms_review
            intent = read_handover() if os.path.exists(HANDOVER) else "(no handover)"
            files = [(os.path.relpath(f, PROJECT_ROOT), open(f).read()) for f in cs_files()]
            proj_name = os.path.basename(PROJECT_ROOT) + "-review"
            findings, clean = coms_review.review(
                proj_name, intent, files,
                validator_model=os.environ.get("COMS_VALIDATOR_MODEL", CODER_MODEL),
                relay_model=os.environ.get("COMS_RELAY_MODEL", CODER_MODEL))
            if clean:
                print("  validator: REVIEW COMPLETE (no behaviour findings)")
            else:
                print("  validator findings:\n" + "\n".join("    " + l for l in findings.splitlines()))
                pre_review = best["snap"]   # known-good passing state to revert to
                fixed = False
                backends = ["pi"] * REVIEW_FIX_ROUNDS
                if ESCALATE_AFTER is not None and os.path.exists(CLAUDE_BIN):
                    backends.append("claude")
                for rf, backend in enumerate(backends):
                    who = "Claude" if backend == "claude" else "Larry (Pi)"
                    print(f"\n--- {who}: fixing review findings (round {rf + 1}/{len(backends)}) ---")
                    if backend == "claude":
                        run_claude_code(build_fix_msg(findings), label="Claude-review-fix")
                    else:
                        run_coder(build_fix_msg(findings), label="Larry-review-fix", timeout=FIX_TIMEOUT)
                    report, passed, score = run_referee()
                    if passed:
                        best = {"score": score, "snap": snapshot_src(), "report": report,
                                "findings": "", "passed": True}
                        print("  review fix applied; referee still PASS")
                        fixed = True
                        break
                    print(f"  review-fix round {rf + 1} regressed the referee — reverting.")
                    if pre_review:
                        restore_src(pre_review)
                if not fixed:
                    print("  review findings not landed cleanly — kept the pre-review passing build.")
        except Exception as e:
            print(f"  review skipped (error: {e})")

    print("\n" + "=" * 60)
    print(f"FINAL REPORT (best round — score {best['score']})")
    print("=" * 60)
    print(best["report"])
    print("=" * 60)

    emit_metrics({
        "project": os.path.basename(PROJECT_ROOT),
        "lang": "cs",
        "coder_backend": CODER_BACKEND,
        "coder_model": CODER_MODEL if CODER_BACKEND == "pi" else "claude-code",
        "duration_s": int(time.time() - t0),
        "first_pass_compile": first_pass_ok,
        "final_compile": best["passed"],
        "autonomous_pass": best["passed"] and not escalated and not mid_escalated,
        "mid_closed": best["passed"] and mid_escalated and not escalated,
        "fix_rounds": passed_round,
        "max_fix_rounds": MAX_FIX_ROUNDS,
        "regressions": regressions,
        "claude_escalated": escalated,
        "mid_escalated": mid_escalated,
        "files_expected": len(EXPECTED_FILES),
        "files_written": sum(1 for f in EXPECTED_FILES if os.path.exists(f)),
    })

    if best["passed"]:
        print("\nRESULT: PASS")
    else:
        print(f"\nRESULT: FAIL (best score {best['score']})")
        sys.exit(1)


if __name__ == "__main__":
    main()

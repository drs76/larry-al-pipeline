#!/usr/bin/env python3
"""
coms_review — validator-peer code review over pi's coms (peer-to-peer) extension.

Boots a persistent VALIDATOR pi agent (a different model, for ensemble diversity)
into a project's coms pool, then runs a headless RELAY agent that coms_sends the
changed source + the handover intent and coms_awaits the validator's findings.
Findings are behaviour/spec bugs the toolchain referee (build/vet/test) cannot see
— the automated form of the manual "Claude review" step.

Used by run-build-go.py / run-build-cs.py when invoked with --review.
Requires the coms extension installed at ~/.pi/coms.ts (see COMS.md).

Env:
  COMS_VALIDATOR_MODEL  default ollama/qwen2.5-coder:14b  (reviewer; MUST differ from
                        the coder — run-build refuses to call a same-model review
                        "independent". 32b was documented here but is not pulled on
                        Larry, and run-build separately defaulted this to CODER_MODEL,
                        so the advertised diversity did not exist either way.)
  COMS_RELAY_MODEL      default ollama/qwen3-coder:30b    (sends/awaits; relay only,
                        not the reviewer — same model as the coder is fine here)
  PI_COMS_REVIEW_TIMEOUT  seconds, default 420
"""
import os, time, threading, subprocess, re

# pty/fcntl/termios/select are POSIX-only. They exist purely to hold a *persistent
# interactive* validator agent open so the relay can coms_send to it. Windows has
# none of them, and importing this module at all used to raise ModuleNotFoundError
# there — which is why `--review` was unavailable on Windows. See review() for the
# headless path used when there is no pty.
_HAVE_PTY = os.name != "nt"
if _HAVE_PTY:
    import pty, struct, fcntl, termios, select

PI    = (os.environ.get("PI_BIN") or __import__("shutil").which("pi")
         or os.path.expanduser("~/.npm-global/bin/pi"))
OLLAMA = os.path.expanduser("~/.pi/ollama-provider.ts")
COMS   = os.path.expanduser("~/.pi/coms.ts")

VALIDATOR_MODEL = os.environ.get("COMS_VALIDATOR_MODEL", "ollama/qwen3-coder:30b")
RELAY_MODEL     = os.environ.get("COMS_RELAY_MODEL", "ollama/qwen3-coder:30b")
REVIEW_TIMEOUT  = int(os.environ.get("PI_COMS_REVIEW_TIMEOUT", "420"))

REVIEW_PURPOSE = (
    "You are a code reviewer. When you receive a review request, reply with a short findings "
    "list — behaviour/spec bugs a compiler cannot catch (dead keybindings, unhandled cases, "
    "handlers defined but never called, logic that contradicts the stated intent). One bullet "
    "per finding as 'file: issue'. If the code correctly matches the intent, reply exactly "
    "REVIEW COMPLETE. Be terse; do not restate the code."
)


def _classify_findings(text):
    """Decide whether a validator reply is 'clean' (no fix round) or real findings.

    Clean when: empty/whitespace, or it says REVIEW COMPLETE, or it has no actionable
    finding markers (no bullet lines, no source-file references). Only a substantive
    finding — a bullet or a mention of a .go/.cs/.al/.csproj file — triggers a fix round.
    This avoids needless fix rounds on empty/flaky/vague reviewer replies.
    """
    f = (text or "").strip()
    if not f:
        return "(empty review — treated as clean)", True
    if "REVIEW COMPLETE" in f.upper():
        return f, True
    finding_like = any(
        ln.strip().startswith(("-", "*", "•")) or re.search(r"\.(al|cs|go|csproj|razor|ts|js)\b", ln)
        for ln in f.splitlines()
    )
    if not finding_like:
        return f, True   # vague chatter ("looks fine", "no issues") — not actionable
    return f, False


def _build_request(intent, files, knowledge_rules=None):
    """The review request itself — identical on both transports."""
    code_block = "\n\n".join(f"=== {p} ===\n{c}" for p, c in files)
    rules_block = ""
    if knowledge_rules:
        try:
            import bcquality
            checklist = bcquality.format_checklist(knowledge_rules)
        except Exception:
            checklist = ""
        if checklist:
            rules_block = (
                "\n\nAlso check the code against these curated BC/AL rules (BCQuality). "
                "For each rule the code violates, add a bullet 'file: issue [rule: <path>]' "
                "citing the rule path. Ignore rules the code does not touch.\n"
                f"RULES:\n{checklist}")
    return (f"Review this code against the stated intent. Report ONLY behaviour/spec bugs a "
            f"compiler cannot catch, as short 'file: issue' bullets. If it correctly matches "
            f"the intent and violates none of the rules, reply exactly REVIEW COMPLETE."
            f"\n\nINTENT:\n{intent}\n\nCODE:\n{code_block}{rules_block}")


def _review_headless(intent, files, timeout, vmodel, knowledge_rules=None):
    """Windows path: ask the validator model directly, one shot, no coms transport.

    The peer-to-peer round-trip buys bidirectional chat between persistent agents;
    a review is a single request/response, so on a host without a pty we skip the
    transport rather than emulate a TUI over ConPTY. Everything that actually
    matters is preserved: a *different* model than the coder (ensemble diversity),
    the same request text, and the same _classify_findings contract.

    --no-tools is deliberate and load-bearing: the intent and every file are inlined
    in the prompt, so the reviewer needs no filesystem access. Left with read/bash it
    wanders the cwd and reviews whatever it finds there instead of the code under
    review (observed: it reported findings about run-build.py). It also guarantees a
    reviewer can never edit the code it is reviewing.
    """
    prompt = f"{REVIEW_PURPOSE}\n\n{_build_request(intent, files, knowledge_rules)}"

    # The prompt goes via pi's @file syntax, not argv. On Windows `pi` is an npm
    # .CMD shim invoked through cmd.exe, which TRUNCATES a multi-line argument at
    # the first newline — the model then receives only the opening line and answers
    # about code it never saw (observed: "I don't see any code provided", and a
    # false REVIEW COMPLETE). @file passes the whole thing intact.
    import tempfile
    fd, ppath = tempfile.mkstemp(prefix="coms-review-", suffix=".md", text=True)
    os.close(fd)
    try:
        with open(ppath, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(prompt)
        cmd = [PI, "-e", OLLAMA, "--model", vmodel, "-p", "--no-session",
               "--no-tools", "@" + ppath]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 60)
        except subprocess.TimeoutExpired:
            return "(review timed out)", True   # never block the build on a review stall
        except OSError as e:
            return f"(review unavailable: {e})", True
        return _classify_findings((r.stdout or "").strip())
    finally:
        try:
            os.unlink(ppath)
        except OSError:
            pass


def _answer_queries(fd, data):
    """Reply to terminal capability queries so the interactive pi agent renders/runs."""
    if b"\x1b]11;?" in data: os.write(fd, b"\x1b]11;rgb:0000/0000/0000\x1b\\")
    if b"\x1b[6n" in data:   os.write(fd, b"\x1b[1;1R")
    if b"\x1b[c" in data:    os.write(fd, b"\x1b[?1;2c")
    if b"\x1b[?u" in data:   os.write(fd, b"\x1b[?0u")


def _boot_validator(project, model):
    """Start the validator as a persistent interactive agent in a pty; return (pid, fd, state)."""
    pid, fd = pty.fork()
    if pid == 0:
        os.execv(PI, [PI, "-e", OLLAMA, "-e", COMS, "--model", model,
                      "--cname", "validator", "--purpose", REVIEW_PURPOSE, "--project", project])
        os._exit(1)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 50, 140, 0, 0))
    state = {"alive": True}

    def pump():
        while state["alive"]:
            try:
                r, _, _ = select.select([fd], [], [], 0.2)
                if fd in r:
                    d = os.read(fd, 65536)
                    if not d:
                        break
                    _answer_queries(fd, d)
            except OSError:
                break
    threading.Thread(target=pump, daemon=True).start()
    return pid, fd, state


def review(project, intent, files, timeout=REVIEW_TIMEOUT,
           validator_model=None, relay_model=None, knowledge_rules=None):
    """Run a validator-peer review.

    project : coms project name (isolates the pool)
    intent  : the handover/spec text describing desired behaviour
    files   : list of (relpath, content) source files to review
    validator_model / relay_model : override the models (else env, else module default) —
        callers pass their own coder model so AL reviews use the AL model, Go/C# the Go model.
    knowledge_rules : optional list of BCQuality rule dicts (see bcquality.rules_for). When
        supplied, they are injected into the request as a cited checklist so the validator
        grounds behaviour findings in curated BC/AL rules. None/empty → unchanged behaviour.
    Returns (findings_text, clean) where clean=True means the validator said REVIEW COMPLETE.
    """
    vmodel = validator_model or VALIDATOR_MODEL
    rmodel = relay_model or RELAY_MODEL

    # No pty (Windows) → one-shot headless review instead of the coms round-trip.
    if not _HAVE_PTY:
        return _review_headless(intent, files, timeout, vmodel, knowledge_rules)

    if not os.path.exists(COMS):
        return "(coms extension not installed at ~/.pi/coms.ts — skipping review)", True

    reg = os.path.expanduser(f"~/.pi/coms/projects/{project}/agents")
    pid, fd, state = _boot_validator(project, vmodel)
    try:
        # wait for the validator to register in the pool
        for _ in range(45):
            if os.path.isdir(reg) and "validator.json" in os.listdir(reg):
                break
            time.sleep(1)

        req = _build_request(intent, files, knowledge_rules)
        prompt = (f'Use tools only, no commentary. Call coms_send with target="validator" and prompt '
                  f'set to the text between <REQ></REQ>. Then call coms_await with the returned msg_id '
                  f'and timeout_ms {timeout * 1000}. Then output the reply text verbatim.'
                  f'\n<REQ>\n{req}\n</REQ>')
        cmd = [PI, "-e", OLLAMA, "-e", COMS, "--model", rmodel, "-p", "--mode", "json",
               "--session-id", f"{project}-relay", "--cname", "relay", "--purpose", "relay",
               "--project", project, prompt]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 60)
        except subprocess.TimeoutExpired:
            return "(review timed out)", True  # don't block the build on a review stall

        m = re.findall(r'"details":\{"response":"((?:[^"\\]|\\.)*)"', r.stdout)
        if not m:
            return "(no validator response captured)", True
        findings = m[-1].encode().decode("unicode_escape").strip()
        return _classify_findings(findings)
    finally:
        state["alive"] = False
        try:
            os.write(fd, b"\x03\x03")
            time.sleep(0.3)
            os.close(fd)
        except OSError:
            pass
        # best-effort registry cleanup
        try:
            import shutil
            shutil.rmtree(os.path.expanduser(f"~/.pi/coms/projects/{project}"), ignore_errors=True)
        except Exception:
            pass

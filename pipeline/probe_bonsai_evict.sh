#!/usr/bin/env bash
# probe_bonsai_evict.sh — does VRAM eviction fail LOUDLY when it cannot free the card?
#
# Executor phase 5 — probes for paths doclink never exercises. A benchmark run calls
# free_bonsai_vram() once and almost always takes the quiet path (nothing running), so
# the branches that matter — the ones that decide whether a build proceeds into VRAM
# contention — are exercised by no build in the corpus.
#
# The contract this guards, from bonsai_vram's own docstring: "A stop that is ATTEMPTED
# and FAILS is loud — silence there previously cost hours, because contention is
# indistinguishable from a model fault." A quiet failure here does not break the build;
# it makes the coder spill to CPU and time out at 1200s, looking like a model problem.
#
# DRY throughout: the real chat server is never stopped. Branches are driven by
# substituting the module's own probe/stop functions, so the eviction LOGIC is exercised
# without touching Larry. Safe to run at any time, including mid-session.
#
# Usage:  pipeline/probe_bonsai_evict.sh
set -uo pipefail
SETUP_DIR="${SETUP_DIR:-/mnt/rojaws/localDev/setup}"
export PYTHONPATH="$SETUP_DIR/pipeline"

python3 - <<'PY'
import os, sys, io, contextlib
sys.path.insert(0, os.environ["PYTHONPATH"])
import bonsai_vram as B

PASS = FAIL = 0
def ok(m):   globals().__setitem__("PASS", PASS+1); print(f"  {m:<58} PASS")
def bad(m,w):globals().__setitem__("FAIL", FAIL+1); print(f"  {m:<58} FAIL — {w}")

def drive(up_seq, cli=(False,False,"no cli"), dash=(False,False,"no dash"), env=None):
    """Run free_bonsai_vram with is_up()/stop paths substituted. Returns (result, output).

    `up_seq` is consumed by successive is_up() calls, so 'reports stopped but still
    answering' is expressible — that branch exists because the module deliberately does
    not trust the stop's own return value.
    """
    # Patch BOTH: the early branch asks state() (which distinguishes down/absent/
    # unknown), while the post-stop "trust nothing" verification still asks is_up().
    # Patching only one leaves the other doing a real curl against the live host.
    saved = (B.is_up, B.state, B._stop_via_cli, B._stop_via_dashboard, dict(os.environ))
    seq = list(up_seq)
    def _next():
        return seq.pop(0) if seq else False
    B.is_up = lambda *a, **k: _next()
    B.state = lambda *a, **k: ("up" if _next() else "down")
    B._stop_via_cli = lambda: cli
    B._stop_via_dashboard = lambda: dash
    B._state["we_stopped_it"] = False
    for k, v in (env or {}).items():
        os.environ[k] = v
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            r = B.free_bonsai_vram(verbose=True)
    finally:
        B.is_up, B.state, B._stop_via_cli, B._stop_via_dashboard = saved[:4]
        os.environ.clear(); os.environ.update(saved[4])
    return r, buf.getvalue()

# 1. Disabled by env: no attempt, no noise.
r, out = drive([True], env={"BONSAI_EVICT": "0"})
ok("BONSAI_EVICT=0 -> True, no eviction attempted") if (r and "disabled" in out) else bad(
    "BONSAI_EVICT=0 -> True, no eviction attempted", f"r={r} out={out.strip()[:60]!r}")

# 2. Nothing running: True, and QUIET (a warning here would cry wolf every build).
r, out = drive([False])
ok("not running -> True and silent") if (r and out.strip() == "") else bad(
    "not running -> True and silent", f"r={r} out={out.strip()[:60]!r}")

# 3. Stopped successfully and confirmed down.
r, out = drive([True, False], dash=(True, True, ""))
if not r: bad("successful stop -> True", "returned False")
elif "VRAM freed" not in out: bad("successful stop -> reports freed", out.strip()[:60])
elif not B._state.get("we_stopped_it"): bad("successful stop -> records we_stopped_it", "flag unset")
else: ok("successful stop -> True, freed, restore armed")

# 4. THE CONTRACT: attempted and failed must be LOUD and False.
r, out = drive([True], dash=(True, False, "503 from dashboard"))
if r: bad("failed stop -> False", "returned True — build would proceed into contention")
elif "WARNING" not in out: bad("failed stop -> LOUD", f"no WARNING in {out.strip()[:60]!r}")
else: ok("failed stop -> False AND loud")

# 5. Cannot even attempt (no CLI, no creds) -> also loud, also False.
r, out = drive([True])
if r: bad("cannot attempt -> False", "returned True")
elif "WARNING" not in out: bad("cannot attempt -> LOUD", "no WARNING")
else: ok("cannot attempt -> False AND loud")

# 6. Trust nothing: stop REPORTS success but the server still answers.
r, out = drive([True, True], dash=(True, True, ""))
if r: bad("reported-stopped-but-alive -> False", "trusted the stop's own return value")
elif "still answering" not in out: bad("reported-stopped-but-alive -> LOUD", out.strip()[:60])
else: ok("reported-stopped-but-alive -> False AND loud")

# 7. 'could not ask' must be distinguishable from 'not running', and must be LOUD.
# Previously is_up() folded every curl failure into False, so an unreachable Larry read
# as "bonsai is not holding the GPU" — and the build loaded 18GB on top of 9.5GB.
saved_health = B.HEALTH
try:
    B.HEALTH = "https://192.0.2.1/health"          # TEST-NET-1, guaranteed unroutable
    st_unknown = B.state(timeout=2)
    # Deliberately NOT via drive(): that substitutes state(), which would defeat the
    # very lookup under test. Call the real function with only HEALTH redirected.
    B._state["we_stopped_it"] = False
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = B.free_bonsai_vram(verbose=True)
    out = buf.getvalue()
finally:
    B.HEALTH = saved_health

if st_unknown != "unknown":
    bad("unreachable -> state 'unknown', not 'down'", f"state={st_unknown!r}")
elif r:
    bad("unreachable -> False (do not assume the card is free)", "returned True")
elif "cannot determine" not in out:
    bad("unreachable -> LOUD", f"no warning in {out.strip()[:60]!r}")
else:
    ok("unreachable -> 'unknown', False AND loud")

# 8. A genuinely stopped server must stay QUIET — otherwise every build cries wolf.
saved_health = B.HEALTH
try:
    B.HEALTH = "https://no-such-host.invalid/health"   # unresolvable -> 'absent'
    st_absent = B.state(timeout=2)
finally:
    B.HEALTH = saved_health
ok("unresolvable host -> 'absent' (no bonsai here, stay quiet)") if st_absent == "absent" else bad(
    "unresolvable host -> 'absent'", f"state={st_absent!r}")

print(f"\n  {PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
PY

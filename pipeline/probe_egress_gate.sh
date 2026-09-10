#!/usr/bin/env bash
# probe_egress_gate.sh — does the egress chokepoint route and BLOCK as its policy says?
#
# Executor phase 5 — probes for paths doclink never exercises. Benchmark runs are
# local-only, so claude_egress.run_claude() is never reached: the single place that
# decides whether anything leaves this machine, and whether it leaves scrubbed, is
# exercised by no build in the corpus.
#
# TWO MODES, because this path COSTS MONEY
# ----------------------------------------
#   DRY  (default, free)  everything up to the chokepoint. A fake claude binary stands
#                         in, so routing, blocking, arming and usage capture are all
#                         asserted without a single token leaving the machine.
#   LIVE (gated)          one real `claude -p` call, to prove the wiring reaches the
#                         actual binary and that usage is recorded at the chokepoint.
#                         Refuses unless PROBE_ALLOW_BILLING=1 is set explicitly.
#
# LIVE is opt-in and fails closed for the same reason the publish gate does: a probe
# that can spend money by default will eventually spend it by accident.
#
# Usage:  pipeline/probe_egress_gate.sh              # dry, free
#         PROBE_ALLOW_BILLING=1 pipeline/probe_egress_gate.sh   # one billed call
set -uo pipefail
SETUP_DIR="${SETUP_DIR:-/mnt/rojaws/localDev/setup}"
export PYTHONPATH="$SETUP_DIR/pipeline"

python3 - <<'PY'
import os, sys, tempfile, subprocess, json, stat
sys.path.insert(0, os.environ["PYTHONPATH"])
import egress_policy, claude_egress

def use_policy(name, root):
    """Set the policy the way production does: env + set_policy_for(), which also
    exercises resolve()'s precedence rather than poking module state."""
    os.environ["EGRESS_POLICY"] = name
    got = egress_policy.set_policy_for(root)
    assert got == name, f"policy did not take: wanted {name}, got {got}"
    return got

PASS = FAIL = SKIP = 0
def ok(m):   globals().__setitem__("PASS", PASS+1); print(f"  {m:<58} PASS")
def bad(m,w):globals().__setitem__("FAIL", FAIL+1); print(f"  {m:<58} FAIL — {w}")
def skip(m,w):globals().__setitem__("SKIP", SKIP+1); print(f"  {m:<58} SKIP — {w}")

def fake_claude(payload):
    """A stand-in for the claude binary that prints a fixed JSON result."""
    d = tempfile.mkdtemp()
    data = os.path.join(d, "payload.json")
    open(data, "w").write(payload + "\n")
    p = os.path.join(d, "claude")
    open(p, "w").write('#!/usr/bin/env bash\ncat "$(dirname "$0")/payload.json"\n')
    os.chmod(p, 0o755)
    return d, p

FAKE_OK = json.dumps({"type":"result","subtype":"success","is_error":False,
                      "result":"probe reply","total_cost_usd":0.0,
                      "usage":{"input_tokens":11,"output_tokens":3},
                      "session_id":"s","uuid":"u"})

proj = tempfile.mkdtemp()
_d, fake = fake_claude(FAKE_OK)

print("probe_egress_gate — DRY (no tokens leave this machine)")

# --- 1. local-only must HARD BLOCK, and must not invoke anything -------------------
use_policy("local-only", proj)
claude_egress.reset_usage()
out = claude_egress.run_claude(proj, "hello", fake, label="probe")
if out != "":
    bad("local-only BLOCKS the call", f"returned {out[:40]!r}")
elif claude_egress.usage_records():
    bad("local-only invokes nothing", "a usage record was created")
else:
    ok("local-only BLOCKS, and invokes nothing")

# --- 2. personal policy routes through and captures usage at the chokepoint --------
use_policy("personal", proj)
claude_egress.reset_usage()
out = claude_egress.run_claude(proj, "hello", fake, label="probe")
tot = claude_egress.usage_totals()
if "probe reply" not in out:
    bad("personal routes to the binary", f"got {out[:40]!r}")
elif not claude_egress.usage_records():
    bad("usage captured at the chokepoint", "no record")
elif tot.get("claude_input_tokens", 0) != 11:
    bad("usage captured at the chokepoint", f"claude_input_tokens={tot.get('claude_input_tokens')}")
else:
    ok("personal routes through, usage captured at the chokepoint")

# --- 3. a missing binary degrades gracefully, never raises -------------------------
use_policy("personal", proj)
try:
    out = claude_egress.run_claude(proj, "hello", "/nonexistent/claude", label="probe")
    ok("missing binary returns '' rather than raising") if out == "" else bad(
        "missing binary returns ''", f"returned {out[:30]!r}")
except Exception as e:
    bad("missing binary returns ''", f"raised {type(e).__name__}")

# --- 4. cloud-mid has no Anthropic route --------------------------------------------
use_policy("cloud-mid", proj)
okc, why = egress_policy.allowed("anthropic")
oke, _ = egress_policy.escalation_available()
if okc:
    bad("cloud-mid denies anthropic", "allowed() said yes")
elif oke:
    bad("cloud-mid is not escalation-available", "escalation_available() said yes")
else:
    ok("cloud-mid denies anthropic and is not escalation-available")

# --- 5. LIVE: one real billed call, only with explicit consent ---------------------
if os.environ.get("PROBE_ALLOW_BILLING") != "1":
    skip("LIVE one-call egress", "set PROBE_ALLOW_BILLING=1 to spend (~1 tiny call)")
else:
    claude_bin = os.environ.get("CLAUDE_BIN", os.path.expanduser("~/.local/bin/claude"))
    if not os.path.exists(claude_bin):
        skip("LIVE one-call egress", f"claude not found at {claude_bin}")
    else:
        use_policy("personal", proj)
        claude_egress.reset_usage()
        print(f"  [LIVE] invoking {claude_bin} — this call is billed")
        out = claude_egress.run_claude(proj, "Reply with exactly: PROBE-OK",
                                       claude_bin, label="probe-live", timeout=120)
        recs = claude_egress.usage_records()
        tot = claude_egress.usage_totals()
        if not out.strip():
            bad("LIVE call returns text", "empty response")
        elif not recs:
            bad("LIVE usage recorded at the chokepoint", "no usage record")
        elif tot.get("claude_input_tokens", 0) <= 0:
            bad("LIVE usage recorded", f"claude_input_tokens={tot.get('claude_input_tokens')}")
        else:
            ok(f"LIVE ok — in={tot.get('claude_input_tokens')} out={tot.get('claude_output_tokens')} "
               f"cost=${tot.get('claude_cost_usd', 0):.4f} missing_usage={tot.get('claude_calls_missing_usage')}")

print(f"\n  {PASS} passed, {FAIL} failed, {SKIP} skipped")
sys.exit(1 if FAIL else 0)
PY

#!/usr/bin/env bash
# probe_escalation_ladder.sh — does the escalation ladder ARM and DISARM as declared?
#
# Executor phase 5 — probes for paths doclink never exercises. Benchmark runs are
# local-only with escalation off, so the arming logic is exercised by no build in the
# corpus. It is also the logic the whole benchmark programme's arm isolation rests on:
# bench-run-suite.sh asserts each run's BANNER against what the arm declared, and voids
# the suite on a mismatch. If the banner can lie, every A/B built on it is unsound.
#
# DRY (default, free): drives run-build.py far enough to print its arming banner, then
# stops. No model call, no egress, no spend. The decisions under test all happen before
# any build work.
#
# LIVE (gated): a real escalation, which BILLS. Refuses unless PROBE_ALLOW_BILLING=1,
# and additionally requires a working `claude auth status` — an expired session makes a
# LIVE run measure the failure path rather than the feature.
#
# Usage:  pipeline/probe_escalation_ladder.sh
#         PROBE_ALLOW_BILLING=1 pipeline/probe_escalation_ladder.sh
set -uo pipefail
SETUP_DIR="${SETUP_DIR:-/mnt/rojaws/localDev/setup}"
RB="$SETUP_DIR/pipeline/run-build.py"
CLAUDE_BIN_REAL="${CLAUDE_BIN:-$HOME/.local/bin/claude}"
PASS=0; FAIL=0; SKIP=0
ok()   { PASS=$((PASS+1)); printf "  %-56s PASS\n" "$1"; }
bad()  { FAIL=$((FAIL+1)); printf "  %-56s FAIL — %s\n" "$1" "$2"; }
skip() { SKIP=$((SKIP+1)); printf "  %-56s SKIP — %s\n" "$1" "$2"; }

# A minimal project: enough for configure_project to parse a manifest and print the
# banner. The build is killed immediately afterwards — nothing is ever compiled.
mkproj() {
    P=$(mktemp -d); mkdir -p "$P/src"
    # parse_manifest() reads a fenced block of ABSOLUTE paths under a
    # "machine-readable manifest" heading. A bullet list parses to zero files and the
    # run aborts before the banner this probe exists to read.
    cat > "$P/larry-handover.prompt.md" <<HANDOVER
# Probe project

## Machine-readable manifest

\`\`\`
$P/src/A.Codeunit.al
\`\`\`
HANDOVER
    # The internal profile gate runs BEFORE the escalation banner and refuses an
    # app.json missing publisher/runtime/application — a stub gets rejected before the
    # thing under test is ever reached.
    cat > "$P/app.json" <<'APPJSON'
{
    "id": "b7f4c2a1-8d3e-4f56-9a20-1c5e7d8b3f44",
    "name": "Probe",
    "publisher": "Probe",
    "version": "1.0.0.0",
    "platform": "27.0.0.0",
    "application": "27.0.0.0",
    "runtime": "16.0",
    "idRanges": [{"from": 50300, "to": 50399}]
}
APPJSON
    echo "$P"
}

# Every experimental variable run-build reads, cleared before each case. Without this
# the probe INHERITS the shell: .zshenv exports ESCALATE_AFTER=4 and ESCALATE_MID_AFTER=2
# globally, so a case meaning "no escalation configured" silently ran ARMED. That is the
# same ambient leak that voided a 20-run suite; a probe that establishes nothing measures
# the shell, not the code.
CLEAR=()
while read -r v; do CLEAR+=(-u "$v"); done < <(python3 "$SETUP_DIR/pipeline/bench_env_contract.py" --names | tr ' ' '\n')

# Run run-build just long enough to emit the banner. Returns its stdout.
banner() {   # env assignments passed as args
    local p; p=$(mkproj)
    local out
    out=$(env "${CLEAR[@]}" "$@" timeout 25 python3 "$RB" --project "$p" 2>&1 | head -40 || true)
    rm -rf "$p"
    printf '%s' "$out"
}

echo "probe_escalation_ladder — DRY (no spend)"

# 1. Escalation requested but policy forbids egress -> DISARMED, and it must SAY so.
out=$(banner EGRESS_POLICY=local-only ESCALATE_AFTER=2 CODER_BACKEND=pi PREWARM_TIMEOUT=1)
if grep -q "Escalation: DISARMED by egress policy" <<<"$out"; then ok "local-only -> escalation DISARMED, and says why"
else bad "local-only -> escalation DISARMED" "$(grep -m1 -i escalation <<<"$out" | cut -c1-60)"; fi

# 2. Policy permits + binary present -> ARMED, naming the round.
out=$(banner EGRESS_POLICY=personal ESCALATE_AFTER=2 CODER_BACKEND=pi \
             CLAUDE_BIN="$CLAUDE_BIN_REAL" PREWARM_TIMEOUT=1)
if grep -qE "Escalation: ARMED — pi does 2 fix round" <<<"$out"; then ok "personal + binary -> ARMED at the declared round"
else bad "personal + binary -> ARMED" "$(grep -m1 -i escalation <<<"$out" | cut -c1-60)"; fi

# 3. Armed but the binary is missing -> must FAIL LOUD, not quietly stay local.
out=$(banner EGRESS_POLICY=personal ESCALATE_AFTER=2 CODER_BACKEND=pi \
             CLAUDE_BIN=/nonexistent/claude PREWARM_TIMEOUT=1)
if grep -q "ERROR: ESCALATE_AFTER set but Claude bin not found" <<<"$out"; then ok "armed + missing binary -> hard ERROR, not silent"
else bad "armed + missing binary -> hard ERROR" "no ERROR line"; fi

# 4. Ladder inversion guard: mid rung must be BELOW the Claude rung.
out=$(banner EGRESS_POLICY=personal ESCALATE_AFTER=2 ESCALATE_MID_AFTER=3 CODER_BACKEND=pi \
             CLAUDE_BIN="$CLAUDE_BIN_REAL" PREWARM_TIMEOUT=1)
if grep -q "Mid tier: DISARMED" <<<"$out"; then ok "mid >= claude rung -> mid DISARMED (no inversion)"
else bad "mid >= claude rung -> mid DISARMED" "$(grep -m1 'Mid tier' <<<"$out" | cut -c1-60)"; fi

# 5. No escalation variables at all -> explicitly reports OFF.
out=$(banner EGRESS_POLICY=personal CODER_BACKEND=pi PREWARM_TIMEOUT=1)
if grep -q "Escalation: off" <<<"$out"; then ok "no escalation vars -> reports off"
else bad "no escalation vars -> reports off" "no 'Escalation: off'"; fi

# 6. LIVE — real escalation. Needs consent AND a working session.
if [ "${PROBE_ALLOW_BILLING:-0}" != "1" ]; then
    skip "LIVE escalation" "set PROBE_ALLOW_BILLING=1 to spend"
elif ! timeout 30 "$CLAUDE_BIN_REAL" auth status 2>/dev/null | grep -q '"loggedIn": *true'; then
    skip "LIVE escalation" "claude not authenticated — run 'claude auth login' first"
else
    # A real escalation, bounded to ONE Claude call: ESCALATE_AFTER=0 hands fix round 1
    # straight to Claude, MAX_FIX_ROUNDS=1 stops there. --skip-larry means no pi write
    # phase, so the only model invocation in the whole run is the escalated fix.
    LP=$(mktemp -d)
    F=/mnt/rojaws/localDev/projects/bench-p1-crud
    cp "$F/app.json" "$F/cleanup.sh" "$LP/" 2>/dev/null
    [ -d "$F/.alpackages" ] && cp -r "$F/.alpackages" "$LP/"
    [ -d "$F/docs" ] && cp -r "$F/docs" "$LP/"
    cp -r "$F/src" "$LP/" 2>/dev/null
    sed "s|${F}|${LP}|g" "$F/larry-handover.prompt.md" > "$LP/larry-handover.prompt.md"
    # One deliberate compile error for Claude to fix: drop a required semicolon.
    tgt=$(ls "$LP"/src/*.Table.al 2>/dev/null | head -1)
    if [ -z "$tgt" ]; then
        skip "LIVE escalation" "no table file in the p1 fixture to seed"
    else
        python3 - "$tgt" <<'SEED'
import io, sys, re
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
s2, n = re.subn(r"(DataClassification = CustomerContent);", r"", s, count=1)
assert n == 1, "could not seed a compile error"
io.open(p, "w", encoding="utf-8").write(s2)
SEED
        echo "  [LIVE] one escalated Claude call — this is billed"
        log=$(mktemp)
        env "${CLEAR[@]}" EGRESS_POLICY=personal CODER_BACKEND=pi ESCALATE_AFTER=0             MAX_FIX_ROUNDS=1 CLAUDE_BIN="$CLAUDE_BIN_REAL" BONSAI_RESTORE=0             timeout 600 python3 "$RB" --project "$LP" --skip-larry > "$log" 2>&1
        if ! grep -qE "RULE ESCALATION|Running Claude Code|backend.*claude" "$log"; then
            bad "LIVE escalation invokes Claude" "no Claude invocation in the log"
            grep -iE "escalation|claude" "$log" | head -3 | sed 's/^/       /'
        elif ! grep -q "usage:" "$log"; then
            bad "LIVE escalation records usage" "no usage line at the chokepoint"
        else
            u=$(grep -m1 "usage:" "$log" | sed 's/^ *//')
            ok "LIVE escalation invoked Claude and priced it"
            echo "       $u"
            echo "       verdict: $(grep -m1 '^RESULT:' "$log" || echo none)"
        fi
        rm -f "$log"
    fi
    rm -rf "$LP"
fi

echo
echo "  $PASS passed, $FAIL failed, $SKIP skipped"
[ "$FAIL" -eq 0 ]

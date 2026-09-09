#!/usr/bin/env bash
# run-suite.sh — interleaved control-vs-challenger AL build benchmark.
#
# Reconstructed 2026-08-10 from the suite4/suite5 run + log layout (the original
# driver was ad-hoc and never committed). Method follows
# setup/reference/larry-benchmark-plan.md §3:
#   - N>=3 repeats per (model x project)
#   - control and challenger INTERLEAVED in one session, so a pipeline change
#     between sessions cannot be mistaken for a model difference
#   - escalation OFF (measure the raw model, never Claude)
#   - fixed fix-round cap, one model resident at a time
#
# Usage:
#   ./run-suite.sh <tag> <control-model> <challenger-model> [projects...] [-- repeats]
# Example:
#   ./run-suite.sh suite6 ollama/qwen3-coder:30b ollama/hf.co/unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL
set -uo pipefail

BENCH="$(cd "$(dirname "$0")" && pwd)"
RUNBUILD="${RUNBUILD:-/mnt/rojaws/localDev/setup/pipeline/run-build.py}"
PROJECTS_DIR="/mnt/rojaws/localDev/projects"

TAG="${1:?usage: run-suite.sh <tag> <control-model> <challenger-model> [projects...]}"
CONTROL="${2:?need control model}"
CHALLENGER="${3:?need challenger model}"
shift 3
PROJECTS=("$@")
[ ${#PROJECTS[@]} -eq 0 ] && PROJECTS=(p1 p4 map doclink)
REPEATS="${REPEATS:-3}"
# Extra env per arm, e.g. CHALLENGER_ENV="AL_BRAIN=1". Empty by default, so a plain
# model-vs-model suite behaves exactly as before.
CONTROL_ENV="${CONTROL_ENV:-}"
CHALLENGER_ENV="${CHALLENGER_ENV:-}"
MAX_FIX="${MAX_FIX_ROUNDS:-5}"

# ---- Arm isolation ---------------------------------------------------------
# An arm must ESTABLISH the configuration it measures, never inherit it. Before
# this, "control" meant "add no escalation variables" — which in a shell where
# .zshenv exports ESCALATE_MID_AFTER/ESCALATE_AFTER/MID_MODEL is a different
# thing entirely, and voided the suite5-mid doclink A/B (both arms armed).
#
# bench_env_contract.py derives the clear-list from what run-build.py and its
# pipeline modules actually read, minus tool locators. Derived, not curated: a
# knob added to run-build.py is isolated the day it lands.
CONTRACT="$BENCH/bench_env_contract.py"
# -f, not -x: the contract is never exec'd, it is passed to python3 below. Requiring the
# exec bit made this guard fire on a file that was present and working — bench_env_contract.py
# is committed 100644, so every suite since 2026-08-25 refused to start with
# "missing", and a fresh clone would have inherited exactly the same dead harness. The
# real usability test is the --names call on the next line, which already fails hard.
if [ ! -f "$CONTRACT" ]; then
  echo "FATAL: $CONTRACT missing — refusing to run an unisolated suite." >&2; exit 2
fi
SANITIZE=($(python3 "$CONTRACT" --names)) || { echo "FATAL: env contract failed" >&2; exit 2; }
CLEAR=(); for v in "${SANITIZE[@]}"; do CLEAR+=(-u "$v"); done

# Expected arming for an arm, read from what the arm DECLARES (not from ambient).
# Compared against run-build's own banner, so the claim is checked against the
# run's behaviour rather than against the variables we believe we passed.
declares() {  # arm_env, var -> value or empty
  echo " $1 " | grep -oE "(^| )$2=[^ ]*" | tail -1 | cut -d= -f2-
}

# fixture key -> source project dir
fixture_of() {
  case "$1" in
    p1)      echo "$PROJECTS_DIR/bench-p1-crud" ;;
    p4)      echo "$PROJECTS_DIR/bench-p4-unseen" ;;
    map)     echo "$PROJECTS_DIR/tsg-map-integration" ;;
    doclink) echo "$PROJECTS_DIR/tsg-document-link-2-az-storage" ;;
    *)       echo "" ;;
  esac
}

# Check a finished run's banner against what the arm declared. Positive on both
# sides: an unarmed rung must be absent BECAUSE nothing set it, and an armed rung
# must actually be armed — "DISARMED by egress policy" is a failed arm, not a
# quiet control.
assert_arm() {         # arm, arm_env, log
  local arm="$1" aenv="$2" log="$3" fail=0
  local want_mid; want_mid="$(declares "$aenv" ESCALATE_MID_AFTER)"
  local want_esc; want_esc="$(declares "$aenv" ESCALATE_AFTER)"

  if [ -n "$want_esc" ]; then
    grep -q "^Escalation: ARMED" "$log" || {
      echo "  !! $arm declared ESCALATE_AFTER=$want_esc but Claude rung is not ARMED:" | tee -a "$SUMMARY"; fail=1; }
  else
    grep -q "^Escalation: off" "$log" || {
      echo "  !! $arm declared no ESCALATE_AFTER but Claude rung is not off:" | tee -a "$SUMMARY"; fail=1; }
  fi

  if [ -n "$want_mid" ]; then
    grep -q "^Mid tier: ARMED" "$log" || {
      echo "  !! $arm declared ESCALATE_MID_AFTER=$want_mid but mid rung is not ARMED:" | tee -a "$SUMMARY"; fail=1; }
  else
    grep -q "^Mid tier:" "$log" && {
      echo "  !! $arm declared no ESCALATE_MID_AFTER but a mid rung was configured:" | tee -a "$SUMMARY"; fail=1; }
  fi

  [ $fail -eq 0 ] && return 0
  grep -E "^(Coder backend|Escalation|Mid tier):" "$log" | sed 's/^/     /' | tee -a "$SUMMARY"
  return 1
}

mkdir -p "$BENCH/runs" "$BENCH/logs"
SUMMARY="$BENCH/${TAG^^}-SUMMARY.log"
: > "$SUMMARY"
t_all=$(date +%s)

run_one() {           # arm, project-key, repeat
  local arm="$1" pk="$2" r="$3"
  local model; [ "$arm" = control ] && model="$CONTROL" || model="$CHALLENGER"
  # Per-arm environment, so an A/B can vary something OTHER than the model — a prompt
  # flag, a knowledge setting. Both arms may name the SAME model; the run directory
  # already carries the arm, so names stay unique and run-build's model/dir guard is
  # satisfied either way.
  local arm_env; [ "$arm" = control ] && arm_env="$CONTROL_ENV" || arm_env="$CHALLENGER_ENV"
  local src; src="$(fixture_of "$pk")"
  # run-build.py guards that the dir name's leading segment matches model_slug()
  # (bench naming: '<model>__<project>__<workflow>__<run>'), so metrics can never be
  # mislabelled. Build the slug the same way it does: strip the provider prefix, ':'->'_'.
  local slug="${model#*/}"; slug="${slug//:/_}"
  local name="${slug}__${pk}__${TAG}_${arm}__r${r}"
  local dst="$BENCH/runs/$name"
  local log="$BENCH/logs/${name}.log"

  if [ -z "$src" ] || [ ! -d "$src" ]; then
    echo "$name: SKIP (no fixture for '$pk')" | tee -a "$SUMMARY"; return
  fi

  rm -rf "$dst"; mkdir -p "$dst"
  # Seed only the inputs. src/ is deliberately NOT copied — the model writes it.
  cp "$src/app.json" "$dst/" 2>/dev/null
  [ -f "$src/cleanup.sh" ] && cp "$src/cleanup.sh" "$dst/"
  [ -d "$src/docs" ] && cp -r "$src/docs" "$dst/"
  [ -d "$src/.alpackages" ] && cp -r "$src/.alpackages" "$dst/"
  # The handover's machine-readable manifest carries ABSOLUTE paths pinned to the
  # fixture dir. Copied verbatim into a run dir those paths still point at the
  # fixture: the manifest check reports every file MISSING, and pi burns the whole
  # 1200s write budget trying to reconcile two locations. Repoint them at $dst.
  sed "s|${src}|${dst}|g" "$src/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md"

  # SEED_GIT=1 makes each run directory its own git repo with the seeded inputs committed.
  # Required by EGRESS_POLICY=enterprise-anon: the anon hook mirrors TRACKED files only, and
  # runs/ is gitignored inside the setup worktree — so run_workspace's "is this a repo" test
  # passes while `git ls-files` returns 0 and the mirror comes out EMPTY. Claude would see no
  # app.json, no handover, no docs, and the run would measure nothing.
  #
  # A harness implementation correction, not an experiment amendment: it changes what the
  # coder can SEE, never the task, the allocation or the scoring. OFF by default so the
  # local-only corpus runs are byte-for-byte what they were.
  if [ "${SEED_GIT:-0}" = "1" ]; then
    git -C "$dst" init -q
    git -C "$dst" add -A
    git -C "$dst" -c user.email=pipeline@local -c user.name=pipeline \
        commit -q -m "seeded inputs (bench $TAG)" || true
    echo "  seeded git repo: $(git -C "$dst" ls-files | wc -l) tracked file(s)"
  fi

  local t0; t0=$(date +%s)
  # HARD per-run cap. run-build has internal timeouts, but a wedged pi does not
  # always trip them: a long agentic run can stall with the stream never finishing
  # (GPU idle, process alive — the known "stream ended without finish_reason" bug).
  # Unbounded, one wedge stalls an entire 24-run suite indefinitely. `timeout`
  # returns 124 on expiry, which is recorded as its own verdict so a stall is never
  # silently counted as a model failure.
  # FIXTURE_DIR lets run-build record WHICH fixture revision produced this result
  # (commit + handover hash). The run dir cannot infer it: the handover is copied in with
  # its paths rewritten, so the run copy never hashes equal to the fixture's original.
  # ${CLEAR[@]} wipes every experimental variable run-build reads, THEN the arm's
  # own settings go on. env applies -u before the NAME=VALUE assignments, so the
  # arm's declarations survive the wipe and nothing else does.
  # BONSAI_RESTORE=0: a suite evicts the chat server ONCE and leaves it down for the
  # duration. Restoring between runs would evict the coder in turn on every single run
  # (`bonsai on` reports "coder evicted"), costing a ~22s cold load per run and thrashing
  # a 24GB card both directions 40 times. The chat server is restored by hand, or by the
  # next non-suite build, once the suite ends.
  env "${CLEAR[@]}" \
    PI_CODER_MODEL="$model" CODER_BACKEND=pi MAX_FIX_ROUNDS="$MAX_FIX" BONSAI_RESTORE=0 \
    FIXTURE_DIR="$src" $arm_env \
    timeout "${RUN_TIMEOUT:-3600}" python3 "$RUNBUILD" --project "$dst" > "$log" 2>&1
  local rc=$?
  local dt=$(( $(date +%s) - t0 ))

  # Did the run behave as the arm declared? run-build prints its own arming banner;
  # that is the authoritative statement of what this build could reach. A control
  # that shows a mid rung, or a challenger silently DISARMED by egress policy, is a
  # void measurement — abort rather than accumulate rows that cannot be compared.
  if ! assert_arm "$arm" "$arm_env" "$log"; then
    echo "$name: VOID(arm-config) in ${dt}s — see $log" | tee -a "$SUMMARY"
    ABORT=1; return 1
  fi

  local verdict
  # run-build.py's own final verdict line — the only authoritative marker.
  # ("BUILD: PASSED" appears mid-run per compile attempt; "RESULT: PASS" is final.)
  if [ $rc -eq 124 ]; then
    verdict="TIMEOUT"
  elif [ $rc -eq 0 ] && grep -q "^RESULT: PASS" "$log"; then
    verdict="PASS"
  else
    verdict="FAIL($rc)"
  fi
  echo "$name: $verdict in ${dt}s" | tee -a "$SUMMARY"

  # Drop the symbol packages now the verdict is recorded. They are ~50MB per run and
  # re-downloadable (run-build fetches them via al_downloadsymbols anyway), so keeping
  # one copy per run is pure waste: 194 runs had grown this directory to 3.0GB, of
  # which 3.0GB was .alpackages and only 5.7MB the generated AL. The AL and the log
  # are the evidence; the symbols are not. KEEP_SYMBOLS=1 to retain them for debugging
  # a symbol-resolution failure.
  [ "${KEEP_SYMBOLS:-0}" = "1" ] || rm -rf "$dst/.alpackages"
}

echo "suite $TAG  control=$CONTROL  challenger=$CHALLENGER" | tee -a "$SUMMARY"
echo "projects: ${PROJECTS[*]}  repeats: $REPEATS  max_fix: $MAX_FIX"

# ---- Preflight: state the effective configuration BEFORE the first fixture run.
# The suite used to report only what it added. It now reports what each arm IS:
# the wiped surface, what the shell was trying to leak into it, and the arm's own
# declarations. A voided A/B should be visible in the first ten lines of the log,
# not reconstructed months later.
CONTRACT_JSON="$BENCH/runs/${TAG}-env-contract.json"
python3 "$CONTRACT" --json > "$CONTRACT_JSON"
{
  echo "--- arm isolation preflight ---"
  echo "sanitized: ${#SANITIZE[@]} vars cleared per run (contract: $CONTRACT_JSON)"
  AMBIENT=$(python3 - "$CONTRACT_JSON" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
a = d["ambient_found"]
print(" ".join(f"{k}={v}" for k, v in sorted(a.items())) if a else "none")
PY
)
  echo "ambient (inherited, CLEARED before each run): $AMBIENT"
  for arm in control challenger; do
    aenv=$([ "$arm" = control ] && echo "$CONTROL_ENV" || echo "$CHALLENGER_ENV")
    m=$(declares "$aenv" ESCALATE_MID_AFTER); e=$(declares "$aenv" ESCALATE_AFTER)
    mm=$(declares "$aenv" MID_MODEL)
    echo "$arm: declares='${aenv:-none}'"
    echo "   mid rung:    $([ -n "$m" ] && echo "ARMED at round $m via ${mm:-run-build default}" || echo "absent — no ESCALATE_MID_AFTER declared, and none inheritable")"
    echo "   claude rung: $([ -n "$e" ] && echo "ARMED at round $e" || echo "absent — no ESCALATE_AFTER declared, and none inheritable")"
  done
  echo "each run's banner is asserted against these declarations; a mismatch VOIDs the suite"
  echo "-------------------------------"
  echo
} | tee -a "$SUMMARY"

# Run order depends on whether the arms differ by MODEL or by anything else.
#
# Different models -> GROUPED. Interleaving would force a model swap every run, and
# the challenger cold-loads in ~210s (ROCm, dense 27B). The plan's rule is "one model
# resident at a time, warm before the timed run", which grouping satisfies and
# interleaving violates. This was the original behaviour and is unchanged.
#
# Same model both arms -> INTERLEAVED. When the treatment is env or code rather than
# the model, there is no swap and no cold-load cost, so the reason for grouping does
# not apply — while the cost of grouping does: every control run happens before every
# challenger run, so within-session drift (GPU thermal state, model residency, page
# cache) is confounded with the arm. The unmask pilot had to drive its own interleaved
# sequence for exactly this reason; suites should not need to.
ORDER=()
if [ "$CONTROL" = "$CHALLENGER" ]; then
  RUN_ORDER="interleaved (same model both arms — no swap cost)"
  for pk in "${PROJECTS[@]}"; do
    for r in $(seq 1 "$REPEATS"); do
      for arm in control challenger; do ORDER+=("$arm|$pk|$r"); done
    done
  done
else
  RUN_ORDER="grouped by model (a swap costs a ~210s cold load)"
  for arm in control challenger; do
    for pk in "${PROJECTS[@]}"; do
      for r in $(seq 1 "$REPEATS"); do ORDER+=("$arm|$pk|$r"); done
    done
  done
fi
echo "run order: $RUN_ORDER" | tee -a "$SUMMARY"
echo | tee -a "$SUMMARY"

ABORT=0
for spec in "${ORDER[@]}"; do
  IFS='|' read -r arm pk r <<< "$spec"
  run_one "$arm" "$pk" "$r"
  # A run whose arming contradicted its arm means the isolation is broken for
  # every later run too. Stop at the first one instead of spending a suite on
  # rows that cannot be compared — the failure the whole patch exists to catch.
  [ "$ABORT" = 1 ] && { echo "ABORTED: arm configuration assertion failed" | tee -a "$SUMMARY"; exit 3; }
done

echo | tee -a "$SUMMARY"
echo "=== ${TAG^^} SUMMARY ===" | tee -a "$SUMMARY"
for arm in control challenger; do
  pass=$(grep -c "__${TAG}_${arm}__.*: PASS" "$SUMMARY")
  tot=$(grep -c "__${TAG}_${arm}__.*: \(PASS\|FAIL\|TIMEOUT\)" "$SUMMARY")
  echo "  $arm: $pass/$tot pass" | tee -a "$SUMMARY"
  grep "__${TAG}_${arm}__" "$SUMMARY" | grep -E ": (PASS|FAIL|TIMEOUT)" | \
    sed "s/${TAG}__//; s/: / /" | awk '{printf "    %-12s %-9s %-4s %s %s\n",$1,$2,$3,$4,$5}' \
    | tee -a "$SUMMARY"
done
echo "  total $(( ($(date +%s) - t_all) / 60 )) min" | tee -a "$SUMMARY"

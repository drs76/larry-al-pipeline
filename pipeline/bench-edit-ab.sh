#!/usr/bin/env bash
# bench-edit-ab.sh — A/B for the EDIT flow (run-edit.py), one variable, N repeats.
#
# The greenfield suite (bench-run-suite.sh) copies a fixture directory and lets the model
# write src/ from nothing. Edit work cannot be benchmarked that way: run-edit mutates a
# real git repo in place and preflights on a clean tracked tree, so every run needs a
# pristine starting point or run 2 measures run 1's leftovers.
#
# Each run therefore gets its own `git clone` of the fixture at HEAD. Untracked inputs the
# repo does not carry — the handover and .alpackages — are copied in afterwards.
#
# Usage:
#   ./bench-edit-ab.sh <tag> <repo> [repeats]
# Env:
#   CONTROL_ENV / CHALLENGER_ENV   extra env per arm, e.g. CHALLENGER_ENV="AL_BRAIN=1"
#   EDIT_TIMEOUT                   hard per-run cap (default 3600s)
#   ONLY                           run-edit --only filter, e.g. ONLY=F2 to isolate one
#                                  task. Only sound when that task is self-contained —
#                                  check its anchors exist at HEAD, or you are measuring
#                                  a task whose preconditions the other tasks used to
#                                  create.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
TAG="${1:?usage: bench-edit-ab.sh <tag> <repo> [repeats]}"
REPO="${2:?need the fixture repo path}"
REPEATS="${3:-3}"
CONTROL_ENV="${CONTROL_ENV:-}"
CHALLENGER_ENV="${CHALLENGER_ENV:-}"
WORK="${EDIT_BENCH_DIR:-/tmp/claude-1000/edit-ab}"
ONLY="${ONLY:-}"
SUMMARY="$HERE/${TAG^^}-EDIT-SUMMARY.log"

mkdir -p "$WORK"
: > "$SUMMARY"
echo "edit A/B $TAG  repo=$REPO  repeats=$REPEATS${ONLY:+  only=$ONLY}" | tee -a "$SUMMARY"
echo "arm env: control='${CONTROL_ENV:-none}'  challenger='${CHALLENGER_ENV:-none}'" | tee -a "$SUMMARY"
echo | tee -a "$SUMMARY"
t_all=$(date +%s)

run_one() {                       # arm, repeat
  local arm="$1" r="$2"
  local arm_env; [ "$arm" = control ] && arm_env="$CONTROL_ENV" || arm_env="$CHALLENGER_ENV"
  local name="${TAG}_${arm}__r${r}"
  local dst="$WORK/$name"
  local log="$HERE/logs/${name}.log"
  mkdir -p "$HERE/logs"

  rm -rf "$dst"
  # HEAD, not the working tree: the fixture's tree carries a previous trial's edits, and
  # cloning the dirty state would hand the model work already done.
  git clone -q --no-hardlinks "$REPO" "$dst" 2>/dev/null || {
    echo "$name: SKIP (clone failed)" | tee -a "$SUMMARY"; return; }
  # Inputs the repo does not track. The handover's manifest carries ABSOLUTE paths
  # pinned to the original repo; copied verbatim into a clone every path resolves
  # outside it, pathguard rejects all 16, the whitelist comes back empty and run-edit
  # aborts before doing anything. Repoint them at the clone — same trap the greenfield
  # runner documents.
  sed "s|${REPO%/}|${dst}|g" "$REPO/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md" 2>/dev/null
  [ -d "$REPO/.alpackages" ] && cp -r "$REPO/.alpackages" "$dst/"

  local t0; t0=$(date +%s)
  env $arm_env timeout "${EDIT_TIMEOUT:-3600}" \
    python3 "$HERE/run-edit.py" --project "$dst" ${ONLY:+--only "$ONLY"} > "$log" 2>&1
  local rc=$?
  local dt=$(( $(date +%s) - t0 ))

  # run-edit's own tallies. Applied/failed counts come from its task loop; the compile
  # verdict is the referee. A timeout is recorded distinctly so a stall is never read as
  # a model failure.
  # Parse run-edit's OWN result line rather than guessing at a log format. The first
  # version invented "TASK n APPLIED" markers that run-edit never prints (applied=0 on
  # every run) and accepted only "RESULT: PASS" — so PARTIAL, which is 22/23 tasks with a
  # GREEN BUILD, was recorded as FAIL. The distinction is the entire experiment here.
  local result applied failed verdict
  result=$(grep -m1 -E "^RESULT:" "$log" 2>/dev/null | sed 's/^RESULT: //; s/ Review with.*//')
  applied=$(sed -n 's/.*— \([0-9]*\)\/\([0-9]*\) tasks applied.*/\1\/\2/p' <<<"$result")
  [ -z "$applied" ] && grep -q "all tasks applied" <<<"$result" && applied="all"
  failed=$(grep -m1 -E "^FAILED TASKS" "$log" 2>/dev/null | sed 's/.*: //')
  if [ $rc -eq 124 ]; then verdict="TIMEOUT"
  elif grep -qE "^RESULT: PASS" "$log" 2>/dev/null; then verdict="PASS"
  elif grep -qE "^RESULT: PARTIAL" "$log" 2>/dev/null; then verdict="PARTIAL"
  else verdict="FAIL"; fi
  echo "$name: $verdict  applied=${applied:-?} failed=${failed:--}  in ${dt}s" | tee -a "$SUMMARY"
  # Keep the tree only when something went wrong — that is the one you need to inspect.
  # A clean run's clone is ~60MB of nothing anybody will read again.
  [ "$verdict" = PASS ] && [ "${KEEP_RUNS:-0}" != 1 ] && rm -rf "$dst"
}

for arm in control challenger; do
  for r in $(seq 1 "$REPEATS"); do run_one "$arm" "$r"; done
done

echo | tee -a "$SUMMARY"
echo "=== ${TAG^^} EDIT A/B SUMMARY ===" | tee -a "$SUMMARY"
for arm in control challenger; do
  echo "  $arm:" | tee -a "$SUMMARY"
  grep "${TAG}_${arm}__" "$SUMMARY" | grep -E "(PASS|FAIL|TIMEOUT)" | \
    sed 's/^/    /' | tee -a "$SUMMARY"
done
echo "  total $(( ($(date +%s) - t_all) / 60 )) min" | tee -a "$SUMMARY"

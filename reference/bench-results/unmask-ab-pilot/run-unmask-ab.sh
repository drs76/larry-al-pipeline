#!/usr/bin/env bash
# Interleaved driver for the unmask retain-vs-revert experiment.
#
# bench-run-suite.sh is NOT used: its loop is `for arm; for project; for repeat`, so it
# runs every control then every challenger. That leaves within-session drift (GPU thermal
# state, model residency) confounded with the arm. The pre-registration requires
# interleaving, so the assignment order comes from the frozen sequence file and this
# driver executes it verbatim.
#
# Nothing here adapts to results. N, the sequence and the endpoint are fixed before the
# first run; this script cannot shorten, extend or reorder the batch.
set -uo pipefail

SB=/tmp/claude-1000/-mnt-rojaws-localDev/564fd1e1-49d3-4737-b912-7e0208433035/scratchpad
PIPE=/mnt/rojaws/localDev/setup/pipeline
FIXTURE=/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage
OUT=$SB/unmask-ab
SEQFILE=$SB/ASSIGNMENT-SEQUENCE.json

# Refuse to run against anything but the reviewed, frozen trees.
if ! sha256sum -c "$SB/FROZEN.sha256" --status; then
  echo "FATAL: a frozen artifact changed since review — refusing to run." >&2
  sha256sum -c "$SB/FROZEN.sha256" >&2; exit 2
fi

mkdir -p "$OUT"
mapfile -t SEQ < <(python3 -c "
import json; print('\n'.join(json.load(open('$SEQFILE'))['sequence']))")
echo "sequence (${#SEQ[@]} runs): ${SEQ[*]}"

CLEAR=()
while read -r v; do CLEAR+=(-u "$v"); done < <(python3 "$PIPE/bench_env_contract.py" --names | tr ' ' '\n')

i=0
for arm in "${SEQ[@]}"; do
  i=$((i+1))
  case "$arm" in
    A) tree="$PIPE/run-build.py" ;;
    B) tree="$SB/armB/pipeline/run-build.py" ;;
    *) echo "FATAL: bad arm '$arm'" >&2; exit 2 ;;
  esac

  # Positive assertion per run, read from the file about to execute. Arm B is the ONLY
  # tree carrying the ARM B marker; arm A is the only one carrying the forward marker.
  fwd=$(grep -c "fixing forward, not reverting" "$tree")
  rev=$(grep -c "ARM B: reverting, not fixing forward" "$tree")
  case "$arm" in
    A) [ "$fwd" = 1 ] && [ "$rev" = 0 ] || { echo "FATAL run $i arm A: fwd=$fwd rev=$rev" >&2; exit 2; } ;;
    B) [ "$fwd" = 0 ] && [ "$rev" = 1 ] || { echo "FATAL run $i arm B: fwd=$fwd rev=$rev" >&2; exit 2; } ;;
  esac

  dst="$PIPE/runs/unmaskab_${arm}_r${i}"
  rm -rf "$dst"; mkdir -p "$dst"
  # Seed ONLY the inputs, exactly as bench-run-suite.sh run_one does. src/ is
  # deliberately NOT copied — the model writes it, and copying it would hand every run
  # a finished tree and measure nothing.
  cp "$FIXTURE/app.json" "$dst/" 2>/dev/null
  [ -f "$FIXTURE/cleanup.sh" ] && cp "$FIXTURE/cleanup.sh" "$dst/"
  [ -d "$FIXTURE/docs" ] && cp -r "$FIXTURE/docs" "$dst/"
  [ -d "$FIXTURE/.alpackages" ] && cp -r "$FIXTURE/.alpackages" "$dst/"
  # The handover manifest carries ABSOLUTE paths pinned to the fixture dir. Copied
  # verbatim they still point at the fixture, so every manifest path is "outside the
  # project root", 0 expected files are parsed, and the run aborts in 2s. Repoint them.
  sed "s|${FIXTURE}|${dst}|g" "$FIXTURE/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md"

  log="$OUT/unmaskab_${arm}_r${i}.log"
  t0=$(date +%s)
  env "${CLEAR[@]}" PI_CODER_MODEL=ollama/qwen3-coder:30b CODER_BACKEND=pi \
      MAX_FIX_ROUNDS=5 BONSAI_RESTORE=0 FIXTURE_DIR="$FIXTURE" \
      timeout 3600 python3 "$tree" --project "$dst" > "$log" 2>&1
  rc=$?; dt=$(( $(date +%s) - t0 ))
  trig=$(grep -c "Unmask: all" "$log")
  res=$(grep -m1 "^RESULT:" "$log" || echo "RESULT: (none)")
  echo "  run $i arm $arm  rc=$rc  ${dt}s  triggers=$trig  $res" | tee -a "$OUT/DRIVER.log"
done
echo "batch complete — $i runs" | tee -a "$OUT/DRIVER.log"

#!/usr/bin/env bash
# tierb-part1.sh — Tier B Part 1: full-run Claude capability on doclink, n=5.
#
# A dedicated driver, NOT bench-run-suite.sh, for one reason: the suite runs a control and a
# challenger arm, which would be 10 billed Claude runs where the pre-registration says 5.
# Everything else follows the suite — the same derived env-contract isolation, the same
# fixture seeding, the same provenance pinning.
#
# Per-run gate: tierb_preflight.py must PASS before Claude is invoked. A workspace that
# cannot produce a populated scrubbed mirror is a run that measures nothing, so it aborts
# rather than spending.
#
#   EGRESS_POLICY=enterprise-anon ./tierb-part1.sh
set -uo pipefail

BENCH="$(cd "$(dirname "$0")" && pwd)"
RUNBUILD="${RUNBUILD:-$BENCH/run-build.py}"
SRC="/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage"
TAG="${TAG:-tierb1}"
N="${N:-5}"
LABEL="claude-code"

[ "${EGRESS_POLICY:-}" = "enterprise-anon" ] || {
  echo "FATAL: Tier B is authorised for EGRESS_POLICY=enterprise-anon only (got '${EGRESS_POLICY:-unset}')." >&2
  exit 2; }
[ -d "$SRC" ] || { echo "FATAL: fixture missing: $SRC" >&2; exit 2; }

SANITIZE=($(python3 "$BENCH/bench_env_contract.py" --names)) || exit 2
CLEAR=(); for v in "${SANITIZE[@]}"; do CLEAR+=(-u "$v"); done

mkdir -p "$BENCH/runs" "$BENCH/logs"
SUMMARY="$BENCH/${TAG^^}-SUMMARY.log"
: > "$SUMMARY"

{
  echo "Tier B Part 1 — full-run Claude capability, doclink, n=$N"
  echo "registration: reference/exp-tierb-claude-preregistration.md"
  echo "egress: enterprise-anon (Anthropic only; openrouter and github denied)"
  echo "scrub boundary: tracked FILES are mirrored; the PROMPT is not scrubbed and inlines"
  echo "  the whole handover. In scope for this synthetic fixture; NOT a guarantee for"
  echo "  customer material."
  echo "sanitized ${#SANITIZE[@]} env vars per run; no escalation rung — Claude is the CODER"
  echo
} | tee -a "$SUMMARY"

t_all=$(date +%s)
for r in $(seq 1 "$N"); do
  name="${LABEL}__doclink__${TAG}__r${r}"
  dst="$BENCH/runs/$name"
  log="$BENCH/logs/${name}.log"

  rm -rf "$dst"; mkdir -p "$dst"
  cp "$SRC/app.json" "$dst/" 2>/dev/null
  [ -f "$SRC/cleanup.sh" ] && cp "$SRC/cleanup.sh" "$dst/"
  [ -d "$SRC/docs" ] && cp -r "$SRC/docs" "$dst/"
  [ -d "$SRC/.alpackages" ] && cp -r "$SRC/.alpackages" "$dst/"
  sed "s|${SRC}|${dst}|g" "$SRC/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md"

  # The anon hook mirrors TRACKED files only; runs/ is gitignored inside the setup worktree,
  # so without its own repo the mirror comes out empty. Harness correction, not an
  # experiment amendment: it changes what the coder can SEE, never the task or the scoring.
  git -C "$dst" init -q
  cat > "$dst/.gitignore" <<'GI'
.alpackages/
.anon/
*.app
GI
  git -C "$dst" add -A
  git -C "$dst" -c user.email=pipeline@local -c user.name=pipeline \
      commit -q -m "seeded inputs (tier B $TAG r$r)" || true

  echo "--- $name : preflight" | tee -a "$SUMMARY"
  if ! env "${CLEAR[@]}" EGRESS_POLICY=enterprise-anon CODER_BACKEND=claude \
        ANON_AUTOCOMMIT=1 python3 "$BENCH/tierb_preflight.py" "$dst" >> "$log" 2>&1; then
    echo "$name: ABORT (preflight failed — no Claude call made). See $log" | tee -a "$SUMMARY"
    tail -20 "$log"
    exit 3
  fi
  echo "$name: preflight PASS" | tee -a "$SUMMARY"

  t0=$(date +%s)
  env "${CLEAR[@]}" \
    CODER_BACKEND=claude EGRESS_POLICY=enterprise-anon ANON_AUTOCOMMIT=1 \
    MAX_FIX_ROUNDS="${MAX_FIX_ROUNDS:-5}" FIXTURE_DIR="$SRC" \
    timeout "${RUN_TIMEOUT:-1800}" python3 "$RUNBUILD" --project "$dst" >> "$log" 2>&1
  rc=$?
  dt=$(( $(date +%s) - t0 ))

  # The coder must actually have been Claude. A silent fallback to pi would look like a
  # capability result and would not be one.
  if ! grep -q "^Coder backend: claude" "$log"; then
    echo "$name: VOID(backend) in ${dt}s — banner does not show the Claude coder" | tee -a "$SUMMARY"
    grep -E "^(Coder backend|Escalation|Mid tier):" "$log" | sed 's/^/     /' | tee -a "$SUMMARY"
    exit 3
  fi

  if [ $rc -eq 124 ]; then verdict="TIMEOUT"
  elif [ $rc -eq 0 ] && grep -q "^RESULT: PASS" "$log"; then verdict="PASS"
  else verdict="FAIL($rc)"; fi
  echo "$name: $verdict in ${dt}s" | tee -a "$SUMMARY"
  rm -rf "$dst/.alpackages"
done

echo | tee -a "$SUMMARY"
echo "=== ${TAG^^} SUMMARY ===" | tee -a "$SUMMARY"
pass=$(grep -c "__${TAG}__.*: PASS" "$SUMMARY")
tot=$(grep -cE "__${TAG}__.*: (PASS|FAIL|TIMEOUT)" "$SUMMARY")
echo "  terminal pass: $pass/$tot" | tee -a "$SUMMARY"
echo "  total $(( ($(date +%s) - t_all) / 60 )) min" | tee -a "$SUMMARY"

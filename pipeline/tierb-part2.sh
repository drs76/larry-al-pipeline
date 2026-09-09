#!/usr/bin/env bash
# tierb-part2.sh — Tier B Part 2: Claude takes over an honest stalled Qwen state.
#
# Harness implementation for the FROZEN registration. It changes no candidate, no selection
# rule, no hypothesis and no scoring. The eight states are fixed in
# reference/bench-results/tierb-part2-corpus-manifest.md and are not substitutable: no
# reserves, no early stop on a favourable result, no redraw.
#
# The selected tree IS the experimental unit, so every run:
#   * copies the manifest-selected state into a fresh workspace (the source stays read-only)
#   * asserts the copied tree's hash against the manifest BEFORE Claude is invoked
#   * runs the repair path only (--skip-larry): no write phase, Claude takes over mid-repair
#   * uses the Part 1 enterprise-anon requirements — preflight, git seeding, ANON_AUTOCOMMIT
#   * asserts the Claude coder and the egress boundary, and hard-aborts before billing
#   * records the source candidate and the manifest hash in the metrics row
#
#   EGRESS_POLICY=enterprise-anon ./tierb-part2.sh
set -uo pipefail

BENCH="$(cd "$(dirname "$0")" && pwd)"
RUNBUILD="${RUNBUILD:-$BENCH/run-build.py}"
FIX="/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage"
MANIFEST="$BENCH/../reference/bench-results/tierb-part2-corpus-manifest.md"
TAG="${TAG:-tierb2}"

# candidate:expected-tree-sha256 — transcribed from the frozen manifest.
CANDIDATES=(
  "doclinkclean2_challenger__r3:ab9a86b5d580790acaa20001e44f2c010fdaf69c4ed4fabb6a296a24713d2fb1"
  "doclinkclean3_challenger__r5:9b6f811b480bb4533c9477556f311c5f1a9d8832ac7446c2673a5d1b07867525"
  "doclinkclean3_challenger__r1:342891fb4545c34287288794171786322cd653912ad7ce7cf524b97b080883d2"
  "doclinkclean3_control__r2:87c8d7338c514d467fbd03d1fbc043914f7412eadf333f13ac8fbfaafb7d4fd5"
  "doclinkclean3_control__r4:01afa6f1f14a758cb75c544ef7f811f7b2f67c47fe0146f605e49195f07a3b36"
  "doclinkclean3_challenger__r4:dc26e54790ee5377a65cc00ddf67a7fa45c6554e68857bb699de3ae6a1a0c2ca"
  "doclinkclean2_control__r4:3f8f40b33738c1f074722fd675c369b27719b4a403cd813fdcc0c01e3595f643"
  "doclinkclean2_control__r2:151490174e7fa4f55109ae4afef493072eab8cb3bafaa51cf655ad6c80265b11"
)

[ "${EGRESS_POLICY:-}" = "enterprise-anon" ] || {
  echo "FATAL: Tier B is authorised for EGRESS_POLICY=enterprise-anon only (got '${EGRESS_POLICY:-unset}')." >&2
  exit 2; }
[ -f "$MANIFEST" ] || { echo "FATAL: frozen manifest missing: $MANIFEST" >&2; exit 2; }
MANIFEST_SHA=$(sha256sum "$MANIFEST" | cut -d' ' -f1)

SANITIZE=($(python3 "$BENCH/bench_env_contract.py" --names)) || exit 2
CLEAR=(); for v in "${SANITIZE[@]}"; do CLEAR+=(-u "$v"); done

# Hashed from INSIDE src/ so only contents and relative paths count. Hashing from outside
# folds the absolute directory path in, and the digest can never survive the copy it exists
# to verify — which is exactly how the first fake-coder run failed.
tree_hash() { ( cd "$1/src" && find . -name '*.al' -type f | sort | xargs sha256sum ) | sha256sum | cut -d' ' -f1; }

mkdir -p "$BENCH/runs" "$BENCH/logs"
SUMMARY="$BENCH/${TAG^^}-SUMMARY.log"
: > "$SUMMARY"
{
  echo "Tier B Part 2 — Claude takeover of stalled Qwen states"
  echo "registration: reference/exp-tierb-claude-preregistration.md"
  echo "frozen corpus manifest: $(basename "$MANIFEST")  sha256=$MANIFEST_SHA"
  echo "candidates: ${#CANDIDATES[@]} (fixed; no reserves, no early stop, no redraw)"
  echo "path: --skip-larry (repair only — Claude takes over, it does not write from scratch)"
  echo "egress: enterprise-anon (Anthropic only). Scrub covers mirrored FILES, not the prompt."
  echo
} | tee -a "$SUMMARY"

t_all=$(date +%s)
for entry in "${CANDIDATES[@]}"; do
  cand="${entry%%:*}"; want="${entry##*:}"
  srcdir="$BENCH/runs/qwen3-coder_30b__doclink__${cand}"
  name="claude-takeover__${cand}"
  dst="$BENCH/runs/$name"
  log="$BENCH/logs/${name}.log"

  [ -d "$srcdir/src" ] || { echo "$name: ABORT (source state missing: $srcdir)" | tee -a "$SUMMARY"; exit 3; }

  # TRUNCATE the log. Every assertion below greps it, and the run dirs are reused across
  # invocations — appending let a PREVIOUS run's "Coder backend: claude" satisfy this run's
  # backend check. Caught by the fake-pi negative test, which reported 0/8 closure instead
  # of VOID: the guard against a silent pi fallback was itself passing on stale evidence.
  : > "$log"

  rm -rf "$dst"; mkdir -p "$dst"
  cp -r "$srcdir/src" "$dst/"
  chmod -R u+w "$dst/src"          # the copy is writable; the source stays read-only
  cp "$FIX/app.json" "$dst/" 2>/dev/null
  [ -f "$FIX/cleanup.sh" ] && cp "$FIX/cleanup.sh" "$dst/"
  [ -d "$FIX/docs" ] && cp -r "$FIX/docs" "$dst/"
  [ -d "$FIX/.alpackages" ] && cp -r "$FIX/.alpackages" "$dst/"
  sed "s|${FIX}|${dst}|g" "$FIX/larry-handover.prompt.md" > "$dst/larry-handover.prompt.md"

  got=$(tree_hash "$dst")
  if [ "$got" != "$want" ]; then
    echo "$name: ABORT (tree hash mismatch — the experimental unit is not the pinned state)" | tee -a "$SUMMARY"
    echo "    manifest $want" | tee -a "$SUMMARY"
    echo "    copied   $got"  | tee -a "$SUMMARY"
    exit 3
  fi
  echo "$name: tree hash OK ($want)" | tee -a "$SUMMARY"

  git -C "$dst" init -q
  printf '.alpackages/\n.anon/\n*.app\n' > "$dst/.gitignore"
  git -C "$dst" add -A
  git -C "$dst" -c user.email=pipeline@local -c user.name=pipeline \
      commit -q -m "stalled state $cand (Tier B Part 2)" || true

  if ! env "${CLEAR[@]}" EGRESS_POLICY=enterprise-anon CODER_BACKEND=claude \
        ANON_AUTOCOMMIT=1 python3 "$BENCH/tierb_preflight.py" "$dst" >> "$log" 2>&1; then
    echo "$name: ABORT (preflight failed — no Claude call made). See $log" | tee -a "$SUMMARY"
    tail -20 "$log"; exit 3
  fi
  echo "$name: preflight PASS" | tee -a "$SUMMARY"

  t0=$(date +%s)
  env "${CLEAR[@]}" \
    CODER_BACKEND=claude EGRESS_POLICY=enterprise-anon ANON_AUTOCOMMIT=1 \
    MAX_FIX_ROUNDS="${MAX_FIX_ROUNDS:-5}" FIXTURE_DIR="$FIX" \
    BENCH_META="{\"tierb_part\":2,\"source_candidate\":\"$cand\",\"source_tree_sha256\":\"$want\",\"corpus_manifest_sha256\":\"$MANIFEST_SHA\"}" \
    timeout "${RUN_TIMEOUT:-1800}" python3 "$RUNBUILD" --project "$dst" --skip-larry >> "$log" 2>&1
  rc=$?
  dt=$(( $(date +%s) - t0 ))

  if ! grep -q "^Coder backend: claude" "$log"; then
    echo "$name: VOID(backend) in ${dt}s — banner does not show the Claude coder" | tee -a "$SUMMARY"
    grep -E "^(Coder backend|Escalation|Mid tier):" "$log" | sed 's/^/     /' | tee -a "$SUMMARY"
    exit 3
  fi
  if grep -q "^Mid tier:" "$log" || ! grep -q "^Escalation: off" "$log"; then
    echo "$name: VOID(egress) in ${dt}s — an escalation rung was configured" | tee -a "$SUMMARY"
    exit 3
  fi

  if [ $rc -eq 124 ]; then verdict="TIMEOUT"
  elif [ $rc -eq 0 ] && grep -q "^RESULT: PASS" "$log"; then verdict="CLOSED"
  else verdict="NOT-CLOSED($rc)"; fi
  echo "$name: $verdict in ${dt}s" | tee -a "$SUMMARY"
  rm -rf "$dst/.alpackages"
done

echo | tee -a "$SUMMARY"
echo "=== ${TAG^^} SUMMARY ===" | tee -a "$SUMMARY"
closed=$(grep -c ": CLOSED" "$SUMMARY")
tot=$(grep -cE ": (CLOSED|NOT-CLOSED|TIMEOUT)" "$SUMMARY")
echo "  terminal closure: $closed/$tot" | tee -a "$SUMMARY"
grep -E ": (CLOSED|NOT-CLOSED|TIMEOUT)" "$SUMMARY" | sed 's/^/    /' | tee -a "$SUMMARY"
echo "  total $(( ($(date +%s) - t_all) / 60 )) min" | tee -a "$SUMMARY"

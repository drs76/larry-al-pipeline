#!/usr/bin/env bash
# Seeded 2x2, remaining arms. Sequential: one GPU, one shared fixture directory.
#
# Each arm restores the fixture to the SAME pre-seed state, seeds the identical
# defect, then runs --skip-larry so the write phase never runs and the fix loop
# starts from the seeded break. Restoring between arms is what makes the arms
# comparable — a leftover repair from the previous arm would silently become the
# next arm's starting state.
set -uo pipefail

SB=/tmp/claude-1000/-mnt-rojaws-localDev/564fd1e1-49d3-4737-b912-7e0208433035/scratchpad
P=/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage
PIPE=/mnt/rojaws/localDev/setup/pipeline

CLEAR=()
while read -r v; do CLEAR+=(-u "$v"); done < <(python3 "$PIPE/bench_env_contract.py" --names | tr ' ' '\n')

seed() {
  rm -rf "$P/src" && cp -a "$SB/src-backup" "$P/src"
  python3 - <<'PYEOF'
import io
fn = "/mnt/rojaws/localDev/projects/tsg-document-link-2-az-storage/src/codeunit/TSGDocumentLinkAZMgt.Codeunit.al"
old = """        Authorize := SSAuthorization.CreateSharedKey(
            Setup.GetSharedAccessKey(),
            Enum::"Storage Service API Version"::"2022-11-02");"""
new = """        // Workaround for AL0151 - explicitly define enum value
        var ApiVersionEnum: Enum "Storage Service API Version";
        ApiVersionEnum := Enum::"Storage Service API Version"::"2022-11-02";
        Authorize := SSAuthorization.CreateSharedKey(
            Setup.GetSharedAccessKey(),
            ApiVersionEnum);"""
s = io.open(fn, encoding="utf-8").read()
assert old in s and new not in s, "SEED PRECONDITION FAILED"
io.open(fn, "w", encoding="utf-8").write(s.replace(old, new))
PYEOF
}

for arm in invariant-only neither; do
  tree="$SB/$arm/pipeline/run-build.py"
  # Positive assertion per arm, from the file about to run — never from intent.
  inv=$(grep -c 'Declare EVERY variable' "$tree")
  hnt=$(grep -c 'is NOT a missing keyword' "$tree")
  case "$arm" in
    invariant-only) want_inv=1; want_hnt=0 ;;
    neither)        want_inv=0; want_hnt=0 ;;
  esac
  if [ "$inv" != "$want_inv" ] || [ "$hnt" != "$want_hnt" ]; then
    echo "FATAL $arm: invariant=$inv hint=$hnt, wanted $want_inv/$want_hnt" >&2; exit 2
  fi
  echo "=== arm $arm (invariant=$inv hint=$hnt) ==="
  seed || { echo "FATAL: seeding failed for $arm" >&2; exit 2; }
  env "${CLEAR[@]}" python3 "$tree" --project "$P" --skip-larry \
      > "$SB/doclink-probe-$arm.log" 2>&1
  echo "  $arm exit=$? : $(grep -E '^RESULT' "$SB/doclink-probe-$arm.log" || echo 'no RESULT line')"
done

# Leave the fixture as found, not as the last arm left it.
rm -rf "$P/src" && cp -a "$SB/src-backup" "$P/src"
echo "fixture restored to pre-seed state"

#!/usr/bin/env bash
# runtime_probe.sh — assert AL-REFERENCE's RUNTIME claims against a live BC instance.
#
# The third guard on the AL ruleset:
#   validate_al_syntax.py   the ✓ patterns COMPILE
#   probe_al_rules.sh       the ✗ patterns FAIL, with the diagnostic codes we cite
#   runtime_probe.sh (here) the claims about what happens when the code RUNS
#
# Runtime claims are the ones that rot quietly: nothing in the build ever contradicts
# them, so a wrong one survives indefinitely. Building this harness immediately caught
# two — see reference/al-runtime-probes/README.md.
#
# Pipeline: symbols → compile → publish → `bcl test` → uninstall. The probe extension
# is removed afterwards unless -keep is given, so an environment is never left dirty.
# Credentials stay inside bcl (it reads the env's .creds itself); this script never
# sees or handles them.
#
# Usage:
#   ./runtime_probe.sh [-name <env>] [-version <ver>] [-project <dir>] [-keep]
#
# Defaults: env bc2, version 27, project reference/al-runtime-probes.
# Requires: bcl on PATH, a running environment, dotnet altool.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"

ENV_NAME="bc2"
VERSION="27"
PROJECT="$REPO/reference/al-runtime-probes"
KEEP=0
PUBLISH_TOOLKIT=0

while [ $# -gt 0 ]; do
  case "$1" in
    -name)    ENV_NAME="$2"; shift 2 ;;
    -version) VERSION="$2";  shift 2 ;;
    -project) PROJECT="$2";  shift 2 ;;
    -keep)    KEEP=1;        shift ;;
    -publish-toolkit) PUBLISH_TOOLKIT=1; shift ;;
    -h|--help) sed -n '2,25p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

command -v bcl >/dev/null || { echo "ERROR: bcl not on PATH"; exit 1; }
AL="$HOME/.dotnet/tools/al"
[ -x "$AL" ] || { echo "ERROR: dotnet altool not at $AL"; exit 1; }
[ -f "$PROJECT/app.json" ] || { echo "ERROR: no app.json in $PROJECT"; exit 1; }

APP_ID=$(python3 -c "import json,sys;print(json.load(open('$PROJECT/app.json'))['id'])")
APP_NAME=$(python3 -c "import json,sys;print(json.load(open('$PROJECT/app.json'))['name'])")
APP_VER=$(python3 -c "import json,sys;print(json.load(open('$PROJECT/app.json'))['version'])")
APP_FILE="$PROJECT/${APP_NAME// /}.app"

say() { printf '\n=== %s ===\n' "$1"; }

cleanup() {
  [ "$KEEP" = "1" ] && { echo "(-keep: leaving $APP_NAME published on $ENV_NAME)"; return; }
  say "cleanup"
  bcl exec -name "$ENV_NAME" \
    "Uninstall-NAVApp -ServerInstance BC -Name '$APP_NAME' -Version $APP_VER -Force -ErrorAction SilentlyContinue;
     Unpublish-NAVApp  -ServerInstance BC -Name '$APP_NAME' -Version $APP_VER -ErrorAction SilentlyContinue;
     'removed'" 2>&1 | tail -1
}
trap cleanup EXIT

# `bcl test` wants the RESOLVED artifact version (27.10.53179.0), not the major (27) —
# given a major it looks for onprem/27/gb/manifest.json and reports a cache miss that
# reads like a missing download. Resolve it here so callers can pass either.
if ! printf '%s' "$VERSION" | grep -qE '^[0-9]+(\.[0-9]+){3}$'; then
  say "resolve artifact version"
  RESOLVED=$(bcl artifact -version "$VERSION" -type onprem -country gb 2>&1 \
             | grep -oE '[0-9]+(\.[0-9]+){3}' | head -1)
  if [ -n "$RESOLVED" ]; then
    echo "$VERSION -> $RESOLVED"
    VERSION="$RESOLVED"
  else
    echo "WARNING: could not resolve '$VERSION' to a full artifact version; passing through"
  fi
fi

say "symbols from $ENV_NAME"
bcl symbols -name "$ENV_NAME" -out "$PROJECT/.alpackages" 2>&1 | tail -3 || exit 1

say "compile"
# The compiler is the referee here as everywhere: a probe that does not build is a probe
# whose claim was written against AL that does not exist.
if ! "$AL" compile /project:"$PROJECT" /packagecachepath:"$PROJECT/.alpackages" \
     /out:"$APP_FILE" 2>&1 | grep -E "error|Compilation ended"; then
  echo "compile produced no output" >&2
fi
[ -f "$APP_FILE" ] || { echo "ERROR: compile produced no .app"; exit 1; }

say "publish to $ENV_NAME"
bcl publish -name "$ENV_NAME" -sync-mode forcesync "$APP_FILE" 2>&1 | tail -2 || exit 1

say "run tests"
# bcl test publishes Microsoft's Test Runner from the artifact cache, drives the
# client-services endpoint inside the guest and returns XUnit results.
TESTLOG="$(mktemp)"
# bcl test publishes Microsoft's test toolkit ONLY when -version is given. Most
# environments already ship it installed, and re-publishing then fails outright:
#   422 ... tries to replace the existing AppSource app 'Test Runner' ... which is a
#   dependency to 'Performance Toolkit by Microsoft, AI Test Toolkit by Microsoft'
# So omit -version by default and make toolkit publishing opt-in via -publish-toolkit
# (needed only on an environment that genuinely lacks the Test Runner).
if [ "$PUBLISH_TOOLKIT" = "1" ]; then
  bcl test -name "$ENV_NAME" -version "$VERSION" -extension "$APP_ID" 2>&1 | tee "$TESTLOG" | tail -40
else
  bcl test -name "$ENV_NAME" -extension "$APP_ID" 2>&1 | tee "$TESTLOG" | tail -40
fi
rc=${PIPESTATUS[0]}

say "result"
# Classify from the CONSOLE results, not from bcl's exit code or the XML file. bcl
# streams "Testfunction <name> Success|Failure" lines from the in-guest runner; those
# are the actual outcomes. The XML on the artifact share sometimes does not appear, and
# an earlier version of this script reported "no test results" as INCONCLUSIVE while
# seven real results sat in the log above it.
PASSED=$(grep -c "Testfunction .* Success" "$TESTLOG")
FAILED=$(grep -c "Testfunction .* Failure" "$TESTLOG")
TOTAL=$((PASSED + FAILED))

if [ "$TOTAL" = "0" ]; then
  echo "INCONCLUSIVE — no test ran; nothing was proved either way."
  grep -m1 -E "artifact not in cache|could not connect|422 Unprocessable|not on PATH" "$TESTLOG" \
    | sed 's/^/  /' || true
  echo "  If the Test Runner is missing from the environment, add -publish-toolkit"
  echo "  (and ensure the artifact is cached: bcl artifact -download -version $VERSION -type onprem -country gb)"
  rm -f "$TESTLOG"; exit 2
fi

echo "$PASSED/$TOTAL runtime claims hold on $ENV_NAME"
if [ "$FAILED" = "0" ]; then
  rm -f "$TESTLOG"
  echo "PASS — every documented runtime claim still holds"
  exit 0
fi
echo
echo "FAILED claims:"
grep "Testfunction .* Failure" "$TESTLOG" | sed 's/^ */  /'
echo
echo "A failure means the DOC is stale, not the test. The instance is ground truth:"
echo "fix AL-REFERENCE / AL-SYNTAX, then re-run."
rm -f "$TESTLOG"
exit 1

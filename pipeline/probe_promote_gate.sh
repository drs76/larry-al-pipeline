#!/usr/bin/env bash
# probe_promote_gate.sh — does `alw promote` actually INVOKE its receipt gate?
#
# Executor phase 5: purpose-built probes for paths the doclink fixture never exercises.
# A normal build stops at RESULT: PASS. Nothing in the benchmark corpus ever calls
# promote, so the gate that decides what ships is exercised by nobody.
#
# WHY THIS IS NOT COVERED BY test_pipeline_security.py
# ----------------------------------------------------
# Those tests call build_receipt.verify() directly and prove the CHECK is correct:
# missing receipt, changed tree and bare-compile results are all rejected. They say
# nothing about whether cmd_promote calls it. That gap is not hypothetical — twice in
# one session a correct check sat behind a broken invocation (a publish gate that
# exited 2 and read as "clean"; a path exemption that could never match). Logic tested
# in isolation, wiring untested, is the recurring shape.
#
# So this probe drives the REAL `alw promote` and asserts the SIDE EFFECT: after a
# refusal, is the tree still sitting in prototypes, or was it moved anyway?
#
# Costs nothing: no network, no model, no money. PROTOTYPES_DIR and CODE_AL are
# redirected to temp dirs, so real prototypes and Code/AL are never touched.
#
# Usage:  pipeline/probe_promote_gate.sh
set -uo pipefail

SETUP_DIR="${SETUP_DIR:-/mnt/rojaws/localDev/setup}"
ALW="$SETUP_DIR/tooling/alw"
[ -x "$ALW" ] || [ -f "$ALW" ] || { echo "FATAL: alw not found at $ALW" >&2; exit 2; }

PASS=0; FAIL=0
say() { printf "  %-58s %s\n" "$1" "$2"; }
ok()  { PASS=$((PASS+1)); say "$1" "PASS"; }
bad() { FAIL=$((FAIL+1)); say "$1" "FAIL — $2"; }

# One isolated world per case: fresh prototypes/ and Code/AL under a temp root.
new_world() {
    W=$(mktemp -d)
    export PROTOTYPES_DIR="$W/prototypes" CODE_AL="$W/code" SETUP_DIR
    mkdir -p "$PROTOTYPES_DIR/demo/src" "$CODE_AL"
    printf 'codeunit 50100 "Demo"\n{\n}\n' > "$PROTOTYPES_DIR/demo/src/Demo.Codeunit.al"
    printf '{"id":"x","name":"demo"}\n' > "$PROTOTYPES_DIR/demo/app.json"
}
drop_world() { rm -rf "$W"; }

receipt() {   # write a receipt for the demo tree; args passed to build_receipt.write
    python3 - "$PROTOTYPES_DIR/demo" "$@" <<'PY'
import sys, os
sys.path.insert(0, os.path.join(os.environ["SETUP_DIR"], "pipeline"))
import build_receipt
root = sys.argv[1]
bare = "--bare" in sys.argv
build_receipt.write(root, referee_ok=True, analyzers=["CodeCop"],
                    bare_compile_only=bare, coder_model="probe")
PY
}

run_promote() { ( cd "$SETUP_DIR" && bash "$ALW" promote demo ) >/dev/null 2>&1; }

echo "probe_promote_gate — does promote invoke its own receipt gate?"

# 1. No receipt at all -> must refuse AND leave the tree where it was.
new_world
run_promote; rc=$?
if [ $rc -eq 0 ]; then bad "no receipt -> refuses" "promote exited 0"
elif [ ! -d "$PROTOTYPES_DIR/demo" ]; then bad "no receipt -> tree survives" "tree was MOVED despite refusal"
elif [ -e "$CODE_AL/demo" ]; then bad "no receipt -> nothing shipped" "appeared in Code/AL"
else ok "no receipt -> refuses, tree untouched"; fi
drop_world

# 2. Valid receipt -> promotes, and the tree actually arrives.
new_world
receipt
run_promote; rc=$?
if [ $rc -ne 0 ]; then bad "valid receipt -> promotes" "exited $rc"
elif [ ! -d "$CODE_AL/demo" ]; then bad "valid receipt -> lands in Code/AL" "not present"
elif [ -d "$PROTOTYPES_DIR/demo" ]; then bad "valid receipt -> leaves prototypes" "still in prototypes"
else ok "valid receipt -> promotes and lands"; fi
drop_world

# 3. Tree edited AFTER the receipt -> hash mismatch, must refuse.
new_world
receipt
printf '// edited after the receipt\n' >> "$PROTOTYPES_DIR/demo/src/Demo.Codeunit.al"
run_promote; rc=$?
if [ $rc -eq 0 ]; then bad "edited after receipt -> refuses" "promote exited 0"
elif [ ! -d "$PROTOTYPES_DIR/demo" ]; then bad "edited after receipt -> tree survives" "tree was MOVED"
else ok "edited after receipt -> refuses, tree untouched"; fi
drop_world

# 4. Bare-compile-only receipt (no analyzers) -> must refuse.
new_world
receipt --bare
run_promote; rc=$?
if [ $rc -eq 0 ]; then bad "bare-compile receipt -> refuses" "promote exited 0"
else ok "bare-compile receipt -> refuses"; fi
drop_world

# 5. The documented override must still work — otherwise the escape hatch is a lie.
new_world
( cd "$SETUP_DIR" && PROMOTE_FORCE=1 bash "$ALW" promote demo ) >/dev/null 2>&1; rc=$?
if [ $rc -ne 0 ]; then bad "PROMOTE_FORCE=1 overrides" "exited $rc"
elif [ ! -d "$CODE_AL/demo" ]; then bad "PROMOTE_FORCE=1 promotes" "not in Code/AL"
else ok "PROMOTE_FORCE=1 overrides the gate"; fi
drop_world

echo
echo "  $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]

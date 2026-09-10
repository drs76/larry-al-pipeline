#!/usr/bin/env bash
# probe_anon_mirror.sh — is the scrubbed MIRROR actually free of real identifiers?
#
# Executor phase 5 — probes for paths the doclink fixture never exercises. doclink runs
# local-only, so the anon hook never fires during a benchmark; the code path that
# decides what a cloud model is allowed to see is exercised by nobody.
#
# WHY THIS IS NOT COVERED BY THE UNIT TESTS
# -----------------------------------------
# test_anon_map asserts residual_reals() == [] on the STRING that forward() returns, and
# test_anon_workspace drives run_workspace with a fake coder. Both are correct and
# neither inspects the MIRROR DIRECTORY — the artefact an agentic coder actually opens,
# greps and reads. A file that never reached forward() (untracked, binary, skipped,
# written by a later step) is invisible to a string-level assertion and perfectly
# visible to the coder.
#
# So this probe builds a real mirror from a repo seeded with real identifiers and walks
# EVERY BYTE OF EVERY FILE in it. Assert the artefact, not the function.
#
# Costs nothing: no network, no model, no spend. Everything happens in temp dirs.
#
# Usage:  pipeline/probe_anon_mirror.sh
set -uo pipefail
SETUP_DIR="${SETUP_DIR:-/mnt/rojaws/localDev/setup}"
export PYTHONPATH="$SETUP_DIR/pipeline"

python3 - <<'PY'
import os, sys, tempfile, subprocess, shutil
sys.path.insert(0, os.environ["PYTHONPATH"])
import anon_map, anon_workspace

PASS = FAIL = 0
def ok(m):  globals().__setitem__("PASS", PASS+1); print(f"  {m:<58} PASS")
def bad(m, why): globals().__setitem__("FAIL", FAIL+1); print(f"  {m:<58} FAIL — {why}")

# (CATEGORY, real) pairs, the format load_names() yields from names.tsv.
LITS  = [("ORG", "AcmeCorp"), ("HOST", "acme-internal.example"), ("PERSON", "JaneDoe")]
REALS = [r for _c, r in LITS]

def build(seed_extra=None, scrub=True):
    """A git repo carrying real identifiers -> a built mirror. Returns (repo, mirror)."""
    repo = tempfile.mkdtemp(); mirror = tempfile.mkdtemp()
    os.makedirs(repo + "/src")
    open(repo+"/src/a.al","w").write(
        'codeunit 1 "AcmeCorp Mgt" { // owner JaneDoe, host acme-internal.example\n}\n')
    open(repo+"/README.md","w").write("AcmeCorp internal. Contact JaneDoe.\n")
    open(repo+"/.gitignore","w").write("secret-notes.txt\n")
    open(repo+"/secret-notes.txt","w").write("UNTRACKED: AcmeCorp merger with JaneDoe\n")
    open(repo+"/logo.bin","wb").write(bytes(range(256))*4)
    if seed_extra: seed_extra(repo)
    for c in (["git","init","-q"],["git","add","-A"],
              ["git","-c","user.email=a@b","-c","user.name=t","commit","-q","-m","x"]):
        subprocess.run(c, cwd=repo, check=True)
    amap = anon_map.AnonMap()
    lits = LITS if scrub else []        # scrub=False is the MUTANT: nothing declared
    anon_workspace.build_mirror(repo, amap, lits, mirror)
    return repo, mirror

def mirror_files(mirror):
    return [os.path.join(r,f) for r,_,fs in os.walk(mirror) for f in fs if ".git" not in r]

# --- 1. no real identifier survives anywhere in the mirror --------------------------
repo, mirror = build()
leaks = []
for p in mirror_files(mirror):
    body = open(p, encoding="utf-8", errors="replace").read()
    for real in REALS:
        if real in body:
            leaks.append(f"{os.path.relpath(p,mirror)} contains {real!r}")
ok("no real identifier anywhere in the mirror") if not leaks else bad(
    "no real identifier anywhere in the mirror", "; ".join(leaks[:3]))

# --- 2. the untracked (gitignored) file must not be mirrored at all -----------------
rel = [os.path.relpath(p, mirror) for p in mirror_files(mirror)]
if "secret-notes.txt" in rel:
    bad("gitignored file is not mirrored", "secret-notes.txt was mirrored")
else:
    ok("gitignored file is not mirrored")

# --- 3. the binary is skipped, not written as replacement-char soup ----------------
if "logo.bin" in rel:
    bad("binary skipped, not mangled", "logo.bin appeared in the mirror")
else:
    ok("binary skipped, not mangled")
shutil.rmtree(repo); shutil.rmtree(mirror)

# --- 4. a HIGH secret aborts the whole mirror, fail closed -------------------------
def seed_secret(r):
    open(r+"/creds.env","w").write("AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE\n")
try:
    repo, mirror = build(seed_secret)
    bad("HIGH secret aborts the mirror", "build_mirror returned instead of raising")
    shutil.rmtree(repo); shutil.rmtree(mirror)
except anon_workspace.SecretAbort:
    ok("HIGH secret aborts the mirror")
except Exception as e:
    bad("HIGH secret aborts the mirror", f"wrong exception: {type(e).__name__}")

# --- 5. DISCRIMINATION: with nothing declared, the probe must SEE the leak ---------
repo, mirror = build(scrub=False)
saw = any(real in open(p,encoding="utf-8",errors="replace").read()
          for p in mirror_files(mirror) for real in REALS)
ok("probe detects an unscrubbed mirror (self-test)") if saw else bad(
    "probe detects an unscrubbed mirror (self-test)",
    "probe saw nothing with scrubbing OFF — it cannot detect what it exists to catch")
shutil.rmtree(repo); shutil.rmtree(mirror)

print(f"\n  {PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
PY

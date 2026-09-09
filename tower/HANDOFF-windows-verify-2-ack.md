# deb → Windows: both test gaps fixed, please re-run

Ack of `HANDOFF-deb-windows-verify-2.md`. The in-flight work you parked behind is done and
pushed — pull to `7eb39e3` or later.

Both diagnoses were exact. I verified each before changing anything and neither needed
re-investigation.

## 1. `al_testgen` — fixed at the source, not just in the assertion

You identified it as "functionally harmless, the assertion isn't portable". Half right, and
the other half is worth knowing: `os.path.join(root, "src/test")` leaves a **non-native
separator inside a constructed path**, and this pipeline does path *containment* checks on
string comparison — `pathguard.is_safe`, the edit-block applier, the mirror abort. Harmless
here, but not a property to leave lying around on the platform where it differs.

So `al_testgen.write()` now normalises the path it builds, and the assertion normalises
**both** sides rather than only the needle. Reproduced your failure from Linux with
`ntpath`, which gives Windows semantics:

```
before   C:\tmp\proj\src/test    'src\test' in path == False   ← your crash
after    C:\tmp\proj\src\test    'src\test' in path == True
```

`AL_TEST_DIR` still overrides, and now works whichever separator you give it.

## 2. `test_pipeline_security` — skips the symlink leg, not the test

`WinError 1314` is an environment gap as you said, but crashing the suite is a code bug:
one unavailable privilege was taking down thirteen unrelated security assertions.

Now only the **symlink leg** skips. Traversal, absolute paths, tilde and empty-string
containment are portable and are most of what those tests guard, so they still run. Skips
are named and counted under the pass line — same rule `test_al_intelligence` already
follows for missing symbols, because a skip that quietly drops coverage is the exact
failure mode that file exists to prevent.

Verified by forcing `os.symlink` to raise `WinError 1314` in-process here:

```
before   crash, whole suite lost
after    exit 0 — "14 PASS, 2 leg(s) skipped"
```

Enabling Developer Mode on that box would restore the two legs. Worth doing, since they
cover symlink-based containment escape and the mirror abort — real properties, not
ceremony.

## What I could not do

**I cannot run these on Windows.** Both fixes are reproduced here by simulating the
platform behaviour, not assumed correct. Please re-run all 11 `pipeline/test_*.py` and
report anything still failing — including the count, since a suite that now *passes* by
skipping too much would be a worse outcome than the crash.

## Also waiting for you on that box

The repo moved a long way while this was parked. `git pull` then the verify steps now in
`windows-host-setup.md` §10 — expect **273/273** on `test_al_intelligence.py`; a failure is
the signal, not the number.

Landed since your last pull: the pi stdin wedge fix (`8eb6f67`, plus `5a015b8` for the go
and cs copies that were missed), one shared `coder.py` replacing three drifted `run_pi`
implementations, grounding state, run-level declared-vs-observed config verification, a
`fixture_commit` provenance repair, and the Bonsai restore.

The `.CMD` argv `@file` workaround moved into `coder.py` during the refactor. It is
byte-identical and I verified it is present, but it has only ever executed on Windows — so
if a build reports `Wrote 0/N expected files` on the **first** attempt, that is the
signature and I want to know.

## WorkPrompts

Left uncommitted, as you did. Dave's call.

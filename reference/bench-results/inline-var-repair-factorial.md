# RESULTS — inline-var repair, 2x2 component attribution (doclink, seeded)

Intervention: commit `7784470`, two changes to the repair path of `run-build.py` —
a declaration invariant in `build_file_rewrite_msg`, and a guarded AL0104/AL0107
hint in `known_fix_hints`.

Probes: seeded, `--skip-larry`, 2026-09-01. Four cells, n=1 each.
Fixture: `tsg-document-link-2-az-storage`, `fixture_commit 3240e31`, handover
`e82168cb3857`. Model `ollama/qwen3-coder:30b`, escalation off, egress local-only.
Raw logs, assertions and hashes: `seeded-2x2/` beside this file.

🧭 **The one idea:** each intervention cleared the seeded cascade on its own. The pair-level
attribution in `7784470` was not wrong, it was **understated** — and the final PASS/FAIL
column is not what shows this.

## Why a seeded probe, not a natural A/B

The natural 5+5 A/B (`dlinvar`, same day, `pre 0548e1f` vs `post 7784470`, interleaved)
produced **no test of this fix**. The targeted defect occurred 0/10 times, and the
pre-registered endpoint counted cascade *occurrence* while the treatment acts only on
cascade *resolution* — the write phase is byte-identical between arms, so the treatment
cannot move an occurrence rate. Classified as a failed endpoint/design test, not a failed
treatment test. See `dlinvar-artifacts/` and memory `feedback_endpoint_mechanism_mismatch`.

Seeding is what made component attribution possible at all.

## Treatment matrix — verified, not assumed

Each arm's compiled treatment was asserted from the file about to execute, immediately
before the run, and captured in `seeded-2x2/ASSERTIONS.txt`:

    neither          invariant=0 hint=0     (worktree at 0548e1f)
    hint-only        invariant=0 hint=1     (7784470, invariant hunk removed)
    invariant-only   invariant=1 hint=0     (7784470, hint hunk removed)
    both             invariant=1 hint=1     (7784470 as committed)

Every arm restored the fixture to the same pre-seed state and seeded the identical
declaration, so no arm inherited another's repair.

## Primary outcome — the first repair transition

| cell | inv | hint | rewrites | hint fired | first transition | cascade |
|---|---|---|---|---|---|---|
| neither | 0 | 0 | 8 | 0 | 46 -> 46 | **not cleared** |
| hint-only | 0 | 1 | 1 | 1 | 46 -> 1 | **cleared** |
| invariant-only | 1 | 0 | 1 | 0 | 46 -> 1 | **cleared** |
| both | 1 | 1 | 2 | 1 | 46 -> 46 -> 1 | **cleared** |

Untreated stays at 46 across eight consecutive file-rewrites — an exact reproduction of
the natural run that motivated the fix. Each intervention alone goes 46 -> 1.

**Finding: each intervention was individually sufficient in this seeded reproduction.
Necessity of either component was not established.**

Two distinct observed routes, not a claim of general mechanistic independence:
`invariant-only` cleared with **zero hints applied**, so it works through the rewrite
instruction alone; `hint-only` cleared without the invariant present. Neither observed
success depended on the other component here.

## What the final verdict column must not be used for

Terminal results were `PASS 0` (hint-only), `FAIL 3` (invariant-only), `FAIL 1` (both).
These are **not** a ranking. They are downstream of unrelated residual errors and the
unmask reset, which is a separate failure mode from the one under test — `invariant-only`
cleared 46 -> 1 and only then lost ground. `both` needing two rewrites where the singles
needed one is likewise within run-to-run variance at n=1. The only contrast that survives
this sample size is treated vs untreated.

## Sharp edges

- **`FAIL(N)` in a suite summary is the process exit code, not an error score.** Every
  historical "0/10, all FAIL(1)" row says nothing about scores.
- **run-build's "best achieved" is not the minimum score observed.** They diverge whenever
  unmask resets the baseline (`dlinvar` challenger r4: minimum 6, reported 13).
- **`error score: N` also appears inside `* new best (error score: N)`.** An unanchored
  regex double-counts the first entry of every trajectory; the first draft of the results
  table here did exactly that.
- **run-build logs the hint COUNT, never the hint text.** Detecting whether a specific hint
  fired by grepping its wording finds nothing; read `known-fix: N hint(s) appended` at the
  seeded round, where only AL0104/AL0107 are present.

## Provenance and one destroyed artifact

The original `both` observation (probe A) had its raw log **overwritten by operator error
before archival and is unrecoverable**. Its finding is preserved in `7784470`'s message but
is no longer independently auditable. The `both` cell above is a **replacement re-run** from
the same seed, and only that replacement is treated as the auditable observation. Nothing was
reconstructed from recollection. Full account: `seeded-2x2/ARTIFACT-INCIDENT.md`.

Corroboration is kept literal: `hint-only` independently reproducing 46 -> 1 is evidence for
the hint-only cell, not for `both`.

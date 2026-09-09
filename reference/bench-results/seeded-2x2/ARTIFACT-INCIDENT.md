# Destroyed artifact — seeded probe A (`both` cell)

## What was lost

The raw run log for the original seeded probe A (both interventions active,
2026-09-01 ~20:04-20:10) was **overwritten and is unrecoverable**.

Cause: an operator `cp doclink-run.log doclink-probeA.log` intended to alias a log
for the analyser. Probe A's log already occupied that exact path, so the copy
replaced it with the unrelated natural run-1 log. No backup existed — the dlinvar
A/B artifacts had been archived, the seeded-probe logs had not.

Detected immediately after, by `cmp` against the source file. The corrupted alias was
deleted rather than kept, so it cannot be mistaken for probe A data.

## What this does and does not change

- The original probe A **observation** is preserved in the contemporaneous record:
  this session's transcript and commit 7784470's message. The claim in that commit
  does not need withdrawing.
- The original observation is **no longer independently auditable**. Nothing
  reconstructs it — a trajectory recalled from a conversation is not an artifact.
- Therefore the `both` cell was **re-run from the same seed**, and ONLY the
  replacement run is treated as the auditable observation for that cell.

## Cell accounting stays literal

Probe B (hint-only) independently reproduced 46 -> 1 -> PASS. That is corroboration
of the same mechanism under a different treatment cell. It is **not** evidence for
the `both` cell and must not be counted as such.

## Containment applied

- Each arm's treatment assertion (invariant/hint counts, read from the file about to
  execute) is captured alongside its raw log, so the matrix is a verified treatment
  matrix rather than a naming convention.
- All four seeded logs are archived to `runs/dlinvar-artifacts/seeded-2x2/` as each
  arm completes, not at the end of the session.

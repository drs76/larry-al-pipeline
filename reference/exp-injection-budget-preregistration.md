# Pre-registration — injection budget and fix-round cap on doclink

Written 2026-08-29, **before** any arm ran. Fixture: `tsg-document-link-2-az-storage`.
Model: `ollama/qwen3-coder:30b`, both arms, every arm. Egress: local-only, escalation off.

## Why

`253273c` fixed two defects in topic selection: the selector was scoring text the pipeline
had appended to its own prompt, and the budget cap evicted genuinely-selected topics in
silence. doclink now receives `08-data-storage` and loses `07-events-errors`, because all
five topics it wants total 15.14k against `INJECT_BUDGET_K=14`.

One post-fix run scored 1 (from a pre-fix 6) and was still descending when it hit the round
cap. n=1 proves nothing about efficacy — AL_BRAIN looked good at n=3 and reversed at n=10 —
so this measures it properly.

## Primary metric — declared before the fact

**Best error score achieved per run** (lower is better), compared by Mann-Whitney U.

**Not pass rate.** doclink's established baseline is 0/10 across n=40, so pass rate is
expected to be 0/10 in every arm and cannot discriminate. An arm that ends at score 1 and an
arm that ends at score 8 are both "FAIL" and are not the same result. Pass rate is still
recorded, and a non-zero pass in any arm is reportable — but it is not the test.

Secondary, recorded and reported, not tested:
- error-class histogram per arm (AL0173/AL0151 went to zero in the pilot; AL0133 rose 2 → 34
  — a vanished class usually unmasks another, and that needs watching, not celebrating)
- wall-clock and rounds consumed, so a win that costs 2x time is visible as such
- whether the best score arrives on the final round (evidence the cap binds)

## Arms

Two interleaved pairwise suites, because `bench-run-suite.sh` is a two-arm harness and its
arm isolation is the part worth keeping. n=10 per arm.

**Suite `injab`** — does the extra topic pay?
| arm | INJECT_BUDGET_K | MAX_FIX_ROUNDS | doclink receives |
|---|---|---|---|
| control | 14 | 8 | 00, 01, 02, 08-data-storage |
| challenger | 16 | 8 | the above **plus** 07-events-errors (15.14k) |

**Suite `roundab`** — does the round cap bind?
| arm | INJECT_BUDGET_K | MAX_FIX_ROUNDS |
|---|---|---|
| control | 14 | 8 |
| challenger | 14 | 16 |

Control is identical in both suites, so its 20 runs also test session-to-session stability.
If the two control samples differ materially, both suites are suspect and get reported as
such rather than pooled.

## Stopping rule

Fixed n=10 per arm. No peeking-and-extending: the sample size is set here.
`RUN_TIMEOUT=3600` per run; a TIMEOUT is recorded as its own verdict and excluded from the
score distribution (a wedged pi is not a model result — the known
"stream ended without finish_reason" bug, seen again in yesterday's go/cs suite where
b64forward burned the full 1200s write budget).

## What would change practice

- Challenger wins `injab` → raise `INJECT_BUDGET_K` to 16 as the default.
- Challenger wins `roundab` → the cap, not the model, was the binding constraint on doclink,
  and `project_incremental_ratchet`'s "route ABS-heavy AL to escalation" needs revisiting.
- Neither wins → keep `253273c` as committed. The fix already pays for itself on p1
  (13.56k → 9.33k injection, identical build result), and that does not depend on doclink.

Null results are reported. `project_mid_ladder_experiment` and `project_routing_economics`
both closed on nulls and the nulls were the point.

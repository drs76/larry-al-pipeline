# Pre-registration — is MAX_FIX_ROUNDS=5 an artificial ceiling?

Written 2026-08-31, **before** any arm ran. Model `ollama/qwen3-coder:30b` both arms.
Local-only, escalation off.

## Why

doclink's local pass rate moved from 2/192 to 13/78, and the cause is `MAX_FIX_ROUNDS`, not any
code change: every historical run used the `bench-run-suite.sh` default of 5, and 10 of the 13
new passes first reached error score 0 at round 6 or later. Detail in
`exp-doclink-topic-swap-amendment3.md`.

That reconstruction is post-hoc — different dates, code and operator, with the counterfactual
produced by truncating rounds after the fact. It identifies the cause well enough to
disqualify a conclusion; it is not a controlled result. This suite is the controlled one.

The stake is not doclink. Two closed findings — `project_doc_link_az_storage` and
`project_incremental_ratchet` — concluded a **model capability ceiling** from runs that were all
capped at 5, and the routing guidance for ABS-heavy AL rests on that. If the cap was binding,
the ceiling was the harness.

## Arms

| arm | MAX_FIX_ROUNDS |
|---|---|
| control | 5 — the historical default behind every prior conclusion |
| challenger | 8 — the value used from 2026-08-29 |

Interleaved, one session, `bench-run-suite.sh` arm isolation (61-var derived clear-list).
Nothing else varies: `INJECT_TOPICS=auto`, current HEAD, same fixture revisions.

## Fixtures and n

| fixture | n per arm | why |
|---|---|---|
| doclink | 20 | the fixture the claim was built on |
| p4 | 10 | repair-depth fixture, uses ~1 round — tests whether the cap binds anywhere else |

**p1 and map are excluded deliberately, not overlooked.** Both pass with **0** fix rounds, so the
cap provably cannot bind on them. That is a logical exclusion from observed behaviour, not an
assumption about what they would do.

60 runs, ~7 hours.

## Primary metric

**Pass rate, Fisher exact, two-tailed, per fixture.** Same justification as the topic-swap
suite: doclink is no longer floor-bound, so pass rate discriminates, and best error score was
dead null across `injab`, `roundab` and `topicab3` while never tracking the passes.

Reported separately per fixture, not pooled — the hypothesis is that the cap binds on doclink
and not on p4, so pooling would hide the thing being tested.

## Predictions, recorded in advance

1. **doclink: challenger > control.** Expect control ≈ 3-4% and challenger ≈ 15-20%.
2. **p4: null.** It converges in about one round, so the cap should not bind.

Prediction 2 is the one that can embarrass this hypothesis. If p4 also improves, the effect is
not "the cap truncated doclink's convergence" but something broader about round budget, and the
mechanism above is wrong.

## Stopping rule

Fixed n, set here. No extension after the fact. `RUN_TIMEOUT=3600`; TIMEOUT is recorded as its
own verdict and excluded from the pass-rate denominator. More than 3 exclusions in any arm and
the suite is reported as compromised rather than analysed.

## Verification, before analysis

- every run's banner shows escalation off and no mid rung
- every run's actual max round is ≤ its arm's cap — the arm asserted from behaviour, not from
  the variable we believe we passed. `injab` passed arm-isolation while both arms ran the same
  configuration, and `topicab`'s control silently lost a topic to ctx-guard. Assert the effect.

## What would change practice

- **Prediction 1 holds:** `MAX_FIX_ROUNDS=8` becomes the default in `bench-run-suite.sh`, and the
  capability-ceiling conclusions in `project_doc_link_az_storage` and
  `project_incremental_ratchet` are marked as measured under a binding harness cap. The routing
  guidance may still stand on cost, but not on capability.
- **Both null:** the historical difference is not the cap after all, and the amendment-3
  attribution is wrong and must be withdrawn.
- **p4 also improves:** mechanism is wrong; re-open with the round budget itself as the variable.

# Amendment 1 — doclink topic-swap suite

Amends `exp-doclink-topic-swap-preregistration.md`. Written 2026-08-30, before the re-run.
The original suite was stopped after 3 runs and produced no usable data; nothing here is
being changed in the light of results, because there are none.

## Why the original arms were wrong

The pre-registration declared:

| arm | INJECT_TOPICS |
|---|---|
| control | `00-gotchas,01-syntax-style,02-objects,07-events-errors` |
| challenger | `00-gotchas,01-syntax-style,02-objects,08-data-storage` |

The control never injected `07-events-errors`. A second budget — `ctx_budget_k()`, 60% of
num_ctx — caps the assembled prompt and trims injected topics from the tail. doclink carries
~7.9k of handover plus BCQuality rules, so the declared control assembled to 21.5k against a
19.66k ceiling and `07-events-errors` was cut before the model saw it. The control actually
ran three topics.

By luck that was still the right comparison: pre-fix doclink also lost `07-events-errors` to
the same trim, so `00,01,02` genuinely is what the old code delivered. But the file said one
thing and the runs did another, and a pre-registration that has to be reinterpreted after the
fact is not doing its job.

The same mechanism voided the earlier `injab` suite outright: its budget-16 challenger
selected five topics and ctx-guard deleted the fifth, so both arms ran the identical
configuration and returned U=50.0 of 100 — a thing compared with itself. Fixed in `eeae64b`,
which gives selection the real headroom so the two budgets can no longer disagree.

## Corrected arms

| arm | INJECT_TOPICS | inject | assembled |
|---|---|---|---|
| control | `00-gotchas,01-syntax-style,02-objects` | 9.33k | 17.3k |
| challenger | `00-gotchas,01-syntax-style,02-objects,08-data-storage` | 10.92k | 18.9k |

Both verified under the 19.66k ceiling, so neither is trimmed and each arm runs exactly what
it declares. Stating the control as three topics also removes the dependency on ctx-guard
happening to drop the fourth.

Everything else stands: n=20 per arm, interleaved, `qwen3-coder:30b` both arms,
`MAX_FIX_ROUNDS=8`, local-only, escalation off, fixed stopping rule, no extension after the
fact.

## Added verification step

After the suite, assert every run's `inject:` line matches its arm's declaration. The suite's
own `assert_arm` only checks the escalation and mid rungs, which is why `injab` passed
arm-isolation while measuring nothing. An arm that does not inject what it declared is void,
and that must be caught by a check rather than by noticing an implausible U statistic later.

## Primary metric unchanged

Pass rate, Fisher exact, two-tailed. The justification is in the original file and has not
changed: doclink is no longer floor-bound, so pass rate discriminates, while best error score
was dead null across both prior suites and did not track passes.

## Note on the wedge

Runs may hang: pi occasionally enters a state where it burns the full write timeout at ~0.4%
CPU and writes nothing. Root cause unresolved — the prompt, model, pi version, invocation and
prompt size are all eliminated, and the same prompt runs clean minutes later. It latches once
triggered and clears when the stuck processes are killed.

`329fcc5` bounds the cost at one write timeout rather than three. A wedged run is recorded as
TIMEOUT and excluded from the pass-rate denominator, exactly as the original stopping rule
says — a hung harness is not a model result. If more than 3 runs per arm are lost this way the
suite is reported as compromised rather than analysed, because the exclusions would no longer
be plausibly independent of the arm.

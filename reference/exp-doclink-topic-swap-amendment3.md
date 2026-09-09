# Amendment 3 — topicab3 results, and what actually moved doclink

Closes `exp-doclink-topic-swap-preregistration.md` (amendments 1, 2). Written 2026-08-31.

## Result: exact null

| arm | INJECT_TOPICS | PASS | FAIL | TIMEOUT | valid n |
|---|---|---|---|---|---|
| control | `00,01,02` | 3 | 16 | 1 | 19 |
| challenger | `00,01,02,08-data-storage` | 3 | 16 | 1 | 19 |

**Pass rate, Fisher exact two-tailed: p = 1.0000.** Median best error score 1.0 in both arms.
Not underpowered-ambiguous — identical counts over 40 runs.

The pre-declared verification passed: every run's `inject:` line matched its arm's declaration
exactly. That is the check `injab` lacked and it earned its place here.

**Adding `08-data-storage` to doclink's prompt does nothing.** The mechanism suggested by the
pilot — `AL0173` and `AL0151` going to zero — was an n=1 artefact and is disconfirmed.

## What actually moved doclink: MAX_FIX_ROUNDS, 5 → 8

doclink's local pass rate really did change. Restricted to genuine local qwen3-coder builds —
excluding 105 synthetic `alloc__*` logs (4 lines, `preflight PASS (fake)`), 5 Claude-backend
runs, 42 escalation-armed runs and 14 that escalated mid-run on the capability rule:

```
before 2026-08-29 :  2/192 = 1.0%
2026-08-29 onward : 13/78  = 16.7%      Fisher p = 0.000003
```

The cause is not any code change. It is a harness parameter I set myself:
`bench-run-suite.sh` defaults to `MAX_FIX_ROUNDS=5`, and every run script from 08-29 onward
passed `MAX_FIX_ROUNDS=8`.

```
max fix-round reached
  before 08-29 (n=192):  {5: 192}                        every run, no exceptions
  from   08-29 (n=78):   {5:3, 6:3, 7:2, 8:60, 9:1, 10:1, 16:8}
```

Of the 13 post-08-29 passes, the round at which each first reached error score 0:

| | |
|---|---|
| converged by round ≤5 — the old cap would have caught them | 3 |
| required rounds 6+ — structurally unreachable at cap 5 | **10** |

Counterfactual, truncating the new runs at 5 rounds:

```
observed      2/192 vs 13/78   p = 0.000003
capped at 5   2/192 vs  3/78   p = 0.1467     ← the step change disappears
cap 5 -> 8    3/78  vs 13/78   p = 0.0152
```

Hold the cap constant and there is no effect left to explain.

## Consequence for two closed conclusions

`project_doc_link_az_storage` and `project_incremental_ratchet` both concluded doclink sits at a
**model capability ceiling**, and the routing guidance for ABS-heavy AL rests on that. Every run
behind those conclusions used cap 5, which removed 10 of the 13 passes the model reaches. The
fixture was at a **harness** ceiling that was never varied.

Stated precisely, because two different claims are involved:

- **Refuted:** "doclink measures the model's ceiling." It measured `MAX_FIX_ROUNDS=5`.
- **Not refuted:** "route ABS-heavy AL to escalation." 16.7% is still a poor local pass rate, and
  the operational call may well survive. It now lacks the justification it was given.

`roundab`'s null is consistent rather than contradictory: 8→16 is genuinely flat (2/10 vs 2/10),
so the returns concentrate in 5→8 and stop. Both facts hold together.

## Caveat on this analysis

The 5-vs-8 comparison is reconstructed from historical runs and a post-hoc round truncation, not
a randomised assignment. The suites differ in date, code and operator. It is strong enough to
identify the cause and to disqualify the ceiling claim; it is not the controlled result. That is
what `exp-fix-round-cap-preregistration.md` is for.

## Status

- Topic swap: **closed, null.** `INJECT_TOPICS` selection stays as committed.
- `injab`: **withdrawn** — both arms ran the identical configuration (ctx-guard trimmed the
  challenger's fifth topic), fixed in `eeae64b`.
- `roundab`: null stands.
- Cause of the doclink shift: **identified as `MAX_FIX_ROUNDS`**, pending controlled confirmation.

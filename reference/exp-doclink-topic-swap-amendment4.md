# Amendment 4 — the MAX_FIX_ROUNDS attribution is WITHDRAWN

Amends `exp-doclink-topic-swap-amendment3.md`. Written 2026-08-31, after the controlled test.

## Withdrawal

**Amendment 3 attributed the historical doclink pass-rate shift (2/192 → 13/78) to
`MAX_FIX_ROUNDS` rising from 5 to 8. That attribution is withdrawn. It did not survive the
controlled test it predicted.**

What happened:

1. The controlled `5 vs 8` comparison ran exactly as pre-registered in
   `exp-fix-round-cap-preregistration.md` — interleaved, arm-isolated, fixed n, nothing altered
   after launch.
2. **Arm verification confirms the manipulation actually occurred.** Control runs reach a
   maximum of round 5; challenger runs reach 6–8. The arms did what they declared, so this is a
   real negative and not another `injab`, where both arms silently ran the same configuration.
3. **Prediction 1 FAILED.** doclink: control 0/19, challenger 1/20, Fisher exact **p = 1.0000**.
4. **Prediction 2 held.** p4: 10/10 vs 10/10, p = 1.0000 — the cap does not bind on a fixture
   that converges in about one round.
5. Therefore the retrospective attribution is withdrawn.
6. **The 08-29 → 08-30 shift remains unexplained.**

## What is NOT being claimed in its place

The controlled cap-8 arm scored 1/20 where the pooled historical cap-8 runs scored 13/78. That
is consistent with large session-to-session variance and with the retrospective comparison being
non-transportable — different dates, code, operator and sessions.

**That is a plausible explanation, not a demonstrated cause, and it is not being adopted as
one.** Replacing a disproved mechanism with an untested one would repeat the exact error this
amendment exists to correct. The honest status is: unexplained.

The methodological lesson is the transferable part. A retrospective comparison produced
p = 0.000003 and a mechanism that fitted every observation — every historical run capped at
exactly 5, and 10 of 13 new passes first going green at round 6 or later. It was still wrong.
A p-value computed across sessions measures the difference between those sessions, not the
effect of the variable you have decided to name.

## The capability finding is NOT withdrawn — it rests on a different experiment

Withdrawing the cap attribution does not touch the capability question, which has now been
measured directly for the first time. Same harness (`codeunit-probe.py`), same three ABS blob
codeunits, same referee, budget varied deliberately:

| backend | repair budget | GREEN | combined |
|---|---|---|---|
| Claude | 2 | **3/3** (repair rounds 0–2) | GREEN, 0 errors |
| qwen3-coder:30b | 2 | **0/3** | RED, 73 errors |
| qwen3-coder:30b | 8 | **0/3** | RED, 2 errors |

Claude's 3/3 replicates across all seven stored probe artefacts.

Stated at the strength the evidence carries:

> On the three tested ABS codeunits, Claude reached GREEN in 3/3 runs under a two-round repair
> budget, whereas qwen reached GREEN in 0/3 under the same budget and remained 0/3 when expanded
> to eight rounds. The expanded budget substantially reduced residual errors (73 to 2 combined),
> demonstrating repair progress without closure. This supports a fixture-specific capability
> difference on the tested construct; it does not establish an absolute capability ceiling for
> qwen.

**Deliberately not saying "qwen is at its capability ceiling."** 0/3 at eight rounds with errors
falling 73 → 2 supports *failure to close within the tested budget*, not a mathematical or
architectural limit. That it gets dramatically closer is evidence against the stronger wording,
not for it.

## Correction to an earlier claim of mine

I previously stated the capability-ceiling claim had "no surviving support" once the cap
confound was found. That was wrong. The support was **missing**, not absent in principle: the
3/3-vs-0/21 contrast in `exp-tierb-claude-preregistration.md` was assembled from two harnesses at
two budgets and was never a head-to-head, which was a fair criticism of the argument. It was not
grounds for concluding the underlying claim false. Having now run the comparison properly, the
conclusion holds.

## Status after this amendment

| claim | status |
|---|---|
| topic swap moves doclink | closed, null (`topicab3`, p = 1.0000) |
| `MAX_FIX_ROUNDS` explains the historical shift | **WITHDRAWN** (`fixcapdl`, p = 1.0000) |
| historical 08-29 → 30 shift | **unexplained** |
| Claude closes ABS codeunits at a 2-round budget | holds, 3/3, replicated |
| qwen closes them within 8 rounds | refuted, 0/3, residual 2 errors |
| route ABS-heavy AL to escalation | stands — now on measured capability as well as cost |

The general lesson worth keeping: **a conclusion can turn out correct after having been reached
with invalid evidence, and the right response is still to withdraw the invalid argument and
rebuild the case from a new experiment.** That is what happened here.

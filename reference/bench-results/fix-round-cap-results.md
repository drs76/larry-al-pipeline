# Results — fix-round cap (5 vs 8), and the ABS capability probe

Pre-registration: `exp-fix-round-cap-preregistration.md`. Run 2026-08-31 from `4bcab9c`.
Model `ollama/qwen3-coder:30b` in both arms. Local-only, escalation off.

## Headline

**Increasing the repair cap from 5 to 8 did not reproduce the historical doclink improvement.
The historical shift remains unexplained.**

## 1. Fix-round cap

| fixture | control (cap 5) | challenger (cap 8) | Fisher exact | prediction |
|---|---|---|---|---|
| doclink | 0/19 (1 TIMEOUT excluded) | 1/20 | **p = 1.0000** | FAILED — improvement predicted |
| p4 | 10/10 | 10/10 | p = 1.0000 | HELD — null predicted |

Wall clock: doclink 345 min, p4 32 min.

### Arm verification, before analysis

| arm | max fix-round observed |
|---|---|
| doclink control | 5 |
| doclink challenger | 6–8 |
| p4 control | 1 |
| p4 challenger | 8 |

The manipulation occurred. Control runs stop at 5; challenger runs use the extra budget. This is
a real negative result, not an arm that silently collapsed — the failure mode that voided
`injab`, where ctx-guard trimmed the challenger's extra topic and both arms ran identically.

### Consequence

The retrospective attribution in `exp-doclink-topic-swap-amendment3.md` is **withdrawn**. See
`exp-doclink-topic-swap-amendment4.md`.

The controlled cap-8 arm scored 1/20; the pooled historical cap-8 runs scored 13/78. Consistent
with large between-session variance and a non-transportable retrospective comparison — but that
is a plausible explanation, **not a demonstrated cause**, and is not adopted as one.

p4 passing 10/10 in both arms also shows the fixture is not repair-limited at all, which is why
it was the right falsifier to pre-register.

## 2. ABS capability probe — a separate experiment, not a rescue of the above

This does not explain, support or soften the failed cap result. It answers a different question
that had never been measured: at equal repair budget on the same harness, does the coder matter?

`codeunit-probe.py`, three doclink ABS blob codeunits, same handover, same verified-green
baseline, same compiler+analyzer referee.

| backend | repair budget | GREEN | combined verdict | elapsed |
|---|---|---|---|---|
| Claude | 2 | **3/3** (rounds 0–2) | GREEN, 0 errors | 289s |
| qwen3-coder:30b | 2 | **0/3** | RED, 73 errors | 645s |
| qwen3-coder:30b | 8 | **0/3** | RED, 2 errors | 2329s |

Claude's 3/3 replicates across all seven stored `PROBE-claude-*.json` artefacts, with per-file
repair rounds of 0–2 — so the two-round budget was demonstrably non-binding on those runs and
re-running Claude at 8 would add nothing.

### Reading

> On the three tested ABS codeunits, Claude reached GREEN in 3/3 runs under a two-round repair
> budget, whereas qwen reached GREEN in 0/3 under the same budget and remained 0/3 when expanded
> to eight rounds. The expanded budget substantially reduced residual errors (73 to 2 combined),
> demonstrating repair progress without closure. This supports a fixture-specific capability
> difference on the tested construct; it does not establish an absolute capability ceiling for
> qwen.

Not "qwen is at its capability ceiling". 0/3 at eight rounds with residual errors falling 73 → 2
supports failure to close **within the tested budget**. Getting dramatically closer argues
against the stronger claim, not for it.

### What this replaces

`exp-tierb-claude-preregistration.md` cites "Claude 3/3 vs qwen 0/21". That was never a
head-to-head: the Claude half came from this probe at a 2-round budget, the qwen half was quoted
from `incrab2`'s runs at `MAX_FIX_ROUNDS=5` under the incremental workflow. Different harness,
different budget. The comparison above is the first same-harness, equal-budget measurement, and
it should be cited in place of the old figure.

## Standing status

| claim | status |
|---|---|
| topic swap moves doclink | null, p = 1.0000 (`topicab3`) |
| `MAX_FIX_ROUNDS` 5→8 moves doclink | **null, p = 1.0000** — attribution withdrawn |
| historical 08-29 → 30 shift | **unexplained** |
| repair cap binds on p4 | no — 10/10 either way |
| Claude closes ABS codeunits at 2 rounds | holds, replicated 7× |
| qwen closes them within 8 rounds | refuted, 0/3, residual 2 |
| route ABS-heavy AL to escalation | stands, on measured capability and on cost |

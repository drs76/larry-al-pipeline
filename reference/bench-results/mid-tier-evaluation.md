# Mid-tier (OpenRouter) evaluated on AL — 2026-08-16/17

**Verdict: the tier works, `kimi-k2` is the model, default stays OFF pending a wider sample.**

The mid rung exists to cut Claude spend, so the criterion is *builds closed that would otherwise
have gone to Claude* — not pass rate. Two such builds were closed across six runs on two fixtures.
That is a real result and too small a sample to set a default on.

## What matters: test the REAL default coder

Every early run used `qwen3.8:27b` as the coder and looked terrible (0/3, active regressions).
That measured the wrong thing twice over — `qwen3.8` was never going to be the default
(see `qwen3.8-27b-evaluation.md`), and pass rate is not the criterion. Escalation cannot
compensate for the wrong coder in the slot; its job is rescuing builds a *good* coder stalls on.

Re-run with `qwen3-coder:30b` (the actual default) and the picture inverts:

| Fixture | Baseline (no mid) | + kimi-k2 mid | What mid did |
|---|---|---|---|
| `doclink` (9 files) | 1/3 | 1/3 | **closed r1**: local plateaued at 5 errors → kimi → **0** |
| `p4` (8 files) | 2/3 | **3/3** | **closed r2**: local stalled at 2 across 2 rounds → kimi → **0** |

Config both times: `EGRESS_POLICY=cloud-mid ESCALATE_MID_AFTER=2 MAX_FIX_ROUNDS=5`,
`MID_MODEL=openrouter/moonshotai/kimi-k2`, `PI_CODER_MODEL=ollama/qwen3-coder:30b`.

**Credit split honestly.** Of p4's three passes only r2 involved the mid tier at all — r1 and r3
were closed locally in 0 mid rounds, and the baseline already managed those. The claim is 3/3 vs
2/3 with the extra pass attributable to kimi, not "mid produced 3 passes".

## Mid-model comparison (same `map` fixture, `qwen3.8` coder)

Pass rates are indistinguishable at n=3; **regression behaviour is not**, and it is mechanistic:

| mid model | pass | trajectories (pre-escalation → final) | regressions |
|---|---|---|---|
| **kimi-k2** | 1/3 | 4→2, **2→0**, 4→1 | **0/3** |
| deepseek-v4-flash-0731 | 1/3 | **2→6**, 1→0, 4→1 | 1/3 |
| deepseek-chat (V3) | 0/3 | **1→4**, 4→3, TIMEOUT | 1/2 |

`kimi-k2` has now run **9 times across 3 fixtures without once making a build worse**, and is ~2×
faster than deepseek-chat. Both DeepSeek variants took a nearly-passing build backwards. Use kimi.

## The unmask path is what makes kimi valuable

On doclink r1 and r2 the score appeared to explode (5→23, 3→8) — that is **not** a regression:

```
Unmask: all 5 previous error(s) cleared; 12 newly surfaced — fixing forward, not reverting.
```

kimi cleared *every* error the local coder had plateaued on, surfacing ones a blocker had hidden,
and the pipeline correctly adopted the unmasked state instead of reverting. That rule exists
because of this fixture (`run-build.py` comment: doclink, 1 AL0282 → 16 unmasked AL0132s → revert
loop for 8 rounds). So kimi's contribution is *breaking blockers*, not incremental patching —
which is exactly the failure mode a local coder plateaus on.

**Beware the display:** `error score: 0 (best so far: 23)` looks like keep-best regressed. It did
not — `best` legitimately became 23 via the unmask rule. Check for the `Unmask:` line before
concluding anything from a score jump.

## Why route-planner was NOT used

It looks like the obvious fixture (4 of the 7 recorded Claude escalations) but it is not a mid-tier
test. The metrics show it was built **incrementally over 56 runs**, growing 11 → 15 → 20 → 26 → 65
files; the escalations happen at the 26- and 65-file marks. Its handover is now **9,450 lines / 72
expected files** — the documented large-cumulative-handover limit that needs `VERBATIM_WRITE=1` or
`CODER_BACKEND=claude`. A mid rung cannot rescue an incomplete 72-file *write* phase; it helps in
*fix* rounds. Running it would measure the handover limit, not the tier.

(Isolation was verified anyway: the run-dir path rewrite leaves **0** references to
`/mnt/rojaws/Code/AL/route-planner` and redirects all 142 — the live promoted copy, which has
uncommitted work, is never touched by a bench run.)

## Not established — why the default stays OFF

- **≥30% of previously-Claude builds closed** (warplan success #9) needs a denominator of
  would-have-escalated builds. Six runs on two fixtures is not that sample.
- **Cost not measured.** OpenRouter spend vs avoided Claude spend is the actual economic question
  and no token accounting was done.
- **Go/C# untouched, and there is nothing to save there:** every one of the 7 recorded Claude
  escalations is AL. Go has never escalated — the `gow` suite ran 8/8 locally. The tier's original
  target has a denominator of zero.

## Reproduce

```bash
EGRESS_POLICY=cloud-mid ESCALATE_MID_AFTER=2 MAX_FIX_ROUNDS=5 \
MID_MODEL=openrouter/moonshotai/kimi-k2 \
PI_CODER_MODEL=ollama/qwen3-coder:30b CODER_BACKEND=pi \
  python3 pipeline/run-build.py --project <run-dir>
```
Verify `MID_MODEL` ids against OpenRouter's live `/models` endpoint first — the catalogue moves.
Summaries: `DOCLINK-MID`, `P4-MID` (real default coder) and `KIMI`, `V4FLASH`, `MIDESC`
(`qwen3.8` coder, mid-model comparison only).

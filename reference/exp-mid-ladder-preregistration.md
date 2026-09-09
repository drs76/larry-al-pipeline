# PRE-REGISTRATION — mid-tier escalation ladder on the locked fixture matrix

Written and committed **before any Tier A run**. Decision rules here are fixed; a result
that does not fit them is reported as not fitting, not reinterpreted.

## The question

> Does the cloud-mid rung turn otherwise-exhausted Larry runs into completed work often
> enough to justify enabling `ESCALATE_MID_AFTER` by default?

This is a **routing-policy** experiment, NOT a coder-model A/B. Both arms give
`qwen3-coder:30b` the identical first opportunity on the identical handover. The only
intervention is who takes over after the threshold.

    control     qwen3-coder:30b, local only
    challenger  qwen3-coder:30b + ESCALATE_MID_AFTER=2, mid rung closes

## Why the design is asymmetric, and why symmetry would be worse

Escalation only engages where the local model FAILS. After this session's fixture repairs,
that is doclink and almost nowhere else:

| fixture | clean round-1 | mid rung fires in | informative? |
|---|---|---|---|
| p1 | 20/20 | 0/20 | no — challenger IS control |
| p4 | 18/20 | ~2/20 | marginal |
| map | 18/20 | ~2/20 | marginal |
| doclink | 0/20 | 20/20 | **yes** |

A symmetric 10+10 across four fixtures would spend ~60 of 80 measurements on arms that are
identical by construction. **Symmetry is not fairness when the treatment only applies to a
subset of executions.** The meaningful sample size is the number of runs where escalation
can actually occur.

Noted honestly: the fixture repairs made three fixtures too clean to exercise an escalation
rung. That is the correct fixture state, and it narrows rather than weakens the experiment
— Kimi is not being tested as a replacement for Qwen on easy work, which was never the
architectural proposal.

## Configuration — pinned, identical across all runs

    EGRESS_POLICY=cloud-mid                      OpenRouter only; NOT Anthropic, NOT github
    MID_MODEL=openrouter/moonshotai/kimi-k2      pinned; the default is deepseek-chat
    ESCALATE_MID_AFTER=2                         pi does 2 fix rounds, then mid closes
    ESCALATE_AFTER unset                         ladder is pi -> mid -> STOP, no Claude rung
    control model / challenger model             ollama/qwen3-coder:30b (both arms)
    RUN_TIMEOUT=1800                             MAX_FIX_ROUNDS default (5)

Fixture commits, locked and not to be edited during the experiment:

    p1       26d56c9      p4       a00035f
    map      422c749      doclink  167b68a

## Allocation — 36 runs

| fixture | runs | role |
|---|---|---|
| **doclink** | **10 + 10** | PRIMARY decision fixture |
| p4 | 5 + 5 | regression / interaction check |
| map | 5 + 5 | regression / interaction check |
| p1 | 3 + 3 | health gate |

## Outcomes

**Primary (doclink):** terminal pass rate.
**Secondary (doclink):** exhaustion rate, repair rounds, duration, and — recorded
separately — whether the mid rung actually CLOSED after escalating (`mid_closed`), since
`mid_escalated` only says it was handed the work.

**p4 / map (not scoring):** no reduction in terminal pass rate; no new `dominant` or
`spec-trap` round-1 signature; escalation frequency recorded; any escalated run inspected
individually.

**p1 (gate only):** clean completion required. Earns NO credit for passing or for being
fast — it is intentionally flat. Anything other than clean completion is a regression to
investigate before reading anything else.

## Decision rule — operational thresholds, not significance alone

At 10+10, demanding statistical significance would make the experiment trivially
dismissible as underpowered. The decision is tied to what Larry needs:

| result | reading | action |
|---|---|---|
| **Strong win** | Kimi closes a clearly material number of doclink runs that control does not, no regression elsewhere | candidate for default mid escalation |
| **Promising** | some additional closes, too few to distinguish confidently | expand doclink only; do not enable by default yet |
| **No evidence** | no meaningful improvement in closes | do not enable by default; retain as manual/escalation-only |
| **Regression** | worse outcomes, new harmful signatures, or pipeline instability | disable and investigate |

Fisher exact will be reported for the primary outcome, but **is not the gate.** A p-value
is one input to the operational reading, not a substitute for it.

## Excluded from outcome counts

The two instrumentation smokes — `midsmoke` (p4) and `midsmoke2` (doclink) — are evidence
that the ladder works and is observable. They are NOT arm data and do not count toward any
repeat. `midsmoke` armed but never escalated (both runs passed first attempt, which is what
exposed the design problem above); `midsmoke2` escalated and populated
`mid_model=openrouter/moonshotai/kimi-k2`, `mid_escalated=true`, provenance `tracked`.

Historical model results are NOT pooled with this shootout. The locked matrix starts a new
measurement epoch: every prior kimi row is `legacy_missing` and predates every fixture
repair. Old runs inform candidate selection only.

## Amendment 1 (2026-08-23) — protocol implementation correction

This amends how the protocol is EXECUTED. It changes no hypothesis, allocation, candidate,
threshold, or scoring rule. Everything above still governs the valid runs.

**Defect.** `bench-run-suite.sh` established an arm by ADDING variables. It never cleared
them. `.zshenv` exports `ESCALATE_MID_AFTER=2`, `ESCALATE_AFTER=4` and
`MID_MODEL=openrouter/moonshotai/kimi-k2` into every interactive shell, so "control" meant
"added no escalation variables" rather than "ran without escalation". Both nominal arms of
the doclink block were armed with Kimi.

**Invariant now enforced.** An arm must positively establish the configuration it claims to
measure. Absence of an override is not a configuration.

**Implementation.** `bench_env_contract.py` derives the clear-list from every environment
variable `run-build.py` and its pipeline modules actually read, minus tool locators
(`PI_BIN`, `CLAUDE_BIN`, `AL_CLI`, …). 55 variables, derived rather than curated, so a knob
added to the pipeline is isolated the day it lands. The suite clears all of them per run,
then applies the arm's declarations. It writes `runs/<TAG>-env-contract.json`, prints an
effective-config preflight before the first fixture run — including what the ambient shell
was trying to leak — and asserts each finished run's own arming banner against what its arm
declared. A control that shows a mid rung, or a challenger `DISARMED by egress policy`,
VOIDs the run and aborts the suite.

`.zshenv` is deliberately not changed. The user's normal shell is not the defect.

**Status of the runs already executed under the contaminated environment:**

| runs | status |
|---|---|
| doclink 10+10 | **INVALID for A/B.** Both arms received Kimi. Excluded from Tier A outcome counts and from every threshold in the decision rule. Retained as an uncontrolled capability observation only. |
| p4 5+5, map 5+5, p1 3+3 | Operationally valid as the gate/regression checks they were pre-registered as. `mid_escalated` false throughout, so the leaked arming never activated. Recorded as executed under a contaminated ambient configuration. |

The 26 non-doclink runs are not rerun. The leaked set was audited mechanically against what
`run-build.py` reads: `ESCALATE_AFTER`, `ESCALATE_MID_AFTER`, `MID_MODEL` (escalation only,
never fired), `COMS_VALIDATOR_MODEL` / `COMS_RELAY_MODEL` (read only under `--review`, which
the suite does not pass), and `PI_CODER_MODEL` (already overridden per run by the suite). No
leaked variable could affect a non-escalated run.

**`0/20 mid_closed` from the invalid block is not a model-selection result.** It is worth
inspecting diagnostically — it is a poor showing against the earlier historical evidence for
Kimi — but it cannot answer the pre-registered question, which is whether the mid rung beats
the local-only path. Only the valid rerun answers that.

**Valid rerun:** doclink 10+10 only, under the thresholds already registered above.

    CONTROL_ENV="EGRESS_POLICY=cloud-mid" \
    CHALLENGER_ENV="EGRESS_POLICY=cloud-mid ESCALATE_MID_AFTER=2 MID_MODEL=openrouter/moonshotai/kimi-k2" \
    REPEATS=10 RUN_TIMEOUT=1800 \
    ./bench-run-suite.sh midladder2 ollama/qwen3-coder:30b ollama/qwen3-coder:30b doclink

`EGRESS_POLICY=cloud-mid` is declared on BOTH arms deliberately: control is then disarmed
because no escalation variable is set, not because a policy happened to block the egress.

## Tier B — deferred, not part of this registration

Claude on doclink at small pre-declared n, as a reference ceiling only. It answers how much
headroom exists above the local baseline and how much of it Kimi captures. Requires a
separate egress decision (`cloud-mid` does not permit Anthropic) and its own registration.

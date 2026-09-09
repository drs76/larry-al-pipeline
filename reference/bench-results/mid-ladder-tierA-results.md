# RESULTS — mid-tier escalation ladder, Tier A (doclink)

Registration: `reference/exp-mid-ladder-preregistration.md` + Amendment 1.
Suite: `midladder2`, 2026-08-23, 88 min, 20 runs, 0 VOID.
Fixture: `tsg-document-link-2-az-storage`, provenance `tracked`, `fixture_commit 422c749`,
handover `e82168cb3857`, tree clean — byte-identical to the voided `ladderdoc` block.

## Arm isolation — verified, not assumed

The shell that launched this suite still exported `ESCALATE_AFTER=4`,
`ESCALATE_MID_AFTER=2`, `MID_MODEL=kimi-k2`, `COMS_VALIDATOR_MODEL`, `COMS_RELAY_MODEL`,
`PI_CODER_MODEL`. All six are recorded in the preflight and were cleared per run. Each run's
own banner was asserted against its arm:

    control    10/10  "Escalation: off", no mid rung line at all
    challenger 10/10  "Mid tier: ARMED — pi does 2 round(s), then kimi-k2 ... pi→mid→stop"

`EGRESS_POLICY=cloud-mid` was declared on BOTH arms, so control is disarmed by the absence
of escalation variables, not by a policy block. The treatment is the rung, not cloud access.

The rung fired and did the work: `mid_escalated` 10/10 challenger, 0/10 control,
`mid_model=openrouter/moonshotai/kimi-k2`, 3 mid rounds in every challenger run — 30 billed
Kimi invocations.

## Primary outcome — terminal pass rate

| arm | pass | exhausted | mid_escalated | mid_closed |
|---|---|---|---|---|
| control (qwen local only) | **0/10** | 10/10 | 0/10 | — |
| challenger (+ Kimi at round 2) | **0/10** | 10/10 | 10/10 | **0/10** |

Fisher exact **p = 1.0**. Reported, not gating.

## Secondary

| measure | control | challenger |
|---|---|---|
| first-pass compile | 0/10 | 0/10 |
| files written / expected | 9/9 all runs | 9/9 all runs |
| manifest_ok | 10/10 | 10/10 |
| duration, median | 280s | 222s |
| first-pass errors, mean | 15.7 | 5.1 |
| fraction of first-pass errors cleared, median | 0.00 | 0.17 |
| fraction cleared, mean | 0.27 | 0.32 |
| regressions, total | 13 | 2 |

Read the fraction, not the raw count. Raw `errors_cleared` averages 11.6 (control) vs 2.5
(challenger), which looks like a large Kimi deficit and is not one: control run 7 started
from 101 first-pass errors and cleared 94 of them, and first-pass error counts range 1–101
across runs. Normalising per run reverses the apparent direction to a small challenger
advantage. Neither reading is load-bearing at n=10 with that variance; both arms end
exhausted with a tree that does not compile.

Dominant diagnostic is AL0482 in both arms, first pass and final. No new `dominant` or
`spec-trap` signature appeared in the challenger arm.

## Classification against the pre-registered thresholds

**No evidence** — no meaningful improvement in closes.

**Action, per registration: do not enable `ESCALATE_MID_AFTER` by default. Retain as
manual/escalation-only.** This matches the standing default (OFF) in
`project_mid_tier_routing`; the experiment does not move it.

Not "regression": the challenger arm produced no worse terminal outcome, no new harmful
signature, and no pipeline instability. It cost 30 cloud calls to reach the same place.

## Uncontrolled capability observation — separate, not scoring

The voided `ladderdoc` block (both arms armed, see Amendment 1) recorded Kimi closing 0/20
doclink escalations. `midladder2` now adds 0/10 under a controlled arm. Consistent, and
consistent with the historical 1/3, but it answers a different question than the
registration asked and carries no threshold. It is evidence about the rung's capability on
THIS fixture, not a model-selection result.

## What this does and does not say

It says the Kimi rung does not rescue doclink.

**Correction to the first draft of this section.** It claimed doclink fails as a first-write
problem, so no repair rung could help. The metrics do not support that, and the claim is
withdrawn. Across the 20 runs the best-achieved error score is
`[1,1,1,1,1,1,2,3,3,4,5,6,7,7,9,9,9,9,11,14]` — **six runs ended one error from green, ten
within five.** Across the 81 tracked doclink failures the median residual is 2 errors. The
tree is not wrecked; it stops just short.

The residual is small but **persistent and of one class.** Final-round errors across the 20
runs: AL0133 (wrong type passed) 60, AL0132 (object has no such member) 35, AL0173 (operator
applied to wrong type) 24 — the ABS Storage codeunit contract, chiefly treating
`"ABS Operation Response"` as a Boolean and calling members that do not exist. Plus invented
identifiers (AL0118: `ABSOptionalParams`, `GetPassword`, `InputBox`, `LastDelimiter`).

Two counting errors in that first draft, also corrected: **AL0482 and AL0789 are warnings,
not errors** — AL0482 ("image X is not valid in this context") led an earlier version of this
table and does not belong in a residual-error count at all. And `diagnostic_codes` in the
metrics is a severity-blind presence list, one entry per code per run, so it cannot be read
as an error frequency. The error arithmetic elsewhere in this document uses
`first_pass_diagnostics` / `errors_cleared`, which are sarif-filtered to errors and stand.

So the corrected scope: doclink is **knowledge-bound, not effort-bound.** More repair rounds
from a model that lacks the ABS contract produce more attempts at the same wrong idea — which
is exactly what 30 Kimi rounds closing 0 looks like, and consistent with `codeunit-probe`
(Claude 3/3, qwen 0/21 on ABS). The ladder was tested with a rung that does not have the
missing knowledge either.

That makes **Tier B the discriminating test, and it is now the most valuable next run rather
than a deferred nicety.** With six runs one error from green, the question is sharp: if
Claude closes them, the ladder concept is sound and only the rung's model was wrong; if
Claude also fails, the defect is in the fixture or handover and no routing change will touch
it. Either answer redirects the roadmap.

**Instrumentation gap found while writing this.** Final-round diagnostics are not persisted
in categorised, severity-filtered form — only `first_pass_diagnostics` is. The residual class
above had to be recovered by grepping logs. Emitting a `final_diagnostics` category dict
alongside the first-pass one is a small change and should land before the next experiment.

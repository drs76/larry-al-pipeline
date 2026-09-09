# AMENDMENT 1 — routing economics: Arm C replacement after treatment-delivery failure

Amends `exp-routing-economics-preregistration.md`. **Implementation correction to deliver the
already-registered treatment — not a change of hypothesis, allocation, thresholds, candidate,
scoring, stopping rule or analysis.**

## Original suite: `routecon2`, SHA `9d2f39d`

120/120 completed, 0 driver VOIDs.

| arm | status |
|---|---|
| **A** (40 runs) | **RETAINED, valid.** 0 Claude calls, $0.00, as designed. Never depended on the defective predicate. |
| **B** (40 runs) | **RETAINED, valid.** Independent fixed-round path; doclink 8/10 pass, 10 attributed calls, $4.4684; p1/p4/map 0 calls. Carries the successful live instrumentation validation. |
| **C** (40 runs) | **VOID as an intervention.** |

## Why Arm C is void

The registered rule **fired** — 9/10 doclink runs — and escalation was suppressed by an
incorrect egress-availability predicate:

    my guard        egress_policy.allowed("anthropic")[0] is not False   -> (False, ...) at rest
    correct         egress_policy.escalation_available()                 -> (True, "")

Under `enterprise-anon`, `allowed("anthropic")` is deliberately False AT REST — Anthropic is
armed only inside `claude_egress`'s scrub context. Testing it at the decision point concluded
"escalation unavailable" and every arm C run stayed local:

    Rule fired at round 3 but escalation is unavailable — staying local.

**This is not analytical contamination. The intervention was never delivered.** Arm C ran as
a second "never" arm while every row reported `routing_policy=rule`. Its results are NOT used
as Arm C outcome observations.

**Why the integrity gates passed it.** Every Arm C assertion checked the policy LABEL —
`routing_policy`, `escalate_after`, `rule_fingerprint`. None checked that a fired rule
produced a Claude call. Thirteen validated gates, and the one that mattered was not among
them.

## Replacement

**Arm C only, exactly 40 cells, fresh tag and fresh artifacts.** No substitution, no
reallocation, no modification of the A/B observations. The invalid original Arm C artifacts
are preserved, not deleted.

**Code change, limited to restoring the registered mechanism:** replace the incorrect
availability predicate with `escalation_available()`, the same semantic the established
`ESCALATE_AFTER` path in `run-build` already uses.

**Frozen and unchanged:** fixture revisions, model, handovers, 10 runs per fixture, rule
fingerprint `v1:553cfa8b91e6a4e8`, thresholds, allocation, scoring, strict usage, analysis
plan, deferred weighting.

## New production invariant — behavioural, not label-based

`run-build` now records `rule_fired` and `rule_fire_round` independently of whether
escalation followed. The driver VOIDs on:

    arm C, rule FIRED, claude_calls == 0   -> suppressed intervention, not a null result
    arm C, rule did NOT fire, calls > 0    -> escalation without a trigger
    arm C, rule_fired absent               -> treatment delivery unverifiable

**The guard lives in production, not only in the validation suite**, so this defect class
cannot recur silently.

Fake-validated on all four branches: fire+delivered passes, fire+suppressed VOIDs (the exact
`routecon2` defect), non-fire+no-calls passes, non-fire+calls VOIDs.

Real local-only p1/arm-C rehearsal of the NON-FIRE branch through actual `run-build`, zero
spend:

    qwen3-coder_30b__p1__rehc_armC__r1: PASS calls=0 cost=$0 in 61s
    routing_policy=rule   rule_fingerprint=v1:553cfa8b91e6a4e8
    rule_fired=False      rule_fire_round=None
    claude_calls=0        claude_calls_missing_usage=0

**The FIRE branch is fake-verified only.** p1 never fires, so no free real firing case exists;
the first real fire will be a doclink arm C run, which is billed. That is the accepted
position — fake-controlled coverage of the fire branch, with the production invariant standing
guard on the real one.

## How the completed experiment must be described

**Not** as one untouched 120-run execution. As a **120-cell experiment with Arm C replaced
after treatment-delivery failure**:

    A   original routecon2, 40 valid observations
    B   original routecon2, 40 valid observations, incl. live instrumentation validation
    C   replacement tag, 40 observations under this amendment

That provenance is stronger than pretending the failed Arm C run never happened.

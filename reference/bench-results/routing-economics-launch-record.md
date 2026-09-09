# LAUNCH RECORD — routing-economics experiment

## Superseded launch SHA: `b2454b2`

**Unexecutable.** VOID on the first, unbilled run: the driver's run-directory naming
violated `run-build`'s model/run-dir provenance invariant
(`check_model_matches_rundir`), which requires any `__`-containing directory to lead with
the coder's model slug. run-build aborted before emitting metrics, and the driver correctly
refused to score a run that produced no measurement.

    VOID: routecon__p1__armA__r1 — produced NO new metrics row
    ERROR: model/run-dir mismatch — directory claims 'routecon',
           coder model is 'qwen3-coder_30b'

Execution record preserved at `routecon-b2454b2-failed/` (background task `blucov94n`).
Not deleted, not overwritten, not resumed.

**Why it was missed.** The fake-validation stub did not implement run-build's own
preconditions, so the matrix validated the driver against a test double more permissive than
production. Thirteen checks passed on something that could not complete one real run. The
stub now enforces the same guard.

## Approved launch SHA: `9d2f39d`

**Naming correction only.** `${MODEL_SLUG}__${fx}__${TAG}_arm${arm}__r${r}`, conforming to
the existing invariant rather than bypassing it — `ALLOW_MODEL_MISMATCH=1` was refused
because it accepts exactly the mislabelled rows the guard exists to prevent.

Validated end to end with a real, local-only rehearsal through actual `run-build`:

    qwen3-coder_30b__p1__rehearse_armA__r1: PASS calls=0 cost=$0 in 64s
    routing_policy=never  escalate_after=None  rule_fingerprint=None
    claude_calls=0  claude_calls_missing_usage=0  provenance=tracked  + 1:1 ledger note

## Experimental status at transition

**No valid economics observations and ZERO billed Claude calls occurred before the
replacement.** Allocation, pre-registration, arms, trigger thresholds, model choice, routing
policy, scoring, stopping rules and analysis plan are all unchanged. Nothing about the
experiment moved — only the harness's ability to execute it.

The first billed Claude invocation under `9d2f39d` remains the pre-registered live
instrumentation validation: `attributed=true`, non-zero tokens,
`claude_calls_missing_usage == 0`, else hard-abort and VOID.

## Relaunch

Fresh tag, clean state. `blucov94n` and its cells artifact are preserved as the failed
pre-billing execution record and are neither resumed nor reused.

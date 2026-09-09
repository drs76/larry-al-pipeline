# AMENDMENT 4 — routing economics: Arm C relaunch after an unexplained write-phase timeout

Amends `exp-routing-economics-preregistration.md`, following Amendments 1-3.
**No change to the driver, rule, thresholds, allocation, fixture revision, strict attribution,
containment, foreign-row rejection, or scoring. No timeout change, no retry, no mitigation.**

## Transition

The preceding Arm C execution (`routecon5`) was VOIDed by an **unexplained local-coder
write-phase timeout**: `Larry-write TIMEOUT after 1200s` on a p1 cell that had taken 65-74s in
`routecon4`. 0/40 cells, $0.00, 0 Claude calls, artifacts preserved and excluded.

Subsequent independent probing confirmed that Larry and the end-to-end production write path
are **currently functional**, but **did not reproduce or explain the failure**:

    host / service    up 0.28ms; /v1/models 200 in 21ms on port 11443;
                      qwen3-coder:30b RESIDENT at 21.7 GB VRAM; live generation 200 in 0.24s
    quarantined probe p1 via real run-build, production write path, local-only egress,
                      metrics and shadow log redirected to scratch, no bench identity:
                      Larry-write done in 46s, 6/6 files, first-pass compile,
                      RESULT: PASS, duration 71s

**The probe is diagnostic only. It is NOT an experimental observation** and is not used as a
cell, a validation of any cell, or evidence about the routing policy.

**What the probe establishes, and what it does not.** It rules out a continuously broken
path. It does **not** establish that the original failure was transient: a single success is
equally consistent with an intermittent wedge that did not fire. `routecon4` had already
produced 23 consecutive working runs before its unrelated map failure, so one more success
adds little. **Root cause remains undiagnosed.**

## Decision

The replacement is launched under the unchanged frozen experimental conditions, **accepting
residual risk of recurrence**. The reasoning:

- the failure is not persistent;
- a bounded reproduction loop has asymmetric value — another success teaches almost nothing,
  while a recurrence may consume substantial wall-clock without guaranteeing diagnosis;
- the suite's integrity behaviour is already proven: a recurrence produces no valid
  observation and VOIDs rather than scoring a false zero;
- billed work is concentrated late, in doclink, so an early local failure costs wall-clock
  rather than Claude spend.

## STOP RULE — binding on the next occurrence

**If the write-phase timeout recurs in this replacement, option 1 is not chosen again by
default.** Two independent occurrences materially change the evidence and justify diagnosing
the wedge — the known "stream ended without finish_reason" class, whose shape the `routecon5`
log matches — before committing another multi-hour allocation.

## Lineage

    1. routecon2 C   treatment not delivered (wrong egress predicate)
    2. routecon3 C   recursive child accounting ($0.9476 unassigned, preserved separately)
    3. routecon4 C   map fixture cleanup destroyed the per-run git repository
    4. routecon5 C   unexplained local-coder write timeout; Larry later healthy; UNDIAGNOSED
    5. routecon6 C   this replacement

Arms A and B from `routecon2` remain frozen and valid throughout.

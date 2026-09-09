# AMENDMENT 2 — routing economics: Arm C replaced again (recursive child accounting)

Amends `exp-routing-economics-preregistration.md`, following Amendment 1. **Execution
containment only** — no change to the rule, thresholds, allocation, models, fixtures,
handovers, scoring, or analysis.

## 1. `routecon3` Arm C is VOID for economics analysis

40/40 cells, 0 driver VOIDs, and the registered treatment WAS delivered (rule fired 6/40 real
cells, all 6 escalated). It is void for a different reason.

The escalated Claude runs under `--permission-mode bypassPermissions` inside the anon mirror
and **invoked `run-build` itself**. The child inherited `BENCH_META`, `ESCALATE_ON_RULE` and
`BUILD_METRICS`, and therefore:

    emitted a second benchmark row as project "."
    escalated RECURSIVELY — rule_fired=true, 3 further Claude calls
    spent $0.9476 attributable to no cell

Arm C's true doclink spend was $9.2564 against $8.3088 recorded — an **11% understatement
concentrated in the treatment arm**, where cost-weighted regret is the primary endpoint.

All artifacts preserved at `bench-results/routecon3-armC-void/`, including
`unassigned-spend.json`. The $0.9476 is retained as **unassigned spend from invalid Arm C
execution** — not deleted, not merged into any rerun's accounting, and not used in analysis.

**Retroactive attribution was considered and rejected.** The orphan row carries
`fixture`/`arm`/`repeat` and is mappable, but the registered cell accounting never specified
post-hoc attribution of child pipeline runs. Repairing the measurement rule after seeing
where the spend landed is precisely what pre-registration exists to prevent.

## 2. `routecon2` Arms A and B remain frozen and valid

Executed under the frozen treatment definitions with working instrumentation. Neither uses
the rule path; arm B's fixed-round escalation produced no orphan rows. Their validity does
not depend on Arm C's later recursion defect.

## 3. What the replacement changes — execution containment only

**`claude_egress._child_env()`** strips `BENCH_META`, `BUILD_METRICS`, `ESCALATE_ON_RULE`,
`ESCALATE_AFTER`, `ESCALATE_MID_AFTER`, `CAPABILITY_SHADOW_LOG` from the escalated child, and
sets the sentinel `PIPELINE_NO_BENCH=1`.

**`PIPELINE_NO_BENCH=1` in run-build** suppresses `emit_metrics` entirely and forces
`ESCALATE_AFTER=None`, `ESCALATE_ON_RULE=False`. A nested run may still compile — the
legitimate reason an agent invokes the build — but cannot act as a benchmark.

**Note on the mechanism, recorded to prevent a false sense of safety.** Stripping
`BUILD_METRICS` does NOT redirect the child's writes: in the real suite that variable is
unset, so parent and child both default to the same `.build-metrics.jsonl`. **The sentinel is
the operative guard**; the env-stripping is defence in depth.

**Driver: foreign-row rejection.** Every metrics row created during a cell must belong to
that cell. A row that cannot — such as `project="."` — now VOIDs the suite. The previous
matcher ignored it, which is exactly how the spend escaped accounting: silently ignoring a
foreign row understates the arm's cost.

## 4. Validation

Unit:

    child env         all 6 variables stripped, PIPELINE_NO_BENCH=1, PATH preserved
    sentinel          emit_metrics suppressed; ESCALATE_AFTER=None; ESCALATE_ON_RULE=False

Full path — a fake `claude` that deliberately invokes `run-build` from inside the child,
while the parent holds `BENCH_META`, `ESCALATE_ON_RULE=1` and `ESCALATE_AFTER=4`, with the
child running a COMPLETE local p1 build:

    child build            RESULT: PASS   (ran to completion)
    benchmark rows emitted 0
    sentinel fired         1
    child escalations      0   ("Escalation: off" despite the parent's armed env)
    parent accounting      1 call, $0.05 — the sole accounting unit

Two earlier attempts at this test were killed by a tool timeout mid-build and are recorded as
inconclusive, not as passes.

## 5. Lineage

    A / B      routecon2   valid, frozen
    C          routecon2   VOID — treatment not delivered (Amendment 1)
    C          routecon3   VOID — recursive child accounting (this amendment)
    C          replacement 40/40 under a new SHA and tag

Only the replacement C combines with the frozen A/B for the pre-registered per-fixture
analysis. The completed experiment is described as a 120-cell experiment with Arm C replaced,
never as one untouched execution.

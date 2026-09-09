# PRE-REGISTRATION — routing economics: is the trigger worth paying for?

Written before any run. **The TRIGGER is the experimental intervention.** Model capability is
settled (`bench-results/larry-escalation-evidence.md`, claim 1) and is not re-tested here.

## The question

> Given a repair-capable cloud rung that demonstrably closes stalled local builds, does an
> automatic trigger deliver more value than it costs, compared with the two policies we can
> already run for free?

Not "can Claude fix it" — that is answered. **Whether a policy that decides *without knowing
the outcome* beats the alternatives, once the bill is counted.**

## Arms — the routing POLICY varies, the models do not

Every arm uses the same coder (`qwen3-coder:30b`) and the same rung (Claude Code via
`enterprise-anon`). Only the decision rule differs.

    A  never          escalation explicitly OFF (no ESCALATE_AFTER, no rule)   free, the floor
    B  fixed-round    ESCALATE_AFTER=4, set LITERALLY by the driver
    C  compound rule  ESCALATE_ON_RULE=1 — capability_shadow rule v1, FROZEN,
                      fingerprint v1:553cfa8b91e6a4e8
    D  oracle         escalate exactly the builds that do not reach LOCAL_GREEN locally
                      (not implementable; the CEILING, computed post hoc from arm A)

Every arm sets its policy EXPLICITLY. `.zshenv` exports `ESCALATE_AFTER=4` globally, and this
project has already voided a 20-run experiment to that exact leak — arm A must be off because
the driver turned it off, never because nothing happened to set it. The derived env-contract
clear-list applies as it does to every other suite.

`ESCALATE_AFTER=4` for arm B is the value the shadow projections were computed against, so
the arm measures the policy actually in place rather than a newly invented one.

**Arm C required new pipeline capability, and this is called out rather than buried.**
`capability_shadow` was observational by construction — it recorded `fire_round` and nothing
read it. `ESCALATE_ON_RULE=1` (default OFF) makes run-build latch to Claude when the frozen
rule fires. The rule itself is untouched: run-build only READS `fire_round`.

Two consequences handled up front:

- Rows produced while the rule is acting are marked `acted=true`. The 297-row prospective log
  is validation data for a rule that did NOT act; a row where it drove the outcome is a
  different population and **must never be pooled with the observational ones**.
- Each shadow row and each metrics row now carries `rule_version` and `rule_fingerprint`,
  covering the four thresholds AND the predicate source, so "we ran rule v1" is checkable
  rather than asserted. Metrics also carry `routing_policy` and `escalate_after`, recorded by
  the run itself rather than inferred from a directory name.

D is not a run. It is arm A's outcomes re-scored under perfect foresight, and it exists so a
positive result for C can be read against how much of the available value it captured.

## BLOCKING PREREQUISITE — cost instrumentation does not exist

The pipeline records `duration_s` and nothing else. **There is no token count and no spend
figure for any Claude call, anywhere.** Without it every outcome below is uncomputable.

Required before arm B or C runs, and to be validated the way the Tier B preflight was —
asserted, with a deliberate negative test:

    per escalated call   input tokens, output tokens, model id, wall-clock latency
    per build            total escalated calls, total tokens, total latency attributable
                         to escalation, and the local rounds actually displaced

**STATUS: implemented and validated 2026-08-23** — `reference/claude-usage-schema.md` (frozen
schema), captured in `claude_egress._raw`, the single chokepoint every escalation passes
through. Per-call and per-build records; `claude_*` totals emitted into every metrics row.

Two conditions are now mandatory for every economics arm:

    CLAUDE_USAGE_STRICT=1        an unpriceable call raises rather than scoring as zero
    claude_calls_missing_usage   must be 0 on every row; any row with a non-zero value
                                 VOIDS its arm — a cost of 0 and a cost of unknown are
                                 different facts and must never be summed together

Validated against a controlled fake CLI with no billed calls: well-formed result object,
plain-text output, wrong JSON `type`, empty stdout, accumulation across calls, and strict
mode raising on each unattributable path. Four tests in `test_al_intelligence.py`.

### Live-capture validation — folded into the first allocated arm, with a hard stop

The schema was read out of the shipped CLI binary and exercised only against a fake, so live
capture is unverified. It is validated **in the first real production invocation of the first
allocated arm**, not by a standalone probe.

Chosen deliberately. A probe validates a call shape; folding it in validates attribution
*through the actual economics harness*. This project has repeatedly caught failures at the
boundary between "the check works" and "the production path is really using it" — the
`_OBJREF_RE` gap, `event_verify._SUB_RE`, the Part 2 driver's backend guard reading stale
logs, and the zero-token case below. Validating anywhere other than the real path leaves that
boundary untested.

Protocol, declared in advance so the run stays valid if it passes:

    1. the first arm runs with CLAUDE_USAGE_STRICT=1 from its first invocation
    2. that first Claude call must yield  attributed=true
                                          input_tokens + output_tokens > 0
                                          claude_calls_missing_usage == 0
    3. any failure  -> hard-abort immediately, VOID the arm, score no economics
    4. success      -> the run is a valid first observation. The requirement was
                       pre-declared and neither the task nor the routing policy changed to
                       accommodate it, so nothing about the measurement was altered by
                       validating on it.

**A well-formed result object is NOT proof of a priced call.** The CLI synthesizes
`{type:"result", subtype:"success", total_cost_usd:0, num_turns:0, usage:{zeros}}` on some
paths. Strict mode originally accepted that and scored it at $0 — the guard recognising the
healthy shape while a degenerate instance walked through. Zero tokens is now classified
unpriceable, not free, and hard-fails under strict mode. Regression-tested.

## What the prospective shadow log already tells us

`.capability-shadow.jsonl`, 297 rows, rule v1 frozen and observational throughout. Not
retuned, not fitted on this data.

    fired                    81 / 297  (27%)
    terminal class overall   LOCAL_GREEN 181, BROAD_BOUNDARY 59, NARROW_STALL 57
    among the 81 fires       BROAD_BOUNDARY 57, NARROW_STALL 24, LOCAL_GREEN 0
    recovered_after_fire     0 / 81
    rounds_saved             median 4 (range 0-5)

**Zero of the 81 fires landed on a build that then recovered locally.** That answers the
pre-registered SAFETY question for rule v1 as strongly as observation can: a live trigger
would never have spent tokens pre-empting a build that would have healed itself.

**A label needs revisiting, and this is flagged BEFORE the experiment rather than after.**
Rule v1 counts its 24 `NARROW_STALL` fires as `would_be_false_fire`. That definition was fixed
before Part 2 showed Claude closing narrow ABS-contract stalls **8/8**. A narrow stall that
never recovers locally and that the rung reliably closes is not obviously a false fire — it
may be the most profitable thing to escalate. This is a **hypothesis to be tested here, not a
reinterpretation to be assumed**, and the rule itself stays frozen either way.

Two segmentation rules carried over, both mandatory:

- Exclude the 13 Claude rows (`claude-code` 5, `claude-takeover` 8). They are not local builds
  and a trigger never sees them.
- Segment before aggregating. 284 of 297 rows are `qwen3-coder_30b` bench runs; pooled numbers
  describe the suite, not the workload.

## ALLOCATION — declared before the driver exists

Declared first deliberately: a driver written before the allocation quietly encodes the
sampling decision in its loop structure.

**120-run balanced factorial, 10 per cell.**

| fixture | A: never | B: fixed-round | C: compound | total |
|---|---|---|---|---|
| doclink | 10 | 10 | 10 | 30 |
| p1 | 10 | 10 | 10 | 30 |
| p4 | 10 | 10 | 10 | 30 |
| map | 10 | 10 | 10 | 30 |
| **total** | **40** | **40** | **40** | **120** |

doclink is the hard, escalation-engaging case and tests whether B/C buy successful repair.
p1 is the non-engaging control population and tests unnecessary-trigger behaviour. p4 and map
supply the intermediate populations that actually exist in the corpus, rather than pretending
doclink is the workload. Equal cells keep arm comparison and fixture segmentation simple, and
10 per cell matches the existing block scale so the known block-level variability stays
visible instead of being averaged away.

### Why not the leaner 105-run variant (5/arm on p1)

Because it saves nothing it is meant to save. Projected from 284 local shadow rows:

    fixture   n     B fires   C fires   never-green
    p1       48       0  0%     0  0%        0%
    p4       72       5  7%     1  1%        1%
    map      50       3  6%     2  4%        4%
    doclink 114     114 100%   78 68%       99%

    120-run balanced: ~18.7 escalating builds -> ~30 billed Claude calls (arm A: 0)
    105-run variant:   0.0 billed calls saved, 15 local runs saved (~75 min wall clock)

**p1 escalates 0% under both B and C across 48 observations, so the p1 cells cost nothing to
begin with.** Trimming them reduces local wall-clock, not spend. If billed exposure is the
limiting resource the only lever is doclink — and doclink is the informative cell, so cutting
it costs the experiment the thing it exists to measure. The lean variant is the wrong economy.

Total projected exposure ~30 billed calls, against 19 for Tier B Parts 1 and 2 combined.

### Segmentation and weighting — binding

**Fixture is the primary unit of analysis.** Every outcome is reported per fixture first.

**Equal allocation does NOT assert that the workload is 25% each fixture.** It is a design
choice for comparison power, nothing more. Any pooled or "overall workload" number requires an
explicit weighting rule over fixtures, **fixed before launch**. That rule is a statement about
the real job mix and is not derivable from this corpus — it is not declared here.

**Until a weighting rule is declared, no aggregate is reported at all.** Segment-level results
stand on their own; an unweighted pooled figure would describe the design, not the workload.

**DECLARED 2026-08-23: weighting is explicitly DEFERRED.** This experiment reports per-fixture
results only. No workload mix is invented from the benchmark corpus. A later
deployment-specific weighting may combine these per-fixture estimates under its own declared
job mix; that is a separate exercise and not part of this registration.

## Outcomes

**Primary — cost-weighted regret per build, against the oracle.** For each arm, the value lost
relative to escalating exactly the right builds: unnecessary spend on builds that did not need
the rung, plus unclosed builds the rung would have closed.

**Secondary, reported separately and never folded in:**

    net closure rate      builds reaching green, by arm
    spend per closed build
    latency per build     local rounds displaced vs escalated call time
    fire precision        fires that were BROAD_BOUNDARY / NARROW_STALL / LOCAL_GREEN
    capture ratio         fraction of the oracle's available value that arm C realises

## Decision rule — pre-declared

    C beats B and A on cost-weighted regret        adopt the compound trigger
    C beats A but not B                            keep the fixed-round policy; the rule adds
                                                   complexity without value
    B and C both worse than A                      escalation is not economic at this price;
                                                   revisit only if the rung's cost changes
    C's capture ratio is low but positive          the rule works and is badly tuned — a
                                                   RETUNING is a new pre-registration, never a
                                                   post-hoc adjustment of this one

## Guardrails

- **The rule is frozen.** Its parameters were fitted on p1/p4/map and tested on doclink, i.e.
  without the workload judging them. Retuning on the shadow log and then citing that log as
  validation destroys the only property making the data worth having.
- **Fixture matrix.** doclink is the only fixture where escalation reliably engages; p1 fires
  0/20. An economics experiment run only on doclink measures the price of the hardest case.
  Allocation across the matrix must be declared before running, and the noise floor applies —
  two identical 10-run blocks of the frozen corpus gave residual medians 7 and 3.
- **Cost is per-token and real.** Every arm's spend is recorded and reported, including runs
  that end up excluded.
- No arm may be added, dropped or re-scored once the first billed run starts.

### NO SPEND CAP — declared 2026-08-24

There is **no discretionary suite-level spend ceiling**, and this is a measurement decision
rather than a budget one. A cap driven by realised cost makes the stopping rule depend on an
OUTCOME: the expensive cells consume the budget first, later observations go selectively
missing, and the per-fixture estimates stop being based on the fixed allocation they were
registered with.

    the fixed allocation (120 runs) is the ONLY exposure bound
    ~30 billed calls is a PLANNING ESTIMATE, never a stopping rule

The hard stops that remain are all measurement-integrity guards, none of them budgetary:
strict-usage failure, missing attribution, first-live-call validation failure, arm isolation
failure, rule fingerprint mismatch, backend or provenance failure, and any other pre-declared
VOID condition. The distinction held throughout this project: **a guard that prevents an
invalid measurement is legitimate; a guard that selectively stops expensive valid measurements
changes the experiment.**

If an external or provider-level limit prevents completion, **record the interruption
explicitly**. Do not replace missing runs, and do not silently rebalance cells — either
requires a new registration.

### Cost telemetry — recorded, structurally unable to feed back

    per call   label, attributed, cost_usd, input/output tokens, wall_s
               -> claude_call_costs on every metrics row
    per run    claude_calls, tokens, cost_usd, api_ms, turns, calls_missing_usage
    per suite  bench_ledger.py — cumulative runs, calls, cost, tokens, and a count of
               rows whose spend is INCOMPLETE

`bench_ledger` only reads metrics that already exist and appends a line. It exposes no
threshold, no predicate and no boolean — there is deliberately nothing in its return value for
a driver to branch on — and it is fail-open, so telemetry can never itself be the reason a
suite stops. Regression-tested on all three properties.

## Explicitly out of scope

Model selection (settled), fixture repair, prompt changes, and anything requiring the eight
reserve takeover states — those need their own registration.

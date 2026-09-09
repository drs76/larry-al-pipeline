# PRE-REGISTRATION — unmask: retain the rewritten tree, or revert it?

Written and committed **before any run**. Decision rules here are fixed; a result that does
not fit them is reported as not fitting, not reinterpreted.

## The question

> When the unmask condition triggers, does reverting to the pre-repair tree versus retaining
> the rewritten tree affect subsequent resolution?

## What is randomised, and what is NOT

    A  unmask enabled (current)  when error_keys satisfies the existing disjointness
                                 condition, RETAIN the rewritten tree and continue
    B  always-revert             when the SAME condition would trigger, revert to the
                                 pre-repair tree and continue

**The trigger predicate is byte-identical in both arms.** What is randomised is the
consequence of the trigger, not whether the trigger occurs. Arm B must evaluate the same
`error_keys` disjointness test and log the same trigger event; it differs only in the branch
taken afterwards. An implementation that changes when the condition fires voids the suite.

Nothing else changes: not `error_keys`, not the scoring, not the repair prompts, not the
fix-route selection, not `MAX_FIX_ROUNDS`.

## Why arm B is not obviously the safe arm

Unmask exists because reverting re-fed the same blocker indefinitely: one AL0282 surfaced 16
AL0132s, reverting restored the AL0282, the coder renamed it again, and the run spent all 8
rounds on that cycle. Arm B may thrash by construction. **That is the thing under test, not a
reason to skip it.**

## The estimand, stated explicitly

> The effect of retaining the rewritten tree rather than reverting it, **conditional on the
> run reaching an unmask-trigger event.**

## Primary endpoint

**Final terminal error score, restricted to runs in which the pre-registered unmask trigger
fired at least once.** A vs B compared on that population.

This restriction is not post-hoc selection. Triggering is the treatment-eligibility
condition, and both arms use the identical trigger, so the eligible populations are defined
the same way in each. Comparing across all runs would drown the effect in runs where the
intervention never occurred — the endpoint/mechanism mismatch already recorded against the
`dlinvar` suite.

## Experimental unit

**The run.** Not the trigger event. A run that triggers three times contributes one
observation. Repeated triggers are a secondary measure, never independent samples.

## Secondary endpoints — pre-registered, and NOT substitute causal endpoints

1. Terminal pass/fail among triggered runs.
2. Repair rounds executed after the first trigger.
3. Count of additional unmask triggers after the first (the suspected thrash mechanism).
4. Best score reached after the first trigger, recorded separately from the terminal score.
5. Trigger-to-terminal trajectory, including error-set transitions at each round.

If the primary endpoint is null, a secondary that moves does not rescue the result. It
becomes a hypothesis for a later experiment, stated as such.

## What will NOT be used

- Unconditional pass rate.
- All 1195 historical runs as the treatment population.
- `pre-unmask best` treated as a valid baseline score.
- The retrospective `205/311 ended worse` count as evidence that unmask is harmful.
- The `HALT` parse-halting classification. It was invented during exploration and is
  **withdrawn**: the unmask docstring's own founding case is AL0282, a semantic error that
  demonstrably masked 16 downstream diagnostics, so "only parse-halting errors can mask" is
  false. Nothing derived from it enters the evidence base.
- Retrospective classification of which errors "really were" masked, as any endpoint.

## The clause that keeps this an intervention

> **No claim about whether masking is genuine will be inferred from the observed error-set
> disjointness.** This experiment tests the CONSEQUENCE of the existing unmask decision, not
> the truth of its causal interpretation.

Without this the suite silently reverts to "prove the mechanism, then evaluate the treatment",
which is the failure mode already recorded in `feedback_mechanism_needs_intervention`.

## A change that is explicitly out of scope

Keeping a separate minimum-ever snapshot for the final restore, so a run cannot report worse
than a score it reached. **Rejected before running.** If the masking is genuine, that
low-scoring tree carries hidden errors, and restoring it ships precisely what unmask exists to
expose. It would improve the reporting optics by changing repair semantics. Not a candidate.

## Sample size and stopping rule

Sample size is **not** derived from the 313 retrospective events: those are events rather than
independent observations, and the triggered subset is selected by construction.

- Fix N runs per arm **in advance**, interleaved, assignment sequence written down before the
  first run.
- Report how many runs actually triggered.
- If the triggered count is small, the result is reported as **underpowered**. The window is
  not widened until the result becomes persuasive.
- First batch is deliberately modest and **diagnostic**: enough interleaved runs to show
  whether A/B trajectories separate at all. It does not establish a population effect and will
  not be described as doing so.

## Harness

Reuses the `dlinvar` machinery: a git worktree per arm plus a dispatch wrapper selecting the
tree from a per-arm environment variable, with the compiled treatment asserted from the file
about to execute immediately before each run and captured beside the log. Fixture restored to
an identical state before every run.

## Status

Everything above this section is the registration **as written before any run and before arm B
existed**. That is the boundary: it records what was committed to in advance, and nothing in it
has been edited since.

**Executed 2026-09-05.** Results: [`bench-results/unmask-ab-pilot-results.md`](bench-results/unmask-ab-pilot-results.md),
artefacts in `bench-results/unmask-ab-pilot/` (12 raw logs, frozen assignment sequence and
hashes, `armB.patch`, the void harness batch).

**Outcome: underpowered, inconclusive, no treatment-effect claim.** Primary endpoint —
terminal error score among triggered runs — A 2 triggered (4, 2), B 5 triggered (2, 1, 5, 5, 1).
Seven of twelve runs contributed to the estimand. Underpowered **by the design registered
above**, which committed in advance to reporting a small triggered count as underpowered rather
than widening the window. That commitment was honoured: no larger N has been chosen from these
results, because sizing a follow-up on an observed direction would make it an implicit
continuation rather than an independent test.

Two observations recorded there, neither used as evidence about efficacy: trigger incidence
differed (A 2/6, B 5/6) which is unexpected given an identical pre-trigger implementation and
too sparse at this n to diagnose; and arm B triggered repeatedly, descriptively consistent with
the predicted revert/thrash mechanism.

The pre-run requirement above was met: arm B's diff was reviewed against the identical-trigger
predicate before any run — trigger predicate, `error_keys()` and `count_build_errors()` all
verified byte-identical across arms, with no changed line outside the unmask consequent.

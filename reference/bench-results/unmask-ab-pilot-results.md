# RESULTS — unmask retain-vs-revert, pilot batch

Registration: [`../exp-unmask-revert-preregistration.md`](../exp-unmask-revert-preregistration.md)
@ `9ba5b96`, written before any run and before arm B existed. Its Status section links back
here; everything above that section is the registration as committed in advance and unedited.

**Arm B is reproducible from `unmask-ab-pilot/armB.patch` alone.** It lived in a throwaway
worktree by design and that worktree has been removed; the patch was verified byte-identical
to the live worktree's diff and to apply cleanly before removal.

Batch: 12 runs, 6 per arm, interleaved, 2026-09-05, doclink fixture,
`ollama/qwen3-coder:30b`, escalation off, egress local-only, `MAX_FIX_ROUNDS=5`.
Artifacts in `unmask-ab-pilot/`.

> ## Verdict: underpowered, inconclusive. **No treatment-effect claim.**
>
> Underpowered **by pre-registered design** — the registration fixed a modest diagnostic
> batch and committed in advance to reporting a small triggered count as underpowered
> rather than widening the window. It was not failed by the trigger imbalance below.

## Arms

    A  unmask enabled (main @ 9ba5b96)      retain the rewritten tree, fix forward
    B  always-revert (worktree, armB.patch) revert to the pre-repair tree

Arm B is a 3-line change inside the unmask consequent. With log lines stripped its body is
md5-identical to the existing ordinary-regression branch, so arm B introduces no new code
path — it routes the trigger into a branch the pipeline already exercises constantly.
Verified before running: trigger predicate, `error_keys()` and `count_build_errors()` all
byte-identical across arms; no changed line outside the consequent.

## Primary endpoint — terminal error score among triggered runs

| arm | assigned | triggered | terminal scores | mean |
|---|---:|---:|---|---:|
| A | 6 | 2 | 4, 2 | 3.00 |
| B | 6 | 5 | 2, 1, 5, 5, 1 | 2.80 |

Seven of twelve runs contribute to the estimand. Arm A contributes two. **3.00 vs 2.80 is
not evidence of an effect** and is not reported as one.

Secondary endpoints carry nothing: **0/12 passes**, and every run used all six rounds.

## Two observations, neither used as evidence about efficacy

**Trigger incidence differed: A 2/6, B 5/6** (Fisher p = 0.2424). The pre-trigger
implementation is *required* to be identical, so this is an **unexpected observation**. The
batch is too small to determine whether it reflects stochastic variation or an
implementation/environmental divergence. It is compatible with chance; it is not established
as chance, and it is not used as evidence about treatment efficacy. If a larger batch
preserved this gap, the byte-identical-predicate assumption would need re-examining rather
than explaining away.

**Repeated triggers within arm B:** events per triggered run A `[1,1]` mean 1.00, B
`[4,2,1,1,1]` mean 1.80. This is descriptively consistent with the revert/thrash mechanism
the unmask docstring predicts — reverting restores the blocker, the coder re-fixes it, the
condition recurs. Genuinely interesting, and **not** a treatment-effect rescue for a null
primary. Per the registration it becomes a hypothesis for a later experiment.

## Execution record

What the batch established cleanly, independent of the null result:

- The void batch (below) is excluded from analysis entirely.
- The repaired driver was validated before relaunch — seeding checked without GPU time.
- The frozen sequence and both arm trees were verified unchanged immediately before dispatch.
- Assignment was genuinely interleaved: `A B B B B A A A B A A B`, seed 20260905.
- Per-run arm assertions read the marker from the file about to execute; an arm substitution
  would have aborted rather than produced an uncomparable row.

`bench-run-suite.sh` was NOT used. At the time its loop was `for arm; for project; for repeat`,
so it ran every control then every challenger — within-session drift confounded with the arm.
Not fixed mid-experiment, because refactoring it would have made the reviewed arm-equivalence
stale.

**Since fixed, but narrowly.** The grouping was deliberate and carried a comment saying so:
interleaving forces a model swap every run, and a dense-27B challenger cold-loads in ~210s.
That rationale holds for model-vs-model suites and is untouched. It does NOT hold when both
arms share a model and the treatment is env or code — as here — so the suite now interleaves
in exactly that case and groups otherwise, announcing which in the preflight. A same-model
suite no longer needs to drive its own sequence.

## The void batch, preserved

The first dispatch produced 12 runs that died in 2-3s each with no RESULT line. Zero
observations, so nothing influenced N, the sequence or the endpoint, and the registration was
not compromised. Preserved intact in `unmask-ab-pilot/void-harness-batch/`.

Two driver bugs, both mine, both from reimplementing fixture seeding that
`bench-run-suite.sh` had already solved:

1. **No handover path rewrite.** The manifest carries absolute paths pinned to the fixture
   dir; copied verbatim into a run dir every path is "outside the project root", 0 expected
   files parse, and the run aborts. `run_one` carries a comment explaining exactly this,
   written because it had already cost a previous session its write budget.
2. **`src/` was copied.** The suite deliberately does not copy it — the model writes it.

The second is the valuable audit finding. The path bug failed loudly in two seconds. The
`src/` bug would have failed **silently**: full logs, real scores, plausible trajectories,
every run handed a finished tree, and an entire batch of confident nonsense. Only the loud
bug prevented the quiet one from reaching the analysis. A harness failure that announces
itself is worth more than one that produces publishable-looking output.

## What happens next

**Nothing, for now.** No larger N is chosen from these results: sizing a follow-up on an
observed direction would make the next round an implicit continuation of this one rather than
an independent test. A larger experiment, if wanted, needs its own pre-registration with its
own rationale for N. This 12-run batch is a completed pilot, not a truncated first half.

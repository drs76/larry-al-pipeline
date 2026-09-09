# TIER B PART 2 — Claude takeover of stalled Qwen states

Registration: `exp-tierb-claude-preregistration.md`. Corpus: `tierb-part2-corpus-manifest.md`
(frozen, sha256 `c85ebfe368194755…`, recorded in every metrics row). Suite `tierb2`,
2026-08-23, driver `aec5f45`, 16 min.

The eight pre-declared states, run exactly as frozen. No reserves substituted, no early stop,
no redraw.

## PRIMARY OUTCOME — terminal closure: 8 / 8

| candidate | source residual | closed | rounds | duration |
|---|---|---|---|---|
| `b2_challenger/r3` | 1 — `AL0133` | **yes** | 1 | 41s |
| `b3_challenger/r5` | 2 — `AL0151`, `AL0122` | **yes** | 1 | 56s |
| `b3_challenger/r1` | 3 — `AL0151`×2, `AL0173` | **yes** | 1 | 53s |
| `b3_control/r2` | 3 — `AL0133`×3 | **yes** | 1 | 53s |
| `b3_control/r4` | 4 — `AL0133`, `AL0132`×3 | **yes** | 4 | 281s |
| `b3_challenger/r4` | 6 — `AL0133`×5, `AL0173` | **yes** | 1 | 86s |
| `b2_control/r4` | 7 — `AL0133`×6, `AL0132` | **yes** | 2 | 113s |
| `b2_control/r2` | 15 — `AL0132`×10, `AL0133`×3, `AL0173`, `AL0122` | **yes** | 2 | 156s |

**Pooled: 8/8.**

The comparison is within-state, which is stronger than a between-group test: these eight trees
ARE Qwen's terminal outputs. Qwen had its full five fix rounds on each and closed none of them.
Claude, taking over at the repair stage on the identical tree, closed all eight.

    same eight states:   Qwen 0/8 (terminal, 5 rounds each)   Claude 8/8

**Answer to the registered question: yes. Claude closes honest, Qwen-generated stalled states
when taking over at the repair stage.**

## Verification

    coder                claude-code / backend=claude   x8
    path                 --skip-larry; logs show only "Claude-fix" calls, no "Larry-write"
                         — Claude repaired, it never wrote from scratch
    tree hash            asserted against the frozen manifest before every call; 8/8 matched
    first_pass_compile   false x8 — the stalled state does not compile, as it must not
    files                9/9, manifest_ok true x8   (8 AL sources + app.json)
    referee              bare_compile_only false, analyzers_missing none, profile_failures []
    final_diagnostics    {} x8
    escalation           claude_escalated false, mid_escalated false x8 — no rung armed
    provenance           tracked, fixture_commit 422c749 x8
    identity in metrics  source_candidate, source_tree_sha256, corpus_manifest_sha256 on
                         every row

## Secondary — description only

Rounds `[1,1,1,1,1,2,2,4]`, median 1. Duration median 71s, total 839s across all eight.

Difficulty does not order the effort. The 4-error state took the most rounds (4) and the
longest time (281s); the 15-error state took 2 rounds and 156s; five states closed in a single
round. With n=1 per state and no repeats, none of this supports a claim — it is recorded
because it is the shape of the data, not because it means something yet.

Residual movement is degenerate: every state went to zero.

## What this establishes

Combined with Part 1 — **and deliberately not pooled with it** — the two parts answer different
questions and both came back positive:

    Part 1  Claude writes doclink from scratch          5/5   (4 of 5 clean on first compile)
    Part 2  Claude closes a stalled Qwen tree           8/8   (median 1 repair round)

Part 2 is the one that bears on architecture. A capability ceiling alone would have been
consistent with "Claude is better at writing"; closure from Qwen's own stalled trees shows the
advantage transfers to **takeover at the repair stage**, which is what an escalation rung
actually does.

Per the pre-registered decision tree, this is the first branch: **escalation architecture is
viable, and Kimi was the wrong rung.** The next question is routing economics and trigger
design — when does Claude earn an escalation — not whether late escalation can recover local
failures. It can, on this fixture, in this error class.

## Limits, stated plainly

- **n=8, one attempt per state, no repeats.** There is no variance estimate. A state that
  closed here might not close on a second attempt.
- **One error class.** The corpus is ABS-contract by construction; the parse-class states were
  excluded as masked. This says nothing about those, nor about fixtures other than doclink.
- **Cost is unmeasured** beyond wall-clock. Routing economics needs token and money
  accounting, which this experiment did not collect.
- **`Unmask` behaviour was not re-examined** here — every run reached zero, so there was no
  residual to mask.

## Implementation prerequisites — not evidence

The enterprise-anon harness corrections (`38802b6`) and the Part 2 driver (`aec5f45`) carry no
weight for the hypothesis. Recorded because two of their defects were caught by validation
rather than by results, and each would have produced a FALSE NEGATIVE:

1. Path-dependent tree hash — could never have survived the copy it existed to verify.
2. The backend guard passing on stale log evidence: the fake-pi test returned 0/8 closure
   instead of VOID, so a silent fallback to the local model would have been reported as
   "Claude cannot close these".

A 0/8 from either defect would have been indistinguishable, in the summary line, from the real
result's opposite.

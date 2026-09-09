# TIER B PART 1 — full-run Claude capability on doclink

Registration: `reference/exp-tierb-claude-preregistration.md`. Suite `tierb1`, 2026-08-23.
n=5 as pre-declared, 25 min, `EGRESS_POLICY=enterprise-anon`, preflight PASS before every run.

## Primary outcome — terminal capability

    Claude          5 / 5   pass
    frozen corpus   0 / 20  (qwen3-coder:30b, same fixture, same handover)
    all tracked     0 / 82  qwen doclink runs, every configuration to date

Fisher exact against the frozen corpus: **p = 1.9e-05**. Against all 82: p = 3e-08.

**Claude crosses the ABS boundary. Qwen never has.**

Four of the five passed on the FIRST compile, with no fix round at all. One needed a single
round. This is not a narrow win at the margin — the fixture is close to trivial for Claude
and has been impossible for the local model across 82 runs and every intervention this
session.

## Verification — because a 5/5 is exactly when to check hardest

    coder_model            claude-code   (x5)   backend=claude
    banner                 "Coder backend: claude (Claude Code, Pro sub)"   x5
    escalation             "Escalation: off"    x5, no mid-tier line — Claude is the CODER
    anon mirror really used  "Running Claude Code (Larry-write) in scrubbed mirror
                             (enterprise-anon)" x5, plus one Claude-fix call. No
                             "mirror was EMPTY" warning on any run.
    files                  9/9 written, manifest_ok true   x5
    referee completeness   bare_compile_only false, analyzers_missing none,
                           profile_failures [], profile_unenforced {}   x5
    final_diagnostics      {} on all five
    autonomous_pass        true x5; claude_escalated false, mid_escalated false
    provenance             tracked, fixture_commit 422c749,
                           handover e82168cb3857, fixture_dirty false — identical to the
                           frozen corpus

The pass is a full referee pass, not a bare compile, on the same fixture revision and the
same handover bytes the 20-run baseline used.

## The contract Qwen could not hold, held

The frozen corpus failed on one class. In a passing Claude tree:

    if not ABSOperationResponse.IsSuccessful() then          ← AL0173 x19 in the baseline:
                                                               `not` applied to the codeunit
    TenantMedia.Content.CreateInStream(ReadStream);          ← AL0133 x39 in the baseline:
                                                               OutStream where InStream required
    ABSOperationResponse := ABSBlobClient.GetBlobAsStream(BlobName, ReadStream, ABSOptionalParams);
    Error(ABSOperationResponse.GetError());

`IsSuccessful()` on the response rather than a truthiness test, and `CreateInStream` on the
Tenant Media content rather than a mismatched stream. These are exactly the two errors that
account for most of the baseline residual.

## Residual — DESCRIPTIVE ONLY, per the registration

`final_diagnostics` is empty on all five runs, so there is no residual to characterise.
Durations 249–346s, mean 300s, indistinguishable from the local runs' ~300s — recorded as
description, not as a claim. At n=5, and against a baseline whose two identical 10-run blocks
gave medians of 7 and 3, no residual-size statement would have been decision-grade anyway.

## What this establishes, and what it does not

**Establishes:** doclink is knowledge-bound. The fixture is solvable and the handover is
sufficient — a model with the ABS contract compiles it first try. The pre-registration's first
branch is the one we are in: escalation architecture is potentially valid and Kimi was simply
the wrong rung. The alternative branch — "defect is in the fixture, the handover, or the repair
loop" — is refuted for the fixture and the handover.

**Does NOT establish that escalation works.** A full Claude run shares nothing with a Qwen run
except the handover. Whether Claude can close a tree Qwen has already stalled is Part 2, which
is a different question and is not started. No pooling with this result.

**Does not license reinterpreting the frozen corpus.** It stays as measured.

## Harness corrections this run depended on

Both recorded in `38802b6`, both changing what the coder can SEE and never the task, the
allocation or the scoring:

1. Per-run `git init` + commit of the seeded inputs. `runs/` is gitignored inside the setup
   worktree, so the anon hook's repo test passed while `git ls-files` returned 0 and the
   mirror came out empty.
2. `ANON_AUTOCOMMIT=1` (opt-in). Round 2's mirror contained no `src/`, because an applied
   patch is left uncommitted and only tracked files are mirrored. Without it every fix round
   hands Claude a workspace missing its own output.

Caught by the preflight before any billed call, not discovered in the results.

## Scope

`enterprise-anon` scrubs the mirrored workspace, NOT the prompt — `run-build.py` inlines the
full handover into the prompt and it egresses verbatim. In scope for this synthetic fixture
and stated in the run banner. **It must not be generalised into a guarantee for customer
material.**

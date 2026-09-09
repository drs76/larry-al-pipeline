# PRE-REGISTRATION — Tier B: Claude on doclink (capability ceiling + takeover repair)

Written before any Tier B run. Two parts, deliberately separate. **They answer different
questions and must never be combined into one number.**

Follows `exp-mid-ladder-preregistration.md` (+ Amendment 1) and its result,
`bench-results/mid-ladder-tierA-results.md`.

## Why this experiment exists

Tier A returned a clean null: the Kimi rung closed 0/10 doclink runs, control 0/10, p=1.0.
That result cannot distinguish two very different worlds, because Kimi and Qwen may lack the
same knowledge:

- **Escalation architecture is sound, the rung was wrong.** A model that HAS the missing
  knowledge closes these runs. → the live question becomes which rung, and at what cost.
- **Escalation cannot help at all.** Even a strong model fails from the same states. → the
  defect is in the fixture, the handover, or the repair loop, and no routing change touches
  it.

`codeunit-probe` already contrasts Claude 3/3 with qwen 0/21 on the ABS construct, which is
why Claude is the discriminating candidate rather than another mid-tier model.

## A finding that constrains the design — read before Part 2

The 20 Tier A runs do not fail as one class. They fail as at least two, and one of them is
not a capability failure at all:

| stratum | n/20 | residual | class |
|---|---|---|---|
| **namespace/using** | 5 | 1–3 errors, AL0247 "target Table … not found" | mechanical |
| ABS contract | ~9 | 6–14 errors, AL0133 / AL0132 / AL0173 | knowledge |
| other / mixed | ~6 | 1–9 errors, AL0185, AL0134, AL0124 | unclassified |

The namespace stratum separates perfectly. A run whose table extension declares its own
`namespace` but omits `using Microsoft.Foundation.Attachment` hits AL0247 in **5/5** runs;
every other combination hits it in **0/15**:

    ns=1 using=0  → AL0247   5/5
    ns=1 using=1  → clean   5/5
    ns=0 using=1  → clean   6/6
    ns=0 using=0  → clean   4/4

This is not a spec defect. `larry-handover.prompt.md:393` states the rule explicitly, with a
correct/incorrect worked pair at lines 314–333. The model has the rule in context and drops
it in 25% of runs.

**And the pipeline already has an auto-fix that should have caught it.**
`add_missing_using_directives()` (`run-build.py:958`) inserts the `using` lines a file needs
— it fires on these very runs, logging "added 2 missing using-directive(s)". It misses this
case because `_OBJREF_RE` (`run-build.py:950`) matches only variable-declaration forms:

    \b(?:Record|Codeunit|Page|Report|Query|XmlPort|Enum|Interface|TestPage|Database)\s*(?:::)?\s*("[^"]+"|\w+)

An object **header** reference is not that shape:

    tableextension 50110 "TSG Doc Attachment Ext" extends "Document Attachment"

So when a file's only reference to a base-app object is its `extends` target, the auto-fix
never sees it, adds nothing, and the extension fails to resolve. `implements` on an interface
has the same shape and the same gap.

That reframes option (a) below: it is not "write a new lint", it is "close a known gap in an
existing auto-fix" — materially cheaper, and it removes a defect that silently costs 25% of
doclink runs. `validate_al_syntax.py` is a separate matter: it has no namespace rule and is
not wired into `run-build.py` at all.

**Consequence for Part 2:** four of the six near-green states fail on this rule. Handing them
to Claude measures whether Claude can add a `using` line. That is not the escalation question
and must not be scored as it.

**Open decision, to be resolved before Part 2 runs** (deliberately not pre-decided here):

    (a) Fix the mechanical class first — add the namespace/using rule to the referee, re-run
        doclink 10, and take the near-green corpus from the cleaned population. Cleanest
        measurement, costs one local suite (free), and delays Tier B.
    (b) Stratify and report separately — run Part 2 over both strata with the namespace
        states labelled, scoring only the non-mechanical ones. No delay, weaker corpus.

Part 1 is unaffected by this decision and can run either way.

## Baseline — FROZEN 2026-08-23

`bench-results/doclink-frozen-corpus.md`, n=20 (`doclinkclean2` + `doclinkclean3`), pipeline
at `b0c329f`. Both mechanical layers closed: AL0247 namespace/using 5/20 → 0/20 (fixed),
AL0114 bare-identifier subscriber 3/10 → 0/20 (absent, unexplained). Residual is one class,
the ABS Storage / Temp Blob / Media contract, led by stream direction — AL0133 88 errors in
14/20 runs, 39 of them `OutStream` where `var InStream` is required. 0/20 passes.

**Two constraints this baseline imposes on the design below.**

*Noise floor.* Two identical 10-run blocks, same commit, gave residual medians of 7 and 3.
Any effect smaller than that swing is unmeasurable at n=10 per arm. Part 1's n=5 can support
a claim about passing or not passing; it cannot support a claim about residual size.

*Corpus selection bias.* `doclinkclean3/control/r1` showed keep-best preferring a MASKED tree:
round 4 scored 1 because an unparseable subscriber suppressed the rest of that object, round 5
repaired it and revealed 4 contract errors scoring 4, so the run reverted to the masked tree.

### Corpus selection rule for Part 2 — binding

**A takeover state is NEVER selected by minimum observed error count.** A masked tree scores
better than the unmasked state that contains more truth, so "lowest score" and "most
diagnostically exposed" are different orderings and the first is the wrong one.

Selection requires, per candidate:

    final_diagnostics     the residual's CLASS composition, not its size
    score trajectory      every round's error score, so a masked dip is visible as a dip
    Unmask events         where and how often the loop surfaced suppressed errors
    residual codes        from the final round, to confirm the class is ABS-contract

A candidate qualifies only if its residual is ABS-contract by composition. A state whose
residual is a single parse-class error (AL0247, AL0114, AL0151-from-a-malformed-attribute) is
**excluded**: it is masked by construction and its true distance is unknown.

Record the selected states and the rejected ones with the reason, so the corpus can be
audited rather than trusted.

## Part 1 — full-run Claude capability (end-to-end)

> Given the doclink handover from scratch, does Claude produce a compiling extension where
> Qwen never does (0/82 tracked first-pass, 1/82 terminal)?

    CODER_BACKEND=claude
    fixture     doclink, locked, handover sha e82168cb3857
    n           5 runs, pre-declared, no extension without a new registration
    MAX_FIX_ROUNDS 5, RUN_TIMEOUT 1800
    escalation  none — Claude IS the coder here, not a rung

**Outcome — terminal capability only.** Does Claude cross the ABS boundary and compile the
fixture? Pass or not pass, against Qwen's 0/82.

**Residual reduction is DESCRIPTIVE, not decision-grade.** Two identical 10-run blocks of the
frozen baseline gave residual medians of 7 and 3. At n=5 a residual difference carries no
information, and no reading of this experiment may rest on one. Report `final_diagnostics`,
first-pass compile, fix rounds and duration as description of *how* it passed or failed.

**Reading:** this establishes the ceiling. It does NOT establish that escalation works — a
full Claude run shares nothing with a Qwen run except the handover.

## "Near-green" is not a safe description — error masking, measured

The case for Part 2 was originally "six runs ended one error from green". **That claim is
withdrawn.** A low error score does not mean a short distance to compiling, because AL
diagnostics mask: one unresolved symbol suppresses everything downstream in that object.

Score trajectories across the 20 Tier A runs: **14/20 reached ≤2 errors at some point, only
7 ended there.** The `Unmask` path fired in 9/20 runs, and four runs went from ≤1 error to
7–14 and never came back.

Traced through `challenger/r10` (`[3,3,1,1,14,14,14,14]`):

    round 1  score 1   AL0132  'Record "TSG Doc Link AZ Setup"' has no such member
    round 2  score 14  AL0126  no overload for 'GetBlobAsStream' takes 4 arguments
                       AL0133  argument 3: cannot convert from 'Dictionary of [Text,Text]'
                       AL0774  Try methods should not specify an explicit return value

Clearing the single error revealed the ABS contract failure underneath. The one-error state
was a mask, not a near-miss.

**Two consequences.** First, the `Unmask` rule is behaving correctly — it surfaces truth
rather than destroying good states, and the earlier suspicion that the repair loop wrecks
near-green trees is not supported. Second, `best achieved: N` cannot be used to select a
"nearly finished" corpus, which is what Part 2 assumed.

This also compounds the namespace finding: an unresolved `extends` target suppresses every
downstream error in that object, so the five AL0247 runs are masked by construction and their
true residual is unknown until the auto-fix gap is closed.

## Part 2 — takeover repair (the actual escalation architecture)

> Given a Qwen-produced tree that the local model could not close, can Claude close it?

Note the weakened framing: these are **stalled** states, not near-green ones. Claude will have
to do the unmasking work too, which is a legitimate escalation test but is not "close the last
error".

Harness already exists: `run-build.py --skip-larry` runs the fix loop over an existing tree
without a write phase. Seed each run from a captured Tier A run directory.

    CODER_BACKEND=claude, --skip-larry
    corpus      captured runs/ trees from midladder2, best-state on disk
    n           the pre-declared near-green set below, one Claude attempt each

Corpus, best-achieved error score ≤3, **with stratum labelled** — selected on final score,
which the masking finding above shows is a weak proxy for difficulty:

| run | best | stratum |
|---|---|---|
| control r1 | 1 | other (AL0185 Isolated Storage missing) |
| control r4 | 1 | namespace (+AL0124) |
| challenger r2 | 1 | namespace |
| challenger r5 | 1 | namespace |
| challenger r6 | 1 | namespace (2×AL0247) |
| challenger r8 | 1 | other (AL0134 'Object' not a valid type) |
| challenger r7 | 2 | other |
| challenger r1 | 3 | namespace |

**Scored:** the non-namespace states only. Namespace states are reported separately and carry
no threshold, per the finding above.

**Contamination note, recorded now:** four of these eight trees come from the challenger arm,
so their near-green state was reached partly by Kimi rounds, not by Qwen alone. Only
`control r1` and `control r4` are pure-Qwen states. Any claim of the form "Claude closes what
**Qwen** could not" is limited to those two. This is a corpus limitation of reusing Tier A
runs and is the second argument for option (a) above.

**Outcome:** closes / does not close, per state. No pooling with Part 1.

## Egress — AUTHORISED 2026-08-23, scoped

`EGRESS_POLICY=enterprise-anon`, **for Tier B only**, Anthropic access for this registered
experiment, no widening beyond what this pre-registration requires. Per-run billed cost.

Asserted by `tierb_preflight.py` before any call, in the same spirit as the arm-isolation
preflight — state the configuration positively rather than inferring it from an absent
override. It checks the effective policy (noting that `<root>/.anon/config.yml` OUTRANKS the
env var), that Anthropic is denied at rest and reachable only through `claude_egress`'s
`anon_scrub_active()` arming, that `openrouter` and `github` remain denied, that
`CODER_BACKEND=claude` with a real binary, that no escalation variable leaked in — Claude is
the CODER here, never a rung — and that the run directory can actually produce a scrubbed
mirror.

**Scope note, recorded because "enterprise-anon" could be read as more than it is.** The anon
hook scrubs *tracked files* into the mirror. The **prompt is passed through unscrubbed**:
`run_workspace(repo, prompt, coder_fn)` hands `prompt` to the coder verbatim, and
`run-build.py` inlines the full handover text into it (`read_handover()` reads the real root,
not the mirror). For this fixture the handover is the experiment input and is the user's own
synthetic TSG material, so this is within the authorisation — but the scrub boundary is
files, not prompts, and any future use of this path on customer material must account for it.

## Decision branches, declared in advance

**Claude closes (either part):** doclink is knowledge-bound; escalation architecture is
potentially valid; Kimi was the wrong rung. Next work is cost/routing design — when does
Claude earn escalation, and does the compound trigger in `project_capability_trigger` predict
those runs? (That trigger is currently frozen at shadow-logging.)

**Claude fails from the same states:** the blocker is not established as a model-capability
boundary. Revisit fixture/API contract and repair-state handling. Do not shop for models.

**Split result (Part 1 passes, Part 2 fails):** end-to-end capability exists but does not
transfer to takeover — the interesting case, and an argument that a stalled tree carries
damage a repair rung cannot undo. Would motivate write-shape work over routing work.

## Instrumentation this registration depends on

`final_diagnostics` / `final_diag_source` / `objtypes_failed_final` (`run-build.py`,
validated 2026-08-23 on two failing doclink runs). Every claim about a residual class in
this document had to be recovered by grepping compiler logs; from now on the residual is a
queryable field. Note when reading it: `final_diagnostics` describes the **best** round, and
the `Unmask` path can adopt a higher-error state as best, so it may legitimately exceed
`first_pass_diagnostics`. That is the true residual, not a regression in the metric.

## Excluded from outcome counts

Tier A's voided `ladderdoc` block. The Tier A `midladder2` rows themselves (they are the
source of the corpus, not comparison data). Any run whose arm assertion VOIDs.

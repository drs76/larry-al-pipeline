# PHASE 2 — doclink remeasured on the patched pipeline

Suite `doclinkclean`, 2026-08-23. 10 runs, local-only, 0 VOID, ~55 min.
Fixture unchanged: `fixture_commit 422c749`, handover `e82168cb3857`, provenance `tracked`.
Model unchanged: `qwen3-coder:30b`. Escalation off on every run (banner-asserted).

Delta from Tier A, and only this: the `extends`/`implements` gap in
`add_missing_using_directives` closed (`a6ce8f4`), and `final_diagnostics` persisted
(`4c78548`). The AL0789/no-namespace warning noise was deliberately left in place so this
remeasurement carries one intervention, not two.

**Purpose was not to improve doclink. It was to see what doclink is once a known masking
defect is gone.** Pass rate is 0/10, and that is not the finding.

## Q1 — did AL0247 disappear? Yes, 0/10

    runs with AL0247 in the final round:  0 / 10   (Tier A: 5 / 20)

    namespace/using contingency, after the fix
      ns=1 using=1   6 runs   no AL0247
      ns=0 using=1   4 runs   no AL0247
      ns=1 using=0   0 runs   ← the failing combination no longer survives

The auto-fix now converts every `ns=1 using=0` file before compile. End-to-end confirmed.

## Q2 — the unmasked residual

From `final_diagnostics` (sarif, severity-filtered, category-bucketed) — first use of the
field on a full population.

    per-run residual errors   [2, 2, 3, 3, 3, 4, 5, 7, 8, 9]   median 4
    pooled categories         type-mismatch 15, other 13, syntax 11,
                              missing-method-event 5, missing-symbols 2

    for contrast, first pass  syntax 176, other 112, type-mismatch 9,
                              missing-symbols 7, missing-method-event 5

The residual is no longer a single masked error. It is a small, honest, mostly type/contract
set. Note the shape change between first pass and final: syntax collapses 176 → 11, while
type-mismatch *grows* 9 → 15. Repair fixes shape and then meets the contract wall.

## Q3 — Unmask frequency: 5/10 (Tier A 9/20)

Rate essentially unchanged, so closing the namespace gap did not remove masking generally —
it removed one specific masking layer.

    challenger/r1  [3,3,2,2,7,5,5,4,4,4]            → 4    unmask 1
    challenger/r2  [91,91,89,89,51,51,51,9,9,16]    → 9    unmask 0
    challenger/r3  [8,8,2,2,1,1,6,4,4,2,2]          → 2    unmask 1
    challenger/r4  [105,105,65,65,5,5,3,3,3,3]      → 3    unmask 0
    challenger/r5  [6,6,8,8,3,3,3,3]                → 3    unmask 1
    control/r1     [1,1,7,8,7,58,8,8]               → 8    unmask 2
    control/r2     [9,9,10,7,7,6,6,5,5,6]           → 5    unmask 0
    control/r3     [78,78,13,13,14,4,4,4,2,2]       → 2    unmask 0
    control/r4     [1,1,14,13,13,12,12,8,8,7,7]     → 7    unmask 1
    control/r5     [7,7,6,6,6,4,4,3,3,3]            → 3    unmask 0

## Q4 — is there a dominant deterministic signature? **YES. Do not freeze this population.**

The residual splits into two populations, not one:

**Population A — 7/10 runs: contract/type failures.** AL0133 (25 errs, 6/10 runs) led by
"Argument 2: cannot convert from 'OutStream' to 'var InStream'" ×11 and Temp Blob ×5; AL0193
Media argument types; AL0173 `not` on `"ABS Operation Response"`; AL0132 missing members;
AL0118 invented names. This is the broad ABS/Temp Blob/Media contract class — the boundary
Tier B exists to probe.

**Population B — 3/10 runs: a malformed `EventSubscriber` attribute.** The model writes the
event name as a bare identifier instead of a string literal:

    written   [EventSubscriber(ObjectType::Table, Database::"Document Attachment", OnAfterInsertEvent, , false, false)]
    correct   [EventSubscriber(ObjectType::Table, Database::"Document Attachment", 'OnAfterInsertEvent', '', false, false)]

**14 of the 16 AL0114 errors sit on an EventSubscriber attribute line.** The rest — AL0104
"'}' expected" ×9, AL0198, AL0219 — are parse cascade from the same break. These three runs
are exactly the three with catastrophic first passes (91, 105, 78 errors): one malformed
attribute breaks parsing of the whole codeunit and inflates the error count by an order of
magnitude.

Not a spec defect. `larry-handover.prompt.md:221` shows the correct quoted form.

**And the pipeline has a matching blind spot, the same class as the one just fixed.**
`event_verify._SUB_RE` (`event_verify.py:41`) requires a quoted event name:

    r"'(?P<event>[^']*)'\s*"

A bare identifier does not match, so `if not m: continue` skips the attribute in silence.
The pre-compile subscriber verifier only inspects subscribers that are already well-formed —
precisely how `_OBJREF_RE` only inspected object references that were already declarations.

Per the Phase 3 gate, this is an audit hit: **fix or explicitly accept before Tier B.**
Two options, and they differ in risk:

    (a) DETECT — have event_verify flag a malformed attribute as a finding, so the fix loop
        gets one clear message instead of a 90-error parse cascade. Low risk.
    (b) REPAIR — quote the bare identifier automatically, as the using-directive fix does.
        Higher risk: it must first confirm the identifier is a real event on the target
        object, which event_verify already has the symbol machinery to do.

## Q5 — unexpected terminal passes: none. 0/10

The masking layer was never the whole remaining blocker on this fixture. Consistent with the
`challenger/r2` trace from Tier A, where clearing the last error revealed the ABS contract
set underneath.

## Status

**Population NOT frozen.** Q4 returned a deterministic signature affecting 3/10 runs, and
freezing now would hand Tier B a corpus in which 30% of the residual is a syntax cascade
Claude would simply repair — measuring transcription, not the ABS boundary.

Recommended: close the `event_verify` gap, remeasure 10, re-run this checklist. If Q4 then
returns no dominant signature and the profile is Population A alone, freeze and proceed to
Tier B.

Observation, not a controlled comparison — the pipeline changed between them: Tier A control
best-error median was 5.5, Phase 2 is 4.0. Both 0/10 pass.

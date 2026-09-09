# FROZEN — cleaned doclink population, n=20

Blocks `doclinkclean2` + `doclinkclean3`, 2026-08-23. Local-only, 0 VOID, 0/20 passes.
Pipeline frozen at `b0c329f`; tree verified clean at launch of the confirmation block.
Fixture `tsg-document-link-2-az-storage`, handover `e82168cb3857`, provenance `tracked` on
all 20 rows. Same model, same settings, no change between the two blocks.

This is the Tier B baseline.

## Freeze condition — met

No new deterministic mechanical signature beyond the ABS contract boundary. The two that
existed are closed:

    AL0247 namespace/using   Tier A 5/20  →  0/20   (fixed, a6ce8f4)
    AL0114 bare-identifier   Phase 2 3/10 →  0/20   (absent, see below)

## Malformed subscribers — the detector fired once, and the answer is nuanced

**Occurrence: 1/20 runs.** Not the Phase 2 bare-identifier shape, which never recurred
(0/20; Fisher against Phase 2's 3/10 gives p = 0.03 — now unlikely to be chance alone,
though nothing in the detection-only change can explain it, so it stays recorded as
unexplained rather than fixed).

The one firing was a **new shape**: a doubled object-reference prefix.

    [EventSubscriber(ObjectType::Table, Database::Database::"Document Attachment", 'OnBeforeExportToStream', '', false, false)]

`_SUB_RE` cannot match it, so pre-`106ba54` this would have been skipped in silence. It was
classified `subscriber-unparseable` — the third class, the one that exists precisely for
shapes we cannot read but must not ignore. The catch-all earned its place.

**Detector → repair: 1/1 successful.** `doclinkclean3/control/r1`, round by round:

    round 4   model introduces Database::Database:: while fixing something else
              event check: 1 finding — "cannot read the publisher or event out of (...)"
              compiler: AL0151 at 48,41 — error score 1, new best
    round 5   NO event-check finding, NO AL0151 → the model repaired the exact defect
              but the same round surfaced 4 ABS/Temp Blob contract errors → score 4
              keep-best reverts to round 4; run ends "best achieved: 1"

The model acted correctly on the precise message the first time it received one. n=1, so
this is an existence proof, not a rate.

**But the artifact kept the defect.** The final tree still contains
`Database::Database::`, because keep-best scores by raw error count and round 4's score of 1
was *itself masked* — the unparseable attribute suppressed the rest of that object. The
repair loop preferred a masked tree over an unmasked one.

That is a repair-loop policy issue, not a residual signature, so it does not block the
freeze. It does bear on Tier B: **a takeover corpus selected by "best error score" is biased
toward masked trees.** Recorded here so Part 2 does not rediscover it.

## Pooled residual

    per-run   [1,1,1,1,1,2,3,3,3,4,4,4,5,6,6,7,7,10,15,15]   median 4
    pooled    type-mismatch 40, other 31, missing-method-event 16,
              missing-symbols 10, syntax 2

    AL0133  88 errs  14/20 runs   39x "Argument 2: cannot convert from 'OutStream' to 'var InStream'"
    AL0132  31 errs   5/20 runs   'Document Attachment' has no such member
    AL0118  28 errs   5/20 runs   invented names — LastDelimiter, AttachmentOutStream
    AL0173  19 errs   6/20 runs   `not` applied to "ABS Operation Response"
    AL0193  14 errs   7/20 runs   Media argument types
    AL0122  14 errs   5/20 runs   implicit conversion from "ABS Operation Response" / Media
    AL0151  11 errs   4/20 runs   see split below
    AL0175   9 errs   1/20 runs   `<>` applied to "ABS Operation Response"

**AL0151 is two causes, not one.** 3/20 runs invent Option-style access on non-Option types
— `Guid::"0000…"`, `Guid::Zero`, `Media::""` — which is invented API surface, the same family
as AL0118, and carries a specific non-cascading compiler message. 1/20 is the doubled-prefix
subscriber above. Neither is a validator gap.

Everything here is contract or vocabulary: stream direction, ABS Operation Response used as a
Boolean, Media/Guid conversions, invented member names. The compiler messages are specific
and correctly located. No cascades, no blind spots.

## Unmask and the masking caution

    Unmask fired                     9/20   (Phase 2 5/10, Tier A 9/20 — unchanged)
    reached <=2 errors at some point 11/20
    ENDED <=2                         6/20

Unchanged across every intervention. A low intermediate score still carries no information
about distance to green, and five of the six runs ending <=2 got there through oscillation.

## Block-to-block variance — the number Tier B must be designed against

    doclinkclean2 residual median 7   [1,1,1,5,6,7,7,10,15,15]
    doclinkclean3 residual median 3   [1,1,2,3,3,3,4,4,4,6]
    pooled                        4

Two identical 10-run blocks, same commit, same fixture, medians 7 and 3. **That is the noise
floor.** Any Tier B effect smaller than this swing is unmeasurable at n=10 per arm. Design
accordingly, and do not read a median difference of a few errors as a result.

## Pass rate — before/after context only

    Tier A control   0/10
    Phase 2          0/10
    Phase 3B         0/10
    confirmation     0/10

The pipeline changed between these, so this is a sequence of observations, not a controlled
effect estimate. Qwen has never compiled this fixture: 0 passes and 0 first-pass compiles in
all 82 tracked doclink runs.

## What Tier B now measures

With both mechanical layers removed, a doclink failure is attributable to model knowledge or
model response, which is what the experiment was always meant to test. The remaining
boundary is one class: **the ABS Storage / Temp Blob / Media contract**, led by stream
direction at 39 occurrences in 14/20 runs.

Blocked on the `enterprise-anon` egress decision — `cloud-mid` does not permit Anthropic.

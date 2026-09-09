# PHASE 3B — doclink with malformed-subscriber detection live

Suite `doclinkclean2`, 2026-08-23. 10 runs, local-only, 0 VOID.
Fixture, model, handover identical to Phase 2. One commit of delta: `106ba54`, detection only.

**Headline: the EventSubscriber signature did not recur, and the detector never fired. Those
are the same sentence, and it means the signature is ABSENT, not RESOLVED.**

## Q1 — verifier firing rate: 0/10

    runs with subscriber-event-unquoted / -element-unquoted / -unparseable:  0 / 10
    "event check" printed at any fix round, any run:                         0 / 10

Not because the detector is dead. Verified live, and verified through the production call
path rather than by unit test alone:

    _symbol_index() on a real run tree     8800 entries  (so run-build's `if _idx:` gate opens)
    event_verify.verify() on that tree     0 findings    (the tree is genuinely clean)
    same tree, one attribute un-quoted     1 finding, subscriber-event-unquoted, correct line

The reason for 0/10 is simpler: **all 30 subscriber attributes written across the 10 runs
were correctly quoted.** Nothing malformed occurred at any round, so nothing could fire.

## Q2 — model response: UNANSWERABLE

No findings were issued, so there is no repair behaviour to measure. The question the
detection-not-repair design was built to answer remains open.

## Q3 — the catastrophic syntax population

    AL0114 runs           Phase 2  3/10   →  Phase 3B  0/10
    syntax category       Phase 2   11    →  Phase 3B   1

It disappeared. **The fix cannot be the cause.** `106ba54` is detection only, it never fired,
and nothing in it can change what the model writes. This is run-to-run variance:

    Fisher exact, 3/10 vs 0/10:  p = 0.21

Ten runs cannot distinguish "a ~30% signature stopped occurring" from "a ~30% signature
happened not to occur". Declaring it resolved on this evidence would be exactly the
inference this project has spent the session learning not to make.

## Q4 — final residual: broad, and no new mechanical signature

    per-run residual   [1, 1, 1, 5, 6, 7, 7, 10, 15, 15]   median 7   (Phase 2 median 4)
    pooled             type-mismatch 26, other 18, missing-method-event 13,
                       missing-symbols 10, syntax 1

    AL0133  55 errs  7/10 runs   27x "Argument 2: cannot convert from 'OutStream' to 'var InStream'"
    AL0118  28 errs  5/10 runs   invented names — LastDelimiter, AttachmentOutStream
    AL0132  25 errs  4/10 runs   'Document Attachment' has no such member
    AL0122  12 errs  4/10 runs   implicit conversion from "ABS Operation Response" / Media
    AL0193   9 errs  4/10 runs   Media argument types
    AL0173   9 errs  3/10 runs   `not` applied to "ABS Operation Response"
    AL0175   9 errs  1/10 runs   `<>` applied to "ABS Operation Response"

Every one of these is the ABS / stream-direction / Media contract class. No pipeline blind
spot behind them: unlike AL0247 and AL0114, the compiler's message here is specific,
correctly located, and does not cascade. The stream-direction error (27 occurrences) is
recurrent but it is a contract misunderstanding, not a validator gap.

**So: no new dominant deterministic signature.** That is the freeze condition — with the
caveat in Q3.

## Q5 — Unmask: 5/10, unchanged (Phase 2 5/10, Tier A 9/20)

    challenger/r1  [2,2,12,8,8,1,1,7,8]                  ->  7   unmask 2
    challenger/r2  [2,2,18,19,12,12,11,11,10,10]         -> 10   unmask 1
    challenger/r3  [12,12,8,8,5,5,5,3,3,1,1]             ->  1   unmask 0
    challenger/r4  [10,10,10,4,4,1,1,1,1]                ->  1   unmask 0
    challenger/r5  [31,31,30,30,19,19,11,11,6,6,5]       ->  5   unmask 0
    control/r1     [16,16,2,2,15,1,1,1,14]               ->  1   unmask 1
    control/r2     [11,11,7,7,1,1,16,16,15,15]           -> 15   unmask 1
    control/r3     [17,17,16,16,18,16,16,15,15]          -> 15   unmask 0
    control/r4     [1,1,11,7,7,10,7,7]                   ->  7   unmask 1
    control/r5     [16,16,14,14,9,9,15,6,6,10]           ->  6   unmask 0

The oscillation is the point: runs reach 1 error and bounce to 15. Consistent with the
masking finding — a low intermediate score carries no information about distance to green.

## Q6 — terminal passes: 0/10

## Variance warning, which bears on the freeze

Residual median moved 4 → 7 between Phase 2 and Phase 3B with **no pipeline change capable
of causing it**. Same fixture, same model, same settings. That is the noise floor of a
10-run block on this fixture, and it is large relative to any effect Tier B is likely to
show. Any Tier B comparison drawn against a 10-run local baseline will be underpowered by
this alone.

## Recommendation — do not freeze yet; one more free block

Two open items, both closed by the same action:

1. The subscriber signature is absent-not-resolved (p = 0.21). A second block takes the
   observation to n=20; if it recurs, the detector finally gets exercised and Q2 becomes
   answerable — which is the more valuable outcome.
2. The residual estimate is unstable (median 4 vs 7). n=20 gives Tier B a baseline whose
   spread is known rather than assumed.

The block is local-only and costs nothing but ~55 minutes. Freezing on n=10 with a 4→7
median swing would hand Tier B a baseline that cannot support the comparison.

If the second block shows no malformed subscribers and the same broad ABS profile, freeze
the pooled n=20 population and proceed to Tier B, recording explicitly that the subscriber
signature was never observed again and the detector remains unexercised in production.

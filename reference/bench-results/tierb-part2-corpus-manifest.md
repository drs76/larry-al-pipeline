# TIER B PART 2 — takeover corpus manifest (FROZEN)

Frozen 2026-08-23, before any billed takeover. Source: the frozen doclink corpus, n=20
(`doclinkclean2` + `doclinkclean3`), pipeline `b0c329f`, fixture `422c749`, handover
`e82168cb3857`. Registration: `exp-tierb-claude-preregistration.md`.

**No selection, harness or scoring change is permitted once the first billed takeover starts.**

## How each state was characterised — and why not from the logs

Two methods were tried and discarded before this manifest was built, both recorded because
either would have produced a wrong corpus:

1. **Last-round errors.** The takeover state is the tree on disk, which is the BEST round,
   not the last. On `b2_control/r1` that is the difference between 15 errors and 1.
2. **Best round located by the `★ new best` marker.** The `Unmask` path reassigns best
   WITHOUT printing that marker, so runs with an Unmask event resolve to the wrong block —
   `b2_challenger/r1` came out as 1 code against a recorded residual of 7.

The manifest therefore **compiles every on-disk tree**. That is literally the state Part 2
hands Claude, so it is authoritative by construction. All 20 compiled residuals match the
recorded `final_diagnostics` exactly, so the two independent sources agree.

## Selection rule applied (from the registration, binding)

A candidate qualifies only if its residual is **ABS-contract by composition**. Minimum error
count is explicitly NOT a selection criterion. Parse-class residuals are excluded as masked
by construction: an unresolved or unparseable construct suppresses every downstream error in
its object, so the state's true distance is unknown.

## Rejected — and note these are the LOWEST-scoring states available

Four of the five smallest residuals in the corpus are rejected. If the corpus had been
chosen by minimum error count, all four would have been selected, and Part 2 would have
measured syntax transcription rather than the ABS boundary.

| candidate | residual | why rejected |
|---|---|---|
| `b2_challenger/r4` | 1 — `AL0104` "Syntax error, 'of' expected" | parse-class; masks its object |
| `b3_challenger/r2` | 1 — `AL0107` "Syntax error, identifier expected" | parse-class; masks its object |
| `b3_control/r1` | 1 — `AL0151` on `Database::Database::` | the malformed-attribute run; masked by construction, and the one state where the subscriber detector fired |
| `b2_control/r1` | 1 — `AL0185` "Codeunit 'Dialog' is missing" | unresolved symbol, not ABS-contract; an unresolved codeunit type suppresses member errors on that variable |

## Not selected, held in reserve — no defect, simply outside the pre-declared n

`b2_challenger/r1` (7), `b2_challenger/r2` (10), `b2_challenger/r5` (5), `b2_control/r3` (15),
`b2_control/r5` (6), `b3_challenger/r3` (4), `b3_control/r3` (3), `b3_control/r5` (4).
These qualify on composition. Using them later requires a new pre-registration; they are not
a pool to draw from if the selected eight give an unwelcome answer.

## SELECTED — n=8, pre-declared, one Claude takeover attempt each

Purposeful coverage across residual difficulty (1 → 15) and across the dominant ABS-contract
error modes (`AL0133`, `AL0132`, `AL0173`, `AL0151`, `AL0122`, `AL0193`), so closure can be
read against difficulty rather than confounded with it.

Deliberately NOT described as stratified: this registration defines no strata and no
by-stratum analysis, and calling it stratification would imply an analysis plan that does not
exist. The eight are analysed as one fixed set, per state and pooled.

### Tree hashes — the driver asserts these before invoking Claude

The selected tree IS the experimental unit. Each hash is the sha256 of
`find . -name '*.al' | sort | xargs sha256sum` run from INSIDE `src/`, so it covers file
contents and relative paths only. A mismatch aborts before billing.

An earlier revision hashed from outside `src/`, which folded the absolute directory path
into the digest — the hash could never survive the copy it exists to verify. The driver's
own assertion caught it on the first fake-coder run, before any billed call.

    doclinkclean2_challenger__r3  ab9a86b5d580790acaa20001e44f2c010fdaf69c4ed4fabb6a296a24713d2fb1
    doclinkclean3_challenger__r5  9b6f811b480bb4533c9477556f311c5f1a9d8832ac7446c2673a5d1b07867525
    doclinkclean3_challenger__r1  342891fb4545c34287288794171786322cd653912ad7ce7cf524b97b080883d2
    doclinkclean3_control__r2     87c8d7338c514d467fbd03d1fbc043914f7412eadf333f13ac8fbfaafb7d4fd5
    doclinkclean3_control__r4     01afa6f1f14a758cb75c544ef7f811f7b2f67c47fe0146f605e49195f07a3b36
    doclinkclean3_challenger__r4  dc26e54790ee5377a65cc00ddf67a7fa45c6554e68857bb699de3ae6a1a0c2ca
    doclinkclean2_control__r4     3f8f40b33738c1f074722fd675c369b27719b4a403cd813fdcc0c01e3595f643
    doclinkclean2_control__r2     151490174e7fa4f55109ae4afef493072eab8cb3bafaa51cf655ad6c80265b11

All eight source trees are write-protected; each run works on a fresh copy.

### `doclinkclean2_challenger__r3`  — residual 1

    source run        qwen3-coder_30b__doclink__doclinkclean2_challenger__r3
    block / arm       block 2_challenger
    trajectory        [12, 12, 8, 8, 5, 5, 5, 3, 3, 1, 1]
    Unmask events     0
    final_diagnostics {'type-mismatch': 1}
    compiled residual 1 error(s)  {'AL0133': 1}
      AL0133: Argument 2: cannot convert from 'OutStream' to 'var InStream'

### `doclinkclean3_challenger__r5`  — residual 2

    source run        qwen3-coder_30b__doclink__doclinkclean3_challenger__r5
    block / arm       block 3_challenger
    trajectory        [9, 9, 6, 6, 4, 4, 5, 4, 2, 2]
    Unmask events     0
    final_diagnostics {'other': 2}
    compiled residual 2 error(s)  {'AL0151': 1, 'AL0122': 1}
      AL0122: Cannot implicitly convert type 'None' to 'Boolean'. Use an explicit co
      AL0151: Expression must be an Option type. Use '::' to access option members (

### `doclinkclean3_challenger__r1`  — residual 3

    source run        qwen3-coder_30b__doclink__doclinkclean3_challenger__r1
    block / arm       block 3_challenger
    trajectory        [11, 11, 8, 8, 7, 7, 4, 4, 4, 3, 3]
    Unmask events     0
    final_diagnostics {'other': 3}
    compiled residual 3 error(s)  {'AL0151': 2, 'AL0173': 1}
      AL0151: Expression must be an Option type. Use '::' to access option members (
      AL0173: Operator 'not' cannot be applied to an operand of type 'Codeunit Syste

### `doclinkclean3_control__r2`  — residual 3

    source run        qwen3-coder_30b__doclink__doclinkclean3_control__r2
    block / arm       block 3_control
    trajectory        [7, 7, 1, 1, 11, 8, 8, 6, 6, 3, 3]
    Unmask events     1
    final_diagnostics {'type-mismatch': 3}
    compiled residual 3 error(s)  {'AL0133': 3}
      AL0133: Argument 2: cannot convert from 'OutStream' to 'var InStream'
      AL0133: Argument 4: cannot convert from 'Dictionary of [Text, Text]' to 'Codeu

### `doclinkclean3_control__r4`  — residual 4

    source run        qwen3-coder_30b__doclink__doclinkclean3_control__r4
    block / arm       block 3_control
    trajectory        [6, 6, 11, 7, 7, 7, 6, 6, 4, 4]
    Unmask events     1
    final_diagnostics {'missing-method-event': 3, 'type-mismatch': 1}
    compiled residual 4 error(s)  {'AL0133': 1, 'AL0132': 3}
      AL0132: 'Media' does not contain a definition for 'RecordID'
      AL0132: 'Media' does not contain a definition for 'Table ID'
      AL0133: Argument 1: cannot convert from 'Integer' to 'Text'

### `doclinkclean3_challenger__r4`  — residual 6

    source run        qwen3-coder_30b__doclink__doclinkclean3_challenger__r4
    block / arm       block 3_challenger
    trajectory        [21, 21, 14, 14, 15, 10, 10, 7, 7, 6, 6]
    Unmask events     0
    final_diagnostics {'other': 1, 'type-mismatch': 5}
    compiled residual 6 error(s)  {'AL0133': 5, 'AL0173': 1}
      AL0133: Argument 1: cannot convert from 'SecretText' to 'Text'
      AL0133: Argument 2: cannot convert from 'Codeunit System.Utilities."Temp Blob"
      AL0133: Argument 4: cannot convert from 'Option' to 'Codeunit System.Azure.Sto
      AL0173: Operator 'not' cannot be applied to an operand of type 'Codeunit Syste

### `doclinkclean2_control__r4`  — residual 7

    source run        qwen3-coder_30b__doclink__doclinkclean2_control__r4
    block / arm       block 2_control
    trajectory        [1, 1, 11, 7, 7, 10, 7, 7]
    Unmask events     1
    final_diagnostics {'type-mismatch': 6, 'missing-method-event': 1}
    compiled residual 7 error(s)  {'AL0133': 6, 'AL0132': 1}
      AL0132: 'Codeunit System.Utilities."Temp Blob"' does not contain a definition 
      AL0133: Argument 2: cannot convert from 'OutStream' to 'var InStream'
      AL0133: Argument 3: cannot convert from 'Dictionary of [Text, Text]' to 'Text'
      AL0133: Argument 4: cannot convert from 'Dictionary of [Text, Text]' to 'Codeu

### `doclinkclean2_control__r2`  — residual 15

    source run        qwen3-coder_30b__doclink__doclinkclean2_control__r2
    block / arm       block 2_control
    trajectory        [11, 11, 7, 7, 1, 1, 16, 16, 15, 15]
    Unmask events     1
    final_diagnostics {'other': 2, 'missing-method-event': 10, 'type-mismatch': 3}
    compiled residual 15 error(s)  {'AL0133': 3, 'AL0173': 1, 'AL0132': 10, 'AL0122': 1}
      AL0122: Cannot implicitly convert type 'Text' to 'Media'. Use an explicit conv
      AL0132: 'Media' does not contain a definition for 'Clear'
      AL0132: 'Record "Document Attachment"' does not contain a definition for 'GetT
      AL0132: 'Record "Document Attachment"' does not contain a definition for 'Tabl
      AL0133: Argument 1: cannot convert from 'SecretText' to 'Joker'
      AL0133: Argument 1: cannot convert from 'SecretText' to 'Text'
      AL0133: Argument 4: cannot convert from 'Text' to 'Codeunit System.Azure.Stora
      AL0173: Operator 'not' cannot be applied to an operand of type 'Codeunit Syste

## Why these, over lower-score alternatives

Every rejected state above scores 1 — lower than six of the eight selected. They were passed
over because their composition is parse-class or an unresolved symbol, both of which mask.
The selected set instead spans the difficulty range with honest ABS-contract residuals, which
is the only way a closure result can be attributed to the contract rather than to how little
was left.

## Primary outcome

**Terminal closure from an honest stalled Qwen state: does Claude compile it, per state?**

Reported separately, and never combined into the primary number: rounds taken, residual
errors changed, duration. Part 1 is not pooled with this — a full Claude run shares nothing
with a Qwen run except the handover.

## Implementation prerequisites — NOT evidence for the hypothesis

The two enterprise-anon harness corrections (`38802b6`) were required to make the registered
experiment executable and carry no weight for the hypothesis. Their value is that they
prevented two plausible FALSE NEGATIVES: an empty first-round workspace, and a code-blind
repair workspace on every round after the first. Without them Part 1 would have returned 0/5
and read as "Claude cannot do it either".

## Part 1 record

Immutable: `reference-part1-manifest.txt`, trees write-protected, sha256 per tree.

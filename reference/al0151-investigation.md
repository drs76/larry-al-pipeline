# AL0151 — what actually causes it in the doclink corpus

> **Closed 2026-09-01, compiler-verified.** AL0151 is not an enum problem. In 46 recoverable
> sites it is the coder applying option-member syntax (`Type::Member`) to a type that has no
> option members — overwhelmingly **Media**, then **Guid**.

🧭 **The one idea:** the model's own comment named the wrong cause, and the first
investigation followed that comment instead of the diagnostic. Probing what a model *says*
it was working around tests the model's explanation, not the compiler's complaint.

## The diagnostic

    error AL0151: Expression must be an Option type. Use '::' to access option members
                  (e.g., MyOption::Value).

## Method

Historical run logs carry the diagnostic with a file/line/column, and suite `runs/<name>/src/`
trees persist. Where a run *ended* with AL0151 unresolved, the offending line survives in that
run's final source. Diagnostics were taken from the FINAL REPORT section only, so the line
read is the line that was still broken when the run stopped.

    resolved sites            46
    unresolvable (dir gone)    3

## Result — the receiver, not the member

| receiver used with `::` | sites |
|---|---:|
| `Media` | 39 |
| `Guid` | 6 |
| `ObjectType` | 1 |

Dominant expressions, all attempts to CLEAR a Media field or test a Guid:

    19   DocumentAttachment."Document Reference ID" := Media::"";
     8   Rec."Document Reference ID" := Media::"";
     3   ... := Media::Empty;
     3   ... := Media::None;
     2   ... := Media::NoMedia;
     1   ... := Media::new();
     2   if ....MediaId() = Guid::"00000000-0000-0000-0000-000000000000" then

The member name varies freely (`""`, `Empty`, `None`, `NoMedia`, `new()`) because none of them
exist. The constant is the receiver: a non-option type on the left of `::`.

## Compiler probe — cause and fix, both directions

Against the doclink `.alpackages` (BC28 / runtime 17.0), snippet probes:

| construct | outcome |
|---|---|
| `DocAttach."Document Reference ID" := Media::"";` | **rejected — AL0151** |
| `DocAttach."Document Reference ID" := Media::Empty;` | **rejected — AL0151** |
| `if DocAttach."Document Reference ID".MediaId() = Guid::Zero then` | **rejected — AL0151** |
| `Clear(DocAttach."Document Reference ID");` | verified |
| `if IsNullGuid(DocAttach."Document Reference ID".MediaId()) then` | verified |

So: **clear a Media field with `Clear(...)`; test a Guid with `IsNullGuid(...)`.** There is no
assignable empty-Media literal and no empty-Guid literal.

## Relationship to the existing hints

This is the same underlying confusion already covered for a *different* diagnostic. `AL0175`
fires when the coder tests Media/Guid emptiness with `= 0`; `AL0107`/`AL0224` fire on
`GUID::{}`. AL0151 is the third face of it — reaching for `::` instead. The existing
`known_fix_hints` entries for AL0175 (Media `.HasValue`, Guid `IsNullGuid`) and the
`al-errors.yml` AL0107 entry already teach the correct idioms; nothing teaches them when the
diagnostic that arrives is AL0151.

## The earlier wrong turn, kept deliberately

The first attempt (same day) failed to reproduce AL0151 and the investigation was closed as
"cause unknown, no hint written". That was the right call on the evidence then, but the
evidence was gathered wrongly:

- The trigger was found in a run where the coder wrote
  `// Workaround for AL0151 - explicitly define enum value` and invented a mid-body
  `var ApiVersionEnum: Enum "Storage Service API Version";`.
- Reading that comment, three `CreateSharedKey` overload hypotheses were probed — two-arg with
  `Enum::`, without `Enum::`, and one-arg. **All three compile clean.** They were never
  candidates; the enum call was fine.
- The model's comment was an explanation it invented for a diagnostic it had not understood.
  Anchoring on it cost the investigation. The diagnostic's own coordinates — which were
  available the whole time — identified the construct in one pass.

That specific run's source remains unrecoverable (`snapshot_src()` holds snapshots in memory,
and the final best-restore overwrote the tree), so *that* site is still unclassified. The
population result does not depend on it.

## Follow-ups this enables

1. An `al-errors.yml` entry for AL0151 — none exists today.
2. A `known_fix_hints` entry keyed on AL0151, naming the receiver type from the source line,
   in the same guarded style as the inline-var hint: read the blamed line, confirm a `::` on a
   non-option receiver, and only then speak.

## Status

Everything above `## Status` is the evidence as it stood at `5927194`, **before** either
follow-up existed. That is the boundary: it records what was known without the fix. Both
follow-ups have since landed, as two independently testable commits:

- `84e2247` — the `al-errors.yml` entry. Data only; changes no repair behaviour.
- `63eb6ae` — the guarded `known_fix_hints` entry and five tests.

**The claim, stated narrowly.** In the seeded AL0151 reproduction, the diagnostic-gated hint
fired on the targeted `Media::""` construct and the model applied the probe-verified
`Clear(...)` remediation, eliminating AL0151 in one repair round. This establishes mechanism
evidence for the implemented hint **in that reproduction**. It does not establish
population-level resolution effectiveness.

The 39/6/1 distribution above is targeting and motivation evidence. It does **not** license a
claim that the hint is generally effective because `Media::` dominates the corpus — one
seeded success is a mechanism probe, nothing more.

No natural A/B was run, deliberately: an occurrence endpoint cannot measure an intervention
that acts only after occurrence (`feedback_endpoint_mechanism_mismatch`).

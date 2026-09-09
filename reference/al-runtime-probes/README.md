# AL runtime probes

Test codeunits that assert **runtime** claims made by `AL-REFERENCE.md` / `AL-SYNTAX.md`
against a live BC instance.

Run with [`pipeline/runtime_probe.sh`](../../pipeline/runtime_probe.sh):

```bash
./pipeline/runtime_probe.sh -name bc2 -version 27
```

It fetches symbols from the environment, compiles, publishes, runs `bcl test`, and
uninstalls the extension again (`-keep` to leave it published).

## Why this exists

The AL ruleset had two guards, and both stop at the build:

| Guard | Proves |
|---|---|
| `validate_al_syntax.py` | the ✓ patterns **compile** |
| `probe_al_rules.sh` | the ✗ patterns **fail**, with the diagnostic codes we cite |
| **this** | what the code does when it **runs** |

Runtime claims are the ones that rot. Nothing in the build ever contradicts them, so a
wrong one survives indefinitely — which is precisely how `AL-SYNTAX` rule 7 carried a
false "SaaS hard requirement (PTE/CodeCop)" for months inside a file titled
*compiler-verified*.

## Claims covered

19 probes, all green on bc2 (BC 27.0.52102.0).

| Test | Defends |
|---|---|
| `TypedJsonGetterThrowsOnMissingKey` | typed JSON getters throw on a missing key |
| `JsonTypedGetterReturnsPresentValue` | a present key round-trips |
| `JsonGetReturnsFalseForMissingKey` | `Get(Key, var Token)` is the safe probe — returns `false` |
| `JsonTwoArgGetterIsSafeOnMissingKey` | the 2-arg form yields `''` rather than throwing |
| `InterfaceAsErrorsOnInvalidCast` | interface `as` errors on an invalid cast |
| `InterfaceIsGuardsTheCast` | `is` returns false instead of throwing |
| `GuardedCastSucceeds` | a guarded cast yields a usable interface value |
| `ExitReturnsTheValue` | `exit(value)` actually returns it (AL has no `return`) |
| `TryFunctionReturnsFalseAndSwallowsTheError` | `[TryFunction]` declares no return type yet returns `false` on error |
| `TryFunctionReturnsTrueOnSuccess` | …and `true` on success |
| `InsertWithRunTriggerFiresOnInsert` | `OnInsert` is the trigger name, and `Insert(true)` runs it |
| `InsertWithoutRunTriggerSkipsOnInsert` | `Insert(false)` does **not** run it |
| `ModifyWithRunTriggerFiresOnModify` | same contract for `OnModify` |
| `TableEventSubscriberFires` | auto-event subscriber params bind BY NAME (the AL0282 rule) at runtime |
| `IsEmptyTracksTheTable` | `IsEmpty()` is honest — what makes the `DeleteAll` guard meaningful |
| `FindSetIteratesEveryRow` | `FindSet` + `Next` visits every row |
| `TernaryEvaluatesTheChosenBranch` | the ternary exists and picks the right branch |
| `ContinueSkipsTheIteration` | `continue` skips exactly one iteration |
| `ResourceDefaultEncodingDiffersFromUtf8` | resource text really does default to MS-DOS, not UTF-8 |
| `ResourceReadAsUtf8RoundTrips` | passing `TextEncoding::UTF8` recovers the original |

Compile-time claims (`:=` vs `=`, `begin end`, `NoImplicitWith`, promoted actions,
`DataClassification` values) belong to `probe_al_rules.sh`, not here. Tooltips and
anything else the **client** renders cannot be reached from either.

## Three doc/packaging errors this harness caught while being built

**1. There is no `GetText(Key, DefaultValue)` overload.** The gotcha table advised
`JObj.GetText('k', DefaultValue)` as the safe way to probe a missing key. The 2-arg
form's second argument is a **Boolean**, not a fallback value:

```
error AL0133: Argument 2: cannot convert from 'Text' to 'Boolean'
```

The safe probes are `Get(Key, var JsonToken): Boolean` and the 2-arg
`GetText(Key, true)`, which yields `''`. The harness settled that second point the hard
way: the test originally asserted the 2-arg form *threw*, and the runtime disagreed —
which is the harness doing its job on its own author.

**2. `is` / `as` do not work on a Codeunit variable.** The idiom reads
`Provider is IFoo`, which invites writing it against a codeunit variable. That is
`AL0851: The type 'Codeunit' doesn't support casting`. The source has to be an
**interface-typed** value:

```al
var
    ImplA: Codeunit "Probe Impl A";
    Face: Interface "Probe IFace";
begin
    Face := ImplA;                       // assign, no cast
    if Face is "Probe IOther" then ...   // cast applies to the INTERFACE value
```

**3. Embedded resources need a `resourceFolders` root in app.json**, and the name used
in `GetResourceAsText` is relative to that root — `'encoding.txt'`, not `'res/encoding.txt'`.
Without the declaration the file is silently absent from the `.app` and the call fails at
runtime with *"A resource matching … could not be found"*. AL-REFERENCE §13 says to declare
a root folder but shows only rooted-looking paths in its examples, which is easy to misread.

All three were caught the moment a claim was written down as executable AL — which is the
argument for this harness in one line.

## Adding a probe

1. Add a `[Test]` procedure naming the claim it defends in a comment.
2. Assert with the local `AssertEqual` / `AssertTrue` / `AssertFalse` helpers — the
   extension deliberately has **no dependency** on Microsoft's test libraries, so it
   compiles against plain platform symbols and publishes anywhere.
3. Run the harness. If a probe fails, **fix the doc, not the test** — the instance is
   the ground truth.

## Limits

Anything rendered by the **client** is out of reach: tooltips, captions, field
visibility. Those still need a human with a browser. The BC27 tooltip-inheritance
question was settled that way, not here.

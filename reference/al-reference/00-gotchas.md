<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# LLM gotcha summary — READ FIRST

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## LLM Gotcha Summary — Read First

| Wrong | Right | Why |
|---|---|---|
| `x = 5` (assignment) | `x := 5` | `=` is comparison only in AL |
| `return true;` | `exit(true);` | AL has no `return` keyword |
| `{ }` for blocks | `begin end;` | AL block syntax |
| `[TryFunction] proc(): Boolean` | `[TryFunction] proc()` | return type implicit — do NOT declare |
| `BeforeInsert` trigger | table trigger = `OnInsert`; subscriber event = `OnBeforeInsertEvent` | triggers are `OnInsert/OnModify/OnDelete`; the `OnBefore…Event`/`OnAfter…Event` names are system EVENTS (no IsHandled param) — there is no `OnBeforeInsert` trigger |
| `Find('-')` | `FindSet()` | `Find('-')` is deprecated pattern |
| `DeleteAll()` without guard | `if not IsEmpty() then DeleteAll()` | avoids lock on empty table |
| `//comment` | `// comment` | one space after `//` required |
| `if X then exit;` (one line) | split across two lines | one statement per line rule |
| `Amount := 0;` (bare field) | `Rec.Amount := 0;` | modern apps enable `NoImplicitWith` — qualify record access (`Rec.`/`xRec.`) explicitly |
| `Promoted = true; PromotedCategory = …` on an action | `area(Promoted)` + `actionref` | legacy promoted properties are banned house-style (and don't compile under `NoPromotedActionProperties`) — see §7 |
| `JObj.GetText('k')` on a key that may be absent | `if JObj.Get('k', Tok) then …` — or the 2-arg `JObj.GetText('k', true)`, which yields `''` instead of throwing | the 1-arg typed getter **throws** on a missing key. **There is no `GetText(Key, DefaultValue)` overload** — the 2nd argument is a **Boolean**, so `GetText('k', 'fallback')` is `AL0133`. Runtime-verified (§4) |
| `Provider as IFoo` unguarded | `if Provider is IFoo then (Provider as IFoo)…` | interface `as` **errors** on an invalid cast — always guard with `is` first (§24) |
| `GetResourceAsText(name)` and trusting the text | pass the encoding: `GetResourceAsText(name, TextEncoding::UTF8)` | default resource text encoding is **MS-DOS** → wrong output otherwise (§13) |
| hand-rolling `if C then X := A else X := B` for a value | `X := C ? A : B` (ternary, 2024w2) | ternary exists; `continue` also exists to skip a loop iteration (§4) |
| repeating a `ToolTip` on every page just to be safe | declare it once on the **table field** — pages inherit it (2024w1), and mixing inline + inherited on one page is fine | runtime-verified BC 27.0.52102.0: inherited tooltips render on a mixed page (the old 2024w1 bug is fixed). `ToolTip` missing entirely = `AA0218` warning (fields AND actions); missing `ApplicationArea` = `PTE0008` **error** |
| `DataClassification` repeated on every field | declare it **once as a table property**; fields inherit, and only need their own to differ | verified BC27: table-level + bare fields is clean under CodeCop/PTECop. Per-field is legacy habit — and it multiplies a wrong value into one error per field |
| `DataClassification = EndUser` / `CompanyContent` / `PersonalData` | `DataClassification = CustomerContent` | **default to `CustomerContent`** for ordinary business data. Only 7 values exist; invented shortenings are `AL0169` (compiler-verified BC27: `CustomerContent`, `SystemMetadata`, `EndUserIdentifiableInformation`, `EndUserPseudonymousIdentifiers`, `OrganizationIdentifiableInformation`, `AccountData`, `ToBeClassified`) |

---

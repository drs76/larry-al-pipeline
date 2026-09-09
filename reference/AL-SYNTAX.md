# AL-SYNTAX — compiler-verified syntax rules

**Target floor: BC27 / runtime 16.0** (application `27.0.0.0`). Publisher-neutral; the rules are the
language grammar + code-cop requirements, not any one project's patterns.

This file fixes the **compile-break class** — the AL0xxx / AAxxxx / PTE00xx failures a model hits when
it *authors* AL from prose (using-placement, quoted paths, usercontrol scope, permission sets…). It
does **not** cover the **API surface** (real table / field / event / method names): those change every
release and must come from **symbols / RAG**, never from memory. Split the job:

| Layer | Volatile? | Source |
|---|---|---|
| Grammar + cop rules (this file) | ~never | AL-SYNTAX.md |
| Version-gated language features | slowly | this file's `since` table + the target floor |
| Object surface (names/signatures) | every release | `.alpackages` symbols, `al_downloadsymbols`, AL-REFERENCE §18 |

## How this file is kept honest
Every ✓ pattern below is lifted from a **canonical extension that compiles clean** with the code cops
(CodeCop + UICop + PerTenantExtensionCop) on BC27 / runtime 16.0:

- Gold source: `setup/reference/al-syntax-examples/` (copy-paste-correct; do not add anything that
  doesn't compile).
- Re-verify any time: `python3 setup/pipeline/validate_al_syntax.py` → must print `CLEAN ✓`.

If a rule here and the compiler ever disagree, **the compiler wins** — fix this file and the gold
example, then re-run the validator.

---

## Structure & grammar (never version-dependent)

**1. `using` goes ABOVE the object — the single most common break.**
Order: `namespace` → `using` lines → blank → object → `{`. A `using` after the opening `{` cascades
into `AL0104 '}' expected` + `AL0114` + `AL0107`.
- ✓ see `src/SYXGreetMgt.Codeunit.al` (`using System.Environment;` sits above `codeunit …`).
- ✗ `codeunit 57902 "X" { using System.Environment; … }`

**2. Object = a declaration line THEN a `{ }` body; id required (except controladdin/interface).**
Triggers first, then a codeunit-level `var` section, then procedures. Keep the `var` at object level —
don't fold it into a procedure.
- ✓ `src/SYXGreetMgt.Codeunit.al`.

**3. Lowercase keywords; `begin…end` for multi-statement blocks; `exit(value)` with a return type.**
- ✓ `procedure Greet(Name: Text): Text … begin … exit(Result); end;`

**4. String literals (paths, captions) are single-quoted.**
- ✓ `Scripts = 'src/addin/board.js';`   `Caption = 'Player Setup';`
- ✗ `Scripts = src/addin/board.js;` → `AL0219: string literal expected`.

**5. File name = object name minus spaces, then `.<Type>.al`.** CodeCop `AA0215` otherwise.
- ✓ object `"SYX Examples PTE"` → file `SYXExamplesPTE.PermissionSet.al`. Table
  `"SYX Player Setup"` → `SYXPlayerSetup.Table.al`.

**6. Every identifier a procedure uses must be declared** (a `var` block or a parameter). Models copy
snippets verbatim; an undeclared name becomes `AL0118` ×N. Write snippets self-contained.

## Tables & fields

**7. `DataClassification` goes on the TABLE, not on every field.** Declare it once as a table
property and the fields inherit it; a field only needs its own when it differs from the table's.
**Default to `CustomerContent`** — the right choice for ordinary business data.

```al
table 50100 "My Table"
{
    Caption = 'My Table';
    DataClassification = CustomerContent;   // ← fields inherit this

    fields
    {
        field(1; "Entry No."; Integer) { Caption = 'Entry No.'; }              // inherits
        field(2; "Contact Name"; Text[100])                                     // overrides
        { Caption = 'Contact Name'; DataClassification = EndUserIdentifiableInformation; }
    }
}
```

Verified on BC27 / runtime 16.0: a table declaring it with bare fields compiles clean under
CodeCop **and** PerTenantExtensionCop. Repeating it on every field is legacy habit from older
runtimes — harmless, just noise. (No cop in this toolchain — CodeCop, PTECop or AppSourceCop —
actually errors on a *missing* `DataClassification`, so treat it as a data-governance obligation
rather than a build gate.)

The value is an enum with exactly **7** members. Anything else is `AL0169: The option value 'X' is
not valid` — and if it is written per field, one wrong guess costs one error per field.
Compiler-verified on BC27 / runtime 16.0:

| Value | Use for |
|---|---|
| `CustomerContent` | **default** — ordinary business data the customer owns |
| `SystemMetadata` | technical/plumbing fields (entry no., timestamps, internal keys) |
| `EndUserIdentifiableInformation` | identifies a real person (EUII) |
| `EndUserPseudonymousIdentifiers` | pseudonymous user ids (EUPI) |
| `OrganizationIdentifiableInformation` | identifies an organisation (OII) |
| `AccountData` | billing/subscription account data |
| `ToBeClassified` | placeholder for unreviewed fields — do not ship |

✗ `EndUser`, `CompanyContent`, `PersonalData` — all plausible-looking, all rejected by the compiler
(verified: each produces `AL0169`). `EndUser` is the EUII label truncated; `CompanyContent` is the
one models reach for instead of `CustomerContent`.
- ✓ `src/SYXPlayerSetup.Table.al` — declares it per field (legacy style, still valid).

**8. `Caption` on the table and each field; a `keys` block with a clustered PK.** **House style, not
enforced** — verified BC27: omitting captions, the whole `keys` block, or `Clustered = true` produces
no diagnostic under CodeCop/UICop/PTECop. Do it anyway (captions drive translation; an explicit
clustered PK documents intent), but do not expect the compiler to catch it.
- ✓ same file.

**9. `SecretText` is NOT a valid table field type — it is a hard compile error, `AL0156`.** Not a
SaaS style preference: the compiler rejects it outright on BC27. Use `IsolatedStorage` for secrets.
- ✗ `field(2; Sec; SecretText) { … }` → `AL0156`.

## Pages

**10. `ApplicationArea` AND `ToolTip` on EVERY field and EVERY action, on every page.** Both are
required — write them every time, no exceptions.

| Missing | Diagnostic |
|---|---|
| `ApplicationArea` on a field | **`PTE0008` — error**, breaks the build (AppSourceCop equivalent: `AS0062`) |
| `ToolTip` on a field | `AA0218` — warning (VS Code shows the yellow squiggle) |
| `ToolTip` on an action | `AA0218` — warning (plus `AA0194` with no `OnAction`/`RunObject`) |

Field tooltips should **begin with "Specifies"** — house convention Microsoft enforces via
`AA0218`/`AA0219`/`AA0220`; `AA0234` (Info) nudges tooltips onto table fields too. Page
fields also want a filled `Caption` (`AA0225`/`AA0226`). See
[`16-analyzer-rules.md`](al-reference/16-analyzer-rules.md) for the full code lists.

**Two ways to satisfy the tooltip, and you must pick ONE per page.** Since 2024w1 a `ToolTip` can be
declared once on the **table field**; every page bound to that table inherits it (verified BC27:
table tooltips + bare page fields compiles clean, no `AA0218`).

**Mixing the two styles on one page is fine on BC27.** A page can give some fields an inline
`ToolTip` and let the rest inherit from the table; the inherited ones still render. Runtime-verified
2026-08-16 on BC **27.0.52102.0** — a mixed page and an all-inherited control page both showed the
table tooltip on the inherited field.

> History worth knowing if you target older builds: mixed pages were seen to drop the inherited
> tooltips around the 2024w1 introduction of table tooltips. That is fixed by BC27. On an older
> floor, keep a page to one style.

> Probing pitfall, in case you re-check this: bind a probe page to a **base-app** table (Customer,
> Item…) and you will see no `AA0218` at all — MS moved those tooltips onto the table fields in
> 2024w1, so your page silently inherits them. Test tooltip rules against your OWN tooltip-less
> table or you will "prove" the rule doesn't exist.

- ✓ `src/SYXGreetCard.Page.al` fields/actions.

**11. Hosting a ControlAddin: `usercontrol(...)` lives in `area(Content)` inside `layout { }`, and its
body holds ONLY `trigger` definitions.** Put the page's procedures at PAGE level, never inside the
usercontrol.
- ✓ `src/SYXGreetCard.Page.al` — `usercontrol(Board; "SYX Board")` with only `ControlAddInReady` /
  `ScoreChanged` triggers; `GreetMgt` codeunit + logic sit at page level.
- ✗ a `procedure` declared inside the `usercontrol { }` block.

**12. Call the add-in via `CurrPage.<controlname>.<Method>()`.**
- ✓ `CurrPage.Board.Reset();`

**13. On pages/page-extensions use the page triggers `OnInsertRecord` / `OnModifyRecord` /
`OnDeleteRecord` — NEVER `OnAfterInsert/Modify/Delete`.**
- ✓ `src/SYXCustomerCardExt.PageExt.al` → `trigger OnModifyRecord(): Boolean`.

## Page extensions

**14. `addlast` / `addfirst` MUST nest inside `layout { }` or `actions { }`** — never at page-ext top
level (`AL0104`).
- ✓ `src/SYXCustomerCardExt.PageExt.al` → `actions { addlast(Processing) { action(...) } }`.

**15. A page extension that declares its own `namespace` must `using` the base app's namespace** so
the extended object resolves.
- ✓ same file: `using Microsoft.Sales.Customer;` to reach `"Customer Card"`.

## ControlAddin

**16. Resource paths (`Scripts` / `StartupScript` / `StyleSheets`) are single-quoted and relative to
the PROJECT ROOT** (e.g. `'src/addin/board.js'`).

**17. There is NO `HtmlFiles` property** (`AL0124`). Build DOM in the startup script, anchored to
`document.getElementById('controlAddIn')` — NOT `document.body` (body renders a blank control, no
error).

**18. `event` = JS → AL** (raised in JS via
`Microsoft.Dynamics.NAV.InvokeExtensibilityMethod('Name', [args])`); **`procedure` = AL → JS** (maps
to a global JS `function Name(...)`). ControlAddins have **no numeric id**.
- ✓ `src/SYXBoard.ControlAddin.al` + `src/addin/board.js`.

## Permission set

**19. Object entries take only `= X`; data access goes on `tabledata … = RIMD`.** `table X = RIMD`
is `AL0195`. Required whenever the extension adds a table (`PTE0004` otherwise). List every object
the extension creates.
- ✓ `src/SYXExamplesPTE.PermissionSet.al`.

## Enum

**20. `enum <id> "Name" { value(<id>; Member) { Caption = '…'; } }`** — decl + brace body, each value
has an id and a Caption.
- ✓ `src/SYXPieceColour.Enum.al`.

---

## Version-gated features (`since`) — consulted only when the target floor is below them

At the **BC27 floor these are all AVAILABLE** — use them freely. The table matters only if you ever
build for an older on-prem target (drop the feature or the app won't compile there).

| Feature | Since (approx) | At BC27 |
|---|---|---|
| Namespaces + `using` | BC22 / runtime 11 | ✅ available (and expected) |
| `SecretText` type | BC22 | ✅ (but SaaS: prefer `IsolatedStorage`) |
| `ErrorInfo` / collectible errors | BC19 | ✅ |
| Interfaces | BC16 | ✅ |
| `List` / `Dictionary` / `foreach` | BC17 | ✅ |
| `InherentPermissions` / `InherentEntitlements` | BC24 | ✅ |

To change the floor, edit the "Target floor" line at the top **and** bump `runtime`/`application` in
the gold example's `app.json`, then re-run the validator.

## `target` in app.json
Leave `target` **unset** — an omitted target already defaults to Cloud, which is what SaaS wants, and
it's what compiles clean on the `al` version on this box (18.x). Only add a `target` if the compiler
demands it (`AL0666` wants `Cloud`/`Extension`; `PTE0005` rejects `OnPrem` on newer `al`).

## Not covered here (on purpose)
Object/field/event **names and signatures** — never invent them. Verify against `.alpackages`
symbols (integration-event subscriber parameters bind **by name**). See AL-REFERENCE §18 and the `/al`
skill's symbol tooling.

# AL rules — house ruleset

<!-- al_rules_gen: sources e26d285f2b7bdc0e generated 2026-09-09 -->

> **GENERATED FILE — do not edit.** Regenerate with
> `python3 pipeline/al_rules_gen.py` after any change to the sources below.
> Editing this file directly recreates the drift it exists to prevent.

| Source | Owns |
|---|---|
| [`reference/al-reference/00-gotchas.md`](reference/al-reference/00-gotchas.md) | the gotchas, several runtime-verified |
| [`reference/al-reference/01-syntax-style.md`](reference/al-reference/01-syntax-style.md) | formatting, naming, variables, abbreviations |
| [`reference/house-addendum.md`](reference/house-addendum.md) | house rules, hand-written |

Search the full reference instead of guessing: `kb search "<question>" --corpus al-reference`.

---

# Gotchas — read first

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

---

# Syntax and style

## 1. Formatting & Style

- **Keywords** lowercase: `begin`, `end`, `if`, `then`, `else`, `procedure`, `var`, `trigger`, `table`, `page`, `codeunit`, `repeat`, `until`, `exit`, `for`, `while`, `case`, `of`
- **Built-in methods and types** PascalCase: `FindSet`, `Modify`, `Insert`, `TempBlob`, `Error`, `Message`
- **4-space indentation** — no tabs
- **Curly brackets** always on new line
- **Blank line** between every procedure/trigger declaration
- **One statement per line** — never `if X then DoA(); DoB();` or `if X then exit;` on one line
- **Comments**: `// ` with one space — correct: `// Move below budget` — wrong: `//Move below budget`
- **Sentence case** for labels/captions when verb present: `'Calculate total'`, `'Submit order'`
- **Title case** for noun-only captions: `'Customer Card'`, `'Sales Order'`

---

## 2. File & Object Naming

File pattern: `ObjectName.ObjectType.al`

| Object type | File suffix |
|---|---|
| Table | `.Table.al` |
| Table Extension | `.TableExt.al` |
| Codeunit | `.Codeunit.al` |
| Page | `.Page.al` |
| Page Extension | `.PageExt.al` |
| Report | `.Report.al` |
| Enum | `.Enum.al` |
| Enum Extension | `.EnumExt.al` |
| Query | `.Query.al` |
| Permission Set | `.PermissionSet.al` |

Examples:
- `PTEDocumentLinkAZSetup.Table.al`
- `PTEDocumentLinkAZMgt.Codeunit.al`
- `PTEDocumentLink.TableExt.al`

**Reference objects by name, not ID:**
```al
// correct
Page.RunModal(Page::"Customer Card", CustomerRec);

// wrong
Page.RunModal(21, CustomerRec);
```

---

## 3. Object Structure Order

All object types follow this sequence inside the object block:

1. Properties (`Caption`, `DataClassification`, `Access`, `PageType`, etc.)
2. Object-specific constructs (`fields`, `layout`, `actions`, `triggers`)
3. Global variables — Records, Codeunits, Pages, then primitives, **Labels LAST** (see §4)
4. Methods/procedures

---

## 4. Variables & Types

**Procedure skeleton — every declaration goes in the `var` section, before `begin`.**
Compiler-verified against BC27 / runtime 16.0:

```al
// [local] procedure Name(Param: Type; var ByRefParam: Type) ReturnName: Type
procedure MigrateOne(DocAttach: Record "Document Attachment"; var FailedCount: Integer) Migrated: Boolean
var
    // Records, Codeunits, Pages, then simple types — LABELS LAST (AA0021)
    Setup: Record Customer;
    BlobName: Text[2048];        // ALL locals declared HERE — never mid-body
    Attempts: Integer;
    NotFoundErr: Label 'Blob %1 was not found.', Comment = '%1=blob name';
begin
    BlobName := Format(DocAttach.SystemId);
    if BlobName = '' then
        exit(false);
    exit(true);
end;

local procedure Helper(): Integer   // unnamed return: exit(<value>)
begin
    exit(1);
end;
```

**Declaration order is enforced by CodeCop AA0021, not by house style.** Probe-verified
against BC28 / runtime 17.0 with the cops on:

| order | AA0021 |
|---|---|
| `Label`, `Record`, `Integer` | **fires** |
| `Label`, `Codeunit`, `Integer` | **fires** |
| `Record`, `Label`, `Integer` | clean |
| `Codeunit`, `Label`, `Integer` | clean |
| `Integer`, `Label` / `Label`, `Integer` | clean |

What the rule actually requires is that a `Label` comes **after the object types**
(`Record`, `Codeunit`, `Page`, …). It is indifferent to a `Label`'s position relative to
simple types. **Labels LAST is the safe stricter convention** — it can never trigger AA0021,
so write it that way — but a `Label` sitting before an `Integer` is not a violation and does
not need "fixing". See [[16-analyzer-rules]] §AA0021.

**AL has NO inline variable declaration.** This is the single most expensive mistake a
C#-shaped model makes here, because the compiler does not report it as one:

```al
// ✗ WRONG — a declaration where a statement must be
repeat
    var BlobName: Text[2048];    // AL0104 "'until' expected" reported HERE
    BlobName := Rec.Name;
until Rec.Next() = 0;            // and AL0224/AL0111 again at the real `until`
```

The parser derails at the declaration and then reports the **loop terminator as missing** —
so `AL0104 'until' expected` or `'end' expected` with `repeat`/`until` **balanced** means a
declaration is sitting mid-body, not that a keyword is absent. Chasing the reported keyword
cannot fix it: observed 2026-09-01, a doclink build spent all 8 fix rounds rewriting the same
file to the same 6 errors because the message pointed at the symptom, 28 lines from the cause.

- PascalCase for all variable names
- `Temp` prefix on temporary record variables
- Object name must appear in the variable name

```al
var
    // Records
    PTESetup: Record PTEDocumentLinkAZSetup;
    TempSalesLine: Record "Sales Line" temporary;

    // Codeunits
    ABSBlobClient: Codeunit "ABS Blob Client";

    // Primitives
    BlobName: Text;
    LineCount: Integer;
    IsHandled: Boolean;
    Success: Boolean;

    // Labels LAST
    UploadFailedErr: Label 'Upload to ABS failed: %1', Comment = '%1=error text';
    BlobNameLbl: Label '%1/%2/%3/%4.%5', Comment = '%1=Code, %2=Caption, %3=Key, %4=File, %5=Ext';
```

Type declaration: colon immediately after name, single space, then type:
```al
var
    Customer: Record Customer;
    LineCount: Integer;

local procedure MyProc(Param: Text; Count: Integer): Boolean
```

Variable declaration order (alguidelines): Records → Codeunits → Pages → Reports → XMLports → Text/Code → Integer/Decimal/Boolean → others

**Newer language features (2024w2–2026w1) — types, operators, strings, JSON:**
```al
// Ternary (2024w2) — one-line value pick (don't nest; hurts readability)
Style := IsOverdue ? 'Unfavorable' : 'Favorable';

// continue (2025w1) — skip to next loop iteration anywhere in the loop
if Rec.Blocked then continue;

// Multi-line / verbatim string literal (2025w1): @'...' — newlines are literal
Body := @'Line 1
Line 2';

// ToText on simple types (2025w1): no-arg = Format(x); invariant variant = Format(x,0,9)
T := SomeInt.ToText();          // culture-formatted
T := SomeInt.ToText(9);         // invariant

// IncStr with negative step (2025w1) — decrement
NextCode := IncStr(CurrentCode, -1);

// this (2024w2) — self-reference; qualify a member shadowed by a param, or pass current object
procedure Set(Value: Integer) begin this.Value := Value; end;

// Date/Time component properties (2024w2): cleaner than Date2DWY/etc.
D := Today(); y := D.Year; m := D.Month; dow := D.DayOfWeek;   // Mon=1..Fri=5
h := Time().Hour;

// List of [Interface] / List of [Codeunit] (2024w2) — assigning a non-implementer errors
var Handlers: List of [IHandler];
```
JSON convenience (2025w1) on `JsonObject` — skip the JsonToken/JsonValue dance:
```al
Txt := JObj.GetText('name');            // ⚠ THROWS if 'name' missing
Txt := JObj.GetText('name', true);      // 2nd arg is a BOOLEAN — yields '' instead of throwing
// ✗ a Text 2nd argument is AL0133 — there is NO (Key, DefaultValue) overload
if JObj.Get('name', Tok) then           // the explicit guard, when you need to branch
  Txt := Tok.AsValue().AsText();
n   := JObj.GetInteger('qty');          // also GetBoolean/GetByte/GetChar/GetArray…
JObj.WriteToYaml(); JObj.ReadFromYaml(YamlText);   // YAML I/O — backported to runtime 14.3
JObj.SelectToken('$.lines[*].id', TokenList);      // multi-token select (2026w1)
```
Types: `SecretText` for passwords/tokens (kept out of debugger/memory dumps — see §14; forward path
over plain `Text`); `Cookie` type (set on requests, auto-reuse response cookies for the HttpClient
lifetime); `RichText` (needs `MultiLine=true`, alone in its own group, value is HTML) and `Barcode`
extended data types; variant gains `IsDictionary`/`IsList` (implicit convert to Dictionary/List).
`Callstack()` (2025w1) / `SessionInformation.Stack` return the current call stack **without** throwing
first (CPU-expensive — use sparingly). `HttpClient` gained `Patch`.

---

## 9. Conditionals & Flow

```al
// if/then — single statement, NO begin/end needed
if not IsReady then
    exit;

// if/then multi-statement — begin/end required
if Condition then begin
    DoA();
    DoB();
end;

// if/then/else
if Condition then begin
    DoA();
end else begin
    DoB();
end;

// case/of
case Rec.Status of
    Rec.Status::Open:
        HandleOpen();
    Rec.Status::Released:
        begin
            HandleReleasedA();
            HandleReleasedB();
        end;
    else
        HandleDefault();
end;

// repeat/until (record loop)
if MyTable.FindSet() then
    repeat
        ProcessRecord(MyTable);
    until MyTable.Next() = 0;

// for
for i := 1 to TotalCount do
    DoSomething(i);

// while
while Queue.Count() > 0 do
    ProcessNext(Queue);

// exit with value
exit(true);
exit(MyCodeunit.Run());
```

---

## 17. Common Abbreviations (alguidelines standard)

| Full word | Abbreviation |
|---|---|
| Account | Acc |
| Address | Addr |
| Amount | Amt |
| Archive | Arch |
| Buffer | Buf |
| Customer | Cust |
| Description | Desc |
| Document | Doc |
| Entry | Entry (not abbreviated) |
| General Ledger | GL |
| Inventory | Invt |
| Journal | Jnl |
| Line | Line (not abbreviated) |
| Management | Mgt |
| No. (Number) | No. |
| Purchase | Purch |
| Quantity | Qty |
| Sales | Sales (not abbreviated) |
| Setup | Setup (not abbreviated) |
| Temporary | Temp |
| Vendor | Vend |
| Worksheet | Wksh |

---

---

# house rules

Hand-written, and the only part of this file that is not derived from the reference.

## 1. Labels and `Locked`

No raw string literals. Every string is a Label variable.
- Technical/protocol strings: `Locked = true`
- User-facing strings: `Locked = false` (or omit)
```al
var
    RoleLbl: Label 'role', Locked = true;
    KeyNotSetErr: Label 'API key not configured.';
```

## 2. TextBuilder

Never concatenate strings for multi-line text. Use TextBuilder.
```al
var
    TB: TextBuilder;
begin
    TB.AppendLine(Line1Lbl);
    TB.AppendLine(Line2Lbl);
    TB.Append(LastLineLbl);
    exit(TB.ToText());
end;
```

The source states no threshold — the rule is written as absolute for multi-line text, and it
is recorded here as it stands rather than given a boundary it never had.

## 3. Custom telemetry conventions

- Treat telemetry as a public API — versioned, documented, non-breaking
- PascalCase field names, no spaces or special chars
- Message format: "Object ActionInPastTense" (e.g. "Web service call failed")
- Emit from the object where the condition occurs, not a central handler
- Only emit data the customer can act on
- DataClassification::SystemMetadata for all telemetry dimensions
```al
CustomDimensions.Add('HttpStatusCode', Format(Response.HttpStatusCode));
Session.LogMessage('MyExt0001', 'Web service call failed',
    Verbosity::Error, DataClassification::SystemMetadata, TelemetryScope::ExtensionPublisher, CustomDimensions);
```

The event ID scheme is shown only by example (`MyExt0001`); the source defines no prefix
allocation, and none is invented here.

## 4. Project overrides

Add per-project overrides in that project's `CLAUDE.md`, referencing this file.

**Every rule here is overridable, and no override is valid without a written reason.**
(Decided 2026-08-28. The source defined no boundary at all — it said only the one line above —
so this is a new rule, not a recovered one.)

An override must name the rule it displaces and say **why** this project differs, inline in the
project's `CLAUDE.md`:

```markdown
## AL rule overrides
- **§2 TextBuilder** — overridden. This extension targets runtime 11.0, where TextBuilder is
  unavailable; concatenation is the only option until the platform bump.
```

A bare "we do it differently here" is not an override; treat the house rule as still in force.
The reason is the point: it makes an override reviewable, and it dates itself, so a constraint
that has since lifted is visible rather than permanent.

This applies uniformly rather than marking some rules non-negotiable. Singling out §1 and §2
was considered and rejected — a rule that cannot be overridden gets worked around silently,
which is harder to find than a stated exception.

---

## What must NOT go in this file

Recorded because the old ruleset accumulated all of it, and every item below is where it
contradicted the reference:

- Variable declaration order — `al-reference/01-syntax-style.md` owns it.
- Abbreviation tables — the alguidelines list is in `01-syntax-style.md`.
- Record-access patterns such as `Find('-')` versus `FindSet()` — `00-gotchas.md` owns those,
  and it is runtime-verified.
- `NoImplicitWith` and record qualification — `00-gotchas.md`.
- Anything about language features, analyzer codes, JSON, namespaces or `DataClassification`.


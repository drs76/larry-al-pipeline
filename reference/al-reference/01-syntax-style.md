<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Formatting, naming, structure, variables, flow, abbreviations

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

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

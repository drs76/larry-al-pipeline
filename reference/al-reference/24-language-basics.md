<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# AL language basics — operators, variables, statements, scope

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

Distilled from Microsoft Learn (*The AL programming language*, 2026-08-16). Split out of
`01-syntax-style.md`: absorbing these took that file 1.8k → 7.4k tokens, which consumed over
half the handover's ~12.5k injection budget and evicted `02-objects.md` from the injected set
entirely — control builds went 2/3 → 0/3 on the bench with `AL0104` brace errors on tables.
Per-file size was never breached; the binding constraint is the **injection set total**.

---

<!-- ingested: Programming in AL | 2026-08-16 -->
### Programming in AL — fundamentals (Learn: Programming in AL)

- AL = language for BC data manipulation (retrieve/insert/modify records) and control of object execution (pages, reports, codeunits).

**Where AL code can live — objects with triggers:**
- Tables and table extensions
- Table fields
- Pages and page extensions
- Reports and report extensions
- Data items
- XMLports
- Queries

**How code gets invoked:**
- Actions.
- Any object holding an instantiation of the code-bearing object — e.g. a variable declaration of a codeunit.
- Gotcha: a `local` method cannot be called from another object. Only non-local (global/public) methods are reachable externally.

**Variable declarations:**
- `var` keyword introduces the block:
  ```al
  var
      myInt: Integer;
  ```
- Multiple vars of same type on one line, comma-separated:
  ```al
  var
      myInt, nextInt, thirdInt : Integer;
      isValid, doCheck : Boolean;
  ```
  (Note the space before `:` in the multi-variable form as shown in the docs; single-variable form is written `name: Type`.)
- `protected` keyword makes variables accessible between a table and its table extensions, and between a page and its page extensions. See Learn "Protected variables".

**Code placement guidelines:**
- Default: put code in codeunits, not on the object it operates on. Reasons: clean design, reuse, and security.
- Security rationale: users typically lack direct permission on sensitive tables (e.g. G/L Entry) and lack permission to modify objects. Grant the codeunit access to the table, grant the user execute permission on the codeunit — table security stays intact while the user still gets the data.
- If code must sit on an object, put it as close as possible to what it acts on — e.g. record-modifying logic in table field triggers.

**Reuse:**
- Centralise logic so the same calculation isn't duplicated across triggers sharing a source expression; duplicates cause inconsistencies and missed edits when the rule changes.

<!-- ingested: · AL operators | 2026-08-16 -->
### AL operators (Learn reference)

**General**
- `.` — member access: record fields, page/report controls.
- `:=` — assignment (right side → left side). `=` is equality test only, never assignment.
- `()` grouping/call, `[ ]` indexing, `..` range.
- `::` — scope operator, yields an object's ID: `Report::MyReport`, `Query::"My Query"`. Quote names with spaces.
- `@` — case-insensitive match (used in filter expressions).

**Arithmetic**
- `+ - * /`, plus `div` (integer division) and `mod` (modulus). `div`/`mod` are keywords, not symbols.

**Comparison**
- `> >= < <= = <>`. Not-equal is `<>`, not `!=`. Result is Boolean.

**Logical** (Boolean operands only)
- `and`, `or`, `not`, `xor` — word operators, no `&& || !`.

**Conditional (ternary)** — BC 2024 wave 2 (v25) and later
- `cond ? valueIfTrue : valueIfFalse`, e.g. `myVar := myExpression ? 'True' : 'False';`
- Not available on older runtimes — guard by `application`/`runtime` version in app.json.

**Compound assignment**
- `+=`, `-=`, `*=`, `/=`. No `div=`/`mod=` variants listed.

**Unary vs binary**
- `+` and `-` work as both unary and binary; `not` is unary only; everything else binary.
- Operator behaviour is type-dependent: `+` on numbers = addition, `+` on Text = concatenation.

**Precedence** (highest → lowest)
1. `.` `[ ]` `()` `::` `@`
2. `not`, unary `-`, unary `+`
3. `*` `/` `div` `mod` `and` `xor`
4. `+` `-` `or`
5. `>` `>=` `<` `<=` `=` `<>` `in`
6. `..`

**Gotchas from the precedence table**
- `and`/`xor` sit at multiplication level and `or` at addition level — same tier as arithmetic, so mixing arithmetic and Boolean logic in one expression evaluates in a non-obvious order. Parenthesise.
- Comparisons bind *looser* than `and`/`or`: `a = 1 and b = 2` does not parse as expected. Always write `(a = 1) and (b = 2)`.
- `2 + 3 * 4` = 14; `(2 + 3) * 4` = 20.

<!-- ingested: · AL variables | 2026-08-16 -->
### AL variables — naming, initialization, assignment conversion

**Kinds**
- User-defined: global (all methods of object) or local (single method). Both scoped to the object they're declared in.
- System-defined: supplied by the platform — `Rec`, `xRec`, `CurrPage`, `CurrReport` (and others). Auto-initialized; no setup needed.
- System-defined values are set *before* the trigger/method runs, not refreshed mid-execution. Writing to them does not propagate back to system state.

**Naming rules**
- Case-insensitive: `Smith` and `SMITH` are the same identifier.
- Max length 128 chars. Names must be unique within a scope; a local may shadow a global but avoid it.
- Cannot reuse an AL method name or reserved word in any casing (`begin` is invalid).
- Unquoted identifiers: first char must be a letter or underscore, followed by up to 29 more chars of letters/digits/underscores.
- Any special char (space, `.`, `/`, `@`, non-ASCII) requires double quotes: `"Customer No."`, `"Purchase/Sales"`, `"@Vendor"`. Quotes are syntax only, not part of the name.
- Invalid: leading digit (`34467`), unquoted spaces (`Stock Group4`), embedded stray quote (`"Sale"s in GBP"`), leading punctuation (`)-Names`), reserved word (`END`).
- Note the mismatch: 128-char max overall, but the unquoted grammar as documented allows only 1 + 29 chars — verify current compiler behaviour before relying on long unquoted names. `[sic?]`

**Automatic initialization** (before code runs; no manual init needed)
- Boolean → `false`; numeric → `0`; Text/Code → `''`; Date → `0D`; Time → `0T`.
- Complex types are initialized too; each component gets its own type's default.

**Assignment & implicit conversion**
- `:=` and parameter passing both convert implicitly when the source type is convertible to the target.
- Numeric family converts freely among `Byte`, `Char`, `Integer`, `Decimal` (also `Option`, `BigInteger`, `Duration`) — overflow is a *runtime* error, not a compile error.
- String family converts between `Code` and `Text` — overflow (length) possible in both directions, including Text→Text of smaller length.
- Non-convertible values (e.g. DateTime into an Integer parameter) raise a runtime error.
- Conversion matrix highlights: `Char` target overflows from almost anything; `Decimal` → `Integer`/`BigInteger`/`Duration` may overflow; `Integer`/`Option` ← `BigInteger`/`Duration`/`Decimal` may overflow. Widening (`Char`/`Option`/`Integer` → `BigInteger`/`Duration`/`Decimal`) is safe.
- Arrays follow the same rules, plus dimensions on both sides must match.
- `BigText` takes no plain assignment — use the BigText methods.

**Gotcha**: convertibility is checked by the compiler, range is not. Any int-narrowing or string-narrowing assignment is a latent runtime error.

<!-- ingested: · System-defined variables | 2026-08-16 -->
### System-defined variables

- BC auto-declares and initializes these — no `var` declaration needed:
  - `Rec` — current record *with* pending changes applied (in modify context).
  - `xRec` — record values *before* changes.
  - `CurrPage` — current page object.
  - `CurrReport` — current report object.
  - `RequestOptionsPage` — request page of current report.
  - `CurrFieldNo` — field no. of current field in current table; legacy, kept for compatibility only. Avoid in new code.

**Rec / xRec**

- Standard pattern: in a field's `OnValidate`, compare `Rec."Customer No."` vs `xRec."Customer No."` to detect a real change, then reject it if a state gate says the record is locked down (e.g. order already shipped).
- Header/line design context: header stores only the FK (e.g. customer no.); descriptive fields (name, address) get pulled from the related table during validate of the FK field.
- **Gotcha:** do not write to `xRec`. `Rec` and `xRec` may share underlying state for perf/compat reasons — mutations can leak into `Rec` unexpectedly. Treat `xRec` as read-only.

**CurrPage**

- Gives access to page controls and dynamic page/control properties at runtime.
- `CurrPage.Editable` — runtime value of the `Editable` property. Can be changed at design time, set programmatically, or flipped by the user switching view mode.
- `CurrPage.Update([SaveRecord])` — saves current record (when `SaveRecord` is true) and refreshes controls.
- Mode relationship: when page View mode is false, Edit / New / Delete modes are true.

**CurrReport**

- Exposes report properties for dynamic reads/sets, e.g. `CurrReport.Preview` to test whether the report runs in preview.

**RequestOptionsPage**

- Exposes request-page properties for dynamic read/set from report code.

<!-- ingested: · Protected variables | 2026-08-16 -->
### `protected var` (BC 2019 wave 2+)

- `protected` keyword on a `var` block makes those variables visible to the object's extensions: table ↔ tableextension, page ↔ pageextension, report ↔ reportextension.
- Also crosses app boundaries: a dependent app's extension object can read/write protected vars of the base object.
- Mixed visibility needs two separate `var` sections — one `protected var`, one plain `var`:

```al
protected var
    myInt: Integer;      // visible to extensions

var
    myLocalInt: Integer; // object-local only
```

- Pattern: base page declares `protected var ShowBalance: Boolean;`; a `pageextension` binds it to a group's `Visible` property and flips it in an action's `OnAction` trigger. Extension-controlled UI state without events or a new setup field.
- Related properties for access control: `Access`, `Extensible`.

<!-- ingested: AL simple statements | 2026-08-16 -->
### Simple statements (assignment, AssertError, with)

- Simple statements = single-line, run in sequence, no flow control.
- Assignment operator is `:=`. RHS is any AL expression: constant, variable, arithmetic, or a method call (the return value is assigned).
- Compound assignment operators exist: `+=`, `-=`, `*=`, `/=`. `Counter += 1;` is equivalent to `Counter := Counter + 1;`.
- `+=` also works on `Text` variables to append: `String += 'World';`.
- Optional return values: if a method returns a Boolean success flag and the call result is discarded, a runtime error is raised when it returns `false`. Handle it with `if <call> then ... else Error(...)`. Example given: `File.Open` (on-premises only).

#### AssertError

- `AssertError <statement>;` — used in test methods; declares that the following simple or compound statement is expected to fail.
- If the statement errors, execution continues at the next statement in the test method. Retrieve the error text with `GetLastErrorText`.
- If the statement does NOT error, `AssertError` itself raises an error and the test result is `FAILURE` ("An error was expected inside an AssertError statement").
- `AssertError` catches any error type, including UI error messages.
- Typical pattern: call the failing method under `AssertError`, then compare `GetLastErrorText` with the expected label and `Error()` if it doesn't match.

#### with (deprecated)

- `with <Record> do <Statement>` let fields be addressed without the record prefix inside the block. Deprecated since BC 2020 release wave 2 — currently a warning, planned to become a compile error.
- Reason for deprecation: unqualified member names collide when several extensions add members to the same object.
- Implicit `with` also exists — table objects and pages bound to a record. Same deprecation applies. Controlled via the `ImplicitWith` pragma / directives in AL.
- Nesting was allowed; the inner block shadows the outer for identical names, which is exactly why it's unreadable. Old convention was that a nested `with` should attach to a variable of the same type as the outer one.
- Refactor rule for modern code: always qualify — `CustomerRec."No." := '1234';` — never rely on implicit or explicit `with`. A quick action in the editor can fix a whole file.

<!-- ingested: AL control statements | 2026-08-16 -->
### Control statements (compound, conditional, repetitive)

**Compound statements / blocks**
- `begin ... end;` groups multiple statements where syntax allows only one.
- Semicolon is a *separator*, not a terminator. A trailing `;` before `end` is legal — parsed as an empty statement.
- Style: `begin` goes on the same line as `then`, `else`, or `do`, separated by one space.
- With long/multi-line conditions, put `then` on its own line aligned with `if`, then `then begin` / `end else begin`.

**if-then-else**
- `if <Cond> then <Stmt1> [else <Stmt2>];` — `else` part optional.
- **No semicolon is allowed before `else`.**
- Nested `if` without `else`: a dangling `else` binds to the nearest preceding `if` that lacks one.
- Style: `if` and `then` on one line, `else` on its own line; write the more probable outcome as the `then` branch.
- If the `then` branch ends in `exit` or `error`, drop the `else` and continue at the outer level instead.

**case**
```al
case <Expression> of
    <ValueSet>:
        <Statement>;
    <ValueSetA>,
    <ValueSetB>:
        <Statement>;
    else
        <Statement>;
end;
```
- Value sets are expressions or ranges (`10 .. 100`); multiple values on one line separated by commas, no spaces; colon directly after the last value, no preceding space.
- `<Expression>` **cannot be an application-object variable** (no comparator defined for those).
- Value-set data types must match or be convertible to the expression's type. Conversion happens at runtime and **can overflow**.
- **Gotcha:** if the expression is a `Code` variable, value sets are *not* converted to `Code`. Result: `MyCode := 'ABC'` does not match value set `'abc'` — falls through to `else`. (Code comparison elsewhere is case-insensitive/upper-cased; the case value sets are not.)
- Convention: use `case` for more than two alternatives, `if-then-else` otherwise. `begin` on its own line, except after `else` where it stays on the `else` line.

**Loop mechanisms**
| Construct | Behaviour |
|---|---|
| `for ... to / downto` | fixed iteration count via control variable |
| `foreach` | iterates a collection |
| `while ... do` | pre-tested; zero or more iterations |
| `repeat ... until` | post-tested; always at least one iteration |

**for-to / for-downto**
- `for <Ctrl> := <Start> to|downto <End> do <Stmt>;`
- Control/start/end types must be Boolean, number, time, or date.
- `to` increments by 1 per iteration, `downto` decrements by 1. Step size is not configurable.
- Start and end values are converted to the control variable's type — **this can raise a runtime error** (e.g. `for Count := 1000 to 100000000000000` with `Count: Integer` overflows).
- Changing the control variable inside the loop gives undefined behaviour; its value after the loop is undefined.

**foreach**
- `foreach <Element> in <Collection> do <Stmt>;`
- Supported collection types: `List of [T]`, `XmlNodeList`, `XmlAttributeCollection`, `JsonArray`.
- From BC 2023 wave 1 (v22), `foreach` also works over `Text` variables, iterating individual characters — useful for detecting/removing/replacing chars.
- `<Element>` must be type-compatible with the collection elements.

**while-do**
- Condition tested first; body may never run.
- Style: single condition → `while` and `do` on one line; multiple conditions → conditions on separate indented lines with `do` on its own line aligned with `while`.

**repeat-until**
- Body always runs at least once; condition tested after each pass, loop exits when true.
- `repeat` always on its own line.
- Canonical record loop:
```al
if Customer.FindSet() then
    repeat
        Count += 1;
    until Customer.Next() = 0;
```
  `Next()` returns 0 when there are no more records.

**exit**
- `exit([<Value>])` — interrupts the current trigger/method immediately, even from inside a loop; also the way a method returns a value.
- `exit` with no argument in a method that returns a value yields the type default (`0` / `''`).
- Compile-time error if a return value is passed to `exit` in a system-defined trigger or in a method with no return value.

**break**
- `break;` terminates the innermost enclosing `for` / `foreach` / `while` / `repeat` loop.
- Distinct from the report/XMLport `Break` **method**, which also terminates the trigger it runs in.

**continue** (BC 2025 wave 1 / v26, runtime 15.0+)
- `continue;` skips to the next iteration of the enclosing loop.
- **Gotcha:** for backwards compatibility, if a procedure or variable named `Continue` is in scope, `continue` is parsed as invoking *that* instead of the statement. This fallback is slated for removal — rename conflicting identifiers.

<!-- ingested: AL code comments | 2026-08-16 -->
### XML documentation comments

- Available BC 2020 wave 2 and later. Syntax: `///` triple slash before the declaration being documented.
- Must sit immediately above the user-defined type or member it annotates — codeunit, table, interface, field, method.
- Typing the third slash triggers IntelliSense to emit a template comment.
- Rendered on hover, in completion lists, and in signature help — both in the authoring project and for consumers extending a built app.
- `allowDownloadingSource: false` in app.json strips XML comments from the downloaded app package.
- ALDoc (ships with the AL Language VS Code extension) generates help files from these comments.

#### Top-level tags

| Tag | Use |
|---|---|
| `<summary>description</summary>` | Object/member summary |
| `<param name="name">description</param>` | One per method parameter |
| `<returns>description</returns>` | Return value |
| `<example>description</example>` | Usage example |
| `<remarks>description</remarks>` | Supplements `<summary>` |

#### Formatting tags (valid inside a top-level tag)

- `<paramref name="name"/>` — reference a parameter from `<summary>` or `<remarks>`.
- `<para>` — paragraph break inside `<summary>`, `<remarks>`, `<returns>`.
- `<b>`, `<i>` — bold, italic.
- `<c>` inline code; `<code>` multiline code block.
- `<list type="bullet|number|table">` with optional `<listheader>`, then `<item>` entries; each holds `<term>` and `<description>`.

```al
/// <summary>
/// Provides functionality to create and send e-mails.
/// </summary>
codeunit 8901 "Email"
{
    Access = Public;

    /// <summary>
    /// Enqueues an email in the outbox to be sent in the background.
    /// </summary>
    /// <param name="EmailMessageId">The ID of the email to enqueue</param>
    procedure Enqueue(EmailMessageId: Guid)
    begin
        EmailImpl.Enqueue(EmailMessageId);
    end;
}
```

#### Gotcha — angle brackets

- Comment body is parsed as XML. Literal `<` and `>` must be HTML-encoded as `&lt;` / `&gt;`, else the comment breaks.

```al
/// <summary>
/// This property always returns a value &lt; 1.
/// </summary>
```

#### Content guidance

- Say *why*, not what the signature already shows; never restate the obvious.
- Properties/methods: active voice — "Sets…", "Gets…", "Specifies…".
- Document parameter preconditions (nullability, ranges) and post-conditions affecting how callers treat the return value.
- Document errors the method can raise and when.
- Note side effects, global-state mutation, and anything surprising.
- Where near-identical methods exist, state the difference between them.
- Keep terminology consistent; review comments like code.

<!-- ingested: Using access modifiers in AL | 2026-08-16 -->
### Access modifiers (Access property)

- `Access` property sets visibility of **tables, table fields, codeunits, queries**. Default when omitted: `Public`.
- Purpose: API design — shrink the surface dependent extensions can bind to, so internals stay refactorable without breaking consumers.
- Values:
  - `Internal` — usable only inside same module (extension). Cross-module access granted via `internalsVisibleTo` in app.json.
  - `Local` — table fields only; reachable only from code in the table or table extension where field is declared.
  - `Protected` — table fields only; reachable from the table and any table extension of that table.
  - `Public` — reachable from any module referencing it. Default.
- **Not a security boundary.** Enforcement is compile-time only.
- Runtime escape hatches that bypass `Access = Internal`:
  - `RecordRef` (reflection-style record access)
  - `TransferFields`
  - `Codeunit.Run` can fire `OnRun` on an internal codeunit
- Consequence: never rely on `Internal` to protect data or hide privileged logic — use permission sets / permissions for that.
- Pairing: `Access = Internal` on objects + `internalsVisibleTo` (app.json) is the pattern for splitting one logical product across multiple apps while keeping the API private.

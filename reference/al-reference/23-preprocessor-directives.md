<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# preprocessor directives

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: · Preprocessor directives | 2026-08-16 -->
### Preprocessor directives in AL

- Available BC 2020 wave 2 (v17) and later. Three groups: conditional directives, regions, pragmas.
- Symbols are boolean flags only — defined = true, undefined = false. No values can be assigned.

**Conditional directives**

| Directive | Effect |
|---|---|
| `#if SYM` | Start conditional block; code compiles only if `SYM` defined |
| `#elif SYM` | else-if branch |
| `#else` | Fallback branch when no preceding clause true |
| `#endif` | Close the `#if` block |
| `#define SYM` | Define symbol; scope = the file it sits in |
| `#undef SYM` | Undefine symbol from that point onward in the file |

- Logical operators inside `#if` / `#elif`: `and`, `or`, `not`. e.g. `#if DEBUG and TESTING`, `#if not PRODUCTION`.
- Conditional compilation works on *any* code, including table field declarations — a field can be compiled in/out:

```al
table 50100 MyTable
{
    fields
    {
        field(1; "Basic Field"; Code[20]) { }
#if PREMIUM_FEATURES
        field(2; "Premium Field"; Code[20]) { }
#endif
    }
}
```

- Gotcha: compiling a field in/out changes the table schema between builds — treat like any breaking schema change.

**Defining symbols globally (app.json)**

```json
{ "preprocessorSymbols": [ "DEBUG", "PROD" ] }
```

- Symbols listed in `preprocessorSymbols` are true for the whole extension. File-level `#define` is scoped to that one file only.
- No built-in/predefined symbols exist in AL. Names like `CLOUD`, `ONPREM`, `DEBUG` only work if *you* define them (file or app.json) — the platform supplies nothing.

**Personalization / profile gotcha**

- User personalization and profile configuration (incl. profile copy) do not support directives: `#pragma`, `#region`, `#endregion` are ignored by the platform; `#if`, `#elif`, `#define` etc. error out where unsupported.

**Example — file-scoped define**

```al
#define TESTING

codeunit 50100 MyCodeunit
{
    trigger OnRun()
    begin
#if TESTING
        Message('Runs only when TESTING defined');
#endif
    end;
}
```

- Related: region directive (`#region` / `#endregion`, collapse/expand only), pragma directive (warning suppression). See separate docs.

<!-- ingested: · Region directive | 2026-08-16 -->
### `#region` directive

- Available BC 2020 wave 2 and later.
- Marks collapsible/expandable code block in editor. Purely editor-level — no compilation effect.
- Syntax:

```al
#region [comment]
// code
#endregion
```

- Optional comment text sits on same line as `#region`, describes block purpose.
- Every `#region` must be closed by `#endregion`.
- `#region` and `#if` blocks cannot overlap/interleave. Nesting either way is legal: `#region` inside `#if`, or `#if` inside `#region`.

<!-- ingested: · Pragma directive | 2026-08-16 -->
### #pragma directive

- `#pragma` passes compiler instructions scoped to the file it appears in. Available from BC 2020 release wave 2 (and later runtimes).
- Actions available to pragma instructions: `disable`, `restore`, `enable`.
- Two pragma instructions in AL:
  - `#pragma implicitwith` — controls handling of implicit `with` statements (tied to the deprecation of explicit/implicit `with`).
  - `#pragma warning` — suppresses or restores compiler warnings/diagnostics.
- Scope is per file, not per project — a `disable` left unrestored applies to the rest of that file only.
- Related directives: `#region` / `#endregion`, conditional directives (`#if`/`#else`/`#endif`).
- Verify exact instruction casing and the full action grammar (e.g. `#pragma warning disable AA0001` / `restore`) against Microsoft Learn or the compiler — source page did not spell out the syntax.

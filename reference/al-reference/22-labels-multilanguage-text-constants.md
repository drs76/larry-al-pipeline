<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# labels & multilanguage text constants

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: Working with labels | 2026-08-16 -->
### Labels

- Label = translatable string constant surfaced in the client (captions, tooltips, messages). Backbone of BC multilanguage/translation files (XLIFF).
- Syntax: text literal followed by up to three optional, comma-separated parameters. Order not enforced.

| Parameter | Type | Effect |
|---|---|---|
| `Comment` | Text | Notes for translators, mainly explaining `%1`-style placeholders |
| `Locked` | Boolean | `true` = excluded from translation. Default `false` |
| `MaxLength` | Integer | Caps label length; unbounded if omitted |

- Four places labels appear: property value, `Label` data type variable, report label, page label.

#### As a property value

- Label syntax valid on UI-text properties: `Caption`, `ToolTip`, `OptionCaption`, `AdditionalSearchTerms`, `InstructionalText`, `PromotedActionCategories`, `RequestFilterHeading`.

```al
Caption = 'Developer translation for %1', Comment = '%1 is extension name', Locked = false, MaxLength = 999;
```

#### `Label` data type

- Declared as a var; holds error messages, confirm questions, captions, tokens.

```al
var
    MyLabelTxt: Label 'Label Text', Comment = 'Do not translate.', MaxLength = 999, Locked = true;
```

- Escape a single quote inside the literal by doubling it (`don''t`).
- BC 2023 wave 2+: hovering a `Label` variable in VS Code shows its text value.
- CodeCop **AA0074** requires an approved suffix on Label variable names (e.g. `Txt`, `Msg`, `Err`, `Qst`, `Lbl`, `Tok`, `Caption`) — see [[16-analyzer-rules]].

#### Report labels

- Consumed by report layouts: field captions, chart titles, report title. Defined in the report's `labels` section rather than as vars.

#### Page labels

- Plain informational/instructional text on a page. Declared as a `label(Name)` control inside `area(Content)`.

```al
label(BeforeSetupCloseMessage)
{
    ApplicationArea = Basic, Suite;
    Caption = 'If you still need to change setup data, don''t change the profile.';
}
```

- Real-world examples live in page `Config. Wizard` (RapidStart Services Wizard).

#### Gotchas

- Escape a single quote inside any literal by doubling it (`don''t`). The source doc's sample
  now shows this correctly (`shouldn''t`); an earlier revision did not, and this note used to
  flag it. Re-checked against the 2026-08-24 page.
- Declaration order is a cop rule: **AA0021** requires a `Label` to come after the object
  types. Labels LAST is the safe stricter form — see [[01-syntax-style]] §4 for the probe table.
- `Locked = true` still allows `MaxLength` to apply.
- Labels are compile-time constants: no runtime string concatenation into a label; use placeholders + `StrSubstNo`.

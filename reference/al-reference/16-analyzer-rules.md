<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Analyzer rules — AppSourceCop, CodeCop, PerTenantExtensionCop, UICop

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

The authoritative diagnostic-code lists (`AS`/`AA`/`PTE`/`UI`), from Microsoft Learn.
This is the ground truth to check a cop claim against **before** writing it into a rule:
AL-SYNTAX rule 7 once asserted a "SaaS hard requirement (PTE/CodeCop)" that no cop
enforces, and rule 10 cited `AA0218` for what is really `PTE0008`. Both would have been
caught here. `pipeline/probe_al_rules.sh` proves a code actually fires; this says which
code to expect.

---

<!-- ingested: · AppSourceCop analyzer rules | 2026-08-16 -->
### AppSourceCop — rules & AppSourceCop.json config

- AppSourceCop = analyzer enforcing AppSource publishing rules. Enable via `${AppSourceCop}` in the enabled code analyzers list (settings / al.codeAnalyzers).
- **Mutually exclusive with PerTenantExtensionCop** — several rules conflict. Enable only one.
- Severity meaning for submission: `Error` = submission fails. `Warning`/`Info` = recommended only. `Hidden` = niche cases, ignorable.
- Rule IDs are `ASxxxx`. Categories: Upgrade (breaking-change vs baseline), Extensibility, Configuration, Design.

#### Rule clusters worth knowing
- **Schema breaking changes (Upgrade, Error):** no deleting published tables/table extensions (AS0001), fields (AS0002), keys (AS0010), pages/pageextensions (AS0029), actions (AS0031), controls (AS0032), views (AS0033), interfaces (AS0065) or interface implementations (AS0064), analysis views (AS0140). No renaming tables (AS0006), pages (AS0030), fields (AS0005), referenceable objects (AS0090). No field type change (AS0004); Integer→BigInteger is a Warning (AS0146). No shortening fields (AS0080, Error); lengthening is Warning (AS0086). Primary-key field length (AS0118) and ID (AS0137) frozen. No changing namespace of published objects (AS0007). No changing a tableextension's/extension object's target (AS0068, AS0124). Clustered key can't be deleted (AS0043) or newly declared on an existing table (AS0123).
- **Public API / signature freezing (Upgrade, Error):** can't remove public procedures (AS0018) or variables (AS0106), change return type (AS0023), add a return value (AS0102), add/remove parameters (AS0024), change param type/subtype (AS0026), change array size (AS0027/AS0028), add/remove `var` on external procedure params (AS0078), remove external scope (AS0022), or narrow an access modifier (AS0049 objects, AS0095 table fields, AS0107 public variables). Extensibility of an object can't be removed (AS0050).
- **Event contract freezing (Upgrade, Error):** can't remove event attributes (AS0019), change event type (AS0020), flip an attribute argument to false (AS0021), modify/rename/remove event params (AS0025), add (AS0077) or remove (AS0063) `var` on event params, change `Isolated` argument (AS0101). External business events: name frozen (AS0114), version change is a Warning (AS0134), must be obsoleted before removal (AS0135).
- **Enums (Upgrade, Error):** can't rename (AS0082) or delete (AS0083) enum values; can't add a method to a published interface (AS0066); adding an interface to a published enum requires a default implementation (AS0067); interfaces can't be added to/removed from a published interface's extends list (AS0129/AS0128). Option→enum conversion must keep member count (AS0069), names (AS0070) and ordinals (AS0071).
- **Obsoletion (Design):** ObsoleteReason required (AS0075, Warning); ObsoleteTag required/format/next-version/consistent-across-branches (AS0072/73/74/76, Hidden by default); referencing a pending-obsolete object with an expired tag = AS0105 (Error). Obsolete state can't jump `No` → `Removed` directly (AS0115).
- **Object moves between apps:** moves need `PendingMove` (AS0117), `MovedTo`/`MovedFrom` AppIds must match (AS0119/AS0120), name must stay the same (AS0121), destination table needs MovedFrom (AS0141/AS0142).
- **Extensibility hygiene:** affix required on new objects (AS0011) and on procedures in extension objects (AS0079, Warning) and AS0098 (Warning); IDs within allocated range (AS0013 fields, AS0084 app range, AS0099 enum members Info); manifest must declare the id range (AS0014); TranslationFile feature must be on (AS0015); Normal fields need DataClassification ≠ ToBeClassified (AS0016); page controls/actions need ApplicationArea (AS0062); new table fields need AllowInCustomizations (AS0139 Warning / AS0138 Hidden); namespaces should be ≥2 levels (AS0127, Warning); avoid duplicate object names (AS0130, Warning).
- **Runtime restrictions:** `AssertError` only in test codeunits (AS0058); reserved database tables read-only in multitenant (AS0059); unsafe methods banned (AS0060); no subscribing to CompanyOpen events (AS0061); compilation target must be SaaS-legal (AS0053).
- **app.json / manifest:** `application` property required (AS0100) and preferred over explicit dependencies (AS0085, Warning); required manifest props for submission (AS0051); `url` must be a valid URL (AS0052); Application Insights resource recommended (AS0092, Warning); extension name length/validity (AS0047/AS0104) and publisher name length (AS0048); name (AS0096) and publisher (AS0097) can't change after publishing.
- **Permission sets:** define in AL, not XML (AS0094, Warning); tables should have a matching permission set (AS0103, Warning); permission set extensions must not include foreign-app objects/sets or wildcards (AS0110–AS0113, Warnings).
- **Baseline resolution failures:** AS0003 (previous version not found), AS0091 (a dependency of the previous version not found), AS0116/AS0122 (moved-symbol source not found).
- `InternalsVisibleTo` is not a security boundary (AS0081) and must not name a different publisher (AS0126).

#### AppSourceCop.json (project root; IntelliSense-backed)
- Baseline selection: `name`, `publisher`, `version` (**version is the only mandatory setting**) identify the previous package to diff against. Baseline .app must sit in `baselinePackageCachePath`, else the project's `al.packageCachePath` is used.
- `mandatoryAffixes`: array of strings; every new object, extension object and field name must contain one. (Legacy `mandatoryPrefix` / `mandatorySuffix` still accepted.)
- `supportedCountries`: ISO 3166-1 alpha-2 codes (validated by AS0056).
- Obsolete-tag validation: `obsoleteTagVersion` (next Major.Minor; supersedes the deprecated `targetVersion`), `obsoleteTagPattern` (regex, default `(\d+)\.(\d+)`), `obsoleteTagPatternDescription` (default `Major.Minor`), `obsoleteTagAllowedVersions` (comma-separated list), `obsoleteTagMinAllowedMajorMinor` (drives AS0105 — **has a compile performance cost**).
- `sourceMovedObjectsPackagesCachePath`: folder with the source apps (plus their dependencies) that tables/fields were moved from. Empty = move validation disabled.
- Scope toggles, all default off: `validateInternalSymbols`, `validateObsoleteSymbols`, `validateOnPremSymbols`. By default breaking-change checks run only on public, non-obsolete, Cloud-scope symbols — **except schema breaking-change validation, which always runs regardless of these three**.
- Multi-root workspace: each project folder needs its own AppSourceCop.json.
- Example diagnostic text: `AS0011: The identifier 'CustomerListExt' must have at least one of the mandatory affixes 'Foo, Bar'.`

<!-- ingested: · CodeCop analyzer rules | 2026-08-16 -->
### CodeCop analyzer — rule map (AA0xxx)

CodeCop enforces the official AL coding guidelines. Enable in `settings.json` / `al.codeAnalyzers`. Rule IDs are stable; use them in `#pragma warning disable` and rulesets. Grouped by what they force you to do:

**Formatting / readability (mostly Warning)**
- AA0001/AA0002/AA0003: exactly one space each side of binary operators (`:=`, `+`, `-`, `and`, `or`, `=`); no stray spaces; one space after `not`.
- AA0005: `begin..end` only around compound statements (not single statements).
- AA0008: call parameterless methods with `()`.
- AA0013: `begin` stays on the same line as `then`/`else`/`do`, one space before.
- AA0018: `end`, `if`, `repeat`, `until`, `for`, `while`, `case` must start their own line.
- AA0021: order variable declarations by type.
- AA0022: prefer `case` over long `if..then..else` chains.
- AA0040: no nested `with`.
- AA0241: reserved keywords all lowercase (default Hidden).
- AA0248: add `this.` qualification (default Hidden).
- AA0477: `using` statements must be ordered (see [[14-namespaces]]); AA0247 (Info) pushes namespaces at all.

**Naming**
- AA0072 (Info): suffix variable/parameter names with type or object name.
- AA0073 / AA0237: temporary record vars prefixed `Temp`; non-temporary vars must NOT be.
- AA0074: `Label`/`TextConst` names need an approved suffix (Msg, Err, Tok, Lbl, Qst…).
- AA0100: no quoted identifiers.
- AA0215: general style-guide naming.
- Shadowing family — AA0198 (local vs global same name), AA0202 (local vs field/method/action in scope), AA0203 (method vs field/action), AA0204 (global vs field/method/action), AA0244 (parameter vs global), AA0245 (parameter vs field/method/action).

**Dead / wasted code**
- AA0136 unreachable code; AA0137 unused variables; AA0228 unused local method; AA0205 use before init; AA0206 assigned value never used; AA0150 `var` parameter never written; AA0194 actions with no effect; AA0249 PageField trigger dead because of a property value.

**Data access & performance** (cross-ref [[03-records-performance]])
- AA0175: don't `Find`/`Get` a record you never read.
- AA0181: `FindSet()`/`Find()` only when paired with `Next()`; AA0233: `Get()`, `FindFirst()`, `FindLast()` must NOT be followed by `Next()`.
- AA0210 (Info): filtering on non-indexed fields.
- AA0211: `CalcFields` only on FlowField or Blob (otherwise runtime error).
- AA0214: modify the in-memory record before writing it to the database.
- AA0222: no SIFT index on the primary/unique key.
- AA0232 (Info): index the fields a FlowField calculates over.
- AA0242: avoid partial-record JIT loads — select all fields you need up front.
- AA0475 (Error): `Truncate` only on normal tables with no Media fields, and not inside a TryFunction.

**Localizability** (cross-ref [[02-objects]])
- AA0216/AA0217: user-facing messages and errors come from Label/TextConst; no concatenation; `StrSubstNo` format string must be a constant.
- AA0131: parameter count must match placeholders; AA0470: each placeholder needs an explanatory comment.
- AA0231: don't pass `StrSubstNo(...)` or concatenation directly into `Error()` — build the label instead.
- AA0218/AA0219/AA0220: every page Field and Action needs a filled ToolTip; field tooltips should begin with "Specifies". AA0234 (Info): tooltips on table fields too.
- AA0225/AA0226: page fields need a filled Caption.
- AA0221/AA0223/AA0224: OptionCaption required and correctly counted when the source expression isn't a table field.
- AA0448: use `FieldCaption`/`TableCaption`, never `FieldName`/`TableName`, in user-facing text.
- AA0462: `CalcDate` takes a DateFormula variable, or a string wrapped in `<>`.
- AA0471–AA0474 (Info): Decimal fields on pages and tables need `AutoFormatType`; amount AutoFormatTypes need `AutoFormatExpression`.

**API objects** (cross-ref [[09-api-web]])
- AA0101–AA0104: camelCase for API page property values and field control names, and for API query property values and column names.
- AA0105 (Error): a PagePart must not point back at a parent page.
- AA0106 (Error): an API page may reference the same subpage only once.

**ApplicationArea**
- AA0189 valid values only; AA0199 correct ordering; AA0200 `All` must stand alone; AA0201 `Basic` must be paired with `Suite`.

**Permission sets**
- AA0050–AA0052: a permission set extension must not grant permissions for objects, permission sets, or transitively-included sets owned by another app.
- AA0053: no wildcard permissions in permission set extensions.
- AA0087: `Codeunit.Run` style permission lowering is test-only.

**Events, obsoletion, upgrade** (cross-ref [[07-events-errors]])
- AA0207: EventSubscriber methods must be `local`.
- AA0213: `ObsoleteState` must be Pending or Removed with an `ObsoleteReason` justification.
- AA0250–AA0252: external business events need an obsolete marker (Warning); marker without the obsolete attribute is an Error; moving an external business event to another app is an Error.
- AA0227: don't omit the optional return value in upgrade codeunits; AA0243: never call/run an upgrade codeunit from code.
- AA0235 (Info): if you use `OnInstallAppPerCompany`, also subscribe to `Company-Initialize::OnCompanyInitialize`.

**Misc**
- AA0139: don't assign text into a smaller-sized target (silent truncation).
- AA0161: `AssertError` only in test codeunits ([[13-testing]]).
- AA0230: no version on internal assembly references.
- AA0240: no email addresses or phone numbers anywhere in source.
- AA0246: blanket suppression of all diagnostics is not allowed.
- AA0476 (Error): invalid AI test configuration ([[12-agents-coding]]).

**Severity note** — most rules default to Warning. Errors: AA0105, AA0106, AA0251, AA0252, AA0475, AA0476. Info: AA0072, AA0210, AA0232, AA0234, AA0219, AA0247, AA0471–AA0474, AA0477. Hidden: AA0241, AA0248. Severity is overridable per-rule via a ruleset file.

Source: MS Learn "CodeCop Analyzer Rules", last updated 2026-03-11. Rule IDs and titles verified against that page; re-check severities after each BC release, they drift.

<!-- ingested: · PerTenantExtensionCop analyzer rules | 2026-08-16 -->
### PerTenantExtensionCop analyzer rules (PTE0001–PTE0026)

Analyzer enforcing constraints for per-tenant extensions (PTEs). Enable in `settings.json` / ruleset alongside CodeCop + AppSourceCop where relevant. Rule list as of 2025-09-02 docs snapshot.

| Id | Rule | Category | Default severity |
|----|------|----------|------------------|
| PTE0001 | Object ID must be in free range | Extensibility | Error |
| PTE0002 | Field ID must be in free range | Extensibility | Error |
| PTE0003 | No subscribing to CompanyOpen events | Extensibility | Error |
| PTE0004 | Table definitions need a matching permission set | Configuration | Error |
| PTE0005 | Compilation target must be one allowed in multi-tenant SaaS | Extensibility | Error |
| PTE0006 | Encryption key functions must not be invoked | Extensibility | Error |
| PTE0007 | Test assertion functions not allowed outside test context | Extensibility | Error |
| PTE0008 | Page controls/actions must set `ApplicationArea` | Extensibility | Error |
| PTE0009 | app.json property forbidden for PTEs | Extensibility | Error |
| PTE0010 | Extension name too long | Extensibility | Error |
| PTE0011 | Publisher name too long | Extensibility | Error |
| PTE0012 | `InternalsVisibleTo` is not a security feature | Extensibility | Warning |
| PTE0013 | Entitlements cannot be defined in an extension | Configuration | Error |
| PTE0014 | Permission sets should not be XML-based | Configuration | Warning |
| PTE0015 | Extension name not valid | Extensibility | Error |
| PTE0016 | Permission set ext must not include permissions for objects from another app | Extensibility | Warning |
| PTE0017 | Permission set ext must not include permission sets from another app | Extensibility | Warning |
| PTE0018 | Permission set ext must not include permission sets that cover another app's objects | Extensibility | Warning |
| PTE0019 | Permission set ext must not use wildcard permissions | Extensibility | Warning |
| PTE0020 | Use app.json `application` property instead of explicit Base Application dependency | Extensibility | Warning |
| PTE0021 | Reserved namespaces must not be defined | Configuration | Error |
| PTE0022 | Member ID should be within allowed range | Extensibility | Info |
| PTE0023 | Enum ordinal should be within allowed range | Extensibility | Info |
| PTE0024 | Moving tables/fields not allowed in a PTE | Extensibility | Error |
| PTE0025 | Avoid duplicate object names | Extensibility | Warning |
| PTE0026 | Table fields should use `AllowInCustomizations` | Extensibility | Hidden |

Practical takeaways:
- PTE object/field IDs live in the free (customer) range — 50000–99999 for the tenant range; PTE0001/PTE0002 fire outside it.
- Every table you define needs a permission set covering it (PTE0004); define permission sets as AL objects, not XML (PTE0014).
- Permission set extensions must stay inside your own app: no cross-app objects, no cross-app sets, no wildcards (PTE0016–PTE0019).
- Don't subscribe to CompanyOpen (PTE0003) — startup-path subscribers hurt tenant open time.
- Encryption-key APIs and `Assert`-style test helpers are blocked outside their proper context (PTE0006, PTE0007).
- Depend on the platform via app.json `application`, not a hardcoded Base Application `dependencies` entry (PTE0020).
- Table/field `Moved`-to another app is AppSource-only; unavailable in PTEs (PTE0024).
- `AllowInCustomizations` on table fields is Hidden by default — raise severity in the ruleset if you want it enforced (PTE0026).
- PTE0026 severity `Hidden` means no diagnostic surfaces unless a ruleset overrides it.

Source: MS Learn "PerTenantExtensionCop Analyzer Rules".

<!-- ingested: · UICop analyzer rules | 2026-08-16 -->
### UICop analyzer rules (Web Client extensions)

- UICop = analyzer enforcing Web Client rendering constraints. Enable alongside CodeCop/AppSourceCop/PTECop in `settings.json` `al.codeAnalyzers`. Rule ids `AW####`, category `WebClient`.
- Severity spread: mostly Warning; `AW0005`, `AW0006`, `AW0011` are Info; `AW0007` is the only Error.

| Id | Rule | Sev |
|---|---|---|
| AW0001 | XMLPort request pages not rendered by Web Client | Warning |
| AW0002 | Cue group with both actions and fields — only fields render | Warning |
| AW0003 | Repeater containing parts not supported | Warning |
| AW0004 | Blob cannot be a page field source expression | Warning |
| AW0005 | Actions should set `Image` | Info |
| AW0006 | Pages/reports need `UsageCategory` + `ApplicationArea` to be searchable | Info |
| AW0007 | Repeater containing FlowFilter fields not supported | **Error** |
| AW0008 | Repeaters only on page types `List`, `ListPart`, `Worksheet` | Warning |
| AW0009 | Blob subtype `Bitmap` on a page field deprecated — use `Media`/`MediaSet` | Warning |
| AW0010 | Repeater on a List page must be first in `area(Content)` | Warning |
| AW0011 | Set `PromotedOnly = true` so promoted actions don't duplicate in the default command bar section | Info |
| AW0012 | Teaching-tip properties unsupported in some contexts | Warning |
| AW0013 | Groups holding promoted actions must not be hidden | Warning |
| AW0014 | Groups holding `actionref` targets must not be hidden | Warning |
| AW0015 | Actions with `Scope = Repeater` must be promoted | Warning |
| AW0016 | Rich Text Editor field must be alone in its FastTab group | Warning |
| AW0017 | `MaskType` not allowed inside repeaters | Warning |

Design consequences worth remembering:
- Binary display on pages: `Media`/`MediaSet` only — Blob is out (AW0004/AW0009).
- List page layout is order-sensitive: repeater first in `area(Content)`, other controls after (AW0010).
- Hiding a group (`Visible = false`) silently kills the promoted actions / actionrefs inside it (AW0013/AW0014).
- Repeater restrictions cluster: no parts, no FlowFilter fields, no `MaskType`, only on List/ListPart/Worksheet.

Source: MS Learn "UICop Analyzer Rules" (updated 2025-08-08). Rule titles paraphrased; verify exact wording/severity against Learn or `--diagnostics` output.

<!-- ingested: · Using the code analysis tool | 2026-08-16 -->
### Enabling the code analysis tool (VS Code)

- Analyzers are part of AL Language extension; run in background as you type, plus full-project run on build (`Ctrl+Shift+B`), results in Output window.
- Settings (user or workspace `settings.json`):
  - `"al.enableCodeAnalysis": true` — master switch.
  - `"al.codeAnalyzers": [ ... ]` — comma-separated list; `Ctrl+Space` in the setting gives the pick list.
- Four shipped analyzers: `CodeCop` (official AL coding guidelines), `PerTenantExtensionCop` (PTE-only rules), `AppSourceCop` (Marketplace/AppSource submission rules), `UICop` (web client customization rules).
- Analyzer = library on top of the compiler, evaluating syntax + semantics at build time; violations surface as squiggles with hover text and in the Problems view.
- New project shortcut: `Alt+A, Alt+L`.
- Large projects: analysis cost is real — see Learn "Code analysis performance configuration" for tuning; ruleset files can also filter/re-severity rules.

### Example violation — AA0001 (CodeCop)

- Rule: exactly one space on each side of a binary operator (`:=`, `+`, `-`, `AND`, `OR`, `=`).
- `result := 2+2;` warns; `result := 2 + 2;` is clean.

<!-- ingested: · Ruleset for the code analysis tool | 2026-08-16 -->
### Ruleset files (`<name>.ruleset.json`)

- Custom ruleset file overrides severity of analyzer diagnostics. Filename must match `<name>.ruleset.json` for VS Code IntelliSense/schema.
- Snippets from AL Language extension: `truleset` (whole file), `trule` (single rule entry).

**Root object schema**

| Field | Mandatory | Type | Meaning |
|---|---|---|---|
| `name` | yes | string | Ruleset name |
| `description` | no | string | Doc-only |
| `generalAction` | no | `Error`\|`Warning`\|`Info`\|`Hidden` | Default action for every diagnostic that has no explicit rule, plus any rule set to `Default`. Included file with stricter `generalAction` wins |
| `includedRuleSets` | no | array | Chain other ruleset files |
| `enableExternalRulesets` | no | bool | Turns on/off use of ruleset pointed at by `al.ruleSetPath` |
| `rules` | no | array | Per-diagnostic actions |

**`includedRuleSets` entry**

- `path` (required): included in root ruleset → path relative to that file. Included from the file that `al.ruleSetPath` points to → absolute or relative to project folder. Edits to ruleset-path file apply to every project using it on save.
- `action` (required): `Error|Warning|Info|Hidden|None|Default` — applied to included diagnostics whose action is not `None`/`Hidden`.
- Processing order of included files is undefined — don't rely on precedence between two includes.

**`rules` entry**

- `id` (required): diagnostic code, e.g. `AA0001`.
- `action` (required): `Error|Warning|Info|Hidden|None`.
- `justification` field is accepted in practice (used in MS examples) though not listed in schema table.
- Gotcha: same `id` twice with different actions in one file is invalid.

**Example — escalate CodeCop rule to error**

```json
{
  "name": "Company ruleset",
  "description": "Baseline for all AL code",
  "rules": [
    { "id": "AA0001", "action": "Error", "justification": "Readability; non-negotiable." }
  ]
}
```

**Example — project ruleset extending a company one**

```json
{
  "name": "Personal Project ruleset",
  "includedRuleSets": [
    { "action": "Default", "path": "./company.ruleset.json" }
  ],
  "rules": [
    { "id": "AA0005", "action": "Info" }
  ]
}
```

- Referenced rules: `AA0001` = exactly one space each side of a binary operator (`:=`, `+`, `-`, `and`, `or`, `=`); `AA0005` = use `begin..end` only for compound statements. Both CodeCop.

<!-- ingested: · Using the code analysis tools with the ruleset | 2026-08-16 -->
### Rulesets — enabling analyzers & overriding severities

- Enable analysis in VS Code settings.json: `"al.enableCodeAnalysis": true`.
- Pick analyzers in `al.codeAnalyzers` (comma-separated list; Ctrl+Space completes). Values are AppSourceCop, CodeCop, PerTenantExtensionCop, UICop.
- Ruleset file: any name, convention `<name>.ruleset.json`. Point the project setting **Rule Set Path** (`al.ruleSetPath`) at it, path relative to project root.
- Minimal shape:

```json
{
  "name": "My Custom ruleset",
  "rules": [
    {
      "id": "AA0001",
      "action": "None"
    }
  ]
}
```

- `action` per rule sets the reported severity; `None` suppresses the diagnostic entirely.
- One ruleset applies to **all** analyzers enabled for the project — it cannot scope per-analyzer. Selective enabling is done via `al.codeAnalyzers`, not the ruleset.
- Snippets `truleset` and `trule` scaffold the file and a rule entry.

### Gotcha — ruleset changes not picked up

- AL Language extension does not watch the ruleset file. Edits to it have no effect until you force a reload:
  - reload the VS Code window, or
  - set Rule Set Path to a bogus path, save, set it back, save.
- Analysis runs in background; Ctrl+Shift+B forces a build/recompile.

### Example rule

- AA0001 (CodeCop): exactly one space each side of a binary operator (`:=`, `+`, `-`, `and`, `or`, `=`). `result := 2+2;` warns. AL Formatter fixes it automatically.

<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Newer AL language features (what's-new rollups)

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 10. Record Operations & Performance

### New AL language features (BC What's-new, mibuso 2026-07)
Source: auto-captions — identifier names garbled, verify against Microsoft Learn/compiler.

**Record / data ops**
- `Record.Truncate()` — deletes all records in current filter in one operation. No triggers fire (unlike `DeleteAll`). Use with caution.
- `CreateSequentialGuid` [sic? verify name] — returns GUIDs in sequential order to avoid clustered-index fragmentation from random GUID inserts.
- Lock-timeout method [sic? name unknown — verify] — set how long code waits for a lock before bailing. Persists until new session or reset to another value. Use with caution (session-scoped).
- DataTransfer: destination filter added — target only records not yet processed (e.g. re-runnable upgrades). `UpdateAuditFields` now works in cloud scope (was on-prem only); set `false` to preserve existing audit fields during transfer.

**Namespaces (see [[section-33]])**
- Namespaces now in object metadata — query/find all objects in a namespace (e.g. all Sales objects).
- Fully-qualified name (FQN) exposed as property on Record and RecordRef. Can persist FQN instead of table ID.
- Run codeunit / page / report by FQN (no numeric ID needed). Open RecordRef by FQN.
- RecordId can be formatted with FQN (namespace-agnostic form) as alternative to table name/caption; `Evaluate` parses FQN string back to RecordId.
- Get field value by field name (no need to resolve field ID first).

**Page / field properties**
- `MaskType` property [sic? verify] — masks display value but user can reveal via side icon on demand. Differs from `ExtendedDatatype = Masked` (only shows value while editing). For account/SSN etc. NOT for passwords — use encryption + hash instead.
- `ExtendedDatatype = Document` — for media fields; renders preview in portrait/document orientation.
- `AllowInCustomizations` gained `AsReadWrite` value [sic? verify] — field dragged onto page by user in customization becomes writable, not read-only. DataClassification gained `ToBeClassified` to mark unreviewed fields.
- `AutoFormatType` (not new) — new analyzer rules nudge devs to set it; also helps LLMs infer numeric format.
- Property to disable Copilot page summaries [sic? verify name] — summaries now synthesized on all card pages; turn off per-page in extension where not meaningful.

**JSON / text**
- JSON path queries — filter/select into JsonObject without iterating (e.g. array items matching a predicate).
- String methods added to text constants (previously only on Text).

**Analysis views in extensions**
- Analysis views now shippable from an extension (were client-only). Build in client, export definition to a file, reference file in AL object [sic? verify syntax]; don't hand-edit the exported file. Shipped view is read-only; users duplicate to customize.

<!-- ingested: Microsoft Presents: What's new in AL language - Enhancing Yo | 2026-07-26 -->

<!-- ingested: BC TechDays 2023 - What's new in AL | 2026-07-26 -->
### What's new in AL — BC TechDays 2023 (mibuso, Microsoft dev-tools team)

**Streams**
- `InStream` gained `Position` and `ResetPosition` methods — read/set the current position in a stream so you can re-read data. Verify exact names against Microsoft Learn [sic? caption-garbled].

**RecordRef**
- `RecordRef.SetTable(Rec)` lets a RecordRef and a Record point at the same underlying data, so both work on the same record in one context.

**Reports — render in a non-session language**
- Reports support a `format`/language region so a report renders in a chosen language/culture independent of the current session (e.g. session in Danish, output German). Look up the numeric language ID in the Language table. Verify property/region name against compiler [sic?].

**Records — read isolation**
- `ReadIsolation` property on records controls lock escalation (cross-ref existing Read isolation notes).

**Event publisher/subscriber identifiers (symbols, not strings)**
- Event references can be identifiers (symbols) rather than string literals. Unlocks VS Code navigation: CodeLens showing subscribers+publisher together, F12 go-to-publisher, find-all-references.
- Code action converts a string-based event reference to an identifier; can apply across document / project / workspace.

**Interfaces**
- "Go to Implementations" (right-click or Ctrl+F12) from an interface or an interface-typed variable lists all implementing objects.

**Inherent entitlements / permissions**
- `InherentEntitlements` and `InherentPermissions` properties let code assert license (entitlement) and permission from within the object, so business-critical processes run regardless of the calling user's permissions/entitlements. Verify exact property spelling [sic?].

**External business events**
- The only supported way to raise an event outside BC (older webhook look-alikes are deprecated in favor of this).
- Restrict who may subscribe by declaring a required permission on the external business event.
- Custom event categories by extending the event category enum.

**ErrorInfo actions**
- `ErrorInfo.AddAction(...)` adds a button invoking a codeunit method (e.g. to fix data); `AddNavigationAction(...)` adds a button opening a page/record (e.g. a setup page). Verify method names [sic?] (cross-ref ErrorInfo notes).

**Entitlements & AppSource licensing (public preview at time of talk)**
- Model per-plan licensing in AL: define permission sets that represent the *maximum* permissions per tier (e.g. Gold, Silver, trial/custom).
- Entitlement object with type `per user of a plan` [sic? verify keyword], `Id` = fully-qualified AppSource offer/plan name, mapped to the tier's permission set via object entitlements.
- Type `unlicensed` maps entitlements for users with no plan (usable for trial/custom-licensing gates, since platform has no native trial).
- GOTCHA: entitlements are *implicit* by default (uploading an app grants access to all its objects). Adding the **first** entitlement object to an extension disables the implicit entitlement — from then on only your declared entitlements apply.
- Check at runtime whether the signed-in user is entitled to a given entitlement set (e.g. an `IsEntitled`-style call) to branch Gold/Silver/unlicensed logic; combine with custom "call home" licensing for legacy models. Verify the API name against Microsoft Learn [sic?].

**Attached / regular debugger**
- Regular debugger can now attach to any existing user session (not just your own) and to the next session of a user — reaching parity with snapshot debugging, including service-to-service sessions with no interactive user.
- Attach via session ID (find via Help > support info) in the launch config; optionally scope to a user (debug fails if that user isn't the session owner).
- `breakOnNext` selects the session type (background / web service / web client) when attaching to a user's *next* session; not needed when attaching to a specific session ID.

**Code analyzer / tooling**
- New `backgroundCodeAnalysis` setting: `file`/`true` (default; analyze only active file), `project` (all files in active project), `none` (off). Applies per scope (folder / workspace / user settings). Workspaces <100 files run full analysis by default.
- `outputAnalyzerStatistics` prints per-rule run summary + time spent — use to find/disable slow or irrelevant rules during authoring (still run them in full build/CI).
- External ruleset URLs supported: via `al.ruleSetPath` + `enableExternalRulesets`, or `includeReSet`-style path parameter; also available as a compiler flag. Verify setting names [sic?].
- Additional package cache paths can be shared across projects (shared folder) to avoid re-downloading/copying dependencies.
- Control add-in resource paths (`Scripts`, `StyleSheets`, `Images`) accept wildcards instead of listing every file.
- Code actions to remove redundant `ApplicationArea` (moved to page level) and to promote it, scoped to document/project/workspace.

### More AL language features (What's-new, mibuso 2025-10)

- **`this` keyword** — self-reference. In a codeunit method that returns its own type (e.g. builder pattern), `exit(this)` returns the current instance. Also a scope qualifier: when a parameter/local shares a name with a global variable, prefix `this.` to refer to the global. Usable in codeunits, tables, pages; in a page procedure `this.Field` references a page's global field.
- **Builder pattern** now idiomatic: methods return `this` so calls chain (`.Method().Method()`).
- **Typed JSON getters** — `JsonObject.Get('prop').Get<Type>()`-style typed reads, e.g. `GetDateTime`, avoiding manual token→value→convert. Names garbled in captions — verify exact method names (`GetDateTime`/`GetText`/etc.) against compiler `[sic?]`.
  - Reading a missing property throws. New overload takes a boolean flag to return the type's **default value** instead of erroring when property absent — removes the guard `if Contains(...)` boilerplate. Verify exact signature `[sic?]`.
- **Interface inheritance** — `interface IDeadhead extends IPassenger` — an interface can extend another, adding methods / versioning.
- **`is` / `as` keywords for interfaces**:
  - `if Obj is IInterface then` — test whether an object implements an interface.
  - `Obj as IInterface` — cast to the interface. If the object does NOT implement it, casting throws — always test with `is` before `as`.
- **Collections of complex types** — `List` and `Dictionary` now support codeunits and interfaces as element types (e.g. `List of [Interface IPassenger]`). Previously hard/unsupported.
- **`continue` statement** — inside a loop, skips rest of current iteration, advances to next. (Also confirms loop control keyword available.)
- **Ternary operator** — inline `condition ? trueExpr : falseExpr`. Use sparingly; nested/complex cases hurt readability.
- **`ToText`** — added to most simple types for value→string. Overload with `InvariantFormat` boolean; `ToText(true)` == format `0, 9` (invariant/culture-independent) vs default culture format. Verify exact param name `[sic?]`.
- **Verbatim / multi-line strings** — `@'...'` (at-prefixed) preserves line feeds & special chars across lines; good for JSON/YAML templates with placeholder replacement. Can also live in resource files (`.json`/`.yaml`) loaded via NavApp resource read rather than inline.

<!-- ingested: AL complex types | 2026-08-16 -->
### Returning complex types from procedures (v18.0 / 2021 wave 1+)

- Since BC 2021 wave 1 (v18.0) procedures can return almost any type — user-defined (`Record`, `Codeunit`, enums) and most built-in types (`HttpClient`, `HttpResponseMessage`, `JsonObject`, …), not just simple scalars.
- Two forms:
  ```al
  // unnamed return type + exit()
  procedure GetCustomerByName(Name: Text): Record Customer
  var
      Customer: Record Customer;
  begin
      Customer.SetFilter(Name, '@' + Name + '*');
      Customer.FindFirst();
      exit(Customer);
  end;

  // named return value — no exit() needed
  procedure GetCustomerByName(Name: Text) Customer: Record Customer
  begin
      Customer.SetFilter(Name, '@' + Name + '*');
      Customer.FindFirst();
  end;
  ```
- Perf: `exit(X)` assigns X into the allocated return slot. `Record` is a value type, so that copy costs. Named return value writes the slot directly — prefer it for records and other heavy types.
- Returned value is a first-class expression; no intermediate variable required. Chaining works:
  ```al
  DoSomethingWithSales(GetCustomerByName('spo').GetSalesLCY());
  GetBingClient().Get('', Response);
  GetBingResponse().Content().ReadAs(Result);
  ```
- Pattern for built-in types — return a pre-configured client:
  ```al
  procedure GetBingClient() Result: HttpClient
  begin
      Result.SetBaseAddress('https://www.bing.com');
  end;
  ```
- Note `HttpResponseMessage.Content()` returns `HttpContent`; `ReadAs(Text)` on it fills the text. Method-call chaining on returned complex types is legal in the expression position.
- XML doc comments (`/// <summary>`, `<param name="…">`, `<returns>`) attach to procedures and surface in IntelliSense.

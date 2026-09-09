# designing-for-extensibility

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2018 - Designing for extensibility: Learn strai | 2026-07-27 -->
### designing-for-extensibility (NAV TechDays 2018, app architects)

**Per-tenant extensions**
- Extension Management page → **Upload Extension** deploys a local `.app` to a single tenant only, bypassing AppSource.
- Sandbox uses the least-restrictive check set (supports both AppSource and per-tenant dev), so a package can pass in sandbox but fail on production upload (e.g. missing ApplicationArea). Run the code analysers / AppSourceCop [sic? verify cop name] locally to catch prod-only checks.

**Extensibility surface (fall 2018 figures, indicative only)**
- ~2,760 integration events, but only in ~664 objects (~12% of ~5,800 objects).
- ~11,000 externally-callable procedures (SaaS-safe); ~2,200 more `external` methods planned next update, nearly completing removal of global non-external methods.
- ~50% of code lines / objects are `local` or `internal` → inaccessible.
- ~78-80% of objects have platform events (OnInsert etc.).
- Takeaway: blanket event coverage across tens of thousands of objects is not the intended long-term path.

**Componentization direction**
- Goal: base app split into versioned components (extensions) that can be extended, replaced, removed (can't remove if depended on), or added.
- Component rules: no code customization, no circular dependencies, extensible by design, ideally replaceable, small but valuable.
- A component's interface = a versioned contract, callable from inside and outside BC.
- Layer order being extracted bottom-up: separate app from platform (done, = removal of Codeunit 1) → **System layer** (in progress; wraps unsafe/platform bits safely, cannot be replaced, but open-sourced) → app foundation layer (horizontals) → financials → everything.
- Source to be published on GitHub for partner contribution.

**Extensible design patterns**
- Replace `throw error` default branches in `CASE`/StrMenu with an OnBefore/OnAfter integration event, so subscribers can add/remove menu options and handle new cases. Item Charge assignment distribution menu built this way: event passes the StrMenu string in (subscriber mutates it), then a second call passes back the selected option number for handling.
- Option/enum fields (e.g. Report Selections `Usage`) give compile-time validation but are hard to extend; enums ("modern AL" [sic? = AL enums]) are the recommended extensible replacement.
- Caption Class + dimension pattern: default-dimensions rows keyed by `Table ID` + main-entity key; transactions carry a `Dimension Set Entry No.`; posted entries point to same set. Caption class `1,<n>` resolves shortcut dimension n's caption via Codeunit "Caption Class Management" [sic? verify codeunit name].

**Upgrade code units — six triggers** (per-database and per-company variants of three):
- `OnCheckPreconditions` — fail-fast; detect fixable data problems in ms before running an expensive upgrade over millions of records.
- `OnUpgradePerDatabase` / `OnUpgradePerCompany` — the actual upgrade logic.
- `OnValidateUpgrade` — assert post-conditions still hold after ALL pieces upgraded (e.g. another extension didn't reset a base-table value you set). Of limited use for a single isolated extension.
- All three run inside one transaction; error → whole rollback. Hence push detectable failures into CheckPreconditions.
- Interwoven multi-extension upgrade: platform calls all CheckPreconditions first, then all upgrades, then all validates, in one transaction (subject to transaction-buffer size).

**Upgrade context APIs**
- Execution context option: `Normal` / `Install` / `Upgrade`.
- `Session.GetExecutionContext` [sic? verify] — whole-system state (any extension installing/upgrading).
- `GetCurrentModuleExecutionContext` [sic?] — is MY extension the one upgrading vs someone else.
- `GetModuleExecutionContext(moduleId)` [sic?] — state of a specific extension by app ID (from app.json).
- Common guard: if system is upgrading but my extension is not → exit (skip logic that would fire on every record during someone else's upgrade).
- Module API: `GetCurrentModuleInfo` / lookup by ID → id, name, publisher, versions, dependencies. Use `AppVersion` vs `DataVersion`: DataVersion=0 on first install; DataVersion=AppVersion on reinstall of same version; on upgrade, DataVersion = the version you're coming from (branch upgrade logic on it, e.g. 3→5 needs the 3→4 step that 4→5 skips).
- Attribute-based event-subscriber filtering by context was aspirational, not yet available — write the guard code manually.

**Upgrade gotchas**
- Versions need not be sequential: 1→3 allowed if the extension supports that path.
- Extension can be uninstalled before an upgrade is invoked.
- Table-extension companion tables get default values for every base-table row on install/upgrade; validate those defaults if the extension was absent for a while.
- `COMMIT` is ignored during upgrade (prevents half-committed state).
- Avoid external/web-service calls during upgrade (a network stall rolls the whole upgrade back); do them in a post-upgrade step. Keep upgrade minimal.
- No install/uninstall *code* trigger: uninstall code can't run after the object is removed, and a buggy error there would trap the extension unremovable.
- Multi-extension upgrades run in a fixed but unguaranteed order; dependency order IS respected (a dependency upgrades before its dependent).

**Schema change rules (table extensions)**
- Only additive changes. Cannot delete/rename fields or keys, cannot change data type. Cannot change existing indexes/keys — because multiple tenants with different extension versions can share one physical SQL table, so SQL schema = common denominator; differing indexes/fields would break table sharing. You CAN add new keys/indexes.
- Field removal: set `ObsoleteState = Pending` (values: Normal, Pending, Removed [sic? verify third]), add replacement fields, keep old field readable/writable and maintained for ≥1 major release. Then `ObsoleteState = Removed` blocks all access except read from upgrade code (so you can migrate values out). Actual physical/SQL removal not yet supported — on backlog.

**Replacement / show-my-code (source access)**
- Depend on another partner's app: add its app ID to `dependencies` in app.json; downloading symbols pulls their metadata (tables, fields, pages/controls, global code-unit signatures).
- `showMyCode` (app.json boolean) controls whether others can step into / F12 your actual code; false → they see declarations only. Requested improvement: make it a per-object/table/codeunit property (e.g. hide only a licensing codeunit) rather than all-or-nothing.
- Long-term replacement vision needs each component to publish a strong contract (extend points + required-provide surface), analogous to implementing an interface (cf. C#).

**Localizations**
- Microsoft W1 + growing MS localizations; 10 partner-built localizations went live (2018). Partner localization onboarding via the "get started with apps" AppSource docs/contact link.

**Misc**
- Translation: `.xlf` file covers Label-tagged captions/labels; text constants use the `Label` datatype and are picked up via that label reference.
- Extension memory cost is negligible at runtime (objects indistinguishable from C/SIDE once loaded); very large extensions (~2–4k+ objects) had deploy/compile perf issues, fix targeted for spring release.
- Report extensions (extend the dataset, not just layout) requested, not yet implemented (2018); layout replacement + Custom Report Layouts available.
- AppSource paid/billing model: dependent on the AppStore team, repeatedly "6 months out" — not owned by the BC app team.
- Resources: dev tools + `Open CIL Library` [sic? verify name] GitHub repos; base-app AL extensions being published for viewing/contribution; "extension requirements" and "ready to go" program docs.

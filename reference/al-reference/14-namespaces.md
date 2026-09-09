<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Namespaces & `using`

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 33. Namespaces & `using`

Introduced 2023w2. Declare `namespace` as the **first non-comment line**; one namespace per file,
covering all objects; nestable; identifiers must be CLS-compliant (start with a letter/underscore).
```al
namespace MyCompany.Sales.Documents;

using MyCompany.Foundation;          // bring another namespace into scope (right after the decl)
using System.Utilities;

codeunit 50120 OrderProcessor { }
```
Resolution: your own namespace first, then `using` directives; otherwise **fully-qualify** to
disambiguate (records/recordrefs expose a runtime `FullyQualifiedName`; `Codeunit.Run`, page/report
`Run`, `RecordRef.Open` accept FQN string literals — 2026w1). The add-namespace code action derives a
name from `namespaceTemplate` in settings.json (`${parentFolder}` placeholder) → longest common prefix
of sibling files → `Publisher.ProjectName`.

GOTCHAs (also AL-KNOWLEDGE §3):
- **Do not namespace your own code until ALL dependencies are namespaced** — references break when a
  dependency later adds namespaces.
- Renaming a namespace or moving an object between namespaces is a **breaking change**.
- Never use `System`, `Microsoft`, `Utility`, `Common` as your root — use your own company root.

<!-- ingested: Microsoft Presents: What you always wanted to know about AL | 2026-07-26 -->
### Namespaces — deeper notes (mibuso 2024-06, BC engineering)

- `namespace X.Y.Z;` = first statement in file. No curly braces; covers all objects in file. Recommend one object per file.
- Nest with dots. Name must be CLS-compliant: case-insensitive, no quoting, no spaces/emojis. Can't be renamed without breaking change.
- Same namespace reusable across multiple files and multiple apps — your choice.
- Object in a namespace auto-sees other objects in same namespace. Pull in others two ways:
  - `using X.Y;` — imports ALL objects of that namespace into file scope. Order-independent; placement doesn't matter.
  - Fully-qualified name in var declaration (e.g. `Item: Record Microsoft.Inventory.Item`) — targets one specific object, no bulk import. Reduces ambiguity but doesn't eliminate clash risk.
- Adopting namespaces = opt-in per object. Introducing a namespace onto an object is NOT a breaking change. Renaming/changing an existing namespace IS a breaking change (fully-qualified name is part of object identity).
- VS Code code actions: fix single missing reference (qualify or add using), or bulk "fix all missing using statements" at document / project / workspace level. Retyping an object name auto-adds the using and lets you pick source when names collide.
- Object Explorer (`AL Explorer` [sic? "IL Explorer" in captions — verify]) groups by type/namespace to find which object you actually want when duplicates exist.
- Collapse long using blocks: editor setting `folding import by default` [sic? verify exact setting id] folds imports on file open.

### Namespace restrictions & runtime facts

- Only ONE object of a given kind with a given name allowed per module — regardless of namespace.
- Only ONE object of a given kind with a given name allowed per namespace. Collisions still force a rename, same as today.
- Namespaces have ZERO runtime impact — purely for discovery/organization/dependency analysis. No effect on extension objects or behaviour.
- Object IDs still required; namespaces do not replace IDs.
- 30-char object name limit still applies (namespace does not lift it).
- AppSource affix/prefix (AIX) registration still required for now. Goal: eventually drop it for top-level objects (tables/pages) first, then fields/controls. Not there yet.
- No plan (as of 2024) to make namespaces mandatory, or to add a default-namespace `app.json` property — Microsoft wants namespace choices explicit.
- No partial-qualification / `using X.*` alias syntax planned; long using blocks are intended as a signal to reconsider dependency design.

### Table-extension field namespacing (gotcha)

- A field can be split out of a base table into a table extension in the SAME app and placed in a different namespace (logical grouping by feature).
- BUT field-level namespacing is NOT implemented. When referencing a table you namespace the base TABLE (its origin namespace); the extension's fields are not separately namespace-referenceable in code yet.

### Namespace design guidance

- Avoid generic top-level names (e.g. bare `Sales`) — high collision risk.
- Prefix with company/product; company names not globally unique, may need further qualification. Microsoft Learn recommends `Company.Product.Technology.Feature.SubFeature`.
- Don't reuse another party's namespace even when extending their (ISV/base) object — use your own; their future objects may clash.
- Microsoft internal convention: `Microsoft` as default root; max 3 levels deep (e.g. `Microsoft.General Ledger.VAT.Calculation` [sic? spacing/exact segment names from captions — verify]).
- Design principle: dependencies point DOWN the layer stack, not up (e.g. GL/journal posting must not reference Sales/Manufacturing/Service objects). Search `microsoft.<area>` across a folder to audit cross-namespace leakage.
- Namespace-first refactor pattern: namespace WITHOUT refactoring first to snapshot current structure, then analyze dependencies, then refactor. Enables source-document-agnostic frameworks (reservation, availability) via interfaces + event subscribers instead of large `case`-over-document-type statements.

<!-- ingested: Making Sense of Namespaces in Business Central (mibuso / BC TechDays 2026, Jan Lemke / CTM) | 2026-08-05 -->
### Namespace ADOPTION as an architecture exercise (practitioner methodology)

Core message: writing `namespace` + `using` is trivial; the real work is deciding **domain structure
first**. Adopting namespaces forces architecture decisions you were previously getting away without.
A well-structured domain also gives an AI coding assistant the context to work in the right folder
instead of burning tokens across the whole app. (Anecdote: Claude Opus [sic? "Claude Opus"] generated
a table relation to the wrong `attendee` — it silently resolved to `microsoft.crm.task.attendee`
[sic? exact MS namespace] because the code had no namespaces to disambiguate. Namespaces would have
made the collision a compile error, "removing the bug's hiding place".)

**Decision framework (one worked blueprint, not "the" right way):**
1. **Identify domains + master entities before opening VS Code.** A master entity = the record a
   document cannot be posted without (sales analogue: Customer). E.g. session→Speaker,
   registration→Attendee, sponsorship→Sponsor. Not every domain has a master entity — then treat it
   as a feature/area. A domain is "a boundary where the vocabulary changes".
2. **Feature-map each domain** (e.g. session: submit-proposal, review-submission, register-session).
3. **Feature-internal folder layout:** one folder per feature; **master entity lives in the feature
   root folder** (no sub-folder for it); Microsoft-style subfolders `document` / `history` / `posting`
   for the rest. Define this pattern once, every feature follows it.
4. **Granularity — ONE namespace per FEATURE folder, NOT per subfolder.** Subfolders are file
   organization only, never namespaces. Rationale: objects in the same feature belong together, so a
   posting codeunit shouldn't need a `using` to reach its own feature's master entity. A `using`
   appears **only when you cross a feature boundary** — "fewer usings ⇒ better architecture".
5. **Dependency direction is the crux.** Layer the app: `foundation` (level 0 — shared master data,
   event table, number series, config) at the bottom; business domains (session/registration/
   sponsorship) at level 1. **Dependencies point UP only** (domain→foundation), **never sideways**
   (domain→domain), **never down** (foundation→domain). This makes circular dependencies structurally
   impossible. Audit leakage by searching `<publisher>.<otherdomain>` usings across a feature folder.
6. **Object IDs:** allocate sequentially per type; do NOT reserve per-module ID ranges or leave gaps —
   the **namespace** carries feature identity now, not the ID range. (Old-NAV habit to drop.)
7. **Naming:** `Publisher.Product.Feature` (3 segments; Microsoft says use ≥2). Feature segment
   **matches the folder name**, as Microsoft's base app does.
8. **`namespaceTemplate` in the workspace settings**, e.g. `CTM.communityhub.${parentFolder}` [sic?
   placeholder name — cf. §33 `${parentFolder}`], so the Ctrl+. code action auto-fills. Caution: with
   nested/sub-parent folders it derives a different (wrong) namespace — check the result.

**Cross-cutting concerns get their own namespace but are NOT a business domain:** `foundation`
(shared master data), `import` (demo/seed data, writes-all-temporarily), `rolecenter` (reads all,
owns nothing), `permissions` (no business logic). Kept out of the level-1 domains.

**Three design patterns from the talk:**
- **Root-level abstraction extraction.** Repeated subfolders across features (posting/history/document
  everywhere) signal an abstraction layer. Extract e.g. `interface IPostingHandler` [sic? name] into a
  **cross-cutting root-folder namespace** `Publisher.Product.Posting`. The abstraction knows nothing
  about the features (no usings to session/registration); each domain codeunit gets
  `using Publisher.Product.Posting;`, making the dependency explicit and visible.
- **Mirror namespace for base-app extensions.** When extending Microsoft objects, mirror their
  namespace under your publisher: `microsoft.sales.document` → `ctm.sales.document`, with the folder
  sitting **outside** your product segment (it's a cross-product extension). Reuses MS's own structure
  so it's familiar; **never declare the Microsoft namespace yourself**. Use only when the extension is
  tightly coupled to the MS module.
- **Domain-owned setup extension.** Adding a domain's setup field to a global foundation setup table
  creates a wrong-direction dependency (foundation→domain). Instead the domain adds a **tableextension
  on the foundation setup table under the domain's OWN namespace** — keeps flow upward. Caveat: because
  field-level namespacing isn't implemented (see below), those fields are still reachable cross-domain
  with **no** `using`; keep field-name affixes as protection until MS closes the gap.

**Workflow:** plan architecture → write it down (e.g. `docs/architecture.md` + `docs/structure.md`,
one holding decisions, one summarizing structure) BEFORE coding or prompting Copilot — Copilot won't
invent a domain structure on its own. Refactor in steps: (1) move files into domain/subfolders with
**no** namespaces first, to feel out the domains; (2) add namespaces via the code action; (3) apply
the patterns. Microsoft is said to be providing a **PowerShell script** (CSV mapping → moves files +
stamps namespaces) to assist bulk migration — not a documentation tool.

**Breaking-change nuances (reinforces §33):** adding a namespace to an existing object is NOT breaking;
renaming/moving one IS (AppSource) — speaker tested a rename, it *compiled* fine but is still breaking
per MS docs. Do NOT strip affixes just because you adopted namespaces — removing an object-name affix
needs a full obsolete cycle; affixes on **fields/controls/procedures stay mandatory**. Object-name
affix may be omitted only when the top-level namespace equals your registered affix/reserved prefix.
CodeCop `AA0247` [sic? captions said "247"] now warns "use namespaces to organize your code and isolate
it from changes" (from ~runtime 17 / v23+); some teams suppress it. 30-char name limit and required
IDs both still apply. Per-domain **event-subscriber** codeunits recommended (don't group all
subscribers into one sales/purchase codeunit — split by domain).

<!-- ingested: NAV TechDays 2019 - The road from C/AL to AL | 2026-07-26 -->
### C/AL → AL conversion + early AL language facts (NAV TechDays 2019, MS dev-tools team)

**txt2al conversion pipeline (historical, but explains legacy-origin quirks):**
- Path: technical-upgrade to latest platform → `Export-NAVApplicationObject` with **new-syntax** switch (or FinSQL `Export to new syntax`) → run `txt2al` (source folder + target folder). New-syntax txt has: culture-invariant date/time literals, object refs by **name** not id, `YES`/`NO` → `true`/`false`, keyword/method casing normalized to AL guidelines, generated unique names for all controls/actions (AL requires names on everything).
- `txt2al` runtime param maps to app.json `runtime`; that number = BC info-page version minus 11.
- **DotNet decls**: C/AL declared full qualified type per var; AL centralizes as aliased dotnet declarations. Use txt2al **dotnet type-prefix** option to prefix generated aliases and avoid collisions with imported modules (e.g. two different `XmlDocument`).
- **Control add-ins**: no type info in C/AL, so txt2al needs `--dotNetAddInsPackage` [sic? verify flag name] pointing to an `.al`/config file declaring the dotnet type (assembly + type implementing the add-in, e.g. `IWebPageViewer` [sic?]) marked as control add-in.
- Requires `al.packageCachePath` pointing at **System app** (the `System` symbol package, not System Application) + `al.assemblyProbingPaths` for dotnet assemblies.
- Recommendation: fix compiler-found errors back in C/AL first so existing customers benefit before cutover.

**AL compiler strictness vs C/AL (durable — these are real compile errors):**
- Duplicate `case` branches → error (C/AL silently ran first, ignored rest).
- References to missing objects (e.g. action pointing at deleted page, `Permissions` on removed table) → compile error, not runtime failure.
- Stricter DotNet type-conversion / typecast checking; mismatched types that shared one method in C/AL now error.
- **Symbol resolution is innermost-scope-outward and explicit** (C/AL was ad-hoc). Means a new platform method `Foo` won't shadow/break your own `Foo`.
- `WithEvents` cleanup: leftover event-stub code from a var whose WithEvents was toggled off comes across and errors (var lacks WithEvents attribute).
- Copy-pasted properties invalid in new field context error (e.g. `OptionCaption` on a `Text` field, stray `DecimalPlaces`) — delete them.
- **Event subscriber signature must match publisher exactly.** Attribute-bound handlers (e.g. HyperlinkHandler [sic?], test handlers) must match runtime-exposed signature. `HandlerFunctions` names must exist in the object.
- Report columns: reserved auto-generated `<Column>Format` companion column name → rename required.
- Option `::` numeric-value trick unsupported in AL — must use real enum/option identifiers.
- Identifier length capped at **120 chars** (needed for reflection via virtual tables). C/AL auto-generated long label names from label text → rename.
- `DataCaptionExpression` is Text; C/AL inserted implicit ToString for date/other types — AL requires explicit.
- Test-only attributes used outside test context → remove.

**Access modifiers (`Access` property):**
- On objects: `Public` (default) or `Internal` (only within the app/module).
- On fields/procedures: `Local`, `Internal`, `Protected` (accessible within module incl. its table-/page-extensions), plus public default.
- `Extensible` property (bool) on **tables, pages, enums** — controls whether other apps can extend it. Design extensibility deliberately: pair with events/interfaces when true.

**Facade pattern (System Application convention):** public code unit = documented facade (XML doc comments) forwarding to an `...Impl` code unit marked `Access = Internal`. Consumers call facade only.

**Interfaces + enums (introduced this wave):**
- Interface holds method signatures only — no code, no fields, no inheritance.
- A code unit can implement **multiple** interfaces (`implements A, B`).
- Enum value points to an interface implementation; casting an enum field to the interface type dispatches to that value's impl. Extensibility pattern: base enum has default value(s), `enumextension` adds a value + its interface implementation. Compiler forces the extender to supply the implementation.
- Enum can declare a **default interface implementation** used when a value doesn't specify one.

**Obsoletion:** `ObsoleteState`/`ObsoleteReason`/`ObsoleteTag` attributes on objects, extensible elements, procedures, variables → consumers get compile warning `X is marked for removal`. Obsoleted table fields dropped from SQL schema but retained in DB (this wave).

**Isolated Storage (data isolation per extension):**
- Simple Set/Get API; supports encrypted store and existence check.
- `DataScope` enum adds scoping on top of per-extension isolation: `User`, `Company`, `CompanyAndUser` [sic? verify member names] — restricts retrieval to current user/company. Data always isolated to the extension regardless of scope.
- Pattern for setup pages holding secrets: do **not** base the page on a table; use text global vars bound to fields, persist into Isolated Storage. Store external-service creds (e.g. Key Vault service-principal) there, never hard-coded.

**IP protection:**
- `showMyCode` in app.json (default **false**). True lets dependent apps load symbols + step into/debug your AL. `.app` is a zip archive containing AL source — to distribute without source, build a **runtime package** (only compiled runtime code, requires showMyCode=false).
- `[NonDebuggable]` attribute on a procedure/variable hides it from the debugger even when code is shared — protects secret-handling code.

**VS Code perf knobs:** disable code analysis / CodeLens / code actions, or enable incremental build (reuses in-memory state) to trade IntelliSense features for responsiveness.

**Profiles as AL objects:** `Description` = dev comment; `Caption`/`CaptionML` = translatable displayed name; plus enabled/disabled-by-default and `Promoted` (shows in role-center explorer). Toggling enabled in web client writes an override on top.

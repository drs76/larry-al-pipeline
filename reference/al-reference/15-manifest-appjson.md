<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# app.json manifest & project config

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: Microsoft Learn — JSON files (devenv-json-files) | 2026-08-16 -->
## app.json manifest settings

Source: Microsoft Learn *JSON files*, doc updated 2026-04-01.

Two JSON files auto-generated on new AL project: `app.json` (manifest) and `launch.json`. `rad.json` and `snapshots.json` must not be hand-edited. Data migration uses a separate `migration.json`.

**Identity (mandatory)**
- `id` — GUID. Bound at runtime to table names in the app. Changing it orphans existing table data.
- `name`, `publisher` — used by dependents to express compile-time dependency. Changing either forces dependents to re-download symbols and recompile.
- `version` — package version. Bump it whenever `name` changes.

**Dependency resolution**
- `dependencies`: array of `{id, name, publisher, version}`. Version given is the *minimum*; symbol download and runtime both resolve to the latest matching name+publisher at or above it.
- On runtime 4.0 and earlier the key is `appId`, not `id`.
- System Application / Base Application are NOT listed in `dependencies` — expressed via `application` (version of `Microsoft_Application_*.app`). `platform` gives the min version of `Microsoft_System_*.app`, mandatory if any system object is referenced.
- On-prem code-customised base app: keep `"name": "Application"`, publisher and file name may change.
- `propagateDependencies` (default false): if B sets true, consumers of B can use types from B's dependencies without declaring them. All-or-nothing — no per-dependency exclusion.
- `alternateIds`: list of app IDs this app replaces (base-app replacement scenario).

**Object IDs**
- Use `idRange` `{from,to}` OR `idRanges` `[{from,to},…]` — one or the other, not both. Objects outside range = compile error. Overlapping entries in `idRanges` = compile error.

**Compilation / runtime**
- `runtime`: 13.0 = BC 2024w1, 14.0 = 2024w2, 15.0 = 2025w1, 16.0 = 2025w2. Omitted ⇒ compiler picks highest available major. App publishes to servers at that runtime or higher.
- `target`: `Cloud` (default) or `OnPrem`. OnPrem unlocks restricted APIs + .NET Interop, and the server must also be set to OnPrem. System tables with `Scope = Internal/OnPrem` are unreachable from a Cloud-target app — including via RecordRef, not just direct reference.
- `preprocessorSymbols`: e.g. `["DEBUG","PROD"]`, consumed by preprocessor directives.
- `suppressWarnings`: array of analyzer IDs, e.g. `["AL0458"]`. Per-region alternative is `#pragma warning`.
- `internalsVisibleTo`: `[{id,name,publisher}]` — grants other modules access to `Access = Internal` objects. Triggers an AppSourceCop/PTECop warning on BC online; `Access = Internal` is an API-surface tool, not a security boundary.

**features flags**
- `"features": ["TranslationFile", "GenerateCaptions", "GenerateLockedTranslations"]`
  - `TranslationFile` — emits `\Translations\*.xlf` with labels, label properties, report labels.
  - `GenerateCaptions` — requires TranslationFile; synthesises captions for objects lacking Caption/CaptionML.
  - `GenerateLockedTranslations` — emits `<trans-unit>` for locked labels.
  - `NoImplicitWith` — turns ImplicitWith off by default; use once all code is with-free.

**Ops / packaging**
- `applicationInsightsConnectionString` — App Insights resource for telemetry (recommended for AppSource).
- `keyVaultUrls` — array of vault URLs the app may read secrets from; all must be in the same Entra tenant.
- `resourceExposurePolicy` — four booleans, all default false: `applyToDevExtension`, `allowDebugging`, `allowDownloadingSource`, `includeSourceInSymbolFile`.
- `resourceFolders` — folders whose contents get packaged as resources.
- `source` `{repositoryUrl, commit}` and `build` `{by, url}` — build provenance. Both can be overridden by `alc.exe` command-line parameters, which win over the app.json values.
- `test` — test-framework version `X.Y.U.Z`; only meaningful on BC 14 and earlier (C/AL base app).

**AppSource-only fields** (optional for compile, required to submit): `brief`, `description`, `privacyStatement`, `EULA`, `help`, `url`, `logo`, `screenshots`, `application`, `contextSensitiveHelpUrl`.
- Help URLs: `contextSensitiveHelpUrl` for the app's own docs site; `helpBaseUrl` overrides *all* help for given locales (localisation apps only). Both need `supportedLocales` (e.g. `["da-DK","en-US"]`, first is default) when the URL carries a `/{0}/` locale placeholder.

<!-- ingested: FAQ for developing in AL | 2026-08-16 -->
### AL developer FAQ — symbols, sandboxes, telemetry, menusuites

- **Symbol versions mismatch tenant.** Symbol download always pulls highest *published* version of dependency, not version installed on your environment. Expect downloaded symbols to be newer than what runs on the tenant.
- **VS Code / Designer publishes are volatile on sandboxes.** Extensions published from VS Code or created via Designer are dropped when a sandbox environment updates or is relocated. Data of the app survives — republish + install to restore. PTEs that depend on such an extension are removed too.
- **Partner telemetry:** set `applicationInsightsConnectionString` in `app.json` to receive it. Event ID `LC0105` records reason for environment update/relocation.
- **AL Language extension version:** cloud sandboxes require official Marketplace release (not pre-release/insider builds).
- **App identity** is a fixed set of `app.json` settings that must not change across versions; changing them makes it a different app (relevant to upgrade + AppSource submission, which validates against the Technical Validation Checklist).
- **No Menusuite object in AL.** Replace its two jobs separately:
  - Searchability — page/report properties that add objects to Search (Tell Me).
  - Navigation — extend the Navigation Pane page, and/or add Actions to existing pages used as entry points.

# Migrating customers to the cloud — strategy and leverage

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2019 - Migrate your customers to the cloud, and | 2026-07-27 -->

<!-- ingested: NAV TechDays 2019 - Leveraging the power of the cloud | 2026-07-27 -->
### Leveraging Azure cloud services from BC (NAV TechDays 2019)

- Sample code lives on GitHub `microsoft/BCTech` [sic? verify org/repo]; blog index at `aka.ms/bctech`. All prototype quality, not productized. Most techniques work on-prem too, not just cloud.

**Shared-key auth (service-to-service REST)**
- Client + service share a secret key. Client signs parts of the request (URI/resource, timestamp/TTL) with the key; server looks up key by name (carried in request) and verifies signature.
- TTL limits replay to the identical request. Used by Azure Service Bus and Blob Storage (each signs slightly differently, same principle).
- Header form: `Authorization: SharedAccessSignature ...` [sic? verify exact scheme name] — awkward to compute in AL, so use the published wrapper codeunits.

**Azure Blob Storage as file replacement**
- `File` type removed in cloud. A blob is just a byte stream; directory/folder view is a UI convention on top, not real structure. Rethink data organisation rather than mimicking DOS directories.
- GitHub sample = AL wrapper codeunit over Blob Storage REST (shared-key): put/get/list/delete blob [sic? verify method names]. Upload via built-in `UploadIntoStream` then `PutBlob`; helper derives MIME/content-type from file extension.
- Configured via standard Service Connection setup page.

**Azure Functions for removed .NET interop**
- Cloud blocks arbitrary .NET assemblies. Externalise that logic to an Azure Function (serverless), call it over HTTP from AL.
- Pattern: base64-encode payload in AL, POST to function, decode response. Demo = image→monochrome conversion using an external C# library.

**Service Bus Relay — bridge cloud to on-prem hardware**
- For local devices with no internet (barcode scanners, scales, payment terminals, robots). Browser sandbox can't touch local resources; `RunOnClient`/.NET-local execution gone.
- Azure Service Bus Relay links two networks through the firewall: an on-prem listener + a cloud sender communicate HTTP-style.
- Framework (GitHub) = local agent (runs as CLI or Windows service) that hosts C# (or any .NET) plugins; matching BC extension calls them. Flow: AL extension → framework code → Service Bus Relay → local agent → plugin → response back.
- Plugin/extension pairing: plugin declares relative endpoint; AL side declares HTTP method (GET etc.) + params (params can be on URL, framework unpacks and marshals to the C# method). Consume like `Calculator.Add(...)`.
- Not shipped/maintained by Microsoft; grab and own it. Can bridge to local printers, Bluetooth devices, anything reachable locally.

**IoT Central (for connected devices)**
- For hardware that CAN reach internet (sensors, thermostats). Managed layer over IoT Hub + device registration — infra hidden.
- Device sends telemetry; IoT Central rules fire actions: email, webhook/URL, Azure Function, Logic App, Power Automate, Azure Monitor action groups.
- Concepts: device template (telemetry + settings + properties + commands + rules); settings/commands are cloud→device (two-way), e.g. change telemetry interval, reset scale to zero; properties = device metadata/state.
- Sample device code (ESP8266 [sic? verify] etc.) published by IoT Central team on GitHub. Connect with scope ID + device ID + key. Simulated devices auto-created from a template — test integrations with no hardware.
- Continuous export: push device/telemetry data to Blob Storage, Event Hub, or Service Bus. Demo pushes device list to Service Bus → Logic App → BC custom API, auto-provisioning devices in BC.

**OAuth via Logic Apps (reusable)**
- Auth handled by a dedicated Logic App: pulls refresh token + client secret from Azure Key Vault, POSTs to token endpoint, gets new access + refresh token, stores new refresh token back in Key Vault, returns access token to caller. Reusable across all BC connections.
- Logic App actions can be marked to hide input/output (secret masking) so users with run-history (read) access never see secrets, only editors do.

**Cognitive Services — Computer Vision**
- Recognise printed + handwritten text (OCR). Also image analysis, describe, face/celebrity recognition, content moderation (adult/racy flags).
- Handwriting recognition is async: POST image, get back a result URL, then poll/wait until result ready, then read JSON. All done with plain AL types + JSON API (no .NET).
- JSON result: text broken into lines then words, each with confidence and a bounding box (full coordinate set — supports skewed/angled text).
- Demo: OCR filled-in questionnaire handouts; ticked boxes come back as literal text `x`, so find the question with an `x` to its right. Fragile on small checkboxes — enlarge boxes / instruct users.
- Form Recognizer (preview, US only at time of talk) does key-value pair extraction on invoices/receipts.

**Cognitive Services — Translator Text (extension translation)**
- Add `"features": ["TranslationFile"]` [sic? verify exact keyword] to app.json → compiler generates an XLIFF (`.xlf`) file under a `Translation` folder. XLIFF = international XML translation standard; contains `<source>` per unit, add `<target>` with translated string.
- Translator Text API: POST source-lang + target-lang + JSON of strings → JSON of translations. Recipe: generate XLIFF → extract strings → call API → write targets back.
- Author provided a VS Code extension (TypeScript, GitHub) that automates the round-trip and fills XLIFF targets.
- Out-of-box model = generic; poor on ERP-specific terms. Train a custom model on your existing domain translations for much better quality; little training data needed.

**Application Insights telemetry**
- Three telemetry categories: monitoring/alerting (what's happening now), diagnostics/troubleshooting (what happened), usage (which features used, how often).
- Key cloud advantage over file logging: aggregate + correlate across many tenants/sites.
- Five SDK emission types (function names): `TrackPageView`, `TrackTrace` (diagnostic text), `TrackEvent` (message + metrics for graphs), `TrackException`, `TrackMetric`/`TrackDependency` (metrics; dependency = external calls, separates own vs external time) [sic? verify exact SDK names].
- Emit from AL by HTTP POST of a JSON object to the App Insights endpoint using the instrumentation key. Fire-and-forget — small payload, response ignored. GitHub SDK wraps the first four types for AL.
- From BC v15+: bring your own App Insights key, configured in tenant admin center. v15 emits long-running-query telemetry only; report execution time + OData usage planned later. Same key as your extension telemetry → correlate platform + app events.
- Alerts: pick resource → condition (signal below/above threshold, error count) → action (email/SMS).
- **GDPR**: telemetry is subject to GDPR — do not emit PII (names, addresses, emails).

**Pricing (2019 indicative)**
- App Insights: free up to 5 GB. Translator: 2M chars/month free, ~€8 per extra million; custom trained model pricier. Vision OCR: ~€1–2 per 1000 transactions. IoT Central: 5 devices free, ~€1–2/device/month. Service Bus: ~€0.043 per million operations. Logic Apps/Key Vault/Blob very cheap. Exact figures via Azure pricing calculator.

### BC on-prem to cloud migration (NAV TechDays 2019, BC15 era)

- End state in cloud: everything AL, no CAL. Every table lives in an app — system app, base app, 0+ AppSource apps, plus per-tenant extension (PTE) for customer-specific changes.
- Cloud DB schema is defined by installed apps. To migrate data, on-prem schema must match cloud schema: install the *exact same apps* on-prem (base, system, ISV apps, PTE) so schemas are identical, then replicate.
- Migration path from NAV 2018: (1) while still on NAV 2018, refactor to extract customizations into separate objects, keep modified base objects close to original; (2) upgrade to BC15 (includes CAL→AL conversion + data upgrade); (3) final extraction to pure extensions using events/extensibility. Can sit in intermediate state indefinitely before upgrading.

### Cloud migration data replication (intelligent cloud)

- Requirements: cloud env has Intelligent Cloud Base extension installed (default on new envs). Setup user needs SUPER permissions. On-prem must be BC15, DB compat level ≥130 (SQL Server 2016+), DB <150 GB (recommended <80 GB).
- Data migrated is determined by extensions installed in cloud. Extensions on-prem but not in cloud → their data not migrated (shown as warnings). Tables can opt out via `ReplicateData` property = false in AL.
- Assisted setup wizard: pick source (BC→BC), supply on-prem SQL connection string (need not be externally reachable), configure a self-hosted integration runtime (download + register with auth key), pick companies, optional daily/weekly schedule.
- Architecture: cloud service uses Azure Data Factory to orchestrate. ADF does NOT call into on-prem — it queues instructions; the self-hosted integration runtime polls the queue and pulls work (outbound only, firewall-friendly). Data moves SQL→SQL, not stored elsewhere. Credentials encrypted (Windows secure encryption). On-prem existing tables/data untouched, but migration creates helper tables + runs stored procedures to stage data.
- One integration runtime can serve multiple DBs on the same server — reuse by entering its name in wizard, skip reinstall.
- Cloud Migration Management page: Run Migration (on-demand or scheduled). First run = full copy; subsequent runs replicate only changes via SQL change tracking. Reset Cloud Data action forces next run to be full again.
- Migration deletes/overwrites cloud data — do NOT use cloud env as production during migration (no writes; keep business processes on-prem). When done, disable cloud migration setup (action deletes the ADF pipeline) to prevent accidental data moves.

### What does NOT migrate (users/permissions)

- Users and permission sets do not migrate. Cloud only supports Azure AD (AAD) auth. Custom user-defined permission sets must be recreated (or ship perms in extensions).
- Non-super cloud users get assigned the Intelligent Cloud permission set + Intelligent Cloud user group after run: read-all, no write. Actions/action-groups needing write perms are hidden rather than erroring. Can copy that permission set and trim to restrict reads.
- Username mismatch: on-prem usernames (e.g. john doe) differ from cloud (AAD-email-derived, e.g. jdo), breaking username references (e.g. order.CreatedBy). User Mappings action renames cloud user to match on-prem username, restoring the link — same effect as renaming user on User Card page.
- Even if on-prem already uses AAD (same usernames, mapping unneeded), users still don't migrate — must still assign permissions.

### Testing migration

- Copy a production env to a sandbox to test with write perms without affecting production. Sandbox copy is disconnected from replication so test data isn't overwritten.

### BC Admin Center (management)

- URL: businesscentral.dynamics.com/<AAD-tenant-id>/admin. Lists production + sandbox envs (version, country/localization, type, app link).
- Create/delete environments; copy production→sandbox; multi-country support (separate production env per localization).
- Notification recipients (email): update scheduled, schedule-date changed, update succeeded/failed (with reason), PTE compilation failure in new version.
- Update window: maintenance window (local time) for Microsoft patching/updates outside business hours.
- Updates: email notice with scheduled date/time/env/version. ~2-week window to reschedule the update date.
- Application Insights integration (part of Azure Monitor): set instrumentation key per env in admin center (requires env restart, key is startup param). Was preview/beta at time of talk. Emitted long-running query telemetry (threshold configurable, default >1s), including SQL statement + AL stack trace (app object id, extension publisher, triggering action) + env name/type. Roadmap: report runtime, SOAP/OData call durations, errors, job queue telemetry; and AL-code-emitted messages into App Insights. Custom telemetry initializers from extensions NOT supported at time.
- App Insights: Search for trace events; set alert rules (e.g. email when N slow queries in a window).
- Cloud debugging: set breakpoint in VS Code, Ctrl+Shift+P → debug without publishing, attach to sandbox env. Sandboxes only.
- Database export: admin center Database button → export .bacpac to a blob storage account. Need a SAS token (blob+file access) valid long enough (large DB export can take hours). Use for offline troubleshooting / on-prem restore / backups.
- Support: set partner contact info → shown on in-app Help & Support page. Create support request from admin center (routes via Power Platform admin center). "Red button" = direct line to Microsoft engineers for production outages (no logins, API/web services down) — pages an on-call engineer, use responsibly.

### Admin Center API / automation

- Everything in admin center UI is available programmatically via Admin Center API. Auth via access token (identifies the customer/tenant in Authorization header).
- GET environments returns JSON: App Insights key, env name, country code, version, URLs, data center, platform version, DB size.
- POST export operation: production env → .bacpac, supply same 3 values as UI (storage target etc.).
- Docs: search "business central admin center api". Can script sandbox creation, backups, key management.

### Automated deployment (recommended pattern)

- Source in git repo on Azure DevOps. Build pipeline builds app + runs unit tests → produces .app artifact (build often uses Docker container underneath).
- Release pipeline deploys .app to environments: deploy to UAT (user-acceptance-test) sandbox first, gate with an approval step, then deploy to production.
- Scale to many customers/apps: replicate the setup — one repo + build pipeline + release pipeline per customer per app.

### Gotchas / limits (Q&A)

- DB size limit exists because point-in-time restores (e.g. failed upgrade) can take hours/days on large DBs = downtime. Options for large legacy DBs: trim data, wait for limit increase, or stay on-prem.
- Accidental/malicious production env delete is recoverable for 35 days (customer data retained). No per-env delete protection at time (noted as feedback).
- Copy-to-sandbox side effects: no hook to run cleanup on copy. Mitigate by checking env type in AL (`EnvironmentInformation`-style [sic?] — verify object/method name) to disable functionality (e.g. SMTP notifications) in sandbox. HttpClient outbound calls are auto-blocked in sandbox copies until re-enabled; SMTP not blocked.
- Admin center access: customer global admins have it by default; delegated admins (partners with trusted relationship) also. Customer is ultimately in control.
- No planned feature to restore an exported .bacpac back into a cloud environment (only forward migration or on-prem restore). For point-in-time cloud rollback (lose recent data), contact Microsoft — not self-service.
- Multi-company merge: data migrates per company (except shared tables), so merging separate on-prem companies into one cloud env can work but not explicitly recommended; alternative is separate environments.
- AppSource apps can't be downloaded and installed on-prem — get them from the ISV to match schema before migration.
- No self-service ability to kill a runaway session/report at time (noted as desired feature).

### .NET Framework → .NET Core migration (BC platform, TechDays 2023)

- BC 22 platform migrated core binaries from legacy .NET Framework to .NET (.NET 6). Drivers: modularity, performance, cross-platform (Linux/macOS), flexible deployment (self-contained vs shared runtime), container/AKS support, open-source.
- `.NET Standard` was the compatibility bridge — a common base-library API surface across Framework and Core, enabling gradual migration.
- **dotnet Upgrade Assistant** (CLI + Visual Studio extension) is the easiest first step; offers in-place vs side-by-side and target-framework choice. Handles simple projects; struggles with WCF and complex ASP.NET.
- Migration plan: (1) list incompatible components + their dependencies, (2) pick a strategy per component, (3) execute. Per component ask: alternative in Core? equivalent NuGet package? candidate for refactor/deprecation?
- **In-place** migration for small isolated components (e.g. swap one NuGet package, ~1–2 days). **Side-by-side** for complex web APIs — stand up new host, migrate controllers/middleware one at a time, adjust clients gradually.
- **ASP.NET → ASP.NET Core:** teams using OWIN found migration mostly mechanical (OWIN ≈ ASP.NET Core pipeline). ASP.NET Core versions before 3.0 still run on .NET Framework, so migration can start in-place in the same solution before moving to a new web host.
- **JSON serialization:** ASP.NET Core defaults to `System.Text.Json` (faster) instead of `Newtonsoft.Json`. Both supported. Keep Newtonsoft first if you rely on DataContract serializer attributes or specific Newtonsoft attribute behaviour; migrate to System.Text.Json separately.
- **WCF:** no full replacement. CoreWCF exists but incomplete (e.g. NetTcpBinding [sic? "90 CB binding"] not fully working). Options: CoreWCF, rewrite as plain REST controllers, gRPC + WebSockets for high perf, or custom middleware. MSMQ support was announced for CoreWCF ~v1.4/1.5 (preview at talk time). — verify against Microsoft Learn.
- **SignalR → SignalR Core:** newer, but wire protocol changed (breaking). Yielded large debugging speedup (see below).
- **Config:** both `app.config`/web.config and `appsettings.json` supported in Core; some old settings error out, others silently ignored. Can start with app.config, migrate to appsettings.json later.
- **AL add-ins (dotnet interop):** to target BC 22+, update assembly probing paths from old .NET Framework locations to .NET 6/Core paths. Supporting both v21-and-earlier and v22+ needs different probing-path settings per workspace (left/old paths = v21 and before; Core paths = v22+).
- **Type forwarding:** move a class to a new assembly, leave a type-forward in the old assembly pointing to the new one — no breaking change for referencing code. Fully supported by AL compiler. Most `.NET Standard` packages are type-forwards (mostly to mscorlib).
- **Compatibility mode:** lets .NET Standard/Core projects reference .NET Framework libraries (via type forwarding). Trap: **compiles fine but only covers APIs that existed in .NET Standard** — unsupported APIs throw at *runtime*, not compile time. Hit this in OneDrive integration; forced a switch from basic auth to OAuth. Custom AL app add-ins on v22 load in compatibility mode — invest in real migration to avoid runtime surprises.
- **Leftover components** that couldn't migrate were pushed into microservices. BC 22 on-prem: NST plus two microservices — a reporting service and an **application proxy service** (holds add-ins for local versions, e.g. Mexico/Netherlands). Dataverse 9.1 integration also handled here.
- On SaaS, non-migratable .NET solutions → **Azure Function**. Connecting from AL to an Azure Function was ~20–30 lines; the **Azure Functions system module** (released 2021 wave / BC 21) cuts it to ~2–3 lines. — verify module name against Microsoft Learn.
- **Behaviour changes / gotchas in Core:**
  - Default text encoding is now **UTF-8** (Framework used system-locale default). Always specify encoding explicitly; encoding bugs are hard to diagnose.
  - `Debug.Assert` **crashes the process** in Core (throws) — matters for C# test automation.
  - Read-only fields **cannot be mutated via reflection** in Core.
- **Advice:** invest heavily in test automation; strong platform + application test coverage was what made the migration safe.
- **Results (BC 22, .NET 6):** broad, consistent compute perf gains. Many admin/scenario tasks 30–55% faster. Internal binary build >20% faster. Provisioning tasks (new tenant, adding NST nodes, restart) ~30–50% faster on avg. Pure AL computation ~38–40%+ faster, gains grow with load. SignalR Core cut cross-region debug symbol/AL file download from ~17s to ~3s (~80% faster).

<!-- ingested: BC TechDays 2022 - Cloud Migration | 2026-07-27 -->
### cloud migration mechanics (TechDays 2022)

**Upgrade/migration path**
- v14 is last version supporting C/AL; v15+ dropped C/AL. v14 is the bridge for C/AL customers.
- Two routes from v14: (a) on-prem single-step upgrade to v21 then optionally replicate to SaaS, or (b) replicate v14 data to SaaS first, then run the data upgrade in the cloud.
- Route (b) avoids writing/running on-prem upgrade scripts and is more forgiving of breaking changes.
- Direct migration from v14 (and single-step upgrade) supported "as long as technically possible." Longer you wait = longer upgrade (each release adds upgrade time).

**Prep before migrating (v14 alignment)**
- Must align for both migration and upgrade: primary keys, field names, field data types — mismatch = migration/upgrade fails.
- Cloud migration tolerates (but on-prem upgrade fails on): differing table names (use table mapping), differing table IDs, secondary keys.
- Extra fields added directly to Microsoft base tables are **silently ignored** by migration (full base table copied, added fields dropped, no warning). On-prem upgrade fails on these. Refactor into table extensions. (Speakers mentioned a prototype to auto-split base-table fields into extensions — unconfirmed.)

**Data cleanup**
- Corrupted code fields: legacy non-printing/newline/lowercase chars in Code fields. SQL stores them but platform can't read them → `Record does not exist` errors on read/modify/delete loops (e.g. `FindSet` + loop `Modify`). Detect with dedicated SQL query.
- Fix with `Invoke-NAVSanitizeField` [sic? — verify cmdlet name on MS Learn], scope with `-TableId` param. Run on a copy first to find affected tables.
- Company names can have same corruption but cmdlet won't fix (text not code field) — rename company before migration.
- Use Data Administration / data archive page to compress/delete stale entries before migrating.

**Architecture (Azure Data Factory)**
- Uses Azure Data Factory (ADF): pipelines = groups of activities that copy/transform/orchestrate.
- Self-hosted integration runtime (SHIR) installed inside customer network, registered to ADF via auth key exchange. Only makes outbound calls to ADF. No NST/service tier needed — connects directly to SQL DB.
- Azure integration runtime used if source DB already in Azure.
- Data flows on-prem DB → Azure Blob storage (temp, stays in-region, compressed by SHIR for speed) → tenant Azure SQL DB (decompressed).
- Setup: register runtime → preparation pipeline runs checks (compatibility level, version match) → creates stored procs on both sides → reads company list + installed extensions → builds table list + copy plan → creates replication pipeline → marks env ready → deletes prep pipeline.

**Replication run**
- Trigger: Cloud Migration Management page → Run Migration Now.
- Large tables copied one-by-one through blob storage; progress shows immediately on refresh.
- Small tables optimized: serialized to one big JSON, compressed, chunked into rows of one special table, replicated as single table; cloud stored procs reassemble → progress only shows at end.
- First run = full replication. Later runs use SQL change tracking for incremental (delta) copies = faster. Do NOT replace/restore the on-prem DB between runs — invalidates change tracking, forces full replication again.

**Permissions required**
- BC user doing setup needs SUPER; delegated admin needs customer consent.
- SQL user needs server-level `sysadmin` and DB-level `db_owner` (to create stored procs).

**Common setup errors**
- Connection string keyword/param mismatches — must match documented format exactly; copy from Azure portal for Azure SQL.
- SQL timeouts → SHIR needs min .NET 4.7.2 [sic? verify]; mitigate by updating statistics (stored proc) and reorganizing indexes before migration.
- Version/product-type mismatch → pick current version if major versions match, else previous version. Easily missed: `application version` in tenant database property table must be updated manually after on-prem upgrade or migration errors.
- SQL connection failures / firewall: verify SHIR machine can reach SQL Server, whitelist client IP, enable remote access (stored procs provided).

**Replication-phase errors (~10/month)**
- SHIR offline too long → automated cleanup wipes associated Azure resources → must redo setup. Keep SHIR machine online throughout.
- Invalid object / missing stored proc → DB was replaced/restored mid-run.
- Large metadata: metadata = JSON description of all fields/tables/extensions/companies in the run. ADF limit ~4 MB. Too many companies → ADF errors like "lookup activity result exceeded limitation" / "payload too large" (surfaced raw, uncatchable). Fix: migrate companies in batches (select companies action). Optimal ~10–15 companies per run.
- Uninstall unused cloud extensions before migrating (they bloat metadata); reinstall later.
- Own extensions: set table attribute `ReplicateData = false` to exclude a table from migration.
- Large data, bulk path: out-of-memory in ADF, usually Tenant Media table with large non-compressible images. Workaround: edit `IsFullCopy` [sic? verify] stored proc in on-prem DB to redirect Tenant Media to 1:1 (table-to-table) copy.
- Large data, table-to-table path: "specified row delimiter is incorrect" = ADF can't read temp blob. Workaround: redirect that table into bulk path (may compress and succeed).

**Table mapping / default matching**
- Tables matched by SQL name = company name + table name + extension ID. Full match → data copied (minus extra on-prem-only fields, silently dropped).
- Table in cloud with no on-prem match → warning "table doesn't exist in local installation" (usually safe, verify intended).
- Prefixed/renamed tables: Cloud Migration Management → Table Mapping action; pick extension + cloud table, type matching on-prem table name; respected on next run, moves compatible same-named fields.

**Performance tips**
- Honor SHIR system requirements; monitor source SQL CPU/memory in Azure portal, upscale during migration.
- Update statistics + reorganize indexes once before setup.
- Use a dedicated SQL Server (not shared with production load).

**Cloud data upgrade improvements (2022 release)**
- Migration now reuses the real upgrade code (full upgrade codeunits, all apps, single upgrade logic) instead of adapted-for-migration copies. Previously upgrade code couldn't run because obsolete/removed fields aren't accessible outside upgrade scope.
- Tenant flips to "upgrading" status during run: no hotfix interruption, single session (avoids user-caused locks), full telemetry/reporting, and automatic point-in-time restore on failure.
- Flow: Cloud Migration page → Run Update Now → warns you lose env access → track in Admin Center (status flips to Updating; Operations tab logs history) → ~3 min → Active → status Completed → go live.
- On failure: Operations tab shows failed op + full stack trace; tenant auto-restored to pre-upgrade point-in-time; upgrade shows Pending; fix, replicate more data, retry.
- Old upgrade flow still supported and can be programmatically re-enabled if you took dependencies on it.

**Faster upgrades — DataTransfer**
- Long-running upgrades mostly caused by moving obsolete-removed fields to new fields via record loop + Modify (slow: 1M records = 2–24h+, varies by SQL strength, table-extension count, OnModify subscriber count).
- `DataTransfer` type: declare source→target table, source filters, join statements, field mapping; `CopyFields` runs a single SQL query and raises NO events → ~2–5 min for 1M records.
- Limitations: usable only in upgrade scope to initialize new fields (only valid use = move obsolete-removed fields to new fields, since skipping events would otherwise be a breaking change). Currently marked on-prem target only — not usable in SaaS. 11 long-running methods optimized this release using it.

**Automation API**
- API to manage full migration end-to-end (setup, company management, run migration) — useful for many migrations or many companies (~50+). Examples on BC Tech GitHub.

**Community**
- BC Cloud Migration Yammer group for feedback/support.

**Stats (context)**: ~500–600 unique customers/month migrating; ~1/3 from v14; v20 and v14 most common source versions.

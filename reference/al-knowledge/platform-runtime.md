<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Scale design, NuGet packaging, app packaging

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 1. Platform, Runtime & Performance

**Companion tables (v23) — the table-extension data model.** Previously each table-extension was a
separate physical table joined 1:1 at runtime (n table extensions = n-way join). v23 collapses **all**
extension fields for a base table into **one companion table** → at most one join. Read is the biggest
win; Delete 2–5×, Insert ~2×, Modify up to 2×; smaller DB (one PK + rowversion copy). **No code
action needed.** GOTCHAs: with only ONE table extension you see no change; write gains vary (gated by
AL triggers/events); old model degraded because SQL's optimizer stops optimizing past ~7–8 joins
(a 70-extension table = 70-way join). On-prem direct SQL (Power BI/ETL) breaks — mimic old schema with
DB **views** (samples on GitHub); on-prem upgrades take longer (data rewrite). Delete orphaned
uninstalled-extension data via Installed Extensions. *(Faster data stack 2023 w2)*

**New locking / logging model (default from ~v24, mandatory v25).** Reads run **READ UNCOMMITTED**
until you write to that table-type in the transaction, then further reads switch to **READ COMMITTED**
— replaces old behaviour where any modify made *all* instances of the same table in the session
inherit an update log (an update log could even be taken on a *different* record instance). Opt-in via
Feature Management; **requires an environment restart**, applies to all users at once; may surface
"another user has modified" on some code paths. Audit your `LogTable` calls (base app is removing
many) and prefer the AL `ReadIsolation` property to opt into an update-log read per-instance instead
of a blanket `LogTable`. Flush concurrency/deadlock issues first with the **Business Central
Performance Toolkit (BCPT)** in a sandbox. *(Faster data stack 2023 w2)*

**Memory / Base64 (2026 w1).** Lower per-tenant memory footprint; new platform Base64 conversion
codeunit + stream overloads (OData returns are Base64) cut memory pressure. GOTCHA: platform now
**throws AL errors on excessive Base64 memory** (e.g. a 15 GB doc) — add size limits; one tenant's
memory pressure hurts every session on the tenant. *(Server & database 2026 w1)*

**FlowField perf (2025 w1).** Feature key "Calculate only visible flow fields" computes only
page-visible FlowFields (opt-in now, default later); `RecordRef.SetAutoCalcFields` controls which
FlowFields auto-update — the troubleshooting MCP suggests `SetAutoCalcFields` before `FindSet` when it
sees CalcFields-in-loop. *(Server & database 2025 w1)*

**Index management from the client (2026 w1).** Table Information page drills to **per-index** info
(size per company, seek/scan/lookup/update usage, key vs **included** fields → shows if an index is
covering). Turn metadata/auto-tune indexes **on/off** from the client (can't disable Unique/SystemID).
Disabling drops it in SQL (saves storage + cheaper writes). SaaS: enabling a disabled index is queued
to the next overnight maintenance window; Docker/on-prem applies immediately. Telemetry lifecycle
events LC0063/LC0064. Reminder: more indexes = slower writes. *(Enhanced index management 2026 w1 /
S&DB 2025 w1 Missing Indexes DMV page: Seeks/Scans/Avg cost/Impact/Estimated benefit)*

**.NET 8 + PowerShell 7 (v24).** Server runs on .NET 8 (was .NET 6) — transparent to AL, but
management moves to **PowerShell 7**; a PS5 bridge via consolidated `NavManagement.dll` relays to new
PS7 cmdlets (PS5 to be deprecated). Import via `NavAdminTool` to auto-pick the right version.
*(AL runtime & DB 2024 w1)*

**Web-service resilience / security.** Server returns **HTTP 503 + `Retry-After`** when a request
times out in the queue (backported 22.2) — clients should read status/headers and retry with back-off
(MS shipped copy-paste HttpClient error handling + status-code TSGs). Invalid/duplicate metadata now
disables only the offending endpoint (not all web services) + partner telemetry. Outgoing `HttpClient`
**server-certificate validation** enforced Oct 2025 (SFI hardening; v26 opt-out feature key "HTTP
server certificate validation"; failures in telemetry RT52); URI validation also blocks internal
ports (hosted = no opt-out; on-prem = allowlist server settings; backported v26/v27). Microsoft is
**blocking UI pages as SOAP endpoints** (revert via "Web services on UI pages"; usage in RT53) —
prefer API pages for OData, UI-page OData mainly for Edit-in-Excel. *(Stable web services 2023 w2 /
S&DB 2025 w1 & 2026 w1)*

**Other:** Copy Company up to 5× faster but still takes heavy locks — never during working hours.
On-prem HA: `Enable SQL multi-subnet failover` adds MultiSubnetFailover to cut failover time. Session
creation 2–4 ms faster (~25% throughput gain for many small web-service calls). Telemetry gained
`userType`/`guestUser` dims (RT2/RT4), long-running-call **exclusive** time (`exclusiveTimeMs`), and
MCP config/usage + user hardware/network dims. `EffectivePermissions` includes security-group-derived
permissions; on-prem `Enable Entra groups on prem` grants permissions by Entra security group.
*(S&DB 2023 w2 / 2025 w1 / 2026 w1)*

---

<!-- ingested: Planning table indexes for the best performance | 2026-07-26 -->

<!-- ingested: Telemetry: a developer's Best Friend | 2026-07-26 -->

<!-- ingested: Microsoft Presents: Performance in Business Central | 2026-07-26 -->

<!-- ingested: How we handle large customers in SaaS: Developer edition | 2026-07-26 -->

<!-- ingested: Microsoft Presents: What's new in AL - Package the right app | 2026-07-26 -->

<!-- ingested: "When a dream comes true" aka NuGetized Business Central | 2026-07-26 -->

<!-- ingested: Microsoft Presents: Designing for scale in Business Central | 2026-07-26 -->
### Designing for scale in BC online (mibuso — Microsoft: Christian Simone? [sic? name uncertain], Raina, Maria)

**Compute-tier autoscale & load balancing**
- Each environment maps to compute VMs (web server + NST service) in a cluster, plus one database (1:1 tenant→DB).
- Load balancer routes *new* sessions by VM load (CPU/memory/other thresholds). Once a VM crosses ~60% CPU it stops receiving new sessions; existing sessions are never moved off a VM.
- 60% is a preemptive threshold, not a danger zone (~100% is where OS thread prioritisation degrades everything).
- When too many VMs in a cluster are busy, autoscale provisions more VMs. Observed ~10 min from scale-out request to new VM + NST ready for sessions. Clusters run with large headroom (e.g. 24 VMs ~60% = ~40% buffer), so no way to pre-warm/pre-request capacity; ~10 min ramp can be too slow for a sudden 100k-user burst (acknowledged limitation).

**Database-tier autoscale**
- Can't add DBs, so DB is scaled *up* (more vCores/threads, better IO) when monitored metrics (CPU %, data IO %, log IO, etc.) cross ~70%. Scale-up is near-instant, online, no disruption (maybe one dropped connection; service is resilient).
- Initial DB capacity chosen by two factors: paid vs trial, and production vs sandbox.
- Scale-up is aggressive (short look-back, low thresholds). Scale-down is very cautious: a DB that was scaled up is left untouched for **45 days** (avoids month-end spikes) and only scaled down when metrics low enough to avoid ping-pong.
- **Sandboxes: compute VMs same size as production, but DB tier is NOT scaled up.** Hitting DB limits in a sandbox = no more capacity. Implication: BCPT/perf tests on sandbox are unreliable — run perf validation on a production environment to get realistic DB scaling.

**Operational limits (documented on Learn, ~47 total; examples)**
- Client reconnect window after disconnect: **10 min** (else session cancelled).
- Max companies per environment: **300**.
- Max upload/download file size: **350 MB**.
- Max query execution timeout: **30 min**.
- No limits on: number of users, or UI interactions (browser tabs, clicks, field entry).

**Web service (OData v4) throttling — NEW per-user model (changed ~2024, was per-environment)**
- Old per-environment limits: 5 processed in parallel; up to 100 combined (running+queued), excess queued up to 8 min then rejected 429. Problem: one heavy caller could fill the queue and block important callers (e.g. Power BI / POS).
- New limits are **per user** (identified by the auth header — user or entra app): 5 running in parallel, 100 max combined, 95 max queued, plus a **max requests per 5-min sliding window** (~6000). Exceeding sliding window → 429.
- Side effect: total throughput scales with number of distinct callers (N users → N×5 in parallel). No consumer-side change needed to benefit.
- To get more throughput deliberately: authenticate as **multiple entra apps** and round-robin/randomise requests across them — each app = its own queue.
- Why not just raise 5→500: (1) wouldn't stop one caller blocking others; (2) a single NST can't handle that many parallel calls, so requests are spread across multiple NSTs. Requests from the **same user are pinned to the same NST** to give a consistent (cache-coherent) view — different users may land on different NSTs. NST caches sync via a service bus broadcast with a few-seconds delay, so cross-NST reads can be briefly stale (hence per-user pinning).

**Job queue / scheduled tasks — NEW per-user model**
- Was 5 running concurrently per environment; now **5 concurrent per user**. Recurring job queues typically all owned by one user → less benefit; background posting (e.g. job queued as the posting user) spreads naturally.
- Per-user limits apply **per user per environment** (each environment counts separately; sandboxes same).
- On-premises unaffected — the 5-concurrent + per-user orchestration is a SaaS service-layer feature; on-prem uses NST config settings and has no per-user behaviour.

**Batch/parallel processing pattern**
- Parallelise long batch jobs by creating multiple identical recurring job queue entries differing only by parameter string (which customer/record range to process), all scheduled same time. Invoice *creation* parallelises well (little/no DB locking).
- Two risks for long-running (hours) job queue sessions: (1) sessions stay pinned to a VM for their whole life — if that VM hits 100% they suffer, no rebalancing; (2) NST upgrades (2–3×/week for hotfixes) cancel sessions still running after ~50 min grace (job queue shows failed; configure retry to resume unprocessed records).
- Mitigation: make each run self-limit (e.g. run current-time + 10 min or until work done, then reschedule a new non-recurring immediate job queue entry). Produces grouped log entries but avoids VM-overload stalls and upgrade cancellations.
- *Posting* takes DB locks → doesn't parallelise linearly. Real partner numbers: sequential 6.5h → 2 parallel 4h → 3 parallel 2.5h.
- Locking kills parallelism. Guidance: minimise locks — avoid `LOCKTABLE`, prefer smaller/narrower locks and read-committed where safe, move work out of locked windows, ensure right indexes. See tri-state locking session [[tri-state-locking]].

**Read replicas**
- Some environments get a read-only DB replica for offloading (added only when a problem is detected; not all environments have one). Code must be annotated with read-only intent to actually route there — otherwise queries hit primary.

**Telemetry for diagnosing throttling/delays**
- Web service call event `RT0008`[sic? "rg8" from captions — verify event ID on Learn]: has response code (429 = throttled) and queue time (0 = not queued). Very easy to spot impact.
- Job queue start event `AL0000E25`[sic? "e25" from captions — verify]: has *earliest start time* (scheduled) and *timestamp* (actual start) → compute delay. ~2.5s delay considered fine (job queues are async by nature). User ID present to find whose jobs are delayed.
- Both events carry the *Telemetry user ID* (settable artificial ID on the user card) to identify the impacted user under per-user limits.
- Lock-timeout event fires when a session waits ~30s for a lock then gives up → sign of a DB locking problem. Also the in-product **Database Locks page** shows current lock holders/waiters live (F5 to refresh).
- Scale-up/scale-down events are NOT surfaced in partner telemetry (by design — meant to be invisible). MS considering surfacing signals when an environment is struggling.

**Scale reference figures (public: "Scalability for Business Central online" docs)**
- Observed real customers: >1000 users per environment; DBs 1.4 TB; migrations from on-prem >500 GB tenant data; ~8000 sales orders/hour (60k lines); 10M web service calls/day, 32k web service requests/minute (~140/s) successful; job queue ~16/s average.
- Browser interaction = tab-out/click/open-close (NOT per-character typing). Earlier 2022 figures were inflated by browser add-in pings counted incorrectly.

**Storage/env quotas**
- Default entitlement 80 GB + 1 production / 3 sandbox environments; more storage or environments require buying another production. MS signalled upcoming changes (fall 2024).

### BC apps as NuGet packages (mibuso — Kamil Sáček & Freddy Kristiansen)
- Goal: develop/compile AL without downloading symbols from a live environment. Symbols/dependencies pulled as NuGet packages instead, so dev can start with only `app.json` + a package source.
- Why NuGet (vs Universal Packages, npm, Maven, etc.): Universal Packages can't be anonymous and carry no logic; NuGet is the .NET package format, supports anonymous feeds, and lets custom resolution logic live around it.
- A `.nupkg` is just a zip with a manifest (from a `.nuspec` XML) + payload files. Can be built with the free `nuget` CLI (`nuget pack`), or by BcContainerHelper which zips it directly (no dependency on nuget/paket being installed).
- **Package ID naming:** `publisher.name[.tag].appId` — human-readable, ends in the app GUID (~42 chars). `tag` slot carries localization (e.g. country code), `symbols`, or `runtime`. Publisher/name are normalized to `[A-Za-z0-9_-]`. Max ID length **100 chars**; if exceeded, the app-name portion is truncated (publisher + appId kept). Keep publisher/app names short.
- **Immutability rule:** a given package ID+version must always be the same content across all sources (may be cached locally). Localizations share the same appId → tag disambiguates.
- **One app per package** (recommendation/rule). Max one .app file per package.
- Dependencies listed in nuspec with same naming algorithm + version ranges, including deps pulled transitively. `application` dep in app.json maps to `Microsoft.Application[.localization]` (no tag = W1); `platform` dep maps to a platform package. AppId is NOT included on the application/platform package IDs.
- Versions: full 4-part (major.minor.build.revision) supported, plus pre-release suffixes (alpha/beta/preview). BC has no max-version concept — a dep on e.g. `Microsoft.Application 21.5` means installable on anything ≥21.5.
- **Resolution:** BcContainerHelper and AL-Go search by appId only (like AppSource, finds right version). Kamil's nuget/paket workflow uses full package ID+version — renaming publisher/app can break resolution (usually desired: forces app.json update).
- **Version pinning:** paket's `paket.dependencies` lets you constrain the graph, e.g. `21.5` meaning any build/revision of 21.5 but not 21.6, so you resolve the latest version compatible with your target BC, not just the newest. Not every tool supports lowest/highest/range selection — check before adopting.
- **Windows long-path gotcha:** cache paths hit the 255-char limit fast (temp folder + package-ID subfolder + long .app filename, esp. runtime packages). Set nuget temp/cache to a short root (e.g. `c:\tmp`); avoid deep workspace paths (Documents profile). BcContainerHelper doesn't cache → immune but slower.
- **Sources/feeds:** Azure DevOps Artifacts feeds (public or private), GitHub Packages registry (anonymous or PAT), nuget.org (public — do NOT trust; verify package contents, prefixes like `Microsoft` can be reserved), local/UNC file share, blob storage. Azure DevOps **Upstream sources** only support DevOps feeds + nuget.org gallery — NOT GitHub Packages or arbitrary feeds. Requesting a package not in your feed copies it from upstream into your feed (feed grows; ~cents/GB/month).
- Azure DevOps feed limit: ~5000 versions per feed — relevant given MS hotfix volume.
- Azure DevOps **views** (default/prerelease/release) let you promote versions; consumers filter via `@Release`/`@Prerelease` in the feed URL. Alternative: separate feeds for released vs pre-release, or use version suffixes.
- **MS test/preview feeds (URLs will change):** (1) Microsoft apps full packages, (2) same content but symbols-only (smaller, compile-only, can't publish), (3) AppSource apps symbols-only (compile against ISV apps without spinning up an environment; publishing still needs full package from publisher or online-sandbox install). `Microsoft.Application[.country]` packages exist per localization, many versions each (since ~v17).
### Runtime packages via NuGet — indirect-package pattern
- Runtime package = pre-compiled image (like old .fob). Contains compiled IL (not AL source, but IL is inspectable → obfuscation, NOT IP protection). Can't go to AppSource; can't be a per-tenant extension. Guaranteed only on same **minor version + localization** it was built for → many packages needed. Can be used as symbols for compiling against.
- Use cases: on-prem/DevOps, or licensing workarounds (runtime package can create objects, e.g. table extension, regardless of license granules that block source publish).
- Problem: runtime adds a 3rd dimension (package × version × BC-version); NuGet packages are immutable/can't be updated, so you can't append new BC versions to an existing package.
- **Indirect-package solution:** `publisher.name.runtime.appId` is an **empty** package that the appId resolution finds; it has a dependency on `publisher.name.app.runtime.<appVersion>` which carries the actual runtime .app in the file section, with a tight application dependency range `[23.2,23.3)` so NuGet resolution picks the runtime built for the exact BC version. The real runtime package is never found directly (no appId in it) — only reached as a dependency. New BC version → publish a new runtime package into the second feed, no new app version needed.
- **Localizations for runtime:** not another NuGet dimension — put localization-specific runtime .app files in subfolders (one per country) inside the runtime package, root holds the default. Only needed if a localization genuinely differs (rare: differs only if a function param type/signature diverges between localizations).
### BcContainerHelper NuGet functions
- `New-BcNuGetPackage`, push (like `nuget add`), find/get/download. `Download-BcNuGetPackageToFolder` — package + all deps to a folder (`-downloadDependencies allButApplication` / `allButMicrosoft` to stop traversal at MS apps). `Publish-BcNuGetPackageToContainer` — downloads package+deps and publishes to container in dependency order, skipping already-installed. [sic? verify exact cmdlet names against BcContainerHelper]
- Trusted feeds configured with feed URL + token + patterns (e.g. `Microsoft.*`) and optional code-signing thumbprint to only accept signed packages. Supports DevOps feeds, GitHub feeds, nuget.org.
- No caching → correct but can be slow (walks server for deps); nuget/paket faster in most cases.
### AL-Go for GitHub NuGet support (work in progress at talk)
- Secret `GitHubPackagesContext` → AL-Go auto-publishes all built packages to GitHub Packages and uses that feed for resolution; org-level secret gives every repo access to every repo's packages for auto dependency resolution.
- Setting `TrustedNuGetFeeds` → AL-Go auto-searches these feeds for dependency resolution during build (finds symbols, full, or runtime packages; full apps preferred).
- Secret `NuGetContext` → also publishes apps to that NuGet feed (full apps; runtime-package publishing not yet supported at talk, despite slide).
- `Run-AlPipeline` (BcContainerHelper) installs deps from a NuGet feed via the `InstallMissingDependencies` override (AL-Go supplies it; it calls `Download-BcNuGetPackageToFolder`).
### Misc
- `propagateDependencies` app property works unchanged with NuGet packaging — it only affects compilation visibility, the app is still treated as a normal app with its declared dependencies. `Microsoft.Application` is an empty app with propagateDependencies.

### App packaging: resources, source-control stamping, table/field moves, IP protection (mibuso — What's new in AL)

**Source-control info in app package**
- App package can carry repo URL + commit ID. Auto-stamped by AL-Go for GitHub on release; add manually in own pipelines. Property is a plain string — works with any git host (GitHub, GitLab, Azure DevOps).
- Visible in **Extension Management → card details**; commit ID lets you pin which build introduced a bug.
- Web client action **Open source from git** launches VS Code and clones/opens repo (only if you have repo access + resource policy allows).
- Web client action **Generate launch configurations** (under Help & Support) writes `launch.json` matching the current environment, so symbols download in one step.
- Extension Management multi-select action **Get selected as dependencies → show and copy** (or download into VS Code) emits formatted `app.json` dependency entries + pulls symbols. Avoids hand-editing dependencies.

**Bundled resource files**
- `app.json` gets a `resourceFolders` property (array of folder paths) to package arbitrary files into the extension, readable at runtime. Resources are private to the packaging extension — not accessible by other extensions.
- Read: `NavApp.GetResource` [sic? captions said "nav.get resources text" — verify exact method name/signature vs Microsoft Learn] taking file path relative to resource root.
- List/verify presence: `NavApp.ListResources` [sic? captions "nav app list resources" — verify] with a path filter (e.g. `prompts/`); check for a given file before use and handle absence yourself.
- Use case shown: move AI system prompts out of AL source into `.txt` resource files (IP protection, reuse across codeunits).
- Alternative to bundling secrets: Azure Key Vault. Add `keyVaultUrls` [sic? captions "keyword URL" — verify property name] to `app.json`; read via `AppKeyVaultSecretProvider` → `GetSecret(name)`. Store result in a `SecretText` variable (not `Text`) so it isn't exposed while debugging.

**Moving tables/fields between extensions (platform-handled, no upgrade code)**
- Since ~2024 available for base app; now also for AppSource/regular apps. Platform migrates data during sync — no manual upgrade codeunit.
- **Move a table — 3 iterations:**
  1. Source app: on table set `ObsoleteState = PendingMove` and `ObsoleteReason`/target `MovedTo` app ID [sic? verify exact property names]; fix resulting breaking changes; bump version, publish.
  2. Source app: set `ObsoleteState = Moved`; delete the moved objects from source; bump version, publish.
  3. Destination app: reintroduce the table with `MovedFrom` = source app ID. Table must be identical to original — cannot remove fields or public methods (adding is allowed). Requires source to be in `Moved` state (step 2) or the upgrade fails.
- **Move a field:** same pattern; reintroduce field in destination table extension with `MovedFrom` set. Field move uses a data-transfer style copy.
- Table moves are typically instant — implemented as a SQL rename, not a data copy — so usually fast; field moves may actually copy data.
- Constraint: can move base-table field → table extension, and table extension → another table extension, but **not** table extension → base table. Merging two table extensions into one requires moving all fields into a single extension (you still end up with table + extension).
- Breaking a shared dependency when splitting apps: extract the shared codeunit/enum into its own app and make it a dependency of both. Consider interfaces for maintainability.

**Profiling / performance troubleshooting tools**
- Landing page: aka.ms/bctroubleshooting (~20 tools).
- **VS Code snapshot profiler** (~5 yrs): offline debugging from prod; include performance profile in snapshot → per-method/branch time, jump to source. Uses **instrumentation** (captures everything, incl. sub-ms).
- **In-client performance profiler** (2022): interactive — start/stop recording in web client while running the scenario (Help & Support → Performance Profiler). Shows time per extension (blame MS vs AppSource vs PTE), call stack, objects. Limits: needs someone to repro live; can't catch transient issues; interactive UI flows only (no web service / job-queue / background sessions).
- **Scheduled profiles** (~early 2026): rule-based, non-interactive, background capture. Help & Support → "Analyze performance with scheduled profile" / search "profiler schedules". Define rules: enable flag, active time window, filter by user and activity type (UI click vs web service). Covers web services and background tasks. Captured profiles listed per rule; open an individual capture in the in-client profiler or in VS Code. No jump-to-source from this view yet.
- In-client + scheduled profilers use **sampling** (e.g. ~every 50 ms) — short/fast calls may not appear; only longer executions show. Sampling interval + min-duration filtering are tunable.
- VS Code: `Ctrl+T` symbol search now works across AL symbols — also usable to pass objects (e.g. a table) as context to GitHub Copilot agent for refactoring/generation. Access gated by the same IP/resource-exposure policy.

**IP protection (resource exposure policy)**
- Protection is only enforceable in SaaS cloud. On-prem/container/local installs: source is obfuscated but reachable (SQL/metadata); handing out app/symbol/runtime files = no guarantee.
- Package artifact types: app file (obfuscated AL source + resources), symbols (obfuscated source or metadata-only; with/without resources), runtime packages (obfuscated AL + resources + C# generated for a specific NST version — deploy without compiling on the NST).
- `app.json` property **`resourceExposurePolicy`** with flags: allow debugging, allow download source, include source in symbol files [sic? verify exact flag names]. Defaults are false (locked down); the VS Code project template enables them for easier onboarding.
- **Dynamic access grant:** put a Key Vault secret named `BCResourceExposurePolicyOverrides` [sic? verify exact secret name] in the app's key vault to grant specific partners debug/download/symbol-source access, revocable later. Partners usually grant debug (harder to bulk-exfiltrate) not source download. Not supported for snapshots/profiling — debug on normal sandboxes only.
- Recently extended to **dev extensions** (installed dev deployments normally expose source): apply resource protection policy to a dev extension and grant access the same way. For dev extensions the grant is per-**tenant**; for normal resource policy it's per-**user** (must be a delegated admin).
- Recommendation: lock down AppSource apps, grant trusted partners temporarily/permanently via key vault, only share app files with trusted parties. For PTE: agree IP ownership up front and keep source control (preferably shared with customer).
- Note: AL LSP and debug-adapter protocol implementations are non-standard; no current plan to standardize.

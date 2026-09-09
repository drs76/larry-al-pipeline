<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Performance sessions, telemetry & App Insights

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 1. Platform, Runtime & Performance

### Performance in BC — locking, finds, telemetry (Microsoft session)

**Where time goes**
- Request path: browser ↔ Azure (~50 ms latency) ↔ NST/web server ↔ SQL (separate machine, ~1 ms latency). Page-open time often ~half spent in browser (JS/HTML render), not NST — devs only influence NST = AL + SQL time.
- Rough AL speed: ~1M non-DB AL statements/sec. Each SQL call ≥~1 ms (latency-bound). Base app averages ~10 non-DB statements per DB statement, so ~90%+ of time is waiting on SQL.
- Usability targets cited: page open ~2–3 s okayish; field validation ~0.5 s ok; keystroke echo immediate.
- Client-side/connection can be the real cause (weak device, bad Wi-Fi, battery vs plugged-in). Check `<environment>/connectivity` page for latency; test at customer sites, not just office.

**Profiling / telemetry**
- Help & Support → **Analyze performance** → Start/Stop → **Download** the profile; open in VS Code. Shows total time vs self time per function; sort leaves by self time; double-click to jump to source (project open in VS Code).
- **Scheduled profiler**: define profiles by time window + optional user, and select activity type to capture — client session, background/job-queue tasks, or web-service calls. Sampling profiler polls call stack every ~100 ms (configurable); can set min duration threshold (e.g. ignore <500 ms). Logs same format as manual download.
- `idle time` in a profile = NST waiting on something external (e.g. RDLC report rendering), or user think-time.
- App Insights: emit connection string via app manifest/telemetry setting; **never** commit/share the key (others' telemetry lands in your store). Scope of custom telemetry signals: `all` (customer + extension stores) vs `extensionpublisher` (only where code runs) `[sic?]` — verify exact scope enum names.
- Verbose telemetry: emit with verbose tag; only captured after user enables **additional logging** on Help & Support page, and only for that session/tab (new tab = new session, verbose off). Use for repros; keeps cost down (log only important events normally).
- Tool tip: **Kusto.Explorer** (Windows app) over the browser Data Explorer — F5 runs query, persists queries across restarts. Needs App Insights resource ID prefixed with app-insights URL in connection string.
- Telemetry is expensive at scale — MS emits >1M events/sec across tenants; was one of their biggest costs early on.

**Locking principles**
- Lock scarce/critical resources as LATE as possible (classic `LOCKTABLE` + `FINDLAST` on entry tables serializes posting). Lock in a consistent order to avoid deadlocks; base app posts GL toward end of process.
- UI uses optimistic concurrency → "another user modified this record" error. Explicit `LOCKTABLE`/update-lock = pessimistic → lock timeout (default 30 s).
- **Read isolation**: use read-uncommitted / read-committed isolation hints (increasingly sprinkled in base app). `READ COMMITTED` only avoids locking if **snapshot isolation** is ON for the DB (SaaS has it on); otherwise read-committed can block just like an update lock.
- Tri-state locking (added ~v25): `CalcSums`, `Count`, `CalcFields` no longer take locks even right after an insert that locked the table.
- Deadlocks: SQL detects immediately; NST auto-retries retriable transaction scopes (visible as deadlock + retry telemetry events) — saves many app-level mistakes. Non-retriable / already-committed points fail with lock timeout instead.
- SIFT keys can cause locks and are costly to maintain. Base app sales/purchase line indexes converted to **included fields only** (SIFT removed) to cut locks. Watch for SIFT keys whose leading fields are near-constant (e.g. purchase line Job No./Job Task No. mostly blank) — effectively serializes all posting per document type.

**Concurrent posting (v25/v26)**
- Opt-in concurrent posting: instead of `LOCKTABLE`+`FINDLAST` to reserve entry no., use **number sequence** via per-table `GetNextEntryNo` `[sic?]` (verify name) so multiple sessions post simultaneously.
- Entry tables gained an item-register-no. field for drill-down; old rows keep 0 (not back-filled — hundreds of millions of rows too costly). Drill-down filters on both the entry-no. range AND register no. (0 = old-style range still valid; non-zero = use register no.).
- SIFT **bucket** field added (e.g. warehouse entry no. MOD 5) to spread concurrent SIFT updates across buckets.
- Automatic cost posting to GL defeats concurrency (locks GL). Fix: collect GL entries and post them last. Measured: two 500-line item-journal batches with auto cost posting ran ~19 s alone vs ~23 s combined (near-linear throughput, and 2nd user sees progress immediately). Sales invoice batches (report 297 via job queue) ~15 min ×1 → ~17.5 min ×5 ≈ 4× throughput, saturating around 5 concurrent.
- v25→ warehouse entries, v26→ inventory made more concurrent. Next release: sales-order lines sorted by type+number before posting so you get locks not deadlocks (locks preferred over deadlocks).
- Test concurrency with **BCPT** (multiple background sessions posting same/different items); inspect logs for deadlock/lock-timeout call stacks.

**Find / query efficiency**
- `IsEmpty` when you only need existence; `FindFirst` for exactly one row (calling `Next` after `FindFirst` forces another SQL round trip); `Find('-')`/FindSet for a set; FindSet with count for a bounded batch.
- `Get` (or FindFirst with full primary-key filter, auto-converted to Get) hits the NST cache and is reusable — a query object result is NOT cached. Best SQL call is the one you skip → prefer Get for cacheable lookups.
- Access ranking: Get (PK lookup) > seek (key fully covers set-range/filter fields in order) > index scan (index covers query but wrong order/partial) > full table scan (filter field not in any index).
- **SetLoadFields**: load only needed fields → smaller SQL cursor, faster iteration; also skip flow-field calc. Modify with SetLoadFields only writes loaded fields (plus system audit fields), never blanks unloaded ones. Cursor auto-expands (no extra round trip) if an unloaded field is used later. Also skip FlowFields you don't need.
- Don't mutate filters / SetLoadFields / SetAutoCalcFields between Find and Next — forces query re-issue. Don't `SetCurrentKey` on the field you're modifying (moves cursor). Do Modify/Delete directly on the iterated record, not a copied record instance (copy cuts the link → more restarts).
- Reduce round trips: AutoCalcFields inlines flow-field calc into the fetch; query objects push joins+aggregation to SQL; `CalcSums` offloads aggregation instead of pulling rows to sum in AL.
- Bulk ops: `ModifyAll`/`DeleteAll` only stay set-based if NO row trigger, no global/database trigger, no OnBefore/OnAfter subscriber, no security filter, no media set on record/field. Any of those → silent per-row fallback (still compiles/looks bulk). Triggers can never be bulk. A previously-fast table can regress if another extension subscribes — check telemetry.

**Optimize for Text Search (SQL full-text, v25)**
- Opt-in per field (base-app master-data tables; extendable to your tables/table-extensions). Order-independent, any field combination. Client search turns SQL `LIKE %..%` (full scan) into full-text `CONTAINS`.
- Limitation: word-prefix only — searching "chair" won't match "hair" (contains/ends-with needs wildcards → falls back to slow LIKE). Web client shows dropdown arrow → "modern search"; wildcards auto-routed to full-text when possible, else legacy.
- Query from code via filter group -1 with double-`&&` syntax `[sic?]` (verify exact filter-group/token) so as not to break existing filter logic.
- Query optimizer may skip the full-text index for very selective/other predicates (e.g. single letter, or `FindFirst`) → can be SLOWER than legacy. Mitigation: request more rows (FindSet / first ~50) to nudge optimizer toward the index.
- Cost: each full-text index ×companies ×table-extensions multiplies (base app ~50 indexes × 300 companies ≈ 30k). Tier scaling / SQL restart must reprocess each → slow. Skip full-text on small tables; wildcard LIKE is fine there.

**Flow-field & aggregation improvements**
- v26 opt-in: **calculate only visible flow fields** — previously all flow fields calced even when `Visible=false`. Fields whose visibility flips at runtime (inside a group) still always calc; only stable-visible/invisible fields are optimized.
- v27 (planned): flow fields with identical source table + identical filters are grouped into one SQL query (SUM/AVG/COUNT groupable; MIN/MAX groupable; EXISTS/lookups groupable) — e.g. 4 debit/credit flow fields → single OUTER APPLY instead of 4 joins (~70% lower estimated cost).

**20 tips (misc)**
- AL compiles to C# with monitoring wrappers around every statement; methods are NOT inlined (try/catch + lambdas prevent it). For hot low-level code (JSON, arithmetic) tiny helper methods carry per-call overhead + telemetry-measurement cost — inline manually only when neighbor ops are CPU-bound, not when neighbor is a DB op.
- Pass complex types (records) `var` (by ref) to avoid copies when you own all callers.
- `Query.SaveAsJson` `[sic?]` (verify) is stream-aware like SaveAsXml/SaveAsCsv — build big JSON without piling memory.
- Use native `List`/`Dictionary` (backed by .NET objects) for collecting values instead of temp tables — temp tables use an in-memory DB, heavy on the machine; use only when you need record semantics (insert/search/etc.).
- Upgrade code: use `DataTransfer` (CopyRows/CopyFields, same or cross table, type conversions e.g. Integer→BigInteger) instead of looping hundreds of thousands of rows — one SQL op, no triggers.
- Pages: minimize OnFindRecord/OnNextRecord (block optimizations) except where required (matrix pages). Put important data at top of page; collapse/close fact boxes by default (not rendered = not paid for); client delay-renders offscreen content.
- Invisible field source expressions are NOT evaluated — attach heavy calc functions directly to source expression (skipped when invisible) instead of precomputing in OnAfterGetRecord (always runs).
- Offload heavy work (web calls, big calc) to **page background tasks** for responsive UI.
- Use `TextBuilder` (= C# StringBuilder) for string concatenation — buffer doubles as it grows; avoids repeated allocations / GC pressure.
- Avoid synchronous HTTP client calls in triggers (unpredictable latency blocks the waiting user) — use background session/page background task; cache external values when they don't change often.
- OnOpenCompany must be fast: runs for every child session, background job, and API request. Gate expensive work by client type (do it only for real interactive sessions) so API stays fast.
- Don't over-add integration events (base app ~22k events; code unit 80 has heavy hot methods with 8+ subscribers in ~83 lines). Even unused events cost a method invocation to discover "no subscribers." Reuse existing events; design events for broad reuse.
- Prefer push (**web hooks**, doc'd subscription) over polling APIs (`is timestamp > X`) — polling threads hog machines just to find no new data. Subscribe → get change notification → then call in.
- `SelectLatestVersion` — always pass a **table ID**. Without one it invalidates the entire NST cache for all tables (badly placed in a login process = full cache flush every sign-in). Verify with a table no. so only that table refreshes. (Compiler warning for the no-arg form suggested but not yet shipped.)
- Reading uncommitted data (dirty read): if the writing txn rolls back, your read was invalid — acceptable trade-off for optimistic/observer scenarios (item availability, job-queue status where the record locks itself). Pattern: read uncommitted, do work, then read committed + lock only at the end before commit.

### Telemetry & Application Insights (diagnostics)

- BC emits telemetry to an Azure **Application Insights** resource. Two config levels: *service-level* (set on the environment — external calls, slow SQL, deadlocks, lock timeouts, page/report perf) and *resource/app-level* (set via the app.json AppInsightsKey / connection string — per-extension usage across all tenants/customers).
- One AI endpoint can collect from many customers/tenants — enables cross-customer comparison (e.g. slowest page averaged over all customers vs one). Per-customer endpoints make aggregate stats hard. Practical pattern: a few shared endpoints (customer service-level, ISV app-level, PTE/custom-dev app-level, test system) rather than one per customer.
- Data lands in two tables: **traces** and **pageViews**. These are the only tables BC writes to.
- Query with KQL (Kusto). Options to consume: the free Microsoft-published Power BI app (search "Microsoft 365 [sic — 'Usage Analytics' / Business Central usage] app", connect via AI Application ID + credentials); **Azure Data Explorer (ADE)** dashboards; or the AI Logs blade. ADE persists query tabs/state, supports pinning tiles to dashboards, view-underlying-query, and dashboard **parameters** (time range out-of-box; custom params incl. query-backed dropdowns e.g. tenant list).
- Telemetry availability: BC 2019 release wave 2 (v15/16) and later.
- **Tenant mapping**: raw telemetry shows only AAD tenant IDs. Can map IDs → friendly customer/domain names (Power BI report supports this; or maintain an external JSON lookup joined in KQL).
- On-prem gotchas: no reliable AAD tenant ID (often "default"/"common" unless multi-tenant/AAD configured) — identify customers by company name field present in many events instead. **Deadlock capture and lock-timeout monitoring are OFF by default on-prem** — enable via PowerShell (both on by default on SaaS).

<!-- ingested: BC TechDays 2022 - Telemetry for Business Central from basic | 2026-07-26 -->
### BC telemetry — basics to advanced (mibuso TechDays 2022 — Kenny Pontoppidan (MS) & Krzysztof Bialowas [sic? verify spelling])

**Enabling & sources**
- All telemetry lands in an Application Insights resource. Two source classes: **platform telemetry** (emitted automatically, not developer-controlled) and **custom telemetry** (developer-emitted signals).
- Enable as a VAR at the environment level via BC admin center (or admin center API); on-prem via PowerShell. ISVs enable by putting an App Insights connection string in `app.json` — this separates VAR telemetry (per-environment) from ISV telemetry (per-app, cross-tenant).
- ~0.5% server performance penalty when telemetry enabled; not user-noticeable.
- All telemetry is GDPR-compliant: e.g. job-queue-failure signals show *that* it failed, not the raw error text.

**Event ID conventions**
- Every signal carries an `eventId` in `customDimensions`. Prefix groups: `LC*` = lifecycle, `RT*` = runtime, `CL*` = client [sic? confirm], `AL*` = application/base-app events. Custom feature-telemetry events are prefixed `AL` too — must include that prefix when querying.
- To decode an unknown signal: copy its eventId (e.g. `RT0005`) and search docs at `aka.ms/bctelemetry`. All documented events have sample KQL in the BCTech repo (samples/AppInsights/KQLQueries).

**Telemetry categories (partial)**: environment/company/extension lifecycle, authorization, permissions, configuration, package/database state, long-running queries/SQL, AppSource submission process, Key Vault secret usage/failures, error handling, sensitive-field monitoring, job queues, page views, report generation, retention policy, onboarding/checklists, web-service requests, database wait statistics. Some categories also emit on-prem (documented per-category on Learn); on-prem cannot emit AD tenant ID.
- AppSource submission telemetry: MS validates each app against every declared country AND against the exact `application` version range in `app.json` — lets you see precisely which platform-version validation failed.

**KQL notes**
- Most telemetry (except page views) lands in the `traces` table; page views in `pageViews`. Actual data is in the `customDimensions` JSON column.
- Execution order maps SQL→KQL: table source → `where` (filter early) → `project` (= SELECT) → `summarize by` (= GROUP BY) → `sort by` (= ORDER BY); `top`/`take`/`limit` for top-N. Filter on timestamp early to cut cost while iterating.
- Powerful operators: `let` (scalar and tabular), `union`, `join`, `parse` (regex into columns), `extend` (calculated columns), `evaluate pivot(...)`, and window functions via `prev()`/`next()` after an explicit sort (e.g. compute row-to-row duration deltas).
- Kusto Explorer recommended as the query tool (link on BCTech).
- **Database wait stats** pattern: each snapshot is cumulative across ~23 categories; meaningless alone. Diff two snapshots (using `prev()`, guarding for environment boundaries and chronological order) to get waits in the interval — enables SaaS performance tuning previously impossible.

**Custom feature telemetry**
- Use system-app codeunit `"Feature Telemetry"` [sic? verify], functions `LogUptake` and `LogError`. Uptake status enum covers Discovered / Set up / Used / Undiscovered — instrument page-open (discovered), button/option (set up), and code path (used).
- `LogError` captures errors not surfaced to the user, and "impossible" code paths.
- Feature telemetry is emitted to BOTH the VAR (environment) and the app publisher (ISV connection string).
- To emit, register a logger: implement interface `"Telemetry Logger"` [sic? verify] with a `LogMessage` procedure, and subscribe to `codeunit "Telemetry Loggers"` event `OnRegisterTelemetryLogger` to register it. Without this contract the signals are not sent.
- Signals carry tenant ID, extension/publisher, company, feature name, uptake status, object number/name/type — usable to identify which customer/company/object emitted.

**Power BI apps (no KQL needed)**
- `aka.ms/bctelemetryreport` → "Business Central Usage Analytics" Power BI template app (for VARs). Installs with sample data (usable for pre-sales without customer data). Connect by supplying the App Insights **Application ID** and a look-back window (up to ~2 years, bounded by retention); refreshes nightly with a sliding window.
- Four areas: Usage (sessions by AD tenant/type/interactive-vs-background, clients, browsers, locations, languages, page views, report usage incl. Excel layouts, feature usage, onboarding checklists, integrations, connectors), Errors, Performance (long-running SQL with AL call stack + statement + join count), Administration (version/localization inventory, days-until-update, change report across environment/extension/field/config changes).
- Absence of data is itself signal (untested pages, unused features/apps, no connectors).
- A separate ISV-focused Power BI app also exists (announced public preview at this talk): adds Key Vault usage/failures, app-update performance, cross-tenant install inventory, version-to-version update flows, and noisiest-environment/event-ID views for cost planning.

**Notifications / being proactive**
- Three alerting options: (1) App Insights native alerts (paid, inflexible — email/SMS only); (2) Power Automate; (3) Logic Apps. App Insights has no push trigger — use a timer trigger (e.g. every minute) that runs a KQL query and acts if rows returned.
- Pattern: run KQL for a failure event (e.g. job-queue failure or app-install error), if count > 0 run a second query, render results as an HTML table, send via email/Teams/DevOps. Enables contacting a customer about a failed install before they notice.

**Cost control**
- App Insights: 5 GB/month free ingestion; default 90-day retention (often too short for ISVs tracking installs/upgrades — can extend).
- Levers: (1) **daily cap** — stops ingestion past a threshold (loses data, not money); (2) **data collection rules** — filter/sample before ingestion (e.g. keep only failed web-service calls); (3) **custom endpoint** — point BC at your own Azure Function instead of App Insights directly. Connection string only needs `InstrumentationKey=...` plus the ingestion endpoint host; MS sends the documented App Insights payload format, then you route/store/split as you like (community splitter + filter function by AJ Kauffmann [sic? "Angel Kaufman" in captions — verify; NL MVP]).

**User → telemetry linkage (Wave 1)**
- User card has a **user telemetry ID** field: a rotatable pseudonymous GUID (not the user ID). Lets a VAR attribute actions to a user while staying GDPR-compliant; rotating or zeroing it (tenant admin) breaks the link, satisfying right-to-be-forgotten.

**Partitioning guidance**
- Share-with-customer: one AD tenant/environment → one App Insights → one Power BI, per customer (simple, no leakage).
- Cross-customer analysis: use the splitter function to send one copy to the customer and one (optionally sampled) to yourself, then Power BI on top.
- In cloud a single App Insights key for all apps/customers is fine — filter by environment name. On-prem, use one App Insights per customer/environment since AD tenant ID isn't emitted (or inject a fake instrumentation key routed via custom endpoint).
- On-prem firewalls can block egress to the ingestion host — give IT the connection-string endpoint host to allow (watch for changing IPs).
- Multi-App-Insights querying is done from the Log Analytics back end (union across resources), not from a single App Insights blade.

### Telemetry-based perf analysis

- Duration field naming is inconsistent across signals (duration / executionTime / serverExecutionTime / totalTime). Build one coalesced "elapsed time" field in a KQL base query/view and reuse.
- **Deadlocks**: SQL kills one victim and logs only that one — must accumulate many samples per customer to reconstruct both processes. Deadlock counts correlate strongly with BC version; **upgrading to v23 (snapshot/optimistic locking changes) cut ~90% of deadlocks** in the presenter's data — upgrade customers below v23.
- Parse the **stack trace** to split each slow event into two dimensions: *source process* (bottom of call stack = process entry, e.g. codeunit run) and *slow object* (top of call stack = where time is spent). Split trace on newline, regex out object type/id/line. Lets you aggregate "which process causes most slowness" vs "which object is slowest".
- API incoming-call event ID **RT0008 [sic? — verify against Microsoft Learn]** exposes the OData query filter (not the body — body withheld for GDPR). Use to audit how partners filter your API; catch filters on non-indexed fields → add index or redirect to lastModifiedDateTime.
- SQL-statement telemetry lets you spot AL anti-patterns: many columns in SELECT ⇒ missing SetLoadFields / partial records; `SELECT TOP 1 … WITH UPDLOCK` pattern ⇒ locking IsEmpty (fix with read isolation); locking CalcFields; locking COUNT.
- Actionable filter trick: only events **with a stack trace** have AL code behind them (changeable); no stack trace = platform/page — filter to actionable ones.

### Custom telemetry

- Emit with `Session.LogMessage` — custom event ID + custom dimensions (add any fields). Default dimensions already provided by platform — don't re-add.
- **Telemetry Logger interface [sic? — verify exact name/pattern on Microsoft Learn]**: implement to inject app-wide custom dimensions (e.g. license status) into every `Session.LogMessage` call. Only ONE implementer per publisher; platform dispatches to the registered publisher's logger.
- Treat custom telemetry as an API contract: never change event IDs or dimension field names (breaking); document signals.
- Ideas demonstrated: instrument test framework events (OnBefore/OnAfterRunTest at suite/codeunit/method level) to emit SQL-statement count + duration → performance **regression testing** across daily runs (needs an AI endpoint configured on the test container). Generic start/stop measure codeunit around any operation (e.g. OnAfter Post Sales) for cross-customer/date perf comparison.
- **Daily telemetry**: SaaS runs a job-queue codeunit raising `OnDaily... [sic? — daily telemetry event; verify name]`. Subscribe to emit daily product-wide signals, e.g. missing indexes (aggregate most-missed index across all customers — don't create an index missed only once) and **media orphans** via `Media.FindOrphans` / `MediaSet.FindOrphans` (available ~v20/21) — orphaned media IDs point to blobs with no owning record, bloat DB; caused by Modify/Delete without Validate or batch picture imports.

### Cost control

- High-volume noise (e.g. Jet Reports generating tens of millions of signals/day) inflates AI cost. Don't cap signals/day (loses important ones). Instead set **Data Collection / transformation rules** in the Log Analytics workspace: right-click traces/pageViews table → create transformation → KQL that allow-lists what to keep (e.g. drop successful authorization and API-call signals except named customers/your own API/SOAP). Rule is a KQL `source | where …` filter.

### Related tooling

- **BC Performance Toolkit**: orchestrates simulated concurrent user load (define N users per scenario, e.g. adjust cost entry, calc plan worksheet). Run daily in each context (base app / +ISV product / +customer customisations), capture duration + SQL-statement counts to set a **performance baseline**; graph over time — flat lines good, deviation = regression to investigate.

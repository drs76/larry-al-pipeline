# bc-performance-scaling

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2019 - NAV/BC for high demanding environments | 2026-07-27 -->
### bc-performance-scaling (NAV/BC high-load environments)

Context: e-commerce, ~10k+ orders/day, 100k+ items, 100M+ record tables, 100-200+ users, 24/7 uptime. Pure NAV/BC perf tuning, mostly on-prem/IaaS.

**Front-end / page filters:**
- Default column filters (the per-column filter row) generate SQL that searches the filter value across every field of the page's underlying table — on huge tables this is very slow. Consider disabling for users who need speed.
- Filtering fields one at a time = one SQL round-trip per field. Reduce trips by building a custom filter page where user enters all filter values at once, then apply as single query with controlled index usage.
- Custom "search" pages give control over the query plan: pick a suitable index, or stage data in a heavily-indexed side table (incl. INCLUDE columns), or offload search to an external search engine (50-100ms lookups by email/phone/order no.).
- SQL priority may override your index hint on very large tables; not always honorable.
- Web client speed varies by browser; extra page controls widen the gap. Client version upgrades can regress perf (lazy loading etc.) — retest after upgrade.
- FactBoxes (e.g. Sales Order right pane) cost load time even with background loading; large docs (thousands of lines) make it worse. Want a feature-switch to disable per user.

**Back-end patterns (move heavy work off the front end):**
- **Posting buffer**: don't post synchronously on button click. Write doc to a buffer table, let background jobs post in parallel. Users see ~instant response; parallel posting jobs avoid table locks users would otherwise hit.
- **Reporting buffer**: decouple printout from posting. On "done", copy needed data into a report buffer table used as the report's data source, so the printout works without posting.
- **Stock buffer** / **payment buffer**: maintain a separate available-stock and open-balance layer so users don't need immediate posting to see stock or customer balance. These buffers can also feed high-throughput external APIs (100s calls/sec) without hitting NAV web services directly.
- Use fast CPU for the posting process specifically — biggest posting win.
- With buffers you can eliminate long nightly batch jobs; posting spreads across the working day, freeing nights for infra work.

**Rules of thumb:**
- Adding indexes to standard tables usually does NOT help and often hurts.
- Avoid modifying standard functionality where possible; prefer own objects/extensions.

**Monitoring / diagnostics:**
- Track long-running queries and set SLAs.
- Key SQL wait types to watch: locks (from too much concurrent posting — buffers fix this), async network/IO (queries returning too much data, middle-tier can't drain fast), parallelism waits (CXPACKET-style [sic? he described "splitting queries across threads / more cores"]).
- System waits (task scheduler, active session) show at top but are fast, usually not the problem.
- To reproduce a real plan: capture the exact parametrized statement NAV/BC sends via SQL Profiler and run THAT in SSMS — running your own hand-written query gives different perf due to parameter sniffing. SSMS live execution plan built-in since SQL 2016.
- Deadlock graphs on standard tables often involve index fields NAV maintains and FlowField calc; smaller tables may not need certain index fields.
- Host name in query context reveals number of NST servers in the deployment.
- Native AL diagnostics: SessionSettings/telemetry, write to event log or files, code coverage/AL profiler in recent VS Code — but heavy tracing itself degrades perf.
- **Gotcha / wishlist**: SQL queries from BC carry no user ID, so you can't tell which user caused a slow/locking query — large teams waste much time identifying the culprit. (By design for cloud/multitenancy.)
- NST performance counters exist (sessions, memory) but heavy monitoring slows the server.
- Build custom telemetry: fire-and-forget external HTTP calls on order/status changes (don't await response), or write start/end timestamps to small tracking tables and scrape externally. Track: all jobs running, per-step process health, posting/release throughput over time, and trends across weekly deployments and version upgrades.

**Cloud / IaaS (Azure) migration for scaling:**
- Rationale: 24/7, geo failover, easy scale up/down, public access (no VPN across sites), load balancers, App Service, Application Insights, custom high-throughput APIs, non-relational DB for hot data.
- One VM/NST per ≤50 users as a nicety (not required); ~4 cores + 16GB RAM is plenty. Cores are rarely the bottleneck; you often need less than on-prem sizing.
- Bandwidth: ~2 MB/s per RTC user, less for web client (web client renders server-side). 15 users fine on ordinary broadband; no VPN needed.
- Cloud pushes perf-driven development: test perf against 100M+ record sets, not 5 local records; watch read counts and avoid long transactions in core-change reviews.
- **Web client memory leak gotcha** (2018-era): the web client server process consumes all RAM over time, slowing/blocking all users; bumping VM RAM only delays it. Mitigation: restart the service (nightly). Long-running reports suspected but he tested 2h reports and could NOT reproduce — root cause open.

**Upgrade / go-live downtime reduction:**
- Biggest time sinks in version upgrades: (1) data migration/transformation code in standard upgrade codeunits; (2) having to open the DB with each intermediate client version when jumping releases.
- Convert standard upgrade-codeunit data migrations to direct SQL scripts — hours become minutes.
- To speed the multi-client-open step: split the large DB into N smaller DBs, open/convert them in parallel, then merge back.
- Script all deployment setup + data manipulation (PowerShell / SQL / build pipeline) to minimize downtime.
- **Feature switches**: deploy new functionality behind a toggle, enable during low load, disable instantly if broken — no core rollback.

**Standard-code perf gotcha:**
- Adding/editing a single line on a purchase invoice with ~10k lines triggers full invoice-discount recalculation across all lines (~25 min). Regression vs older versions. Wants a feature-switch to skip invoice-discount recalc.

**SaaS limits (2019/2020):**
- SaaS per-tenant DB cap cited as 85 GB — blocker for TB-scale tenants at the time; verify current limit against Microsoft Learn.
- Multi-environment split strategy: put production/warehouse app in a separate environment/tenant from core (independent upgrades), even mixing versions.

**Team/roles:**
- High-scale BC needs a dedicated ops role (VMs, SQL, load balancers, PowerShell) and a QA/test-automation engineer for regression + smoke testing (not just AL unit tests) — cited as the biggest staffing gap.

<!-- ingested: NAV TechDays 2019 - How to run faster in SaaS | 2026-07-27 -->
### BC SaaS architecture & performance (NAV TechDays 2019 — how to run faster in SaaS)

**Infrastructure (as of 2019, subject to change):**
- NST instances run on Azure VMs, ~4 cores, 14–16 GB RAM. Service Fabric cluster holds ~5–8 NST instances.
- SQL uses elastic pools. Three tiers; cheaper on HDD, premium (P4) on SSD — main difference is disk latency. Production tenants get premium; sandboxes/trials get standard.
- One elastic pool packs 1 to ~100 tenant databases depending on size/activity.
- Primary tenant DB has 2 replicas (mirrors) = two-phase commit on write. `COMMIT` is more expensive than on-prem (microseconds, but non-trivial) because all replicas must ack.
- ~1 ms latency between NST machine and SQL machine.

**Throughput fundamentals (rough, non-scientific):**
- Pure AL: ~300,000 statements/sec.
- SQL round-trips: ~300 queries/sec (latency-bound) — ~1000x slower than AL. So SQL statements dominate perf; optimise those.
- Rule of thumb: ~10 AL statements per 1 DB call (10:1) in typical codeunit code.

**Thread scheduler:**
- Round-robin time-slicing, 50 ms per slot. Active simultaneous threads = 3–4 (depends on cores).
- ~20 slots/sec total. When a session issues SQL, thread yields to next session while waiting; under heavy load you wait for your next 50 ms slot for the result.
- v15.1 [sic? "15:1"] adds prioritisation of UI sessions over background/service sessions, and fixes a bug where the time slot wasn't always yielded back to the scheduler during SQL waits.

**Cache synchronisation:**
- Multi-machine cache invalidation: writes stamp a cache-sync table in the app database; other NSTs listen and flush their caches. Frequent writes to same table across machines = constantly cold caches.
- Improvement: moved cache-sync messaging off the app DB onto a service bus [sic? "as a service" — likely Azure Service Bus] for faster/more reliable delivery.

**Load balancing / tenant affinity:**
- Old model: L4 hardware load balancer, plain round-robin per request — caused skewed sessions and cold caches.
- New: custom L7 gateway service + a tenant-balancer service that maps tenants→machines. Users from the same tenant routed to the same NST for warm cache (big tenants may still be spread across nodes).
- Task scheduler (underlying job queue) also asks the balancer which node to run on — warm cache, but can overload a node; experimenting with dedicated task-only machines.
- Old cluster balancing was by tenant count per cluster; problem: idle trial tenants stick to a cluster until next update, so tenant count ≠ load.

**Isolation-level bug (fixed ~2019, shipping to on-prem next):**
- NST adds SQL hints per transaction isolation mode (e.g. `READUNCOMMITTED`, `UPDLOCK`). Bug: for extension (companion) tables the hint was sometimes never added → excessive locking in some scenarios. Verify against release notes.

**Telemetry (Application Insights):**
- Set the AI instrumentation key in Admin Center → Environment → "Application Insights key". Enabling **restarts the tenant** — do it off-hours.
- Query the `traces` table in Log Analytics/AI. Custom dimensions include object ID, object name, AL call stack, and the actual SQL statement for long-running operations.
- Internally MS uses ETW/Kusto (Kusto Explorer, not public). 2019: only long-running SQL statements emitted to partner AI; errors, report execution time, page load time coming later.
- Key SQL metrics to watch: SQL wait types (waits on locks = fix your locking/queries; waits on network I/O = NST not consuming results fast enough), and per-query execution time (bad queries = missing filters, e.g. a report pulling ~10 GB into the dataset).

**Profiling advice:**
- Cloud NST is the *same binary* as on-prem — reproduce/profile locally first.
- Tools: on-prem SQL Profiler; dotTrace [sic? "blood trace"] Timeline profiler — start the process under the profiler (don't attach to a running NST) for more data; server restarts on start. It lists every SQL query with execution time, plus per-method CPU/memory/JIT/wait time. Use "user methods only" and right-click→mark-as-system to filter noise; merge occurrences per method.
- Check every statement has the correct isolation mode — e.g. an aggregation running under UPDLOCK for 200 ms locks all aggregated rows. Sometimes COMMIT before, or move work to a separate transaction, to avoid locks.
- Note on lock semantics being debated: after `LOCKTABLE`, everything you subsequently touch on that table is locked, not just the specific record — MS considered restricting locks to the explicitly locked instance.

**Perf regression testing:**
- MS counts executed SQL statements + row reads per scenario, on every build, and emails the author on regression. More stable/reproducible metric than wall-clock time.
- Use `SessionInformation` object [sic? verify name] to read SQL statement count and row reads at test start/end (instantiate counters before the action so you measure only the action). Debug variables also show the last ~10 fired SQL statements (configurable).
- Classic regression: subscribing to `OnModify` (database event) turns one `MODIFYALL` (single SQL) into a per-record loop, since the event fires per record. Mitigate with the subscriber's RunTrigger/`Modify(true)` semantics — heavily debated tradeoff (keeping a companion table in sync requires firing per record).

**New performance-related platform features (BC 2020 wave / v15–16 era):**
- **Number sequences** — surfaced as SQL `SEQUENCE` objects (visible under Programmability). Use for any integer counter. Backs number series via an "Allow gaps in numbers" toggle (can turn on/off live) to avoid locking on the No. Series line; downside is gaps on rollback and the last-date-used field is cleared. Don't use gap-allowed sequences for posted documents; fine for customer numbers etc.
- **Page background tasks** — enqueue a background task from a page, wait for complete/fail, exchange results via dictionaries. **No writes allowed** in the task (avoids "another user modified" errors). Task auto-cancels if the user moves off the record (so unsuitable for expensive flowfield calc on list lines).
- **Immutable/system ID** — `$systemId` (SystemId) field added to every table. Stable across primary-key changes and delete+reinsert. Indexed with sequential GUIDs (cheaper to index than random GUIDs). Can be inserted at insert time (incl. via API POST) but not updated. Access via RecordRef get-by-system-id, not by field number.
- **Read scale-out / "Data Access Intent"** — declare read-only intent on a connection so SQL routes to a replica instead of primary (works on-prem too; routes to primary if no replica). Targets: web service/API/OData, reports, queries; MS debating list pages (expensive outer-join/flowfield queries that don't update data).

**Report optimisation pattern (reduce SQL statements):**
- Nested data items (e.g. G/L Account → G/L Entry) fire one query *per parent record* (N+1). With items/value entries this explodes.
- Fix without rewriting layout: declare one global source record; `SETAUTOCALCFIELDS` for calc/date fields; set inner data item to a temp table (`SetTempTableView`/`temp=true` [sic? verify property]) and populate it in code as the outer loop proceeds. Demo: G/L trial balance dropped from ~225 (or ~597 on extended demo data) SQL statements to ~20.

**Scale-out / parallelism:**
- Split large batch work (all items/customers) into chunks, run via background sessions, join at end. Example: RapidStart (config package) import sends each table's XML blob to a background session and waits for all — cut a slow import from ~20 min to ~10 min. Uses StartSession-style pattern.

**Report rendering note:** ~80% of report time is data collection, ~20% rendering. Word layouts render as fast as/faster than RDLC. Customer-specific layouts (per-customer statements) are expensive because one report instance is generated per customer.


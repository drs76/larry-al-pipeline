<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Large customers, job queues, locking, BCPT

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 1. Platform, Runtime & Performance

### Handling large/high-concurrency BC SaaS customers (mibuso session)

**What actually makes a customer "large"** — DB size and licensed-user count are misleading. The real load drivers are: transaction volume + type (shapes locking), concurrency (concurrent active sessions, incl. background/integration), DB growth rate, integration complexity (web-service call volume — the "silent enemy"), and 24/7 requirements. A 1 TB DB with few transactions is easy; 100 concurrent users + thousands of web-service calls/min is not.

**Long-running query threshold** — Microsoft's telemetry flags a SQL query as long-running at >750 ms. Use Azure Data Explorer (KQL) over emitted telemetry rather than the Power BI app for near-real-time analysis; telemetry carries no PII. Useful cuts of the long-running-query signal: filter by client type (Background vs WebClient vs WebServices), by emit timestamp (spot night MRP/job-queue jobs bleeding into work hours), regex the SQL statement text to bucket select/update/insert/delete ratios, correlate by stack trace (like the old Client Monitor CL↔SQL correlation), pivot query count/avg-duration per day to measure before/after a code fix.

**Automatic cost adjustment** — disable `Automatic Cost Adjustment` in Inventory Setup for high-transaction customers; when on, cost adjustment runs inline during posting, taking extra locks and killing posting throughput. Schedule the Adjust Cost - Item Entries report as a background job instead.

**Serialize to kill concurrency** — route posting through background/job-queue serialization to avoid gel-entry [sic? G/L Entry] lock timeouts (the 30s "we can save your changes" error) under concurrent posting.

**Number sequences vs No. Series / autoincrement** — the `NumberSequence` AL object (data type + keyword) is backed by SQL SEQUENCE objects, not a table row, so obtaining a number takes no table lock — far better for concurrency than No. Series (which locks the last-no. row) or SQL identity/OnInsert increment. Can be per-company. Cost is per-ticket latency, so reserve a range in one call when inserting many rows: reserving 10,000 numbers ~40 ms via NumberSequence vs ~2 s via No. Series. Drawback: reserved ranges leave gaps on error — fine for ledger/warehouse entries, not for gap-free fiscal document numbering. Enabled for warehouse entries in v25 (opt-in via Feature Management); v26 extends it to item ledger + value entries. Also in v26 a **sift bucket number** field is added: assigned before insert to statistically spread SIFT rows and cut deadlocks on SIFT keys. Migration: enable the feature flags, add the sift bucket field to your keys — reportedly ~95% good to go.

**Flow fields — calculate only visible flow fields** — v26 preview feature (Feature Management, default OFF; recommended ON) makes a page skip calculating flow fields that are `Visible = false`. Without it, BC calculates all a page's flow fields even when hidden, so one visible flow field on a table with many flow fields still pays for all of them. Caveat: a normal calculated field whose formula references two non-visible flow fields won't compute. Alternative for responsive statistics pages: **page background tasks** — main page passes a parameter to a background codelet that does the calc with read isolation + SetLoadFields, page stays responsive and fills values in when ready.

**Locking hygiene** — apply `ReadIsolation` (ReadUncommitted/ReadCommitted etc.) on CalcSums/IsEmpty/Count and reads that don't need locks to remove needless shared locks that cause lock timeouts/deadlocks. Prefer new AL statements: SetLoadFields, ReadIsolation, `ReadOnly` (uses the read replica query object). Avoid `LockTable` — count and duration of it are up in base-app v26 mostly from copy-paste; devs should rarely use it.

**Avoid loopy loops on huge tables** — replace nested AL record loops that aggregate over a multi-million-row child table with `query` objects (joins + sums run at the DB level). Example cited: ~13 s AL loop → ~1 s query.

**Data growth & retention** — plan retention policy at implementation time; deleting a huge table later on SaaS is painful (had to hand-roll a job queue deleting in small batches over a week because the built-in retention deletes 10k at a time and chokes). A table only appears in the Retention Policies setup if declared as supporting retention — for your own/third-party tables add it in an `Install`/upgrade codeunit via the system-app retention-policy setup API (`RetenPolAllowedTables` [sic? verify object name]). Only the app that owns the table can register it — needs a dependency on the owning extension + the permissions, or ask the publisher / use base-app contribution. Monitor via the retention-policy telemetry signal (rows deleted, run frequency). Track DB growth rate month-over-month via Admin Center capacity or the admin API.

**Blobs out of the DB** — never store blobs/PDFs in the BC DB. Subscribe to an event on the Document Attachment table and redirect the blob to Azure Blob Storage (cheap); transparent-ish to the user, keeps the tenant DB small (and out of every sandbox copy).

**API integration for high call volume**
- Use the read-only replica for read-heavy API objects. Business Critical tier provisions a read replica; General Purpose does not. Set read intent three ways: on the object (API query / API page / report — must have no writes), via the `?$dataAccessIntent=ReadOnly` [sic? verify param] URL param on the GET, or centrally via the **Database Access Intent List** page. Telemetry has a signal for most-used reports — sort by count, flip the top ~30 to read-only. On-prem read intent doesn't guarantee a replica; online depends on tier.
- **Batch API** — POST to `/api/v2.0/$batch` [sic? verify path] with an array of sub-requests each carrying an id, to collapse many calls into one. Headers: `Isolation: snapshot` [sic? verify] to treat the batch as one all-or-nothing transaction; a continue-on-error option [sic? `continueOnError` / `Prefer` — verify]; and `Prefer: return=minimal`/`return=no-content` [sic? verify] to suppress the echoed JSON body and get only per-item status.
- **Caching middle layer** — external GETs hit an Azure Function (Flex Consumption model: highly scalable, no cold start) backed by Azure Redis Cache instead of BC directly. Function checks cache, returns on hit, else calls BC API, stores with a TTL (e.g. 5 min), returns. Massively offloads read traffic; trade-off is staleness bounded by TTL — set per entity. For POSTs (uncacheable) use the same function to enqueue into Azure Queue / Service Bus and let BC drain the queue, serializing and detaching heavy posting.

**BCPT (Business Central Performance Toolkit)** — use to reproduce concurrency load: publish the test codeunit, define a suite/scenario (sessions, duration), run and compare runs (baseline vs new version). Emits to telemetry + log-entry tables (build an analysis view / export to Excel pivot). Online BCPT targets sandboxes only, not production, and the sandbox DB tier is low — good for surfacing concurrency/locking issues, not for true production-scale load timing. Note: changing a Feature Management flag mid-suite requires a fresh login/session for spawned sessions to pick it up.

<!-- ingested: Turbo Mode: Job Queues in Parallel? | 2026-07-26 -->
### Parallel job-queue pattern for high-volume ingestion (mibuso — Jeremy Vyska)

- **Problem:** single serial job-queue codeunit processes one stage (validate → process → emit) across the whole batch before advancing; slow, and downstream systems (3PL warehouse) starve while orders back up. Scales only to a point.
- **Pattern:** run N job-queue entries of the *same* codeunit in parallel, each pulling **finite batches** of work. Every unit of work must be a **tiny atomic transaction** (`Commit` per item). NOT suitable when a whole batch must succeed/fail together (e.g. posting 10k journal lines as one unit).
- **Claim/coordination without locking the source queue:**
  - Naïve claim = filter + `ModifyAll` on the queue table = one write per row = heavy locking. Instead **write-once**: each session picks its batch of primary keys, serialises them to JSON in a blob on a separate control table (row = code + claim timestamp + session id).
  - Each session, before selecting, reads all *other* sessions' control rows, rehydrates their JSON into a combined list of already-claimed keys, and skips any key where `list.Contains(key)` is true. Avoids double-processing without row locks on the queue.
  - Cleanup keyed off the session id stored in the control row.
- **Keys:** demo used single GUID → .NET `List`. For composed/GUID primary keys, store each key as a delimited **string** in a `List of [Text]`, then split back into components at `Get` time. **System ID** is a good claim key — immutable, avoids caring about key composition.
- **Prefer .NET `List`/`Dictionary` over temporary tables** for simple in-memory sets — temp tables are backed by .NET dictionaries/lists under the hood, so skip the middleman.
- **Dynamic batch sizing:** store a target op count with min/max guard rails. After each run compare actual runtime to the job-queue's "minutes between runs"; if faster, grow target ~10%, if slower shrink ~10% (round; clamp to min/max). Lets throughput scale up/down with load.
- **Parameter string:** pass the job-queue entry's parameter string into the codeunit to specialise an instance to one stage only (e.g. a dedicated always-on "emit" worker) so emit keeps flowing regardless of ingestion speed.

### Codeunit.Run as error boundary / isolated transaction

- `if Codeunit.Run(...)` runs the codeunit as a **discrete separate write transaction**; on failure returns `false`, and `GetLastErrorText`/`GetLastErrorCallStack` are available.
- **On-prem: disabled by default** — must be enabled. On cloud it's allowed.
- **Cannot be called mid-write-transaction** — must `Commit` first. If you don't, current Docker/on-prem just crashes with no useful message (event log unhelpful); older versions used to report "write transaction not allowed". 
- To roll back on failure, wrap the dependent writes *inside* the same `Codeunit.Run` (e.g. sales header + lines created together so header rolls back if line creation fails).

### Locking guidance (references Mads' tri-state locking session)

- Modifying a record and *then* reading another can lock more tables than expected. **Frontload reads before the write transaction starts** — gather all needed data into buffers/lists/dictionaries first, then begin writing and committing.
- Excessive in-transaction logging was a real source of lock contention — keep logging light inside hot transactions.
- Serial-number-tracked items are worst case for locking (one item ledger entry per unit) — good stress test.

<!-- ingested: Microsoft Presents: Tri-State Locking: Reducing locking in t | 2026-07-26 -->
### Tri-state locking — runtime read-lock reduction (mibuso — Microsoft, Tom[sic?] & Mads[sic?])

- BC uses the DB for cross-session/cross-process concurrency (AL is single-threaded per session). Read isolation levels used: read uncommitted, read committed, repeatable read, update lock. Writes use SQL default (exclusive lock) — platform does not decorate writes with hints, only reads.
- `LockTable` misnomer: takes no monitor/table lock. It only changes the *table state* for the current transaction so all subsequent reads on that table use the update-lock hint. It is a static/per-table effect, not per-variable — applies across all record variables of that table for the rest of the transaction.
- Any write (Insert/Modify/Delete/DeleteAll/ModifyAll) promotes the virtual transaction to a write transaction; internally, under two-state locking, writes implicitly behaved like `LockTable`.
- Transactions in AL are virtual until first DB op, then promoted; locks held until COMMIT or scope exit; error → rollback.
- Gotchas that escalate locks: `FindSet` on an empty table locks against all future inserts (you become sole inserter); `Count`/range operations in a write transaction take range locks (bigger than row locks); CalcFields on a flow field can take range locks; a failed Insert still enters write-transaction/lock mode.

**Two-state locking (legacy, default until v25, desupported from v26):**
- Reads use `read uncommitted` until a write or LockTable touches the table state in the current transaction; after that, all subsequent reads on that table use `update lock`.
- Caveat: rule holds only for the *default* transaction type.
- Problem: `update lock` is not self-compatible → two sessions reading same rows block each other. ~50% of observed lock timeouts came from reads, not writes.

**Tri-state locking (new):**
- Splits the old second state in two. States: (1) reads before any write/LockTable → `read uncommitted`; (2) after a *write* → subsequent reads use `read committed` (share locks, statement-scoped, released on return from SQL — not held to transaction end); (3) after explicit `LockTable` → `update lock` (unchanged, preserves existing intent).
- Internally writes no longer implicitly call LockTable (that would defeat the purpose).
- `read committed` (share lock) is self-compatible and compatible with update lock → far higher read concurrency after writes; share lock only blocks against exclusive (writers).
- Trade-off: read-committed reads leave no lock, so another session can modify a row between your read and a later write → stale data. Server detects override-of-stale-data on Modify (via timestamp check) and throws. Single-session stale scenario only reachable via DeleteAll-then-Modify path.
- `read committed` behaviour depends on SQL Server config: uses Read Committed Snapshot Isolation (RCSI) if enabled. Azure SQL has RCSI on (so BC uses snapshot); on-prem depends on setup. **On-prem caveat:** enabling RCSI adds ~14 bytes per row to every clustered index → large DBs can grow and (raised in Q&A) potentially cross row-size / DB-size limits.

**Rollout:**
- Tenants created after v23: ON by default. Older tenants: opt in via Feature Management ("Enable Tri-State Locking in AL"[sic? verify exact toggle name] → All Users). ON by default for all from v25 (can still opt out until v26). From v26: only mode, no opt-out. ~12% SaaS opt-in rate at talk time.
- Migration impact: BaseApp needed no significant app changes (already used read isolation in key spots); only minor test-platform tweaks.

**Read isolation (v22+) — per-record-instance override:**
- `ReadIsolation`[sic? verify property/method name] overrides table state for a specific record instance's next-and-subsequent reads, without affecting other instances (unlike LockTable). Reads only; no write hints. Values incl. read uncommitted / read committed / repeatable read / update lock.
- Use `repeatable read` to hold a share lock for full transaction duration (assures no writers) — but can block writers and cause deadlocks; use deliberately.
- **Temporary heightening** pattern: instead of `LockTable; FindLast` (which locks all later reads too), set update-lock read isolation on just the record before the read so only that read is affected. Recommended for event subscribers where you can't know incoming table state. Also supports temporary *lowering*. Generally preferred over LockTable unless you truly need whole-transaction update-lock behaviour.
- `Get` follows same locking rules as `Find` and is affected identically by read isolation / LockTable.

- SQL lock escalation: SQL Server escalates row locks to a table lock after ~5000 rows (memory-driven) — easy to hit via large Counts/reads on big tables.
- Resource: Mads' blog post + Microsoft Learn docs on tri-state locking and read isolation.

### Scheduled-task limits

- Background/scheduled task capacity is **~5 tasks per licensed user** in the environment (not per user who started the queue). 20 users ≈ 500 potential background tasks. Confirmed by MS as intended (simulates user-volume load).

### Job-queue scheduling & operational notes

- "Minutes between runs" is measured **from the end of one run to the start of the next**, not a fixed wall-clock interval. A 15-min job with 1-min-between will run ~every 16 min.
- **On-prem BC14 stuck 'In Progress' entries:** restarting the entry doesn't restart the process; often needs the NST service restarted. Common mitigation: run job queues on a **separate NST instance** restarted frequently.
- **Cannot change the run-as user** of a job queue — intentional (audit traceability requirements in some countries; the licensed user "consents" to the scheduled work). Workaround: a dispatcher job queue (owned by a consenting user) that starts other flagged job-queue entries.
- **Resilience over retries:** route malformed/blocked data (e.g. a blocked dimension can halt all web-order imports) into a separate holding table so the queue keeps processing; handle the bad data out of band. Consider a retry-count field on the work table for transient deadlocks.

### Telemetry for job-queue failures

- There is a telemetry event for **job queue failed / will no longer restart** — alert on *that* one only (retryable errors are just noise). A newer separate event distinguishes "errored, not restarting" from a plain error `[sic?]` (verify exact eventId against Microsoft Learn; presenter's LLM lookup guessed `H7` [sic?] but was unsure).
- Telemetry is not just for Power BI — e.g. an Azure **Logic App** can consume the failed event and fire a Teams/email alert to support.

### Performance toolkit

- Use the BC Performance Toolkit to run a codeunit across **multiple concurrent sessions** (foreground or background) to simulate real load — includes built-in scenarios (e.g. posting sales orders with N lines). Copy its logic for custom posting/ingestion scenarios. Surfaces read-statement counts and per-scenario timings.
- To test external-system coupling, mock via a codeunit that writes into the same tables an inbound API would (simulate fast vs slow warehouses).

<!-- ingested: BC TechDays 2022 - Business Central Performance Toolkit | 2026-07-26 -->
### BC Performance Toolkit (BCPT) — usage & gotchas (mibuso TechDays 2022)
- BCPT = whole-*system* workload simulation, not a stress tester. Models realistic concurrent load (e.g. "2 users creating purchase orders with a delay between iterations"), distinct from unit tests (single-unit) and scenario tests.
- Install: publish the BCPT extension (ships in Docker artifacts by default; on-prem often present but uninstalled in Extension Management; also on AppSource). Source + sample tests on GitHub — modifiable.
- Core object is the **BCPT Suite**; suite lines each point to a test codeunit the tool orchestrates. Key line fields:
  - **No. of Sessions** = concurrent simulated users per line.
  - **Run in Foreground** flag: page-testability (client UI interactions) only works in foreground. Background code is *not* captured by the client profiler.
  - **Delay (sec) between iterations**: pause after each iteration so it's not a stress loop.
  - **Tag**: label each run (e.g. `baseline`, `25`, `100`) to distinguish log entries later during analysis.
- **Log entries** (BCPT Log Entry): per run generates entries with tag, incrementing version no. (auto per run), start/end time, duration, codeunit no. + name, and SQL statement count per scenario. Default-filtered to latest version; clear filter to compare. Export via "Open in Excel" for pivot tables / Power BI. Filter by time to find concurrent activity when diagnosing locks.
- **Scenarios & stopwatches**: `Codeunit.Run` of a test = one scenario. Inside, `StartScenario`/`EndScenario` [sic? verify exact method names against BCPT library] bracket sub-measurements ("stopwatches"); can overlap. Each produces a log entry with the scenario name → gives SQL call count + duration. Use **generic cross-scenario names** (e.g. "enter account number" not "enter customer number") so purchase- and sales-side operations aggregate. Give codeunits/scenarios/tags good names — they become the pivot axes.
- Reuse existing page/unit tests as BCPT tests: unit-style tests use direct field assignment + insert; page-testability tests replay user actions. Both wrapped with start/end scenario markers.

### Running BCPT at scale — PowerShell driver + VS Code helper
- Running from the **client** works for early testing but has limits: page testability = only **one session at a time**; and the cloud caps concurrent **background jobs** (presenter didn't state the number — verify current SaaS limit).
- For larger loads, run the suite via the provided **PowerShell script**, which spins up parallel jobs hitting the web-client endpoint to emulate many client sessions (mirrors the SaaS load-balancer → multiple NST instances topology).
- A **VS Code extension** bootstraps a project: device-login to the tenant, reads **sandbox** environments (production is unsupported — only sandbox targeted), copies renumbered sample tests + the PowerShell scripts + config, and can launch the simulation without hand-entering all parameters.
- Prod vs sandbox performance parity is roughly equal; main difference is the SQL tier.

### BCPT test-authoring pitfalls
- **Number series ranges** in demo data are small — extend them before testing or runs error out by exhausting numbers.
- **Transaction granularity**: don't do everything in one commit. Real users commit per document save/action; model that so measured locking reflects reality, not the test's artificial single transaction.
- **Allow Gaps in No. Series**: without it, picking a number **locks** the series during the transaction (needed for legally gapless docs like posted invoices). Enabling Allow Gaps uses a SQL sequence = non-locking (but leaves a gap if the transaction fails). Enable where gapless isn't required to cut lock contention.
- **SIFT keys** create SQL indexed views; updating affected rows locks those view rows during the transaction → extra locking. Don't hard-code the same item/customer across sessions — spread values to avoid contention (also more realistic).
- **Resource starvation**: many sessions on one machine can starve it; split across two machines.
- **Page testability is flaky** — keep those tests simple/predictable to avoid failures counted as perf noise.
- Account for external pings (webshop, Power BI, web services) hitting the server during the modeled peak hours.

### BCPT — planning & analysis workflow
- Plan a "company simulation": enumerate scenarios, concurrent-user counts (incl. mobile/web-service/API), identify **peak hours** to emulate, define acceptable thresholds (page open, field validation ~1s, report duration), choose environment (on-prem image / Docker / sandbox).
- Analyze by exporting log entries to Excel pivot: rows = scenario/codeunit name, filter = operation, columns = tag, values = **average** duration (also std dev / min / max) in ms; pivot chart to show scaling vs user count.
- Integrations: incline **Performance Profiler** (start → run BCPT test → stop → open profile in AL profiler); **AL-Go for GitHub** action to run BCPT on every PR and flag regressions requiring sign-off; telemetry surfaces in the perf/monitoring app per build.

### Tooling asides

- **Paket + NuGet** can fetch AppSource symbols from Microsoft's NuGet feed instead of the AL "Download Symbols" command.
- `.github/copilot-instructions` and agent-mode rules files feed a repo README/conventions into Copilot on every request (id ranges from app.json, logging, comments, etc.).
- **Mermaid** gantt/flowchart in markdown is a cheap way to visualise process timings from log-entry tables (Copilot can generate a mermaid-emitter from your log schema). DATEFORMULA errors out on very large day counts (~45k+ days).

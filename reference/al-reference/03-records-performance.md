<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Record operations, data access, SQL-level tuning, locking

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 10. Record Operations & Performance

```al
// Get by primary key — throws error if not found
MyTable.Get(PrimaryKeyValue);

// Safe get
if not MyTable.Get(PrimaryKeyValue) then
    exit;

// FindSet for iterating — correct modern pattern
MyTable.SetRange(Status, MyTable.Status::Active);
if MyTable.FindSet() then
    repeat
        // process
    until MyTable.Next() = 0;

// SetLoadFields — load only needed fields (performance critical on large tables)
MyTable.SetLoadFields("Code", Description, Amount);
if MyTable.FindSet() then
    repeat
        // only Code, Description, Amount loaded
    until MyTable.Next() = 0;

// Modify — true = run OnModify trigger
MyTable.Modify(true);

// Insert — true = run OnInsert trigger
MyTable.Insert(true);

// DeleteAll guard — avoids table lock when nothing to delete (alguidelines)
MyTable.SetRange(Code, FilterValue);
if not MyTable.IsEmpty() then
    MyTable.DeleteAll(true);

// Bulk update — prefer ModifyAll / DataTransfer (no per-row loop at all):
MyTable.SetRange(Status, MyTable.Status::Active);
MyTable.ModifyAll(Processed, true);   // one set-based statement; see also DataTransfer (§21)

// Pass FALSE to Insert/Modify/Delete when the table triggers do nothing you depend on —
// the trigger cost is paid per row for identical behaviour:
MyTable.Modify(false);

// ⚠ Do NOT Commit inside a repeat..until loop. A per-row Commit starts a new transaction
// every iteration and throws away atomic rollback (BCQuality performance/avoid-commit-inside-loops).
// AL auto-commits the enclosing module on success — most loops need no Commit at all.
// If a batch is too big for one transaction, checkpoint via Codeunit.Run (each run = one atomic
// transaction with native rollback), driven by an OUTER loop that picks up the next N rows:
while ProcessNextChunk() do;   // codeunit filters next N unprocessed rows, updates, returns rows-remained
// ✗ if MyTable.FindSet(true) then repeat ... if Counter mod 100 = 0 then Commit(); until Next() = 0;

// CalcFields — required before reading FlowField or BLOB
MyTable.CalcFields("Blob Field");
MyTable.CalcFields(Amount);

// LockTable — lock before read-for-update in concurrent scenarios
MyTable.LockTable();
MyTable.FindSet(true);
```

**Newer performance features (2023w2–2026w1):**
```al
// SetBaseLoadFields — load all BASE-table fields (drops the companion-table join) in one call.
// Lower maintenance risk than listing fields; but SetLoadFields still wins for max perf.
MyTable.SetBaseLoadFields();

// ReadIsolation — opt into an update-log read per-instance instead of a blanket LogTable().
// Under the new locking model (default ~v24, mandatory v25) reads run READ UNCOMMITTED until you
// write to that table-type, then READ COMMITTED. See AL-KNOWLEDGE §1 for the full model.
MyTable.ReadIsolation := IsolationLevel::ReadCommitted;

// DataTransfer — targeted bulk update: filter destination rows + control audit fields (2026w1)
DataTransfer.AddDestinationTableFilter(FieldNo(Processed), '%1', false);  // only rows not yet processed
DataTransfer.UpdateAuditFields(false);   // now available in cloud — skip SystemModified update

// NumberSequence (2024w1) — 32% faster; Restart without drop/recreate; get a whole range in ONE DB call
NumberSequence.Restart('MySeq', 1000);
// range-get returns N numbers in one round-trip (vs N calls) — big insert-perf win

// && full-text filter (needs field OptimizedForTextSearch = true, §5) — whole-word / prefix
FieldRef.SetFilter('&& %1', 'Brazil');       // whole-word match
FieldRef.SetFilter('&& %1*', 'Bra');         // prefix / begins-with
// ⚠ if the field is NOT OptimizedForTextSearch this silently degrades to slow case-insensitive CONTAINS

// Visible-only FlowField calc (2025w1) — feature key; plus SetAutoCalcFields to control auto-update
MyRec.SetAutoCalcFields(Balance);            // call before FindSet in tight loops
```
`TestField` (2024w1) now auto-adds a **navigation link** to the failing record (no code) when a
DrillDown/Card page exists, the user has read permission, and it's a different record than the current
one. Prefer `ErrorInfo` (with `AddAction`) over plain `Error()` — it's the forward path for all new
error capabilities. **Query objects** support `RunObject` (open from a page action) and server-side
analysis views — prefer a query over a report for in-client analytics.

---

<!-- ingested: Microsoft presents: What's new in AL | 2026-07-26 -->

<!-- ingested: Validate() - all tables / all fields / always | 2026-07-26 -->

<!-- ingested: BC TechDays 2023 - Locking in AL: Runtime and explicit AL co | 2026-07-26 -->

<!-- ingested: Optimize AL Performance & Embrace New Guidelines | 2026-07-26 -->

<!-- ingested: BC TechDays 2022 - Coding 4 Performance | 2026-07-26 -->

<!-- ingested: BC TechDays 2022 - Bad habits of AL Developers | 2026-07-26 -->
### Bad habits / durable AL facts (mibuso BC TechDays 2022, Vjeko & waldo)

- **Object & field IDs carry no functional meaning.** Field ID does not control display order on a page or in table browse; order fields for readability if you want, but IDs affect nothing. Stop reserving ID ranges or numbering fields to force sort order.
- **Useless keys.** A key declared with SIFT index disabled (`MaintainSIFTIndex = false`) *and* SQL index disabled (`MaintainSQLIndex = false`) contributes nothing — delete it. Often left over from CL conversion or added only to silence a CodeCop "needs index field" warning.
- **Extensible enums need managed extensibility.** Marking an enum `Extensible = true` without code that handles unknown/added values is a latent bug; either don't make it extensible or write code aware other apps will add values.
- **Table-extension performance.** Each table extension is a separate SQL table joined at read time → cost grows with number of extensions on a table. Mitigate with `SetLoadFields` (partial records) so joins to un-needed extension tables are skipped; keeps read cost roughly flat regardless of extension count. Caveat: base-app standard code mostly does *not* use SetLoadFields, so extending heavily-used tables (Sales Header/Line) still pays the join cost in Microsoft code paths — you cannot fix that from an extension.
- **Observed (unexplained) quirk:** accessing a field *not* in the `SetLoadFields` list triggers just-in-time load (two SQL statements: partial + fetch) which measured *consistently faster* than a single full join. Presenter had no explanation (SQL/NST caching suspected). Treat as anecdote, verify before relying on.
- **"Table-extension-extension" anti-pattern.** Collecting all table extensions for a shared table into one dependency app cuts joins from N to 1 but creates heavy inter-app coupling; flagged as architecturally bad despite the perf win.
- **`ApplicationArea = All` is mindless.** Prefer specific application areas (e.g. `Location`) so fields hide for users not using that area. (Platform now supports setting app areas without repeating on every control.)
- **Tooltips:** don't set them equal to the caption or `Specifies the <caption>`. AZ AL Dev Tools (Andrzej Zwierzchowski) can propagate meaningful tooltips, reusing a good tooltip already defined for the same field on another page.

### Validate() — pure vs impure functions

- AL triggers, event publishers, and `Validate` calls are *impure* (side effects: modify global/DB state outside lexical context). Not evil, but you must know what each impure call triggers.
- **`CurrFieldNo` returns 0 when the code is not invoked from a page** — a `OnValidate` guard checking `CurrFieldNo` silently misbehaves when called from code. Common cause of botched fixes to circular validation.
- **Circular validation** (field A validate → field B validate → back to A) causes endless loop / errors; restructure so validation is safe under any call path (page or code, alone or with other extensions attached to the field). In SaaS you cannot assume which other extensions hooked a field's validate.
- Recommendation: do validate, but write validation code robust to being re-entered and to unknown attached validators.

### Code deprecation / refactoring

- Deprecate via `ObsoleteState` + upgrade codeunit path, **not** the force-install ("deploy despite errors") option — force risks unexpected schema/data loss and broken dependencies. Never automate a forced deploy.
- **Function deprecation with overloads:** obsolete the old procedure and add the new overload (e.g. add a parameter) side by side; let the compiler flag callers and handle the transition, rather than deleting outright. Obsoleting (vs deleting) matters because consumers compile against multiple runtimes — the compiler warns callers.
- Do obsoleted-field/table cleanup in scheduled bulk passes (e.g. once a year, with backup) rather than piecemeal.

### Commented-out code

- Delete dead code (git retains history) — don't leave commented blocks; you lose the reason it was commented. If code must be conditionally excluded, use conditional-compilation directives (`#if ... #endif`) instead of comments — the condition documents intent.

### Permission sets

- Don't ship `super` or a single auto-generated "all current extension objects" permission set — functionally no better than super. Consciously author permission sets **per module** (not per app), minimum a read-only and a read-write variant. Cannot be auto-generated meaningfully.

### Commit VS Code workspace/folder settings

- Commit workspace/folder `settings.json` (analyzers, format-on-save, recommended extensions, Object ID Ninja/CRS config) so the whole team shares config. Keep only personal preferences in *user* settings — three scopes: user, workspace, folder.

### Code-4-Performance — data access & coding patterns (mibuso BC TechDays 2022, waldo)

**Keys / indexes**
- Missing key still returns correct results (SQL scans) but slow — applies to `Count`, filtered reads, FlowField sums, queries alike. Don't under-declare keys; also don't over-declare.
- FlowFields on pages slow without a SIFT key. Two fixes: SumIndexField (SIFT) vs an **included column** on an existing index. Included column costs less locking to maintain than SIFT → try included column first; reserve SIFT for very large tables.
- Query indexing still matters — included columns are used by SQL Server (not the NST) inside queries.

**FindSet vs FindFirst/Find('-')**
- Simple loops issue the same SQL-statement count either way; difference is the read buffer. `FindSet` fetches in bulk → better when looping many rows (roughly >50). `Find('-')` can win only when very few iterations. When unsure, default `FindSet`.

**Partial records / CalcFields**
- `SetAutoCalcFields` before a loop → one statement instead of a `CalcFields` per iteration.
- `SetLoadFields` — apply on every read, always. Each installed table extension adds a SQL join; without SetLoadFields cost grows per extension. Consistent SetLoadFields removes that regression. Referencing a field you didn't load triggers a just-in-time extra fetch.
- Avoid Blob fields on table extensions — forces the extension joins even when SetLoadFields is used.
- Team rule cited: on every read apply both SetLoadFields and SetAutoCalcFields.

**DeleteAll gotcha**
- `DeleteAll` acquires a write lock even when the filtered set is empty → can block other sessions. Guard: `if not IsEmpty then DeleteAll;` (same reasoning generalises to conditional bulk ops).

**Bulk inserts**
- Platform buffers inserts (batches ~5) into fewer statements. Broken by: AutoIncrement field, NumberSequence-assigned key, Blob fields, or any Get/Find/Modify/Calc interleaved between inserts — any op other than plain Insert. For insert-heavy tables avoid AutoIncrement; buffer in a temp table then insert.

**DataTransfer type** (introduced ~BC 2022/23)
- Bulk field-move and row-copy executed directly at SQL level → one statement for a whole move/copy vs per-record loop.
- Runs NO triggers and NO events (pure SQL). Allowed only inside upgrade codeunits.

**Queries**
- Replace nested `FindSet` loops with a query object → single flat SQL statement.
- Queries always execute on SQL Server, bypass the NST cache → slow if run repeatedly (e.g. inside a loop). No ChangeCompany support.

**Events / publishers / subscribers**
- Raising events is cheap (~1M events ≈ 16ms). Publishers: unrestricted.
- Subscriber codeunit size (small vs 6000 lines) is negligible for perf; keep small for readability. SingleInstance avoids re-instantiation per call — minor gain, real from 2nd call in a session. Unused **global variables** in a subscriber codeunit measurably cost — avoid.
- **Do not subscribe to database OnModify/OnInsert/OnDelete**: it forces row-by-row execution, breaking `ModifyAll`, bulk insert and `DeleteAll`. Even a *manual/unbound* subscriber merely existing on that table breaks the bulk path. Prefer putting logic in a table-extension trigger, not a database-event subscriber.
- Just-in-time `BindSubscription`/`UnbindSubscription` vs bind-once-per-codeunit: only a few % difference.

**Language / data types**
- No lazy (short-circuit) evaluation in AL — both operands of `and`/`or` are always evaluated. To skip a heavy right-hand side, refactor to a nested `if`. (Microsoft won't change this — base app relies on side effects.)
- Use TextBuilder / List / Dictionary over repeated string concatenation. Dictionary faster than a temp record for key/value data (temp record needed when you need full-record fields).

**Background processing**
- Prefer Job Queue / Task Scheduler over `StartSession`. `StartSession` runs immediately, doesn't survive server restart, and a StartSession inside a loop spawns uncontrolled sessions. Job Queue failures are almost always the AL code failing, not the queue.
- Use Page Background Task for slow Role Center / FactBox calculations to keep UI responsive.

**Reports**
- Dataset columns are loaded as partial records by default. Fields you use in OnAfterGetRecord (or CurrentRecord logic) that are NOT dataset columns are not auto-loaded → add `LoadFields` (or SetLoadFields) in OnPreDataItem for them.

**Tooling**
- Debug console: type `sql<n>` (e.g. `sql1`) to dump the full SQL statement text for a step (copyable, unlike the debugger grid).
- "Analyze performance" page action (Help & Support) → capture profile; can download a **flame graph** (CPU profile) rendering the call stack over time. Profiler is sampling (default ~100ms; can set sampling interval to 1 for denser samples — instrumentation mode can't be started from code).
- Table `Compression` property reported to help read/write (untested in talk).
- NumberSequence [sic — verify exact type name] used by "allow gaps" number series for gap-free-ish numbering without locking.

### AL performance patterns — SQL-level tuning (mibuso TechDays, Stefan Sosic 2025-09)
Measured on BC 25/26; behaviour verified with SQL Server Profiler. `SelectLatestVersion` used before each call to bypass NST cache for raw timing — do NOT use in production.

- **NST (server) cache**: first read hits SQL, later reads of same set served from memory buffer (0 extra SQL statements). Caching is automatic; explicit cache-clearing only for benchmarking.
- **`IsEmpty` before `FindSet`**: usually redundant on repeated loops. After ~4 repeated executions of the same filtered `FindSet`, the platform auto-optimises by wrapping the stored procedure in `IF EXISTS` — so a preceding `IsEmpty` just doubles the query count. Drop `IsEmpty` guard unless the set is (near-)always empty (rare); then the guard can save the `FindSet`. On always-empty tables `FindSet`-only is slightly slower.
- **`SetLoadFields`**: limits columns pulled; primary key auto-loaded. Same statement count but much lighter query. Without it, ALL fields load *including fields from every table extension* → extra joins from other extensions you don't control. Big win on wide/extended tables (25s+ on 1M rows in demo).
- **`Find('-')` vs `FindSet`**: `Find('-')` buffers only 50 records; iterating past 50 issues another query (restarting from last record) + memory reallocation. Use `FindSet` when you know you'll read the whole set. `FindFirst` behaves the same but buffers only 1 record — first `Next` triggers a refill query.
- **`CalcFields` in loop vs `SetAutoCalcFields`**: per-record `CalcFields` fires one extra SQL query *each iteration* (huge overload — ~25k extra statements in demo). `SetAutoCalcFields(<field>)` before `FindSet` folds the flowfield calc into the single find query. Exception: if only a few records actually need the calc (e.g. conditional on a Blob flowfield), plain `CalcFields` can win by skipping calc for the rest.
- **Calc totals in loop vs `CalcSums`**: `CalcSums` sums on the SQL side (one optimised query) — far faster than looping+accumulating, even with `SetLoadFields`. Prefer `CalcSums`.
- **`if not Insert then Modify` anti-pattern**: on non-singleton tables the failing `Insert` raises a *SQL error* that round-trips to NST for parsing before the `Modify` is crafted — expensive. Prefer `if <rec>.Get(...) ` / explicit `IsEmpty` check (a cheap `SELECT TOP 1`) to decide Insert vs Modify. Also blocks buffered inserts. Fine on singleton/setup tables. On temporary tables the pattern is fine (no SQL, no error round-trip).
- **`TextBuilder` vs `Text`**: `Text` is by-value — each concatenation reallocates the whole string. `TextBuilder` is a reference-type .NET wrapper — appends extend memory in place. Use `TextBuilder` for building strings in loops.
- **Pass record `var` vs by value**: `var` passes by reference (cheaper) vs a value copy. Passing only the needed field(s) is fastest and clearest. Keep field-parameter count low (~3–5 max) for maintainability. No SQL difference — pure NST memory.
- **Modify/Delete in loop — separate variable trick**: iterating with rec `A` and doing `A.Modify` forces the buffered read (read-uncommitted) to flip to read-committed mid-loop. Loading into a *second* variable (`A2.Get(A."No."); A2.Modify`) avoids that flip and measures faster. Effect notable for Modify; smaller for Delete.
- **`IsEmpty` vs `Count = 0`**: `IsEmpty` = `SELECT TOP 1` (near-zero reads); `Count` scans the whole table. Use `IsEmpty` for existence checks — gap grows with table size.
- **"Exactly one record?"**: `Count = 1` scans all rows. Prefer `Find('-')` then `Next` (buffers 50, one cheap `Next` check) — faster than `Count`, and better than `FindFirst`+`Next` (which needs a refill query). 10–20s difference over 500 reps on 1M rows.
- **`ModifyAll` / `DeleteAll`**: do NOT precede with `IsEmpty` or `FindSet`. `ModifyAll`/`DeleteAll` already do the row-count/existence check in one statement (takes intent-exclusive page lock + row exclusive locks). `IsEmpty` adds a redundant query; `FindSet` pointlessly buffers the whole set. Note: `DeleteAll` on an already-empty table still takes a lock, which can slow a following `Insert`.
- **Filtering on flowfields**: setting a filter on a flowfield and looping is *not* the disaster expected — performs about as well as (sometimes slightly better than) `SetAutoCalcFields`. Don't avoid it.
- **Changing filters inside a loop**: `SetRange`/`SetFilter` mid-iteration invalidates the record buffer; next `Next` re-runs the query to refill. Instead collect/mark into a temporary table and process that.
- **Temporary tables**: no SQL at all — insert/modify/delete/find are pure NST memory. Declaring a normal table `temporary` (var) gives the benefit; declaring the table object itself as `TableType = Temporary` optimises further still. For partial data, a `Dictionary` can beat a temp table; for full records a temp table beats stuffing everything into a `Dictionary`.
- **Lazy evaluation / early exit**: order conditions cheapest-first and exit early; put heavy predicates last in `and`/`case`/`in` chains so they're skipped when possible. Common inefficiency in nested loops.
- **Query objects**: generate different (often better) SQL than `FindSet`, especially for flowfield/aggregation; on repeated runs a query object outperforms plain `FindSet`.
- **`SetCurrentKey`**: not needed if only the primary key exists. Adds an `ORDER BY` that can add SQL overhead if the wrong/unneeded key is set — but the right key can turn a 20-min report into <2 min. Don't blanket-apply; profile via debugger SQL insights and set deliberately.
- Official patterns live in the community **AL Guidelines** repo (now under Microsoft org): https://alguidelines.dev — Code Cop enforces some (e.g. FindFirst-then-loop rule).

### Read isolation & SQL locking (BC TechDays 2023, mibuso)

**How AL locking maps to SQL**
- AL is single-threaded in-memory; all concurrency/locking happens only at the database. Writes: platform emits the SQL statement and lets SQL Server take whatever lock it wants (usually exclusive, not guaranteed). Reads: the runtime applies an explicit isolation hint.
- Default read = `READUNCOMMITTED` (dirty reads allowed, no locks, no waiting) **as long as no write or `LockTable` has happened on that table in the current transaction**.
- After any write or `LockTable` on a table, subsequent reads on that table use `UPDLOCK` (U-lock) by default, held for the **entire transaction** (until `Commit`).

**LockTable gotchas**
- `Rec.LockTable()` sets intent only; the lock is taken when data is actually **read**, not at the `LockTable` call.
- Lock state is tied to the **table type**, not the record variable/instance. `Cust1.LockTable()` then reading via `Cust2` (same Customer table) still locks — persists for whole transaction.
- Starting a write locks all subsequent reads of that table. Even a failed `Insert` counts as a write and flips the table into locking-read mode.
- `DeleteAll` and `FindSet`/`Count`/`CalcFields`/`CalcSums` can lock the **entire table if the table/range is empty** (no rows returned → SQL locks the whole table so nobody can insert until transaction ends). Bulk ops are the main whole-table-lock offenders.
- FlowField calc reads use the **target/source table's** lock state (e.g. Customer.Balance reads Detailed Cust. Ledg. Entry — that table's state decides UPDLOCK vs READUNCOMMITTED).
- `Delete`/`Insert`/`Modify` internally call `LockTable` under the hood.

**Lock escalation** — SQL escalates row locks to 8KB **page** locks (then higher) to save memory; you can end up locking rows you never read because they share a page.

**ReadIsolation (BC v22+)** — per-record-instance control over read locking, overrides the table-state default.
- Property/enum on the record instance: `Rec.ReadIsolation := IsolationLevel::ReadCommitted;` `[sic?]` verify exact property name (`ReadIsolation`) and enum type/values against Microsoft Learn/compiler.
- Values map to SQL: `ReadUncommitted`, `ReadCommitted` (shared lock for read duration only — no dirty data, minimal blocking; **recommended default**), `RepeatableRead` (holds lock for whole transaction, keeps data consistent, still allows others to read), `UpdLock` (exclusive-style, strongest).
- Set on the **record instance**, not variable/table; survives pass-by-value; ignores current table lock state; only affects that instance, only affects **reads** (not writes). Persists across multiple reads on the same instance until changed/`Clear`.
- Overrides FlowField lock behaviour too — set ReadIsolation on the parent record to avoid FlowField locks.
- **Gotcha:** calling `LockTable` on a record after setting ReadIsolation **resets** the ReadIsolation.
- ReadIsolation does **not** apply to write transactions — to avoid the empty-table `DeleteAll` lock you must guard with `if not IsEmpty then DeleteAll`.
- Once set, later reads in the transaction keep the state; to change it for a `FindSet`, set ReadIsolation on the line **above** the read.

**Patterns / recommendations**
- New code: use ReadIsolation explicitly instead of `LockTable`; be conscious of the isolation level you actually need per read (esp. hot paths).
- "Temporary heightening": to lock one specific row (e.g. get-next-entry-no), set `UpdLock` on just that instance rather than `LockTable`-ing the whole table.
- Especially valuable in **event subscribers** — you don't know what locks prior code took, so specify intent explicitly.
- Do reads before writes; cache read results; keep transactions small/re-entrant; break long processing into chunks. Reducing lock hold time (faster code) is a valid alternative to eliminating locks — lock timeout default ~30s.
- Refactor existing `LockTable` code with caution/incrementally (Telemetry-driven, worst offenders first) — removing a `LockTable` may drop locks something depended on and cause regressions.

**Diagnostics**
- VS Code debugger (v21+): expand Database Statistics → Locks to see current-transaction locks. Also exposes a copy-pasteable SQL query to inspect held SQL locks directly.
- Search "SQL Server lock compatibility matrix" to reason about U/S/X/intent/range lock conflicts.

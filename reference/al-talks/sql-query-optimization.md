# sql-query-optimization

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2022 - Optimizing SQL queries in Business Centra | 2026-07-27 -->
### Indexes & keys in AL/SQL Server

- Keys in an AL table/tableextension `keys` section map to SQL Server indexes. First key = primary key, **clustered by default**.
- Clustered index sets the physical row order (B-tree; root → intermediate → leaf, data stored at leaf). Only one per table. Add `Clustered = false` on the primary key and `Clustered = true` on another key to change which key is clustered [sic? verify `Clustered` key property syntax on Learn].
- Non-clustered index: index stored separately from data (like a book index). Multiple allowed per table.
- BC auto-creates a unique secondary index on the `SystemId` field of every table; `SystemId` exists on SQL but is not shown in the AL keys UI and cannot be changed after insert.
- Keys can be added on standard (base app) tables, but a custom key **cannot mix standard fields with your extension fields**.

### SetCurrentKey vs index selection

- `SetCurrentKey` only requests a sort order — it does **not** force which index SQL uses. SQL's optimizer picks the index from statistics.
- Newer versions: `SetCurrentKey` (and filter/sort) may reference **any** table field, not only fields declared in a key section. Older versions threw a runtime error for undeclared fields.

### Caching layers

- Two cache levels: BC Server (NST) instance cache, then SQL Server data cache, then disk.
- NST cache split into **global cache** (shared across users) and **private cache** (per transaction/user, cleared at transaction end). If the table is locked, reads go to private cache; otherwise global.
- `SELECTLATESTVERSION` ensures the freshest DB data is used.
- SQL admin: `DBCC DROPCLEANBUFFERS` clears data cache; `DBCC FREEPROCCACHE` clears stored/compiled plans [sic? command names reconstructed from garbled captions].

### Partial records (SetLoadFields / AddLoadFields)

- Load only a subset of normal fields; big win with table extensions (avoids joining the extension companion table).
- Without partial records, `Get`/`Find`/`Next` load all normal fields from the data source.
- Methods: `SetLoadFields` (set the initial field set), `AddLoadFields` (append more, e.g. in a subscriber), plus `LoadFields`/`AreFieldsLoaded`-style helpers [sic? verify exact method names on Learn].
- Old limitation: fields used in flowfield/CalcFormula filters were always force-loaded, killing the benefit — fixed in **v21** (just-in-time loading of only the fields needed for the filter/flowfield).
- Benefits: fewer columns → optimizer more likely to pick a covering index; less memory; less data over the wire; fewer joins; better plan-cache reuse.
- **Just-in-time (JIT) loading**: accessing an unloaded field triggers a re-Get on the record and reload — raises an error if the row changed in the DB meanwhile. `Delete`, `Rename`, `Insert` require ALL fields loaded, so they trigger JIT. Use partial records mainly with read paths (`Find`/`Get`/`FindSet`).

### Covering / included-column indexes (v20+)

- SQL "included columns": extra fields stored at the leaf of a non-clustered index so a query is satisfied entirely from the index (no lookup to base table).
- AL: declare via `IncludedFields` property on a key [sic? verify property name]. Before this, all such fields had to be full key columns.
- Keep filter/sort fields as key columns; put payload fields (returned but not filtered/sorted) in included fields → smaller key entries, fewer index I/O ops. Included columns can be data types not allowed as key columns.
- Max 16 key columns per index [sic? talk said "60" — verify; SQL limit historically 16/32].
- Use cases: query objects; combined with `SetLoadFields`; consider revisiting existing keys as covering candidates.

### SIFT keys (SumIndexField)

- A SIFT key in AL is implemented as a **SQL Server indexed view** — one indexed view per SIFT key per table. Stores pre-aggregated sums/counts per key-field combination → `CalcFields`/`Count` are near-instant even on millions of rows.
- Cost: every Insert/Modify/Delete on the base table must update the indexed view(s) → write overhead grows with number of SIFT keys. Measured ~10x slower inserts vs. non-clustered columnstore in the demo.
- Key property `MaintainSiftIndex` (default true) [sic? verify exact property name]. Setting false drops the indexed view; `CalcFields` still works but falls back to scanning the base table (slow).
- Only worth it on large, read-heavy tables. Small/periodic tables: prefer included columns instead.
- **Perf tip**: call `SetAutoCalcFields` before `FindSet`, not `CalcFields` inside the loop (demo: ~77 ms loop vs ~0 ms with SetAutoCalcFields).

### Non-clustered columnstore index (NCCI) — alternative to SIFT

- Columnstore stores data **column-wise** (vertical); one columnstore index per table, multiple fields, field order irrelevant (each column stored/compressed separately).
- No pre-aggregation stored — aggregates computed at runtime. Much cheaper writes than SIFT (demo: ~95 ms vs ~1 s for 1000-row insert).
- Structure: rows grouped into **row groups** (~1M rows ideal each); each row group holds one **column segment** per column. Compressed per segment; **segment elimination** skips whole row groups when filters allow. New rows land in a **delta store** first, then compress into a row group when large enough.
- Requirements to benefit: very large AND wide tables — at least ~1M rows, ideally 5–50M+; avoid string fields / highly-unique values in the index (prefer int/date with repetition); heavy-update tables cause fragmentation and kill the benefit.
- **Caveat**: on small Azure SQL tiers (below a core threshold) NCCI is automatically disabled → no effect. It's memory-intensive.
- Presenter's real-world finding: even with 5–10M rows and segment elimination, NCCI reads were slower than SIFT reads. Community consensus: NCCI wins on **write-heavy** tables; for pure read aggregation you can't beat the pre-computed SIFT indexed view. Both MS and community noted little production NCCI usage yet.
- Migration SIFT→NCCI: declare the columnstore index with the fields, remove the SIFT key; deploy rebuilds indexes (takes time).

### Data compression

- SQL row-level vs page-level compression. Row: shrinks fixed-length types to actual value size. Page: row compression + prefix/dictionary compression.
- AL: `CompressionType` key/table property [sic? verify]; `Unspecified` leaves it to be managed at SQL level.
- BC Online: **page compression enabled by default**. On-prem: use `sp_estimate_data_compression_savings` to compare row vs page sizes — if little difference, use row (simpler); if large, use page.

### Locking

- `LOCKTABLE` locks subsequent reads. SQL Server chooses granularity (row / page / table). Row lock = lowest granularity, others stay usable.
- Triggers of locks: explicit `LockTable`; `FindSet(true)` [update param true] raises a lock; two users hitting the same code path. Most locking issues stem from poor code paths / ordering ["BidiRoll/version conflict" garbled].
- Keep transactions short — longer transaction = more blocking. More keys = slower writes = more frequent locks.
- Diagnostics: DB locks telemetry (won't show cross-NST locks if multiple NSTs); **v21** AL debugger shows a locks section under Database Statistics (useful in SaaS where you have no direct DB access).

### Wait statistics & missing indexes

- SQL `sys.dm_os_wait_stats` [sic? "mosfet states"] categorizes waits: resource waits (locks, latches, network, disk I/O), queue waits, external waits. High lock waits → data contention.
- Missing-index feature: query optimizer records indexes it would have used. Exposed via `sys.dm_db_missing_index_details` [sic?], surfaced to AL as a virtual table. Suggests only non-clustered, disk-based rowstore indexes; does NOT specify key-column order; suggests included columns; skips trivial plans. Treat suggestions as one input — review for duplicates/overlaps against existing indexes before creating.
- SaaS: MS has planned automatic index & statistics maintenance (no manual rebuild from BC code).
- Splitting a wide transactional table into two narrower 1:1 tables: no benefit — every insert/modify now doubles.

### Resources

- `AKirmm/BusinessCentral.LinterCop`-style BC performance tooling and the BC "Performance Developer" toolkit; MS on-prem SQL setup guidance doc [sic? link names not captured — search Microsoft Learn].

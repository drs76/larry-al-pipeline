<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Table indexes, SIFT, NCCI, full-text, key ordering

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 1. Platform, Runtime & Performance

### Table indexes & SIFT — planning for performance

**Keys vs indexes (BC vs SQL):** In SQL a key is a uniqueness constraint, an index is the B-tree. In BC a `key` is an index definition; mark it `Unique` and it also becomes a SQL unique constraint. Every BC key except when disabled is unique on SQL side. Primary key = clustered index + PK constraint. Every table also gets a second SQL index on `SystemId` (unique).

**Clustered index:** always exactly one, leaf nodes *are* the table data, defines physical row order. First key in the list is always the primary key. `Clustered = true` can be moved to a non-first key — this changes which index is clustered but does NOT change the primary key.

**Non-clustered index:** everything else. Leaf nodes hold pointers back to the clustered index; retrieving non-indexed fields costs a **key lookup**. SQL allows 999 non-clustered per table; BC caps at 40. Set `MaintainSqlIndex = false` to define a BC key with no SQL index.

**Seek vs scan:** seek walks the B-tree (fast, needs selectivity); scan reads everything (index scan or table scan). Seek gets logarithmically slower with row count; scan gets linearly slower.

**Cost of indexes:** every insert/update/delete must maintain all indexes. Rule of thumb ~10–20% write slowdown per added index (highly data-dependent). More indexes = longer writes = locks held longer = more lock timeouts/deadlocks. Rule of thumb: more than ~4–5 non-clustered indexes on a table is a smell.

**Covering index / IncludedFields:** an index that supplies all fields a query needs, eliminating the key lookup. Not a special type — always "covering *for a specific query*". Filter fields go in the key (B-tree); selected-only fields go in `IncludedFields` (leaf only). Downside: storage — adding ~5 included fields across 3 indexes measured ~21% table-size growth. SaaS storage is not free.

**Covering index favours query objects over FindSet:** `FindSet` adds unpredictable fields to the SELECT (SystemId, timestamp/rowversion, SystemCreatedAt/By etc., filter fields, JIT-loaded fields, fields added by subscribers), so a guaranteed covering index is nearly impossible — expect a key lookup. Query objects only select declared columns + primary key, so covering indexes are achievable. Add `OrderBy` matching the index to also drop the SORT operator.

**FAST 50 gotcha:** every query BC generates from AL carries SQL `OPTION (FAST 50)` — optimize for returning first 50 rows quickly, not total runtime. Consequence: adding an index can make total query time *worse*. Classic case (SQL 2019+): an unindexed GROUP BY runs a parallel batch-mode clustered-index scan (fast total time); adding a non-clustered index makes SQL prefer a serial seek/scan that returns 50 rows fast but total time is much slower. "Faster" for BC = fast partial results, not lowest total cost.

### SIFT (SumIndexField Technology)

- SIFT is a SQL **indexed view** holding pre-aggregated sums/counts per key-value combination, maintained on insert/update/delete. Pushes aggregation cost from read side to write side. `CalcSums`, `CalcFields`, `Count` are auto-redirected to the SIFT view (execution plan shows a *view clustered append* / GUID-named object + `$VSIFT$key`-style name `[sic?]` — verify exact naming).
- Reads: fastest option for heavy sum/count — beats even a covering index in benchmarks.
- Writes: worst offender. Benchmark inserting 100k rows: no index ~10s, +5 SIFT ~30s, +10 SIFT ~50s.
- **Locking:** SQL uses aggressive **range locks** on SIFT view updates (not granular row locks), held longer because updates are slow → deadlock/lock-timeout risk grows sharply under many concurrent writers. Real cases: deadlocks concentrated entirely on tables carrying 5–6 SIFT views; dropping SIFT views eliminated deadlocks. Rule of thumb: 1–2 SIFT views per table OK, more = reconsider. More distinct values in the SIFT = lower deadlock risk.

### Non-clustered columnstore index (NCCI)

- Table-level property listing covered columns (not brand-new; already usable in BC). Microsoft positions it as successor to SIFT.
- Column-oriented: each column stored/compressed separately; queries only read requested columns. Data split into **row groups** of up to 2^20 (~1,048,576) values per column-segment. High compression → fewer I/O.
- **Segment elimination** lets SQL skip segments — but NCCI has NO seek; every access is at least one full segment scan (decompress ~1M values). Bad for pinpoint/small-subset queries and for `CalcSums` in a loop (marginal or worse than no index).
- BC does NOT yet support ordered columnstore (SQL 2022/2024 do). Unordered → inserted values scatter across all segments over time, degrading segment elimination until it scans the whole table.
- Designed for **parallel** execution: only wins on large tables (millions of rows), expensive queries that trip the parallelism threshold, and set-returning GROUP BY (query object), not row-by-row loops. Write overhead ~7–8% per few columns — far lighter than rowstore/SIFT.

### Full-text index

- Property `OptimizeForTextSearch` creates a SQL full-text index for natural-language / keyword / whole-word wildcard search. Low write overhead but still non-zero — don't apply to every text field.

### Diagnosing index usage

- **Debugger:** breakpoint, step over the statement, read last-executed SQL statements panel (highest number = latest); substitute parameter values (strings single-quoted like AL) and run in SSMS/Azure Data Studio with *actual* execution plan enabled.
- **Missing-index suggestions** view exposed in web client — hints only, no reliable impact estimate.
- **Telemetry:** long-running SQL events (>750ms threshold), plus locking/deadlock telemetry — usable on SaaS where SQL access is unavailable.
- Testing: build enough demo data AND match production data distribution (value skew, chronological vs random dates); the optimizer choice depends on selectivity.

### Key-field ordering

- Put the more selective field first. Example: `PostingDate` (distinct values grow over years) is often more selective than `G/L Account No.` (few dozen accounts), so leading with PostingDate can be more efficient — though differences may be marginal; test.

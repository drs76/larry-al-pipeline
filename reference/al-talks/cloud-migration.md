# Cloud migration & upgrade — replication engine, .NET Core lessons

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2023 - What's new in cloud migration and upgrade | 2026-07-27 -->
### Cloud migration & upgrade — replication engine (BC TechDays 2023)

**Architecture**
- Uses Azure Data Factory pipelines + integration runtimes to copy source→destination. Source = on-prem SQL Server or Azure SQL; destination = always Azure SQL of the BC tenant.
- Large tables: table-to-table copy via dedicated copier activities. Small tables: bulk copy — on-prem stored procs serialize/compress bulks into a staging table, copied to cloud, then reversed by tenant stored procs.
- Uses SQL change tracking to detect incremental changes and do Delta sync where possible.
- Staging uses Azure Blob storage as temporary staging (except Azure SQL→Azure SQL, see below).

**Pipeline improvements**
- Replication metadata now passed via a DB table instead of ADF activity input/output params → bypasses the 4 MB ADF activity I/O limit. Result: unlimited number of tables per run; company-count limit removed (BC still caps 300 companies/env, but all can migrate in one run given strong on-prem SQL).
- On-prem DB size calc moved to setup (done once), no longer per replication run → saves 15–45 min on large DBs, fewer timeouts.
- Added activity to copy SQL sequences → AL `NumberSequence` [sic? verify data-type name] now supported; numbering continues in tenant instead of resetting.

**Table-to-table copy**
- Threshold to pick table-to-table copy lowered from 500 MB → 250 MB (more tables use it, faster status updates).
- Target-table indexes now disabled before copy, rebuilt after → ~8–22% [sic? phrasing garbled, likely a factor or %] faster; also cleanup+copy run with no active indexes.

**Bulk copy**
- Bulk size reduced → more, smaller bulks, easier to serialize/compress, fewer timeouts. Reported 60–80% faster on weak test servers; more frequent status updates.
- Diagnostic runs now respect the smaller bulk size (previously one huge bulk → timeouts/OOM). Safe to use to quickly test a future replication.

**Delta sync**
- Change-tracking retention period forced longer → change-tracking versions stay valid longer → higher chance of fast Delta sync on repeated runs.
- Delta sync now possible for DBs that first enabled change tracking specifically for cloud migration.

**Azure SQL as source (special)**
- If source is Azure SQL, source and destination Azure SQL DBs can be linked directly — no serialized blob staging. Faster; enables replicating `sql_variant` fields; avoids blob-staging errors (e.g. large single field / image failing with wrong-row-delimiter error).
- Recommendation: for high-volume migration, consider deploying on-prem DB to Azure SQL first; prioritize compute + I/O service tier. sql_variant / large-image fields → Azure SQL source is the only option.

**New UI**
- Toggle old/new UI via "enable/disable new UI" action; new UI default for BC cloud migration setup. GP/SL still old UI.
- Shows single overall status + step history (migration log). Actions check overall status, no need to select a record.
- Drill-down distinguishes tables that truly failed vs. tables whose failing run was later superseded by a successful run (no action needed). "Show all replication runs" lists every run a table was in.
- **Unblock table** action: marks a failed small table as passed so you can move its data manually (config packages / rapid start). Note the failing company+table first — it drops off the list after unblocking (failed-table tracking not retained).
- Company overview: filter Replicated = No to see un-migrated companies.
- Table status overview across companies; filter per company. Check pre-database (system) tables. Tenant media tables legitimately show a positive Delta (more records than on-prem) because data is never replaced — if data was replaced or fewer records copied, open a support ticket. Internal / obsolete-removed tables can't be counted → warning shown. No warning system yet for bad replaces.
- Per-table lookup shows why a table wasn't moved (e.g. excluded because `ReplicateData` property, or empty on-prem).
- **Complete cloud migration** runs a sanity check (blocked if failed tables remain).
- **Pause** vs **Abandon** cloud migration: functionally identical except telemetry signal (abandon = planning to delete env). Reconfigurable after either.
- **Sanitize tables** action: runs in SaaS the code that `invoke nav sanitize`[sic? — likely a NAV/on-prem sanitize cmdlet, verify] should have done on-prem; per specific company+table; can hit tenant perf, run outside business hours. Still strongly recommended to sanitize on-prem before copying.

**Moving customized fields to table extensions**
- Shipped in v21 (back-ported). SaaS can't have custom fields on Microsoft tables → custom fields must move into table extensions.
- Base table (e.g. Customer) auto-copied (ReplicateData=true); default mapping matches fields by name+type. Unmapped fields left behind.
- Define **migration table mappings** to split custom fields across multiple table extensions; engine maps fields by name+type automatically.
- Fields must be renamed to match on-prem↔SaaS (prefix). Can rename in AL (allows breaking changes) or via SQL scripts — engine only inspects the SQL definition. Future namespaces work aims to remove prefix/suffix need.
- Prereq: upload/install the target extensions first (Extension Management install status).
- **Add table mappings** UI: paste SQL table name (incl. square brackets, escaped underscores) into name field → auto-parses app ID (if AL table) and DataPerCompany. Select multiple extension rows → inserts one mapping each.
- Import/export mapping config as JSON to reuse across environments/replications.
- Programmatic mappings: subscribe to `OnInsertDefaultTableMappings` event on codeunit 4001 [sic? verify codeunit ID/event name] — fires on wizard completion or "reset migration table mappings" action.
- **Limitation:** cannot move a field into an existing table extension that is already replicated from its own source — engine can't merge two source tables into one target. Workaround: move field to the extension on-prem, OR introduce a new table extension for the migration mapping.

**Telemetry**
- Partner telemetry events added for: replication run started/completed/success; companion tables started/completed; upgrade events + recovery; cloud migration disabled.
- Sample Power BI dashboard (BCTech GitHub) shows status across environments, links to admin center + client, and cloud migration log without accessing the client.
- Subscribe to replication-run-completed and data-upgrade-completed/failed events for email alerts.

**New upgrade / jump-build strategy**
- Direct upgrade + cloud-migration path from v14 will stop at v26 (~2 years out from talk). Reason: cleaning up 7 years of obsolete-removed objects (no table schema deleted since v12; obsolete objects ~10% of DB) + delocalization effort + moving tables between extensions.
- v25 = last version where all on-prem versions (incl. 14) can upgrade/cloud-migrate directly. v26 introduces breaking SQL changes at start of dev (visible in Insider builds); v25 becomes the "jump build": on-prem → 25 → 26.
- Planned cadence: a jump build every 5 versions (30, 31→ jump via 30, etc.).
- Obsolete-object removal (planned, not yet implemented, maybe before v26): mark table/field ObsoleteState=Removed in version N, delete object + clean upgrade code in N+1, run upgrade → engine verifies Removed state, drops SQL definition.
- No enforced breaking-change schedule for partners; Microsoft must follow the schedule. On-prem support: no plans to stop; would be announced in advance. Long-range plans (v35) are current thinking, subject to change.

**Roadmap (backlog at time of talk)**
- Configurable company batch size for replication.
- UI to include/exclude Microsoft-owned tables from migration (table must not be internal) — override MS default without code.
- Delta-sync pre-database (system) tables instead of full replace.
- Option to disable auto-assigning Intelligent Cloud permission sets to all users (shipped as expert feature; blocks service-to-service auth; not auto-disabled initially).
- More UI warnings (tenant media replaced, mappings defined but no data moved).
- Action to cancel an ongoing replication (currently only via disabling integration runtime, which doesn't always cancel).

**Recommendations**
- Large DBs → migrate from Azure SQL source (or very strong on-prem).
- Set longer change-tracking retention for longer Delta-sync windows.
- Use diagnostic runs to test.
- Set up telemetry for troubleshooting/alerts/dashboards.

<!-- ingested: BC TechDays 2023 - Lessons learned from migrating to .NET Co | 2026-07-27 -->

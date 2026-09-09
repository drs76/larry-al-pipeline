# bc-reporting

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2023 - Business Central Reporting demystified | 2026-07-27 -->
### BC reporting — layouts, report objects, Power BI, data analysis

**Report layout types (per report object, multiple allowed)**
- Three layout types coexist on one report via a `rendering` section: RDLC, Word, Excel. Each layout gets a name/description shown in BC's report layout selection.
- RDLC: pixel-perfect, expressions, printable, emailable as attachment; hardest to build.
- Word: printable to PDF, email body + attachment, no expressions, easier. Design by inserting a table, one row for labels + one repeating row bound to a data item.
- Word advantage over RDLC: a second data item can go in a separate table automatically, no filter needed. RDLC requires manual filters to bind two tables to two data items — more complex.
- Excel layout: no print/preview — must download first, then opens in Excel. Very dynamic; supports Power Query, pivot tables/charts, external data (SharePoint, OData/APIs), post-processing/forecasting.
- Developer repackage (Ctrl+Shift+B) generates the Excel/Word/RDLC layout file but empty (Excel has data sheet with columns, no data). Data only appears at runtime in the app.

**Report data set advice**
- Focus design on the data set first; layout depends on it. Test by running to request page then Export to Excel to inspect the runtime data set.
- Don't forget the data item link when joining data items.
- Layout choice can force data-set changes (e.g. building for Excel may need a different shape).

**Report extensions (`reportextension` object)**
- Users cannot add fields to a report's data set; a report extension can. Add columns to existing data items, add new data items, add request-page controls, add triggers/code, add a layout.
- Gotcha: a data item added "after" an existing one lands at the *same level* as that item in a union, not nested/appended as expected — inspect the resulting data set.
- Reusing an existing layout with added fields is cumbersome: export the original layout from BC's report layout selection page, copy into the VS Code project, rename, Ctrl+Shift+B to inject new fields, edit, republish. Simply setting the layout property regenerates an *empty* layout.
- Multiple apps can extend the same report/data set — risk of conflicts and surprising runtime results, especially layouts. Presenter recommendation: often cleaner to clone the whole report than extend.
- Report extension cannot set its layout as the report default. Workaround: subscribe to the `OnAfterSubstituteReport` [sic? — "after substitute report" event, verify name on Learn] to swap the whole report, or write code to mark a layout default in the report layout selection table.
- RDLC vs RDL: RDLC = Report Definition Language Client-side, renders in the BC/report viewer with no report server; RDL needs its own SQL Server Reporting Services server. BC uses RDLC.

**Excel layout workflow**
- Manage under Report Layouts page; shows source extension/base app. Cannot delete extension-provided layouts, only user-created ones.
- The data set appears as an Excel table named `contract` [sic? verify]. You may delete unneeded columns but **must not rename or reorder columns** — breaks the contract.
- Enrich: add OData feed / API via Power Query, merge with the `contract` table (join needs matching column types — convert if needed). Set OData connections to auto-refresh on open.
- To add data to an existing report's Excel layout without a report extension: use an API/web service via Power Query in the Excel file, no data-set change needed.

**Financial reporting (formerly Account Schedules)**
- Search "Financial Reports"; many predefined. Built from row definitions + column definitions; no developer needed. Row types: net change, balance at date, etc.
- Publish via "Financial Report KPI Web Service Setup" [sic? verify name] to consume in Power BI. Marked legacy — prefer the standard Microsoft finance APIs (`reportsFinance` beta group [sic? verify]) which need no BC setup.

**Data analysis mode on list pages**
- Enable via Feature Management ("Analysis mode" / "Analyze data directly", preview). Toggle analysis on any list page.
- Excel-like: choose columns, group, filter, pivot mode (rows/values), multiple value fields, drill-down to month/quarter/year, filters. Copy/export to CSV or Excel; rename/duplicate views.
- Limitation: views are per-user, cannot be shared. Suggest sharing ideas to Kenny Saelen / Ideas site.

**Power BI data sources**
- Options: web services and APIs, both from query or page objects. Recommended: **API queries** (best performance) > API pages > avoid web services.
- Existing standard APIs cannot be extended — create new API objects for custom fields (e.g. added field on customer card). API query is built like a report data item.
- Set `DataAccessIntent = ReadOnly` on queries/reports so they hit the read-replica DB, avoiding locks/blocking during Power BI refresh.
- Reduce granularity in the query: aggregate/group numeric fields (apply a `Method` like Sum) to shrink the data set and speed refresh — but do NOT include the primary key / entry number, or grouping produces no aggregation.
- Query objects can set the SQL join type; reports cannot.
- Version API groups so changes don't break existing reports.
- Page APIs carry extra insert/modify overhead for Power Apps/Automate use — unneeded for read-only Power BI; queries are leaner.

**Power BI techniques**
- Connector: BC SaaS use the Business Central connector; on-prem use OData connector.
- Multi-company / multi-environment: in Power Query, delete the auto-generated navigation steps to step back to the environments/companies list, then expand and select environment + company columns, filter out evaluation/empty companies. Save as a Power BI template.
- Multi-fact (e.g. actuals vs budget with different granularity — sales by day, budget by month) solutions: (1) reduce all tables to common grain (group sales by month); (2) DAX `TREATAS` to move filters between unrelated tables (virtual relationship); (3) bridge table on year-month (union of year-months from both tables) — works but not a true star/snowflake; (4) DAX to reallocate monthly budget to daily by working days (attributed to Marco Russo/Alberto Ferrari, sqlbi.com) — allows day-level compare. Always verify both correct data AND correct totals.

**Data flows (Power BI service)**
- Fetch shared/master data from BC once, cached, instead of every report re-importing simultaneously. Needs Power BI Pro license + a workspace; BC is a built-in data flow connector. It is Power Query Online, supports multi-company/multi-env/multi-source, refresh schedules, better perf monitoring than desktop Power Query, and reusable/shareable with its own security.
- Technically no BC license needed to pull into a data flow (check licensing guide). Reports/Excel then "Get data from Power Platform" → data flows, no API URLs needed.

**Export to Excel from Power BI**
- "Analyze in Excel" (File > Export, or dataset three-dots): Excel with full live data model, relations, measures.
- Export with live connection: on a published report visual, three-dots > Export data > summarized; Excel stays connected to the dataset, limited to ~500k rows.
- Any Power BI report also exports to interactive PowerPoint (.pptx).

**Incremental refresh**
- Manual in Power Query: split table into refresh/no-refresh parts, load, merge. Or use the data flow incremental-refresh setting (needs a datetime field). Caveat: BC APIs don't support query folding well — test that it actually refreshes incrementally.

**Embedding Power BI in BC**
- Default Power BI report part on role centers/list pages; extendable. Add a Power BI fact box via a page extension; wire selection so choosing a record (e.g. purchase order) auto-filters the report. Requires publishing report to Power BI service and enabling "filter on all pages" with the filter field (e.g. document number). Multiple report parts per role center possible; profiles/roles can enable different report sets.

**Power Platform integrations**
- Power Automate to refresh Power BI datasets or alert on metric thresholds; combine Dataverse + BC data; embed Power BI into Power Apps. Contextual filtering in Power Apps: extend the tile-from-dashboard URL with a filter on the primary key matching the app selection.

**Telemetry**
- Power BI telemetry app "Usage" report: which report layouts consumed, action (download/preview/print/save), layout type, per user. "Performance": background vs web client, extensions, SQL stats, incoming web service (API) call performance.

- Reference docs: aka.ms/bcreporting.

**Testing**
- Report objects can have test code (verify data + printouts/layouts). No real test framework for Power BI yet, though CI/CD tooling exists for Power BI.

<!-- ingested: Microsoft Presents: Mastering Power BI Reports in Business C | 2026-07-27 -->

<!-- ingested: Microsoft Presents: Mastering Excel Reports in Business Cent | 2026-07-27 -->
### Excel layouts for AL reports

- New Excel layouts replace the legacy Excel add-in reports. Legacy relied on VBA macros (disabled by default = security risk) and could not be customised. New layouts allow any Excel element (pivot tables, slicers, multiple sheets) **except** VBA/macros, which stay blocked.
- New finance/sustainability layouts ship in **preview** alongside old ones (old ones flagged for eventual removal). Findable via page Search and Role Explorer.
- Both Excel and Power BI are recommended — they serve different reporting needs; Excel is not being dropped in favour of Power BI.

### Report object properties for Excel data sets

- Key property `ExcelLayoutMultipleDataSheets` [sic?] (`= true`) — puts each top-level (root) data item into its own worksheet. Verify exact name against compiler/Microsoft Learn.
- Multi-sheet mode gives ~3x smaller workbook and faster render vs legacy single flat sheet (legacy repeated parent data across rows with many null fields). Also each sheet gets its own 1M-row Excel limit rather than one shared sheet.
- Multiple root data items → multiple data sheets (e.g. main data + dimension sheets for slicers).
- **Data contract**: sheet names = data item names; column names map to report column names. Do not rename in Excel — breaks the contract.
- Migration path for old layouts: set multi-worksheet property true, then update the data sheet references.

### Data set design guidance

- Define `dataset` with data items → tables, columns → fields; nesting supported.
- Set table view (sorting + predefined filters) but avoid over-filtering data out.
- Expose the most important filter fields on the request page from the start so users don't have to add them manually.
- Avoid buffer/temp tables as data items where possible — they consume significant NST memory.
- Choose where to aggregate: aggregate in BC = fewer rows but less flexibility in Excel; aggregate in Excel = more rows but more end-user control.
- Don't use virtual tables if you need captions — platform virtual tables (in-memory) have no field captions, so no translations.

### Labels, captions, translation

- Labels usable in: report object labels (headers), column labels (only emitted when `IncludeCaption = true` on the column). For dynamic captions use `CaptionClass` on the underlying field so caption is programmable, not static.
- Generated **caption data** sheet holds all column + label captions in the language active when the report is run.
- **translation data** sheet = user-defined, custom translations; platform does NOT overwrite it on template update.
- In-sheet translation without AL code: wrap a caption key in `$...$` (dollar signs) in a cell; at render the platform matches against caption data and substitutes the translated value. Works on sheet names, headers, pivot tables, charts, slicers — anywhere a caption shows.
- Rule: reference **captions** not names in `$...$`. Names are Excel-internal; a `$name$` throws an Excel error on next load.
- Not translated: Grand Totals and other Excel-generated values you can't edit.
- Add a new language yourself: copy keys from caption data sheet into translation data sheet, add culture-named column, paste translated values. No AL developer needed. Default (unspecified) language = en-US. Cultures use standard culture names.
- Add new UI strings by adding new caption keys to the translation data sheet.

### Request page & rendering

- `AboutText` / `AboutTitle` live on the **request page** object (UX element), not the report object.
- Use the newer `rendering` syntax to attach one or more layouts to a report. `Caption` and `Summary` on a rendering layout are optional but shown in the layout-selection UI.
- Set `DefaultRenderingLayout` in report properties.
- Quick way to seed a layout: on request page do **Send to → Excel**, download the generated data set workbook, add it to the report's rendering/layout section, then edit.
- User-defined layouts can be uploaded at runtime via the report layouts page (New → name → select file). Must save/close the Excel file before upload.

### Power Query (M) for shaping data

- Power Query is shared with Power BI; language is **M**. Imports/transforms data; can connect to DB, local files, web services, Dataverse, Azure Data Lake. UI-driven, no need to hand-write M.
- `Data → From Table/Range` to load a sheet into Power Query.
- Strongly type columns (e.g. account defaults to integer but should be text; decimals defaulting to integer because demo data is all zeros). Replace the offending step.
- Common transforms in shipped layouts: replace null with blank (nulls break advanced table relationships and confuse users); null decimals → 0; null datetimes → ~100 years in past (visible sentinel).
- Convention: suffix queries with `_query` to distinguish from platform-generated data sheets.
- Load options: Table (exposes data to users), PivotTable, or Connection Only (in-memory).
- Query properties: **uncheck** background refresh (async load breaks multi-query/pivot ordering, forces manual Refresh All); check "refresh data when opening file"; check "enable fast data load" (faster load, less responsive UI during load).

### Pivot tables pattern

- Insert → PivotTable from table/range over a query.
- To flatten (no expand tree): Design → Report Layout → **Tabular Form**; Subtotals → **Do Not Show Subtotals**; PivotTable Options → uncheck expand/collapse buttons; enable "refresh data when opening file".

### Aggregated metadata sheet

- Hidden generated sheet with environment + report info: environment name, company name, **company ID** (usable to call BC APIs from the workbook), user, run date, language, and request-page filters applied.
- Company ID / metadata enables lookups back into BC UI and API-driven refreshable data.
- Supports named ranges (Excel Names) to simplify formulas.
- Can be deleted manually if not wanted; platform regenerates it on next run. (Possible future option to suppress it.)

### Housekeeping / gotchas

- Before shipping a layout, clear table rows and Refresh All → sheets go blank; good test for dangling references. On import the platform strips data from uploaded layouts anyway (prevents leaking one customer's data to another).
- Data sheets and translation data sheet can be pre-hidden; hidden state is saved into the layout and applied for all users on download.
- Standard report/dataset extensibility applies: extension objects can add data items/columns to an existing report; then update the workbook's data tab + query, and pivots pick them up.
- Refreshable (API-backed) Excel layouts are possible but awkward with request-page reports — request pages don't pair well with API refresh, hurting UX. Decide up front: frozen-in-time (data pulled from BC sheet once) vs refreshable (reads from API each open). Can mix multiple queries from different sources in one workbook.
- Printing: hidden metadata/translation sheets are not intended to print, but this was noted as not well tested [sic? verify].

### Power BI integration with Business Central

**Extracting BC data into Power BI — two paths:**
- **Explicit REST APIs** — AL objects of `PageType = API` or `QueryType = API` [sic?] (verify query API type against compiler). Set `APIGroup`, `APIPublisher`, `APIVersion` properties. Publish extension → consumable over HTTP.
- **No-code OData endpoints** — expose any page/query/codeunit via the Web Services page. Generic, not designed as APIs. Gotcha: if the underlying page triggers GUI (message/confirm dialog), it crashes in an API client. Demo-tool-provided web service names are demo data — don't rely on them; no performance guarantees.

**Built-in Microsoft APIs:**
- Always present in every environment; Microsoft maintains their availability.
- Use **v2.0**; v1.0 is deprecated.
- URL shape: `.../api/v2.0/companies({systemId})/accounts` — company addressed by system ID (GUID), then entity (e.g. `accounts` = G/L accounts). Returns JSON.
- Additional first-party API sets: subscription billing, sustainability, and the analytics APIs used by the Power BI reports.

**Power BI connector (Get Data):**
- Generated M function: `Dynamics365BusinessCentral.ApiContentsWithOptions` [sic?] (auto-caption garbled — verify exact name in Power Query). Other three legacy connector functions are deprecated; use this one.
- Params: environment name, company name, API prefix, options record. Args can be null → default values.
- Options include: use **read-only replica** (separate copy DB, takes no locks, independent of primary), response encoding, request timeout, and paging control (connector pages over all records).
- Custom API prefix specified via the same prefix argument.

**Viewing reports:**
- In app.powerbi.com workspaces, or embedded in BC pages — full page, factbox, or context-aware on a record card (e.g. customer card takes the record context).

**Out-of-box analytics reports:**
- Areas: finance, sales, purchasing, inventory, inventory valuation, projects, manufacturing, subscription billing, sustainability.
- Two components: (1) an AL app exposing the `Microsoft.analytics.v0.5` [sic?] API prefix (verify), sitting on top of base apps; (2) Power BI **template apps**.
- Template apps cannot be modified directly → Microsoft is open-sourcing the `.pbix` files so you can inspect measures and queries and customize. Long-term plan: ship pbix inside the app to avoid version-dependency issues.
- Template app contents: semantic model for the domain, measures for common KPIs, a theme.

**Dimension flattening:** dimension set entries are flattened server-side in BC before querying, giving cleaner relationships and saving processing time. (Possible future move of flattening to the Power BI side.)

**Setup flow (via PowerBI Connector Setup page):**
- Install the matching Power BI template app for your BC version (e.g. 26.2) into a workspace.
- Fill connection details (company name, environment name) in the app to replace sample data; set the dataset **privacy level**.
- Semantic model refreshes once/day by default — reschedule via the three-dot menu; check **refresh history** for troubleshooting/support.
- Link workspace reports back into BC via the PowerBI Reports setup wizard; configure date-table range and account-category mapping (which accounts map to assets, etc.).

**Licensing & permissions:**
- **Power BI Pro** license required to schedule refresh and view reports (presenter unsure whether a plain BC user needs a Power BI license to view embedded reports — verify).
- Refresh runs under the **scheduling user's** BC permissions — that user's company/data access governs what the dataset pulls (admin scheduling → dataset has admin-level access).
- BC permission sets can restrict which report pages a user sees inside BC, but do not stop access via app.powerbi.com — restrict from the BC side.

**Performance / gotchas:**
- Large ledger tables (millions of rows) frequently **time out** — many HTTP requests even when paginated by 10,000, and the Power BI service itself times out.
- Mitigation: limit entries / restrict by date for the initial import, then load incrementally from a given date onward.

**Multi-company reports:**
- Not offered out-of-box because cross-company customer consolidation (same customer, different numbers/names per company) is case-dependent.
- Do it in M: define the list of companies from the tenant, then per source table query `<table> in company <prefix>` and combine/merge across companies (helper functions shown in the presenter's repo). Requires a manual matched-customer mapping for true consolidation.

**On-premises:** not supported by default, but an on-prem connector exists — reuse the open-sourced pbix semantic model and measures with it.

<!-- ingested: Microsoft Presents: New capabilities in reporting and analys | 2026-07-27 -->
### Data analysis (analysis mode) — related-table fields (26.2)

- Analysis mode (list pages + queries, web client, no dev needed) shipped 2023 release wave 2. Original limit: only fields already on the list page/query; extra fields needed a page extension or new query.
- 26.2 (released ~2026): end users can add fields from related tables/pages directly in the web client, no developer.
- UI: Analysis tab → **Add columns from** action. Offers: (a) fields from the underlying table not exposed on the page; (b) fields from tables with a table relation to the underlying table (relations read from AL code — a table can appear multiple times if related via multiple relations); (c) **Other source** for the full list.
- Can pick a list/card page implementing the target table instead of the raw table — shows field descriptions + sample values.
- Also add related columns via the per-column menu.
- After adding: reorder/delete columns, group, filter, aggregate as normal. Export to Excel keeps the joined related fields.
- Limitation: analysis assist (natural-language) does NOT yet work with related fields.
- Under the hood: server scrapes AL table relationships for the base table, filters out tables the user can't access + internal/temporary tables, sends list to client. Client shows fields (also filtered: internal/unsupported hidden). Server builds a **dynamic query as an AL object**, compiles it, runs it, returns data. Query has one column per field, one data item per relation, data-item links from the AL table relation.
- Joins are all against the base table only — no chained/multi-level joins (join to A then join A→B not supported). Depth otherwise unrestricted. Feature is analysis-view only, not personalization.
- `GetUrl` [sic? verify method name] gained a **layout** parameter — embed a URL that opens a page directly in analysis mode; other layout-parameter values exist.

### Reporting — AL (recent releases)

- **.NET number formats** now usable via the `AutoFormatExpression` property (advanced/conditional formatting). Only `AutoFormatExpression` — NOT the `Format` function.
- New report trigger **OnPreRendering** [sic? verify exact name] — data-collection step before layout render. Server capabilities added alongside: append/attach a list of PDF documents, embed documents in the PDF, set admin + user passwords to secure the document. Used internally for invoicing but general-purpose.
- Three new AL layout properties to mark a layout obsolete: obsolete **tag/state** and **reason** [sic? verify exact property names]. Shown on Report Layouts page; can also be set via UI (only the uploader of a layout can obsolete it).

### Reporting — runtime / UI

- **Exploring Reports** page: info icon shows About Title/About Text; new action opens the request page in a new window (run report without leaving session). About properties also feed search/discoverability.
- **Report Layouts** page new columns: obsolete flag, Excel sheets, Last Modified Date, Last Modified By (troubleshooting).
- New actions: **Update and export layout** (refreshes layout with latest metadata); **Export report schema** (downloads the custom XML — import into Word to bind an existing Word structure to the BC data items); **create blank layout** toggle when adding a new layout (generates empty Word/Excel doc already containing the custom XML); **Show layout info** (system ID for telemetry, created/modified dates + by); **Validate layout** (runs validation steps, e.g. font validation, reports which failed).
- Font validation currently RDL only — not yet Word/Excel.

### Reporting — Word layouts & Word add-in

- Two always-available metadata objects in the custom XML: **report metadata** and **report request** [sic? verify names] — expose report ID, about, title, name, username, company, etc. No need to code these into AL.
- **Business Central Word add-in** (from AppSource): v1 supports layout comments + conditional visibility controls. Full **section** support (margins, orientation, footers, watermarks, page breaks).
- Layout controls in add-in:
  - **Insert layout comment** — content inside is hidden at render (docs/versioning).
  - **Hide empty table** — hides a table when it has no data.
  - **Hide empty table row** — apply to a data item in a row; row removed if that data item is empty.
  - **Hide empty table column** — apply to the column header data item of a repeater; column removed if all repeater rows are empty for it (frees space).
  - **Hide field if zero** [sic? name] — apply to any data item; hidden when value = 0. Not bound to a table/repeater.
- Controls can be combined on the same data item (e.g. hide-if-zero + hide-empty-row → drop rows whose value is zero).
- Nesting: some nesting supported, not all cases; adding a nested level into an existing layout can fail — improvements planned.

### Reporting — Excel layouts

- New AL layout property **ExcelLayoutMultipleDataSheets** [sic? verify exact name] — previously only on the report object, now settable per layout so each layout can override the report default. Visible/settable in UI.
- **Named formulas**: readable names mapped to `XLOOKUP` formulas under the hood (e.g. type `=CompanyName`). Full list in Excel's **Name Manager**; many common functions pre-mapped; you can add your own.

### Positioning / roadmap notes

- RDL is NOT deprecated and not being removed; MS simply isn't investing in it now — investment focused on Word/Excel. Keep RDL for complex scenarios.
- v27 preview: modernized production-order-statistics gets two new layouts (one Word, one Excel) — telemetry shows both print and export/download use cases; consistent look across layouts planned.
- Not currently possible: extract the generated dynamic query from analysis mode; use a query object as a report data item; e-document attachment via AL API (exposed only via the new trigger due to licensing, not technical, constraints).

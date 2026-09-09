<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Reporting, Power BI, Excel layouts

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 2. Reporting & Power BI (developer / consultant)

**Excel layouts.** Hidden metadata worksheets (v23.3) hold **static metadata** (source extension,
`AboutTitle`/`AboutText`, help link) + **request metadata** (Tenant ID, environment name/type, company
name, **Company ID**, run date/time) + **Caption Data** (from `IncludeCaption` columns + `labels`,
values filled per user language). `$$<caption>` tags in sheet names/chart titles/slicers translate at
runtime — a leaked `$$…` means the tag was unresolvable. **User-Defined Translation Data** sheet
supplies non-caption strings per language. Build **refreshable API reports**: Power Query against the
BC API URI assembled from the env-name + Company ID metadata cells → shrink the dataset to near-zero.
Excel Copilot needs only the raw dataset (workbook on OneDrive). ~7 OOB Excel reports shipped v24
(preview); legacy Excel reports likely deprecated. *(Excel layouts for devs)*

**Word (document) layouts.** Office-store add-in **"Business Central"** (layout-only, holds no data)
adds a ribbon: **Insert Layout Comment** (hidden dev comments that never render); conditional
visibility — **Hide Empty Table / Row / Column** + **Hide Field if Zero** (combine the last two to
blank then drop a column). `WordMergeDataItem` now supports **sections** (2024 w2) → per-section
margins/orientation/watermarks (earlier "unsupported" warning is void). **Themeable** layouts support
Office Document Themes. New barcode fonts (Planet/PostNet/IMB) + Aptos in the service. Revamped data
picker + preview "Insert Table" builder (BC theme, search, dark mode). *(Enhanced doc reporting 2024
w2 & 28.x)*

**Report layout lifecycle & tooling.** Report Layouts page actions: **Export Report Schema** (map
fields onto a customer's Word doc lacking BC metadata), **New** blank layout, **Update and Export**
(inject latest metadata after a report extension enlarges the dataset), **Replace**, **Validate**
(RDL in v26; Word/Excel later), **Show layout info** (System ID = telemetry `layoutId`; created/
modified only populate for user-imported layouts, not app-provided). Word layouts expose a
system-generated **`BC Report Information`** node in the XML Mapping pane (report + request metadata:
env, company, user, render language, date hierarchy) — bind it instead of coding company/user/date
into the AL dataset. Layout **lifecycle states** Draft → Pending Approval → Approved → Retired for any
user-defined layout (stops users breaking customer output on live layouts). Company-level default
document language on Company Information (fallback below the customer card). Layout-lifecycle telemetry
sample `report layout life cycle.kql` at aka.ms/bctelemetrysamples. **GOTCHA:** `Report.WordLayout` /
`RDLCLayout` / `ExcelLayout` methods are being **deprecated** (meaningless with multiple layouts) —
use the `rendering` section. 36 new document-type PDF/GET APIs (28.x). *(Reporting for devs 2024 w2 /
2025 w1 / Enhanced doc reporting 28.x)*

**Power BI embedding.** From AL, configure a Power BI part via `element type` / `element ID` /
`element embed URL` / `context`, usually in `OnOpenPage`; **lock to selected element** to remove the
picker/nav so users can't change the report; `element type = report visual` drills to a single visual
via `page ID` + `visual ID`. Power BI scorecards/metrics embeddable too. v26's ~70–80 new OOB Power BI
reports use the `PageType = UserControlHost` embed for a clean UI — partners get the same by using
that page type (samples aka.ms/bctac). Excel as a Power BI client (Get Data from Fabric → pivot);
Power BI Deployments page for "five clicks to demo" deploy/download PBIX (refresh scheduling still
manual). *(Power BI 2023 w2 / embedding 2025 w1 / Enhanced Power BI & Excel)*

**Analytics surfaces.** Data Analysis mode works on **query objects** (not just list pages); ship
**Analysis Views** from AL apps (build in client → Export Definition JSON → `DefinitionFile` property,
override `Caption`/`ToolTip`/`Visible`; scope to a profile via pagecustomization; app-shipped views
are read-only, users duplicate to edit). Many analytics releases ship OOB analysis views in 28.x
(GL/FA ledgers, item-ledger, sales-order, ABC analysis). Docs "Packaging analysis views"
aka.ms/bcdeveloper, aka.ms/bcanalytics. *(Analysis mode 2026 w1 / Power BI 2023 w2 / analytics videos)*

---

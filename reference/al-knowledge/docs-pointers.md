<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Docs & learning pointers

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 8. Docs & Learning pointers

- **aka.ms/bcdeveloper** — developer docs hub (reorganized 28.x): getting started, "Programming in the
  AL language" (data-type how-tos) vs "The AL programming language" (constructs), Data analytics for
  devs, Reporting (major rewrite incl. Word layouts), Error handling (actionable errors, stack traces),
  Troubleshooting (tools + TSGs), Asynchronous processing (background tasks/task scheduler/job queue),
  Telemetry for AL devs, Security for developers, Extensibility overview. Encourages doc PRs. *(Learning
  content — developers)*
- **aka.ms/bcintegration** — integration hub for architects/integration devs: Office/M365 (Excel/Word/
  Outlook), Power Platform (connector/REST), Dynamics + Dataverse (data sync / virtualization / change
  events / business events), Azure infra (HttpClient + system-app modules: App Insights/Blob/File/
  Functions), foundational services (Entra auth, Universal Print, Purview audit), web services (REST
  recommended; OData + SOAP legacy). Enumerates every API — feed it to agents as knowledge. *(Learning
  content — architects & integration devs)*
- Other: aka.ms/bcanalytics, aka.ms/bcreporting, aka.ms/bcexcelsamples, aka.ms/bctelemetry(+samples),
  aka.ms/bcsecurity, aka.ms/bcsovereignty, aka.ms/bcsamples, aka.ms/bctac, aka.ms/bcideas, aka.ms/bcall,
  aka.ms/ALGoWorkshop, aka.ms/ALGoReleaseNotes, aka.ms/ALGoDeprecations.

<!-- ingested: BC TechDays 2022 - Build collaborative apps for Business Cen | 2026-07-26 -->
### Collaborative apps — Teams cards, Excel layouts, OneDrive share (mibuso TechDays 2022 — Microsoft: Monica, Evgeny, Sam)

**Teams — adaptive cards for entities**
- Sharing BC record link into Teams renders adaptive card preview. "Stage view" = near-full-screen entity view in Teams; pin-as-tab coming in later release. Features online-only.
- Developer controls which fields appear on card. Two mechanisms:
  - **Brick field group** — add a `Brick` field group on the source table listing summary fields. Second field in group is projected bold (matches web/mobile bold-field behaviour) → consistent across clients. Recommended default approach; metadata usually enough.
  - To extend an existing entity's card, in a tableextension use `addlast` on the base `Brick` group rather than defining a new one.
  - **AL events** — 3 events in system app, `Page Summary Provider` module [sic? verify module/event names against Learn]. Demo used `OnAfterGetSummaryFields` [sic?] with params page id, record id, field list. Add/remove fields from the list; add order = display order on card. Filter by page id to target a specific card.
- Developer only controls the field list, NOT card actions. Actions/buttons on Teams cards are a Power Platform concern.
- Test in online sandbox, not Docker (features are SaaS-only). Admins: use centralized deployment so all users get the Teams app.

**Excel layouts / reports**
- Report layout can be chosen/switched at run time (pick primary or new layout); Excel can be set as default report layout for all reports going forward. Layouts ship with the report app.
- "Edit in Excel" / "Open in Excel" gives live data via APIs.

**Organizational data types (Excel)**
- Excel feature that resolves an opaque cell value (e.g. a customer number) into rich ERP data via APIs, abstracted from source.
- Powered by Power BI, so requires **Power BI Pro** license — Power BI holds a caching layer between Excel and BC (Excel→Power BI→BC periodically), avoiding heavy direct query load on BC backend.
- Developer builds custom APIs to expose the data; publish a Power BI report and mark the table as a **feature table**, providing a label and primary-key column so Excel can resolve entities.
- Works with Excel desktop and Excel online.

**OneDrive share / open (developer API)**
- Share action uploads the BC file to user's OneDrive for Business first, then shows standard M365 share dialog (email link, copy link, adjust link settings). Files land in a `Business Central` folder, split by company name.
- Extend via `Document Sharing` codeunit [sic? verify name] in system application, `Share` method taking file name, file extension, and data stream, plus an intent enum: values Open / Share / Prompt (Prompt shows a menu to end user).
- Actions: `Open in OneDrive` and `Share to OneDrive` — reuse base-app captions/tooltips/images for consistency; copy the base-app boilerplate.
- Set the action `Visible` property to the system-app helper that hides actions when OneDrive integration is disabled.
- Recommend keeping a `Download` action alongside open/share so users retain all options. Most open file formats preview in OneDrive; proprietary formats may not. Zip files preview with contents listed.
- Admin: new **OneDrive setup wizard**, environment-wide (cross-company), permission-gated. Two toggles — app features (AL-invoked open/share actions) vs system features (platform, e.g. Edit in Excel, reporting). Migration step shown for legacy SharePoint/OneDrive config. SharePoint admin center sets tenant-wide file-sharing policies (external sharing, link expiry).
- Cannot fully control target directory programmatically; files go to the company directory, though you can append a child directory in the passed path. My Settings → "Cloud storage" link opens the BC folder in OneDrive.
- Outlook share action always opens Outlook **web** app; no one-click to Outlook desktop (copy link instead).

**Approvals via Teams (aside)**
- ~67 out-of-box approval templates deploy as Power Automate flows using the Teams Approvals app; approve/decline from Teams/phone calls back to BC web services. Works today; BC itself lacks a native approval UX pattern for user notifications.

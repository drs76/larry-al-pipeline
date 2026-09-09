# bc-client-features

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2023 - What's new in Business Central clients fo | 2026-07-27 -->
### BC clients — new AL developer features (v22 + lab, TechDays 2023)

**Access keys / key tips (v22)** — platform-generated keyboard access to nav menus, nav links, primary action bar, role Center. No AL code needed; just upgrade to v22.
- Press `Alt` to show key tips; press shown char to invoke; `Esc` goes up a context level.
- Key tip char derived from action Caption (or Name if no caption). Shorter/single-char tips for highest-priority actions; usually first letter of first/second word.
- Some frequently-used actions get a fixed "preferred" key tip for cross-page consistency (e.g. Report = `T`).
- Nav groups grouped under `J`, action groups under `X`, system actions elsewhere — contextual subsetting.
- Position-dependent: moving actions left/right can change their access key. Affected by personalization.
- Contrast with **keyboard shortcuts**: those are AL-defined by developer, only on selected actions, stable across pages, unaffected by personalization/position.

**Personalization of action bar in Parts (v22)** — same designer experience as main action bar; supports split buttons and teaching tips in parts. `Manage` group is pinned by default. Requires **modern action bar** feature enabled. Clearing personalization in a part reflects everywhere that page part is reused.

**Analysis mode / analyze data on list pages (v22)** — enable via feature management; shows `Analyze` toggle on list action bar. Ad-hoc filter/column/group/pivot without a report or dev. Tabs pane, data area, field-modifier pane. Drag columns to row groups / column labels to pivot. Date columns can be grouped by year/quarter/month. Reorder column-label fields to change pivot nesting. Export/copy to Excel etc. Usage visible via Power BI usage reports → client actions (per page/user).

**Actionable error messages (v22, preview → GA in a minor update)** — two new `ErrorInfo` methods:
- `AddAction(caption, codeunitId, procedureName)` [sic? verify method/signature on MS Learn] — runs a codeunit method to resolve the error from the error dialog. Use only when the fix outcome is certain (e.g. reopen a released doc). Procedure name passed as literal string.
- `AddNavigationAction(caption, pageNo)` [sic? verify] — sends user to a page for a multi-step fix. Caution: check user permissions to target page first, else you just chain more errors.
- Not supported in inline validation bar (at time of talk).

**Legacy views deprecated** — migrate to modern views. Legacy = actions on role Center pages using `RunPageView` [sic? verify property name]. Modern views defined declaratively in a `views` section on the filtered page itself; each view can have its own layout. Search role Center pages for the old pattern and move them.

**Rich Text Editor (lab / upcoming)** — usable on any page. Requirements: add a field that sits **alone in its own group**, with properties `ExtendedDatatype = RichContent` [sic? verify] and `MultiLine = true`. Backing table field should be **Blob** (not Text — Text caps at 2048 chars and HTML rich content overflows). Read/write blob via streams: `CalcFields` the blob, create in/out-stream with a text encoding — use the **same encoding** for read and write.

**Tell Me / search on mobile (lab)** — search field added to mobile nav pane opens Tell Me on phone/tablet; searches pages & reports, respects permissions, supports bookmarking. Keyboard shortcut `Alt+Q` on tablet.

**Native barcode scanning (lab / next release)** — annotate a field `ExtendedDatatype = Barcode` [sic? verify] to get a scan action (like drilldown/assist-edit) that opens camera, scans, parses, fills field. Programmatic API: `BarcodeScannerProvider` [sic? verify name] — add dependency, declare variable, initialize early (e.g. OnOpenPage) only if scanner IsAvailable (new devices = phone/tablet), then `RequestScan` [sic?]; callback receives barcode value + format. Hardware scanner support being explored.

<!-- ingested: BC TechDays 2022 - What's new in Business Central clients fo | 2026-07-27 -->
### Control add-in callback throttling (v21)
- Control add-in callbacks to server previously shared same event queue as user interactions (save, activate field) — chatty add-ins slowed whole client.
- v21: add-in callbacks get own internal queue, processed one-by-one, separate from user-interaction queue.
- Queue depth 20 → warning dialog shown (so devs notice runaway add-ins). Depth 50 → new messages ignored/dropped. Numbers internal, may change.
- `InvokeExtensibilityMethod` [sic?] extended with new callback fired when a request fails or is ignored. Note: callback does NOT report which error occurred, and covers queue-drop case only, not arbitrary AL errors. Verify method name + new callback signature on Microsoft Learn.

### List views (existing feature, recap)
- Define alternate data representation on a page: filters, sort, plus UI customization (reorder/hide fields).
- Declared in AL via a `views` section on `page` of type `List`, also usable in page extensions / page customizations; can extend base app pages.
- View properties: `Caption`, filters, `OrderBy` [sic?] with sort direction on one or more fields. Verify exact property names against compiler.
- Two kinds:
  - **Shared layout** — reuses default (`view all`) layout; user personalizations + profile configs apply automatically.
  - **Custom layout** — dedicated `layout` section (like page ext/customization) to reorder fields and set properties (e.g. visibility); NOT subject to user personalization or profile config.
- Users can copy/create/modify views client-side from filter pane dropdown.

### Grid fast data entry — draft rows (v21)
- Old: only 3 draft rows kept ahead. Fast multi-row entry exhausted them, forcing wait for server round-trip to allocate more → stutter.
- v21: draft row buffer raised to 15 (still only 3 shown in UI). Client can add rows browser-side without server round-trip until buffer drained, then refills async in background.

### Scope=Repeater actions (v21)
- Repeater-scoped actions (appear on list-page rows) previously ALSO had to be promoted to always render — undocumented-in-compiler gotcha.
- v20 and earlier: behavior unchanged (still need promotion); new UICop rule warns when targeting those versions.
- v21: repeater actions render regardless of promoted state.

### Split button (v21)
- New action-group render style. Set group property `ShowAs = SplitButton` [sic?] (verify). First visible+enabled action in group becomes primary click target; dropdown arrow reveals rest of group.

### Custom actions / Power Automate flow actions (v21)
- New `customaction` [sic?] construct to trigger actions outside BC. Current type: `Flow`.
- Page's associated Power Automate flows auto-discovered and surfaced in client; user can reposition them.
- Flow custom action needs Flow ID + Environment ID properties (copied from Power Automate) so runtime can trigger. Verify keyword/property names against compiler.

### New promoted-action model — action refs (v21, "V2")
- Old model ("V1") limits: max 20 promoted categories, can't create/reorder categories, can't order actions within a category, no subgroups, promoted actions created implicitly via `Promoted=true` + `PromotedCategory`, plus legacy `PromotedIsBig` (ordering) and `PromotedOnly`.
- V2 introduces explicit `promoted` **area** = left side of action bar (the promoted/left side, vs right-side "action repository").
- New `actionref` construct: a reference to an existing action, defined only in the `promoted` area. Inherits all properties from target action; only `Visibility` (+ obsoletion) can be overridden. No code duplication.
- Capabilities unlocked: top-level promoted actions (no group), arbitrary groups/subgroups (nested), explicit ordering, full group property set (e.g. `ShowAs=SplitButton`), unlimited reorderable categories.
- Cannot mix V1 (promoted properties) and V2 (actionref) syntax within the SAME object. Different objects in same extension may each pick either.

### V1↔V2 interop & conversion
- V1 pages auto-converted to V2 under the hood at runtime, so an extension can be V2 over a V1 base page (and vice versa).
- Auto-generated names you must reuse to avoid breaking dependents:
  - promoted category group → `Category_<CategoryName>`
  - promoted action ref → `<ActionName>_Promoted`
- AppSourceCop rule flags actionrefs/categories not following the naming convention (e.g. error `<name>_Promoted is not found`).
- VS Code **code action** (lightbulb) converts a page V1→V2. Scopes: single instance, whole document, project, or workspace (bulk-convert many pages/projects at once). MS used it to convert system + base app.
- `PromotedIsBig` on conversion reorders — a big action sorts before a non-big one in same category.

### Base app action-bar redesign (v21)
- Action bar auto-pinned on open.
- Actions reordered by telemetry-driven usage; layouts made consistent across pages (same top categories, same action order, same split buttons).
- Top categories trimmed; some demoted to subcategories; split buttons used to reach subcategory actions in one click.
- Merged overlapping Order/Navigate groups.
- `Process` category auto-renamed to **Home** (aligns with other MS products).

### Personalization / UX changes (v21)
- Designer/personalization now supports dragging categories, nesting groups, moving actions to root — previously impossible.
- Old "remove" vs "hide" confusion fixed: "remove" (was `PromotedOnly=true`) and "hide" (`Visible=false`) were inconsistent. v21: remove always removes action/ref from current extension; hide always sets `Visible=false`.
- `PromotedOnly` concept dropped in V2 — all promoted actions treated as promoted-only by default (focus users on left side).
- If ALL actions in a group are promoted, group no longer rendered on right side.
- If SOME actions promoted, group still shows on right with unpromoted actions listed directly; promoted ones tucked into system group **Other** (one extra click). Toggle off short menu to flat-list instead.

### Modern action bar feature flag (v21)
- Feature flag "Modern action bar": OFF for users upgrading to v21, ON by default for new users. Users can "Try out" from Feature Management page.
- Flag OFF reverts highest-UI-impact changes:
  - nested promoted categories moved back to root.
  - **actionref visibility depends on base action visibility** — an action promoted (`Promoted=true`) from a HIDDEN group: V1 showed it on left (copy escaped the hidden group); V2 actionref inherits hidden→invisible. Breaking change; flag-off keeps it visible. UICop rules warn on this pattern.

### Customization conversion to V2
- User personalizations (stored as AL) auto-converted, reusing code-action internals. Silent for users.
- Profile customizations auto-converted, including on import of exported profiles with promoted syntax.
- New partner telemetry signals for profile-config create/update/remove/export/change; import wizard shows warning summarizing converted duplicated constructs.
- Designer mode (sandbox / VS Code-published ext): publishing a page with promoted syntax shows a lock icon in web client; click to auto-convert page (one-click).

### Keyboard access (Q&A)
- Action bar reachable via Tab to focus into it, then navigate buttons. No dedicated shortcut to jump straight to action bar (as of v21).

<!-- ingested: NAV TechDays 2018 - Business Central: The new face of the cl | 2026-07-27 -->
### Modern UI client (Business Central, 2018 spring + fall)

**Role center layout**
- Navigation moved from left sidebar to a top navigation bar; lets users explore areas without navigating in. No metadata/dev work — lights up automatically.
- Ribbon removed; replaced by an **action bar** (flat list of items, wrap layout when rendered beside another control, full-width otherwise). Migrating actions requires reworking action **grouping** and **promotion policy** so they surface correctly.
- **Cues**: two render modes — normal and **wide layout** (wide suited to decimal/multi-digit values). Actions and indicators still supported.
- **Headline control**: newspaper-style carousel of dynamic, actionable messages. Reloaded on every page load — code it to compute insights per load.

**Building a custom headline (procedure)**
- Create a headline **page part** (page of type headline), then a **pageextension** on the role center.
- Hide the built-in headline via `Visibility = false` on its control, then add your part after it.
- Gotcha: **every** headline field AND the added part must set `ApplicationArea` or nothing renders. This was the demo's failure point.
- Business Manager role center is page **9022** `[sic?]` (transcript garbled between 9022/9023 — verify object number).

**Document/card pages (fall release)**
- **Stacked (paper) layout** shows navigation + process context; click grey area or press Esc to go back. Dedicated **back button** added.
- Action bar replaces ribbon on cards/documents too. **Contextual action bar** for page parts sits next to the part (not in the main action bar), reducing clutter.
- New **header** area holds CRUD system actions: Edit toggle (shows edit vs view mode), New, Delete — pulled out of the old Home tab.
- Navigation (previous/next record) actions moved to mid-page.
- **Wide layout** toggle to expand page to full screen; auto-enters wide layout when a FactBox opens. FactBox open/closed state is remembered per page.

**Tell Me (Alt+Q)** — evolution of page search
- Search order: actions from the **root page only** (sub-page actions do NOT surface), then pages & tasks by usage category, then reports, then documentation.
- Documentation results (Microsoft Learn) surface **only on cloud**, not on-prem; currently only Microsoft's own docs.
- Dev requirements: set informative **captions** on pages/reports (used for match); opt in via the **UsageCategory** property (its value decides pages-and-tasks vs reports placement).

**Filtering (new in web client)**
- Filter pane on the left. Supports all prior filter expressions: ranges, date expressions, application-defined tokens, logical operators.
- **Flow filters** reintroduced (reduce data used for computed/FlowField values, vs column filters reducing rows).
- Filter state is **session-stateful** (survives navigating away/back within a session; discarded on session expiry). No saved views yet — a modified view shows its name in italic to indicate dirty state.
- Can filter on **all source-table columns**, not just visible ones (shown below visible columns).
- Known gaps at the time: only one value selectable per option field (multi-option selection not yet supported); document/line pages have no filter pane (use right-click 'filter to this column'; full pane planned via focus/expand mode).

**Keyboard shortcuts** (11 new; ~40 total)
- `Alt+Q` Tell Me; `F3` focus search, `F3` again returns to grid; `Alt+Shift+F3` create filter line on current column (additive); `Ctrl+Enter` return to grid at same column; `Ctrl+Shift+F3` focus flow filters (type-to-search field). Verify exact chords against Microsoft docs.

**Copy/paste**
- Row copy/paste within a list, and between similar lists if column order, count, and type match.
- Paste from Excel/Outlook with same order/count/type constraints; pasted values are recomputed. Copy from BC to Outlook produces HTML-formatted output.

**Quick Entry (work-in-progress, spring)**
- Enter moves through Quick Entry fields; **Shift+Enter** = reverse. Within grid: Enter cycles rows to last Quick Entry field; **Ctrl+Enter** exits grid (to first field after); **Ctrl+Shift+Enter** exits grid to first Quick Entry field after grid. Cyclic (wraps last→first). Configurable in personalization.

**Virtual grid (WIP)**
- Row **virtualization** (React-based) renders only visible rows → loads more data without render cost, lower memory. Continuous scroll loads more from server (no 'load more' wall).
- Grid **focus/expand mode** on document pages: full-screen grid keeping list totals at bottom; enables filter pane on lines.
- **Save indicator** shows when interactions reach the server and record is persisted (draft has no record until a key field set).

**Other**
- Personalization: column **resize** shipped but only inside personalization mode (no direct drag on live page). Column reorder etc. still being prioritised.
- Single mobile app: 'Business Central' app connects to both cloud and on-prem; legacy Dynamics NAV app remains for NAV 2018 and earlier.
- Accessibility: whole modern UI built accessible from ground up; tested each release. Theming engine underlies the UI (dark mode/high contrast architected but not yet exposed).
- Style/indicator colors: fixed palette of 6 modern-theme colors at the time; custom themes not yet available.
- Cross-browser: officially supports Edge, Chrome, Firefox, Safari, IE.
- Microsoft Invoicing (Office 365) rebuilt on the BC platform using this modern UI; reachable via office.com app tile; uses discovery/fifth-line endpoint `[sic?]` for fast tenant resolution — verify term. Customer tile/image list layout available.

<!-- ingested: Microsoft Presents: What's new in Web Client for AL develope | 2026-07-27 -->
### web-client-updates-for-al-developers

Source: Microsoft "What's new in Web Client for AL developers" talk (caption-derived, unverified).

**Productivity (no AL work needed)**
- Role Explorer / Report Explorer: rich tooltips built from page `AboutTitle` + `AboutText` properties. Tooltip supports markdown (incl. links). Info icon on hover.
- Role/Report Explorer: open page/report in new window (icon) so explorer context is not lost.
- Slim mode pages made wider — can show fields + open factbox at once. Field caption-to-value ratio improved (less caption truncation).
- Factbox resizing now has keyboard support: `Shift+F10`. Preference stored per slim/wide mode in **browser local storage** (not profile/customization) — cleared in incognito, not roamed across machines. Works without personalize/design mode.
- New shortcut `Ctrl+Shift+C` = copy single **cell** value from read-only list (vs `Ctrl+C` = whole row).
- KeyTips (access-key hints) extended beyond English — German, French, Spanish, Danish, Norwegian, etc. Plan: enable all Latin-based languages by default.

**Modern search**
- New free-text search for lists, avoids perf blowups on big datasets. Opt-in, still preview, targeted GA in 2027 [sic? — verify].
- Opt-in via new **field property** [sic? verify name] tagging fields into a search index. Untagged pages fall back to old search.
- Matches terms in any order (word-by-word), not exact substring. Magnifier icon shows which fields participate. Can toggle back to legacy search.
- Usable from AL code as well [verify API on Learn].

**Copilot data entry (no dev story yet, free)**
- Autofill: Copilot suggests smart defaults / fills forms from learned company data patterns.
- Summarize: Copilot summarizes page content.

**New AL APIs**
- PDF preview inside BC (no download). Two procedures: `FileViewFromStream` [sic?] (BC on-prem, takes InStream + filename) and `FileView` [sic?] (BC online, from a file). Verify exact names/signatures against compiler. Viewer supports page nav, zoom, fit width/height, pan, download, print.
- Barcode scanner: can now specify target format(s) in AL to fix mis-detection (e.g. Android picking wrong format). Use control add-in `CameraBarcodeScannerProvider` [sic?]; on ready trigger call `RequestBarcodeAsync` [sic?] passing barcode formats as first param (e.g. QR + DataMatrix). Verify names.
- New page type **`UserControlHost`** [sic? verify] for hosting a single client add-in — replaces the old card-page-with-one-usercontrol trick. Strips header UI (New/Edit/mode actions). Currently locked down: cannot extend, cannot add actions. First use = embedded Power BI reports.

**Telemetry**
- New event `CL0005` [sic? shown as CL00005 — verify code] surfaces client add-in (JavaScript) exceptions with JS stack traces to partner telemetry. Previously invisible — JS errors in add-ins did not show as AL errors; can cause stuck pages / perf issues.

**From the lab (not shipped, may change)**
- Collapsible panes (help, page scripting, Copilot tasks) — collapse to narrow ribbon instead of closing; state/context preserved. Aids accessibility (400% zoom, narrow windows).
- Password-protected PDF preview: native password dialog; must re-enter each open. Password is a PDF feature set at generation time, not a BC/AL setting.
- Perf/size: removed jQuery dependency (~200KB off bundle, smaller attack surface, fewer on-prem security rebuilds). On-demand module loading (e.g. designer/personalization loaded only when used). Ongoing goals: cut page run times, fewer initial network round-trips, more initial rows prefetched. Uses websockets (no per-call HTTP handshake).

**Q&A notes**
- KeyTip inconsistency across page types (e.g. worksheet `Shift+Delete` vs list `Alt+C+D`): generation is dynamic based on active controls per page layout. To lock a shortcut, define an application keyboard shortcut. New/Delete kept consistent for common actions.
- PDF preview currently PDF-only; other file types (Word/Excel/images) not supported, gathering votes.
- Report layout hotfix: preview always shows current data you stream through the API — up-to-date, nothing cached.
- Direct print from code available via cloud printing APIs (not on-prem).

<!-- ingested: NAV TechDays 2019 - Developing for Modern clients | 2026-07-27 -->
### Modern web client — role tailoring, productivity, page background tasks (NAV TechDays 2019)

**Windows (RTC) client sunset**
- BC April 2019 (v14) last release including Windows client; sellable until 2020. ~4-year support lifecycle. Move to web client.

**Roles / profiles**
- Profile is now a first-class AL object, not a DB record. Named, with description and initial Role Center. Customizations stored as AL, not the old client-side XML profile artifacts.
- Role Explorer: interactive map of functionality available to the user's role(s), fed from role/profile definitions (not a hand-built menusuite copy). ISVs can add own roles via extensions, or hide/disable shipped ones. Reachable from search ("can't find it? try exploring" link).
- Roles list page: enable/disable roles, see source (base app vs extension vs user-created), promote roles.
- Default role assigned if user has none, so login never blocked.

**Configuration model — 3 layers (bottom→top)**
1. Extensions (base app + ISV) — designer drag/drop.
2. Role/profile customization ("customize pages" in profile) — consultant edits live system through the target role's eyes; hide/show fields, reorder, resize, fast-entry, create views/filters. No AL coding.
3. Per-user personalization.
- **Soft dependencies:** each layer's change applied only if the brick it targets still exists in the layer below. Remove an extension that added an action → any role/personalization change referencing it silently drops (action gone), user still logs in. Reinstall → change reappears. Deliberately not a hard compile-time reference, so system stays flexible not fragile. Downside: ambiguous references can't be surfaced to a no-code user.
- Every UI change in design/personalization/config mode is codegen'd to AL server-side, compiled, stored in an extension. `Export user-created profiles` on roles list → zip of AL (profile object + page customizations + views). Editable, publishable (Ctrl+Shift+P publish-without-debug), deployable to other environments.
- Gotcha: no UI import of profiles yet (deploy as extension). Personalization/config NOT carried across upgrade/migration to a full release version.

**List productivity**
- Column width now drag-adjustable directly (previously buried in personalization mode). Implemented by silently entering/exiting personalization mode per drag.
- Views: full CRUD (create/rename/remove) in personalization layer, per-user, no personalization-mode entry. Views are first-class AL under a page and follow the page.
- `[sic?] SharedLayout` property on a view — verify name against compiler/Learn. When false the view gets a fully custom grid layout (column width, freeze pane, visibility, order — same code you'd write in a page extension) instead of following base page. Shippable in extensions.
- Advanced filter pane / filter-as-you-type. Same filtering now on report request pages and, first time in web client, XMLports.

**FactBox / multitasking**
- Links & Notes system parts now enabled in cloud, under a separate "Attachments" tab with a count indicator.
- Pop-out page (side-by-side editing): reuses the SAME session, syncs data back to list live via WebSocket.
- New browser tab = NEW separate session, so a modal dialog in one tab no longer blocks the other. Pop-out (shared session) can still hit modality — user gets a message instead of a silent block.
- **Session timeout** default raised to 2 hours in cloud (telemetry: cut timeout dialogs ~90%). On-prem default still 20 min, configurable.

**Uninterrupted data entry**
- Web is async; keystrokes during OnValidate previously lost. New input pipeline queues keystrokes while AL runs, applies them in order when the server is idle. Default-on for all grids, no dev change.
- Gotcha: dynamically editable fields still force a stop/wait — avoid dynamic editability or design around it for smooth typing.

**Keyboard shortcuts**
- `ShortCutKey` property on actions now honored in web client (AL access keys). Watch collisions with new system + native browser shortcuts.

**Page Background Tasks (PBT)** — new async paradigm
- Move slow work (totals, BI queries, external API calls) off the main UI thread so page opens in ~2s and refreshes when results arrive.
- Runs in a **child session** (spawned from parent user session). Goes through OnCompanyOpen — keep that light or child sessions are slow.
- API shape (verify names against compiler/Learn):
  - Codeunit does the work; return values passed back.
  - Page trigger to enqueue: run codeunit with parameters + optional max-execution-time limit `[sic?]`.
  - `OnPageBackgroundTaskCompleted` `[sic?]` trigger receives results, bind to page variables, UI refreshes via WebSocket, no manual page update.
  - `OnPageBackgroundTaskError` `[sic?]` optional — handle timeout/killed session/deadlock/failed connection, e.g. offer retry.
- **Hard constraint: read-only.** Child session CANNOT write to the database (incl. temp tables per presenters, and by extension external services/API — session may be killed at any time, low priority, no consistent stop-with-write). Design PBT + any called services read-only.
- Still single-threaded AL; debugger hits breakpoints inside the child-session codeunit (one thread at a time).

**Client add-ins (control add-ins)**
- Stack shift from .NET to web: TypeScript, React, SASS, webpack, Microsoft UI Fabric / Fluent UI (Office Fabric) component library (accessible, keyboard-ready, Microsoft-styled). BC web client itself built on UI Fabric.
- Best practice: match Fluent styling (zero learning curve), be a "good neighbor" (JS single-threaded, don't hog CPU), minimal-useful-first (e.g. show a cue/badge for a heavy 20MB PDF, load on click, don't block card open).
- Browser API experiments shown (client-side only, no cloud): video stream element; barcode scanning via open-source image-recognition lib on the video stream; File System Access API `[sic?]` to read/write a granted local folder and round-trip contents to AL. Verify File System API availability/name.

**Roadmap items mentioned (2019, may have shipped since — verify)**
- Role Explorer search/"pins" + more country content (initially US/CA/UK). Hierarchical/tree grid control alignment with expand-all. Profile import UI. Print in cloud. Faster first render ("ghosting"). Dynamic-editability fix for data entry. No-breaking-changes policy across app + platform + UI.

**Q&A gotchas**
- Codegen'd personalization/role extension NOT visible in Extension Management (Microsoft safeguard against accidental delete); only accessible via export.
- Un-hiding: you can restore hidden *fields* by user action; hidden actions/parts/cues/tiles cannot be re-added yet — only recovery is reset personalization.

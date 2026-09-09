# data-exchange-files

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2019 - Give Business Central access to your dat | 2026-07-27 -->
### Data exchange framework (import/export pipeline)

- Purpose: define a reusable process for importing/exporting files (bank statements, UBL invoices, currency exchange). Set up via **Data Exchange Definitions** page.
- Flow direction: on **import** runs right→left (reading file → fields → mapping); on **export** runs mapping→right (fields → document). Feedback code unit is the user-facing end (auth prompts, confirmations, completion notifications) — used for manual steps.
- Pipeline stages:
  1. **Reader code unit** — loads the raw file blob into the `Data Exch.` table `[sic?]` (verify exact table name), field holding file content is a blob `File Content` `[sic?]`. Source of file is irrelevant (filesystem, API download, etc.).
  2. **Column/line definitions** — parse file content into the `Data Exch. Field` table `[sic?]`. Line defs = record layouts (e.g. header node vs line node in XML, or header vs detail row in Excel); column defs address data by XPath, fixed positions, or delimited column numbers.
  3. **Mapping** — map parsed fields to destination table fields.
- `Data Exch. Field` `value` field is **250 chars** — a real limit. From **v14**, table adds a value blob with SetValue/GetValue helpers `[sic?]`; overflow beyond 250 chars goes to the blob. Backport this pattern for older versions.
- Reader code units exist per file type: flat/fixed, variable/delimited, XML, JSON. You can write your own reader (e.g. an Excel reader).

### Field mapping: direct vs intermediate

- Two mapping targets, flagged on the mapping setup:
  - **Direct to destination table** — e.g. currency service import maps straight into currency exchange table (Table 330 `[sic?]`).
  - **Intermediate Data Import** table (Table 1214 `[sic?]`) — data restructured by destination table ID + field ID (vs field table which is structured by line/record/field). Requires specifying data-handling code unit **1214** `[sic?]` (same number as the table).
- Intermediate path supports pre-map, map, and post-map code units. **Map code unit 1218** `[sic?]` is required; pre/post optional. Pre-map is where you do lookups/transforms (e.g. resolve description→G/L account, find vendor) before mapping.
- Apply logic loops intermediate records for a table, inits a record, applies fields with validation.
- Mapping options per column: **Optional** (value sometimes blank in source), **transformation rule**, **Validate Only** (data validated but not imported — e.g. check incoming GLN matches own company's GLN to reject misaddressed invoices).
- Gotcha: intermediate table has **no blob value column** — problematic for large values like base64-encoded PDF embedded in XML; needs a workaround.
- The generic direct-mapping code (record references + field references) currently lives inside the bank-statement import procedure — must be extracted to reuse; often you'll write a mapping-specific code unit.

### Transformation rules

- Predefined table of rules; types include Replace, Regex, date/time formatting (locale-specific date parsing — US/Danish/Icelandic), and **Custom**.
- Custom = your own code unit shipped in an extension; if implemented correctly it auto-registers and appears as a selectable transformation rule. Example: Unix-timestamp→date converter (single code unit; use TypeHelper for the conversion).
- Use case: strip non-numeric text (e.g. currency code "ISK") from an amount before evaluating to decimal.

### Extending the reader (manual-bound subscription pattern)

- File-import code unit **1240** `[sic?]` now raises an event before showing the file picker, so you can inject a file (from API/download) instead of prompting the user.
- Use the **TempBlob code unit** to carry binary/large data around like a record. NOTE: the `TempBlob` **table** was replaced by a `TempBlob` **code unit** as a breaking change between **v14 and v15** — migrate table usage to the code unit.
- Pattern for injecting data into a subscriber that must carry state:
  - Mark subscriber code unit with `EventSubscriberInstance = Manual` `[sic?]` (verify property name).
  - SetValue data into the instance, `BindSubscription` to activate only that specific instance, run the triggering process, then `UnbindSubscription`.
  - Why: a normal (static) subscriber spawns a fresh blank instance per event — it has no data. Manual + bind lets a pre-loaded instance answer the call. Reference implementation: standard **posting preview** functionality.
- To trigger the whole bank-statement flow, call code unit **1270** `[sic?]`; replace with your own wrapper that does prep (download file → load into TempBlob code unit → bind) then delegates.

### Job queue / task scheduler

- Job queue now runs on the **task scheduler** (OS-style scheduled tasks), replacing the old NAS polling model. Old NAS polled SQL every ~2s asking for work — expensive on Azure SQL, so Microsoft switched to scheduled tasks tracked in a DB table (rescheduled on service restart).
- NAS still exists in the product but no longer drives the job queue.
- Concurrency configured on the service instance: max simultaneously-executing tasks, **default 10** — appears shared regardless of tenant count, so size to machine capacity.
- **No priority** in current release; the priority field on the job queue table is obsolete. Jobs run per available background sessions.
- Reliability gotcha: tasks can fail to start or fail to complete. Mitigations: (1) surface failing-job count in the UI (cue box) so users notice; (2) a lightweight recurring dispatcher whose only job is to spin off other tasks (designed so it can't fail — always runs even if subtasks fail); (3) an error-monitor task that inspects code units for errors, logs to activity log, and restarts stalled services (add backoff logic, e.g. stop restarting after N attempts). Before starting a job, verify one isn't already running for that record.
- Uses beyond automation: async APIs — schedule the posting work and let the caller poll "done?" instead of blocking. Microsoft increasingly pushes work (post-and-send, data upgrades) to background sessions.
- Related: **page background task** exists for offloading page-level work (out of scope here).

### Incoming documents

- The inbox for documents entering BC; converted into purchase, sales, or G/L journal documents.
- **Main attachment must be an XML file** — this is what gets processed. Binary docs (PDF/TIFF) can be sent to a built-in OCR service which returns XML that becomes the main document. Additional files ride along as supplemental attachments (e.g. original PDF alongside a UBL invoice).
- Documents posted from an incoming document retain full traceability — one click from G/L / customer / vendor entries back to the original.
- Has a `Handled` flag; handled docs drop off the Role Center list. Status runs New→…→Posted.
- Avoid **import-from-camera** on phone/tablet — stores full-resolution image, bloats the document.
- **Data Exchange Types** list links an incoming-document type to a data-exchange definition code. Built-ins: OCR debit/credit, UBL debit/credit `[sic?]`.
- Auto-detection: when a main document arrives, BC runs all configured readers, each landing records in the Intermediate Data Import table; the reader that produces the **most** intermediate records wins and stamps its type on the document. So a custom reader that yields more records than built-ins is auto-selected.
- **Create Document** button is disabled unless an XML main document is present.

### File services integration

- Cloud/hosted BC can't reach your filesystem — bridge via file-service APIs: Azure Blob, Azure Files, Dropbox, OneDrive/OneDrive for Business, RushFiles, etc.
- **Azure Blob** — cheapest, fast storage; auth is the most complex part (sample code on Microsoft Docs and in presenter's repo). Managed via storage account in Azure portal; need account name, container name, access key. Pattern: push binary attachments (PDF/TIFF) to Blob and store only the returned URL in BC instead of the blob in the DB.
- **Azure Files** — nearly identical API to Blob, same storage account/access key; difference is it can be mounted as a drive (PowerShell) and synced from a server via a Microsoft sync agent.
- **Dropbox** — create an app in the App Console, generate an access token; files land under Apps/<appname>. Auth = token.
- **OneDrive for Business** — SharePoint-backed; API via **Microsoft Graph**, auth through Azure AD. Test with Graph Explorer / Graph playground. BC SaaS itself is now a Graph endpoint.
- Design a provider framework with a common interface and per-provider implementations (Blob, Files, Dropbox, RushFiles, local server FS) so the UI/setup is uniform; each provider self-registers. Strip the server-filesystem provider to be fully SaaS-ready — the cloud providers use base-app auth functions and work in SaaS.
- Operational tip: after importing a file, move/archive it out of the watched folder. Exporting ~all customers to a file service took ~1 minute (Blob is fast).

### Document scanning / capture

- Any scanner works if it can drop a file into a linked file service. Office Lens (phone) → crop → save PDF to OneDrive → flows into incoming documents.
- Microsoft Flow (Power Automate) can pick email attachments and route them to a file service or directly into incoming documents.
- To feed data-exchange flow: write code that takes the imported file content and creates an incoming document; if OCR service is active, send the binary attachment to OCR via the job queue.

### Centralized/master-data replication (proof of concept)

- Hook the platform **global triggers** code unit (`OnDatabaseInsert/Modify/Delete/Rename`) to capture changes on a table (e.g. Customer) and serialize each change to an XML "data package" describing the modified record and selected values.
- Route the XML to a destination file service; receiving companies import and apply the same package with matching rules — a way to push master data to many companies (e.g. 800 companies).
- Gotcha: a single edit fired the Modify trigger 4 times → 4 packages; account for repeated trigger firing.
- Same XML-serialization trick works to hand-move whole setup tables between environments (pack setup tables into one XML, import on the other side).

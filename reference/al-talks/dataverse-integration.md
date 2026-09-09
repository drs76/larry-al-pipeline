# dataverse-integration

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2022 - Better together Business Central and Data | 2026-07-27 -->
### BC ⇄ Dataverse data synchronization

- Three distinct BC⇄Power Platform integration mechanisms: (1) data sync (replicates records), (2) virtual tables (no replication, proxy), (3) Power Platform connector. BC does not run on Dataverse.
- Setup via two assisted-setup wizards: **Dataverse connection setup** (base entities — customers/accounts, vendors, contacts, currencies) then a second **Dynamics 365 Sales connection** setup (items, resources, quotes, orders, invoices).
- Base setup imports a Power Apps solution (~2-3 min), auto-generates a **non-licensed application user** for service-to-service auth. Must sign in as Dataverse **admin** during setup (needed to create the app user + import solution). Records synced from BC appear as created by this app user, not the admin.
- Initial full sync: wizard analyses both sides and proposes strategy per entity. Where data exists on both sides, you set **coupling criteria** — ordered match fields (e.g. telephone no. as priority 1, website as priority 2). Options: sync immediately after coupling; conflict-resolution direction (e.g. BC wins); create new record in Dataverse when no match found.
- Dataverse has **no dedicated customer/vendor entity** — single `account` entity with a subtype distinguishing customer/vendor/other.
- **Option-set coupling** (payment terms, shipment methods, shipping agents): these are data in BC but metadata in Dataverse. From ~2022 wave 1 (`[sic?]` "wave 122" — verify release) this is a no-code page-driven coupling.

### Integration table mappings & conflict handling

- **Integration Table Mappings** page holds the table-level sync rules; per-mapping you set conflict-resolution strategy (record changed both sides) and a separate strategy for deletion conflicts (a coupled record deleted on one side).
- `Synchronize Only Coupled Records` flag on a mapping — default TRUE. Uncheck to let scheduled sync also pull in newly-created Dataverse records (e.g. new vendors).
- Two troubleshooting pages: **Integration Synchronization Errors** (generic sync errors) and **Coupled Data Synchronization Errors** (records coupled OK but sync later failed — changed both sides or deleted).
- Ongoing sync runs via **job queue entries** (scheduled recurring jobs).

### Bidirectional sales order sync

- Sales connection wizard has Advanced options: bidirectional sales-order sync and item availability (BC availability surfaced in D365 Sales when creating orders).
- Older behaviour synced only the order header, one-way BC→Dataverse. Newer release: bidirectional, more header fields, and **line** sync (adding/modifying lines on a coupled order syncs).
- Sales-order sync only applies to **released** orders — enforced by a table filter on the order mapping.

### Near-real-time wake-up from Dataverse (Power Automate flows)

- BC→Dataverse changes already woke the job queue in near-real-time; the reverse (Dataverse→BC) did not until `[sic?]` "wave 222" (verify release name).
- Mechanism: create a **cloud flow** in Power Automate triggered by Dataverse row added/modified/deleted, which notifies BC and restarts the dormant job-queue entry.
- Microsoft publishes flow templates — search templates for "notify business central": three templates (account [covers customers+vendors], contacts, currencies).
- Only config needed in the template: pick BC environment + company (one that has sync configured). If BC is in a **different Azure AD tenant** from Dataverse, add a separate connection.
- Job-queue entry sits in a **dormant / on-hold with inactivity timeout** state until a change wakes it — avoids running unconditionally every 5 min.

### Extending sync to custom entities (proxy tables)

- Extend the connection to sync a custom Dataverse table (demo: D365 Human Resources `worker` ⇄ BC `employee`).
- Generate an **integration/proxy table** in BC with the **AL Table Proxy Generator** tool ("altpgen") — hidden binary `altpgen[sic?].exe` under the AL VS Code extension's `bin` folder; run via PowerShell with an args/`.rsp` file: project path, package cache path (AL symbols), service URI (org URI), entities list, base object ID (`[sic?]` "Maze ID" = base ID — verify).
- Tool authenticates to Dataverse, pulls entity metadata; if a matching BC table exists in symbols it emits a **tableextension** with extra fields, otherwise a **new table**.
- Generated table has `TableType = CDS` and per-field/table `ExternalName` + `ExternalType` properties mapping to Dataverse metadata. Reads/writes to this table are transparently converted to Dataverse SDK calls when connection enabled.
- Add a BC list page over the proxy table. Use `CRM Integration Management` codeunit `[sic?]` — `CreateNewRecordsFromCRM` (create BC records from Dataverse), `ShowCRMEntityFromRecordID` (deep-link to the coupled Dataverse record). Verify exact codeunit/method names against compiler.
- On the base BC table add a `tableextension` with a `Coupled to CRM`/`Coupled to Dataverse` `[sic?]` boolean field — **the field name is significant**; the sync engine reads it to mark coupling status. Add it to the list page for filtering.
- Card actions to expose: deep-link to Dataverse, Synchronize Now, open Synchronization Log, Set Up Coupling (create new / couple existing), Delete Coupling.

### Extension event subscribers for custom mappings

- Subscribe (codeunit) to these integration events `[sic?]` (verify names against compiler):
  - `OnGetCDSTableNo` — return your proxy table for a given BC table, enabling it in the coupling page.
  - `OnLookupCRMTables` — open your custom list page for the Dataverse lookup; set the currently-coupled record.
  - `OnAddEntityTableMapping` — register the mapping for deep-linking.
  - `OnAfterResetConfiguration` (in "CDS Setup Defaults" `[sic?]`) — **most important**: add the integration table mapping + field mappings here; can also set a table filter on the integration/Dataverse table (e.g. only sync employee-type workers).
- Also add a recurring-job registration so coupled records sync periodically.
- After publishing, run the **Use Default Synchronization Setup** action to fire the subscribers and install the mappings.
- With just this extension you inherit all sync-engine features free: match-based coupling, auto conflict resolution for delete/update, bidirectional sync.
- Prototype VS Code extension "BC to Dataverse" was previewed — generates proxy tables/list pages and maps fields with no hand-coding (preview, unreleased at time of talk).

### Virtual tables (Dataverse virtual data provider)

- Virtual tables = proxy in Dataverse, **no data replicated**. CRUD operations proxied live to BC. Supports read/update queries and CRUD events (create/update/delete) BC→Power Platform.
- Under the hood: a **plugin** (shipped in the AppSource solution) calls BC's **OData endpoint via API pages**. The API pages are what you map onto virtual tables. Works with built-in or custom API pages.
- CRUD events pushed via BC's existing **webhook** implementation → plugin → Dataverse.
- Setup: `Enable Dataverse` checkbox in the Dataverse connection wizard (auto-discovers the environment from tenant). Requires installing the **virtual tables app** from the Power Platform app store (not auto-installed; wizard provides link). App was in preview at time of talk.
- Virtual-table schema naming convention: prefix `[sic?]` "crXXX_dyn365bc" / `dyn365bc` + API page entity name + API publisher/group/version → unique schema name. Verify prefix format.
- Dataverse requires the key to be a **GUID** — BC API Pages V2 were converted to expose `SystemId` everywhere to satisfy this.
- Dataverse **primary attribute** (shown in lookups) chosen from the API page display name, else first string attribute. Labels/translations come from BC captions on tables/fields/enums.
- Generate a virtual table: open the **Available Business Central Tables** entity in Dataverse, find the entity (IPR/route shows source extension), flip the **Visible** flag → Dataverse generates the table (~30s).
- Model-driven Power Apps **require** a native or virtual table (the connector alone won't drive a model-driven app).
- Relationships auto-generated from AL: a page **part** → one-to-many (e.g. sales order → lines); a **table relation** field → many-to-one lookup (e.g. sales order → customer). A part with new **Multiplicity** attribute set to 0/1 gives a one-to-one relation (e.g. customer → customer detail), visualisable via quick-view form.

### Native↔virtual table relationships

- To relate a **native** Dataverse table (e.g. `account`, populated by sync) to a **virtual** table (e.g. sales credit memos) — not possible via the standard maker experience.
- Steps: add a key column on the native table (e.g. account number) and create an **alternate key** on it; identify the filter attribute on the virtual table (e.g. customer number).
- Use the shipped entity **Business Central Table Relation** to create the mapping: relation name, native table, virtual table, the native alternate key, and the field mapping (account number → customer number) using **schema names** (with `dyn365bc`[sic?] prefix). Then build subgrids/apps as normal.

### Virtual-table events & C# plugins

- Because virtual tables register as BC-related, listening to a row added/modified in a Power Automate flow (Dataverse connector) auto-creates a **webhook subscription** on the BC side.
- Events only carry the record **ID** — add a `Get row by ID` step to fetch the full record.
- Advanced: **VS Code Power Platform extension** ("Power Platform Tools"[sic?]) → Power Platform Solution / plugin project template → sign into Dataverse. The **Dataverse Explorer** event catalog has a dedicated Business Central section (only present once virtual tables generated) listing per-table CRUD events.
- Subscribing to an event auto-generates the plugin step registration + code stub. In-plugin: get the `EntityReference` from input params, `Retrieve` full entity via the org service, query related native records, create tasks, etc.
- Plugin assembly must be **signed** (signing key + password) before build/deploy. Deploy registers the webhook subscription on BC automatically.

<!-- ingested: BC TechDays 2023 - Connecting to Dataverse: do's, don'ts, an | 2026-07-27 -->
### dataverse-connectivity-auth (BC TechDays 2023, Rickmans/Matt)

- Dataverse = managed data platform behind Power Platform. Not just relational DB: routes fields to SQL pool (relational), blob storage (file/image fields), Cosmos DB (nosql/logs), and OneLake/Fabric data lake — transparently. File/image fields land in blob storage at fraction of relational cost; developer sees single field, no manual routing.
- Auth model = OpenID Connect (authentication: who are you) + OAuth2 (authorization: what allowed). Azure AD is identity brain; there is always an app + service principal behind any access.

**App registration types**
- Single-tenant: only accounts in home tenant can authenticate. Default; use for internal apps.
- Multi-tenant: any tenant (and optionally personal MS accounts) can sign in. Developer is responsible for validating allowed tenant IDs in code — failing this caused a real Bing app leak (Feb 2023). Secure-by-default only if configured right.
- App registration = the class/definition (shows in App registrations). Service principal = the instance (shows in Enterprise applications). Single-tenant: both live in home tenant. Multi-tenant: consuming tenant gets only a service principal in Enterprise applications, no app registration.

**Delegated vs application permissions**
- Delegated: app acts on behalf of signed-in user; app never gets MORE than the user has. Consent popup grants Scopes. Used by power automate/canvas flows.
- Application (app-only): runs with no user present (Azure Functions, run books, services). Granted by global admin; grants broad Scopes (often full read/write). For Dataverse, additionally requires creating an **application user** in the Dataverse environment mapped to the app registration + assigning security role(s).

**Credential ranking (best→worst)**
1. Managed identity — service principal with secret auto-rotated by Microsoft; no secret management; no license; higher API limits. Recommended.
2. Service principal / application user — client ID + secret; you manage secret lifetime (default 180d, max 2yr, then re-auth everywhere); higher API limits; no license needed.
3. Service account — named account for automation. Bad: needs license, hit by MFA/conditional-access token invalidation (silently kills long-running power automate flows), lower API limits.
4. Named user — worst.
- Connector caveat: most Power Platform connectors only support username/password. Only the Dataverse connector and Azure Key Vault connector (a few others) support application/service-principal auth.

**Security roles** = Dataverse permission sets (analogous to BC permission sets). Assign least-privilege; avoid `System Administrator` role. CRUD + special scopes; "organization" scope = all business units. Business unit ≈ company-ish grouping.

**BC → Dataverse integration options**
- Data synchronization: copies BC data into real Dataverse tables; access = normal Dataverse permissions (user needs no BC access).
- Virtual tables: Dataverse surfaces BC data live via API; uses delegated permissions — caller's credentials passed to BC, so caller MUST have BC access. Follows BC business logic; writes flow back to BC.
- BC APIs directly: user/service principal needs BC permission set.

**Dataverse coding — endpoints/SDKs**
- Use **Web API** (`/api/data/v9.2`, OData V4) for direct/JS access. AVOID: Organization Data Service (OData V2) — deprecated (removal date pushed 5×). AVOID SOAP endpoints directly.
- `CrmServiceClient` [sic? verify name] = old .NET Framework SDK (~4.6.2/4.7), SOAP-based, still required inside the Dataverse plugin sandbox.
- `ServiceClient` [sic? verify] = new SDK for .NET Core / .NET 6+, cross-platform, where new dev happens. Both confusingly called "organization service". Internally mixes SOAP + Web API today; Microsoft goal is transparent move to Web API only.
- Late-bound code: `new Entity("...")`, string field names, runtime validation only, no intellisense.
- Early-bound code: generate typed classes per environment; compile-time validation + intellisense. Risk: schema changes in Dataverse don't break compile (stale classes) → runtime failures; must regenerate after schema changes.
- Class gen tools: `CrmSvcUtil.exe`, XrmToolBox Early Bound Generator (V2), or `pac modelbuilder` (Power Platform CLI). XrmToolBox = open-source plugin-based tool, hundreds of plugins (e.g. FetchXML Builder to prototype queries and see result set before coding).

**BC API SDK generation trick** (no official BC SDK exists — otherwise hand-build HttpClient calls)
- BC OData V4 exposes `$metadata` endpoint (EDMX). Convert EDMX → OpenAPI/Swagger via OpenAPI.NET.OData [sic? verify package], then feed Swagger to **Kiota** (Microsoft; `kiota generate`, multi-language: C#/TS/JS) to generate a fluent-API SDK with request builders per endpoint. Gives intellisense over unfamiliar BC APIs; regenerate to add custom API endpoints.

**Azure.Identity** library (built on MSAL) handles token/refresh-token lifecycle for you — works for BOTH Dataverse and BC (both Azure AD). Supports client-secret credential and `DeviceCodeCredential` (browser device login at microsoft.com/devicelogin). Prefer over hand-rolling calls to login.microsoftonline.com and managing tokens yourself.

**Static-site pattern (secure external data exposure)**
- Instead of live public endpoint to ERP: Azure Function authenticates to Dataverse (application user, read-only role) → static site generator (e.g. Hugo `getJSON` calls the Function) → generated HTML/JS hosted cheaply (Azure Blob/Static Web Apps, Netlify). Rebuild triggered by power automate on data-change event or on schedule (e.g. hourly). External users never touch Dataverse; cached, fast, read-only = minimal attack surface.
- Azure Function auth: `ServiceClient` with connection string carrying app ID + secret works but is NOT best — never store secret in Function app settings; use Key Vault, or better enable Function **managed identity** (Identity → On), register that identity's app ID as a Dataverse application user with security roles. No secret anywhere; only Function code can act as that identity. Store just the environment URL.

**Naming trivia (for Learn searches):** Dataverse was Dynamics CRM → Common Data Service → (briefly DataFlex, dropped over trademark) → Dataverse. API permission still listed under "Dynamics CRM" / "Common Data Service" in Azure AD API permissions (`user_impersonation`). Forms Pro is now "Customer Voice".

**IDs:** use app ID (client ID) in code/UI searches, not object ID. Object ID = internal AAD id (search fallback when app ID not yet propagated).

**Licensing:** BC seeded Power Platform license only covers use in BC context; building own portals / storing data in Dataverse requires separate Dataverse/Power Apps license (starts ~€4/user/mo). BC seeded license gives no Dataverse storage. Verify against MS licensing guide.

<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# API pages, integration patterns, event grid master-data sync

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 6. Developer APIs — permissions, approvals, documents (28.x, API v2)

Read-only/automation families for internal-controls reporting (Copilot Studio / Power BI) **without UI
access**. Docs aka.ms/bcintegration. *(APIs for permissions, approvals, and documents)*

- **Document APIs (~36, PDF/GET):** all Sales types (quote/order/invoice/credit memo/blanket/return +
  archived), Purchase (same incl. archived blanket), Inventory (orders … posted direct transfer),
  Assembly (assembly orders + posted). Extends beyond the previous five.
- **Permission APIs (5, read-only):** `permissionSets`, `expandedPermissionSets` (adds app/expanded-
  permissions + app name), `securityGroups`, `userPermissions`, `accessControl`.
- **Approval/workflow APIs (7, read-only):** `workflows` → `workflowSteps` → `workflowStepResponseOptions`;
  `workflowApprovers`, `approvalUserSetup`, `approvalEntries`, `postedApprovalEntries`.

---

<!-- ingested: Integration Without Aggravation: Best Practices for Business | 2026-07-26 -->

<!-- ingested: BC TechDays 2023 - API best practices | 2026-07-26 -->
### API page best practices (mibuso TechDays 2023 — Alan/Arend-Jan Kauffmann [sic? "Alan Young Kaufman" from captions — verify; NL technical consultant/MVP])

**Creating API pages with AL Dev Tools wizard**
- Use the "New AL file wizard" (AZ AL Dev Tools ext) → add page → switch page type from `Card` to `API`; auto-fills `APIPublisher`, `APIGroup`, `APIVersion` from ext settings.
- Turn off field captions for API pages — captions belong on table fields; only needed if a field is a global variable, or if the API surfaces in a UI (PowerApps, custom web app, needing multi-language).
- `ApplicationArea` not required on API pages — omit it.
- Name-conversion rules map table field names to API conventions: `No.` → `number` (trailing capital N → `number`), `Line No.` → `sequence`, `SystemId` → `id`, `SystemModifiedAt` → `lastModifiedDateTime`. Rules are configurable (e.g. `Description` → `displayName`).
- Always expose `SystemModifiedAt` as `lastModifiedDateTime` — a best practice.
- Add `ODataKeyFields = SystemId` — wizard does NOT add it; you must add manually.
- Wizard can't reorder fields — pick them in final order (id/system fields conventionally go at top).

**Page trigger execution order per HTTP verb** (verified by live tracing; order matters for perf)
- Always run: `OnInit`, `OnOpenPage`. Never run: `OnQueryClosePage`, `OnClosePage` (no user closes an API page).
- `OnInit` can't read URL filters; `OnOpenPage` CAN read them — including the SystemId filter (URL bracket value `(guid)` maps onto the ODataKeyFields field as a page filter).
- GET: OnInit → OnOpenPage → OnFindRecord → OnAfterGetRecord → OnAfterGetCurrRecord → OnNextRecord.
- POST: OnInit → OnOpenPage → OnNewRecord → OnValidate (per field IN THE REQUEST BODY only, executed in the order fields appear on the PAGE not the request) → OnInsertRecord.
- PATCH: OnOpenPage → OnFindRecord → OnAfterGetRecord → OnAfterGetCurrRecord → OnNextRecord → OnAfterGetRecord + OnAfterGetCurrRecord AGAIN → OnValidate (only for fields whose value actually CHANGED — unchanged fields in the body are not validated, and you cannot force validation without changing the value) → OnModifyRecord → OnAfterGetRecord + OnAfterGetCurrRecord a THIRD time.
- DELETE: OnOpenPage → OnFindRecord → get-record triggers → OnDeleteRecord (record gone after, no further get).
- **Gotcha:** `OnAfterGetRecord`/`OnAfterGetCurrRecord` run 2× on PATCH-adjacent flows and 3× on PATCH. Keep heavy code out of `OnAfterGetRecord`; if unavoidable, guard with a counter so it runs once.

**POST silently turning into PATCH/MODIFY (surprising behaviour, ~28.x era)**
- On POST, `OnValidate` fires before insert; `OnNewRecord` still runs. But if the record still has NO field value set by the time insert would fire, the platform runs `OnModifyRecord` instead of `OnInsertRecord` and returns nothing.
- Setting a field value (e.g. assigning `Rec.Name`) in `OnValidate` makes at least one field non-empty, so `OnInsertRecord` fires normally.
- If you explicitly `Rec.Insert` from code inside `OnValidate` (delayed insert is on for API pages), the later platform insert does NOT error "already exists" — it converts to a modify; still returns `201 Created`. Speaker's use case: an external system that could only do GET/POST (no PATCH) — POST-as-upsert let them create-or-update.

**Temporary-table-backed APIs**
- MS docs warn: paging is not performant on temp tables (rule of thumb: >100 records → avoid temp tables). Server-driven paging must load the FULL set into the temp table before top/skip.
- Workaround: force filters in code (reject requests lacking a required filter) and populate the temp table via a query in `OnOpenPage`. Read URL filters with `GetFilter`, validate them (e.g. require a 7-char period filter), then load a reduced set — lets you sidestep the 100-record guidance.

**Bound actions**
- Define as a `procedure` with `[ServiceEnabled]` on the API page; runs against the current record (URL bracket key).
- **Must be called in camelCase** — even if defined with leading capital, invoke with lowercase first letter (`microsoft.nav.setDescription`). Cost the speaker half a day.
- Two return styles, mutually exclusive:
  - Location header: take a `WebServiceActionContext` [sic? verify object name] param BY VAR; call `SetObjectType`(Page), `SetObjectId`(api page), `AddEntityKey`(SystemId field, value), `SetResultCode`(Created) → response carries a `location` header pointing to the created/updated record; returns 201/202/204.
  - Return a value: give the procedure a normal return value (e.g. compute a price via a temp SalesHeader/SalesLine) — caller gets the raw value. Adding a WebServiceActionContext param alongside a return value makes the platform use the context and ignore the return — can't do both.

**Versioning two options**
- MS way: put all APIs in a separate app; new version = new app + bump `APIVersion` on every file.
- Alternative: expose one API in multiple versions — copy only the changed API page, set the new one to e.g. `v1.1`, leave others at `v1.0`. Callers hitting v1.1 only get the changed entity; unchanged entities stay v1.0. Only copy modified APIs, not the whole app.

**Automatic (implicit) relationships between API pages**
- If a field has a table relation to another table that ALSO has an API page, the platform auto-creates the OData navigation — `$expand` works with NO `part`/subpage defined.
- Current BC: it matches the related API by the field's relation target (e.g. `Item Category Id` → the item-category API keyed on SystemId). Older BC matched on the FIRST relating field in the page order, so putting a code field before the id field could break the link — order-sensitive historically.
- Explicit `part` relationships: point a part at another page (API page, or even a plain list part). For a plain page supply entity name/set; for an API page you can omit them. Use `SubPageLink`. `Multiplicity = ZeroOrOne` [sic? verify property] gives a one-to-one so `$expand` returns a single object, not an array.

**Partial records / performance**
- API pages auto-enable partial records (implicit `SetLoadFields` for repeater fields).
- Any code accessing fields NOT in the repeater triggers a just-in-time load per record. Avoid by calling `Rec.AddLoadFields(...)` for those fields in `OnOpenPage`.

**Reducing payload (OData query options)**
- `$select` limits returned fields; works inside `$expand` too.
- Paging: use server-driven paging via the request header `Prefer: odata.maxpagesize=N` (returns `@odata.nextLink`), NOT `$top`/`$skip`. Must resend the `Prefer` header on each nextLink call.
- Navigate to a single property: `.../items(id)/inventory` returns the field; append `/$value` to get the raw value with no JSON wrapper.
- Control OData metadata via `Accept` header: `odata.metadata=full` adds editLink, type info, association links (useful for proxy generators); `odata.metadata=none` strips all `@odata.*` for clean JSON.

**Web service throughput limits / monitoring**
- Incoming web-service queue: max ~100 queued requests, only ~5 processed concurrently; rest wait, and can time out in queue. Long-running Power BI queries against BC consume the same concurrency slots and starve API callers (e.g. warehouse scanners) — no platform fix; offload heavy Power BI reporting to Azure Data Lake / synapse-style store instead of querying BC live.
- Use MS-provided telemetry Power BI to find queued/timed-out calls, non-2xx responses, aggressive callers, time-of-day patterns. From ~22.2, telemetry records API requests that timed out while queued.
- Prefer APIs over OData/SOAP on UI pages.

**Batch / transactions**
- Each API request is its own transaction. For multi-request atomicity (all-or-nothing across several writes) use OData `$batch` with change-set isolation.

**Testing APIs with Postman**
- Pre-request and test scripts (Node.js): set variables before, assert response status/body/JSON schema after with `pm.expect`/`pm.response`. Built-in tiny-validator (`tv4`) validates response against a JSON schema (generate schema from a sample response via an online generator).
- Chain requests in a collection: save response values (`pm.collectionVariables`/`pm.environment.set`) to feed later requests (create customer → item → sales order). Collection runner supports performance runs (virtual users × duration) to load-test from outside — combine with telemetry.

**Debugging web-service / API calls**
- Yes, API/web-service calls are debuggable: `launch.json` request `attach`, `breakOnNext: WebServiceClient`, attach to the (cloud sandbox) environment, then fire the request — breakpoint hits.
- Production debug (snapshot/attach) for web services — speaker couldn't get it working; unverified.

**Consuming BC APIs from C#**
- Auth via `Microsoft.Identity.Client` (MSAL) NuGet — don't hand-roll token HTTP. `PublicClientApplicationBuilder` for interactive/public (no secret); `ConfidentialClientApplicationBuilder` `.WithClientSecret(...)` for confidential. Pattern: `GetAccountsAsync` → `AcquireTokenSilent` (uses refresh token) → fall back to `AcquireTokenInteractive` on `MsalUiRequiredException`.
- Service-to-service (client credentials): `confidentialApp.AcquireTokenForClient(scopes)` — must set the authority with the specific tenant id or no token is returned.
- JSON mapping: `System.Text.Json` with `[JsonPropertyName]` on DTO props (partial DTO is fine — only map fields you need). Collection responses wrap the array in a `value` property — model as a type with a `Value` array.
- `HttpClient.GetFromJsonAsync<T>()`, `PostAsJsonAsync(obj)`, read created record via `response.Content.ReadFromJsonAsync<T>()` — no manual JSON handling.

**Auth: secrets vs certificates**
- Client secrets expire and per MS docs are dev-only — avoid in production; you only learn of expiry from an Azure error, too late. Mitigation if forced: two secrets with staggered expiry, fall back to the second.
- Production recommendation: certificate credentials. Self-signed cert is fine (10–30 yr expiry). Private key stays in BC; upload only the public key to the Azure app registration. AL can generate the cert, create the app registration, upload the public key and grant permissions — so end users click one action in BC instead of touching the Azure portal ("quite some code" but works).

**Bound vs unbound actions** — prefer bound; genuine unbound-action use cases (processes truly unrelated to any record) are rare — most "process" actions can be modelled as bound actions on a record.

### Integration patterns — job queue, external business events & web hooks (mibuso TechDays — Vlad & Ranga, Theta NZ)

**Five pieces of any BC integration:** setup, trigger, mapping, request, response.

**Setup**
- Prefer Assisted Setup (guided wizard, inline validation) over a bare setup table so users can't miss/mis-enter connection + auth details.
- Register external endpoints in the **Service Connections** page (centralised) instead of scattering per-module setup pages users must memorise.

**Trigger (biggest partner mistake)**
- Do NOT call an external service while a business transaction is still open / tables locked (MS cited as ~95% of integration bugs). Two systems can't share one transaction scope — a failed rollback leaves the systems out of sync.
- Fix: never call out from inside a posting routine (e.g. subscribing to OnPost of warehouse shipment and calling the carrier synchronously). Instead **schedule a job queue entry** to do the outbound call. The job-queue entry is written inside the business transaction, so it rolls back with it — no request goes out unless the transaction commits. Bonus: automatic retries, scheduling, queueing.

**Mapping**
- BC supports JSON and XML; use the newer typed JSON wrapper API (access properties directly with types, iterate properties) rather than reading JSON as text and hand-parsing. [sic? exact object name — likely `JsonObject`/`JsonToken`; verify]
- **Data Exchange Definition** lets power users edit the payload without code changes, but it can't do full complex XML exports — you end up writing code anyway. Presenters' strong advice: hardcode mapping in AL unless a customer genuinely needs to self-edit the schema (rare in practice).
- Wrap the whole external-service client in an **interface** for versioning: when a partner changes fields, create a new interface implementation (copy code OK) rather than mutating the existing integration — allows switching back/forth for testing without breaking the current contract. Interface at the client level, not per-mapping. Pass a generic `Record` parameter so future field additions don't change the interface signature.

**Request**
- BC offers ~4 instrumentation options to call external services; a plain REST call can be one line (less code = fewer errors). Pick the lightest tool that covers the case.

**Limitations of the AL-only / job-queue outbound approach**
- Poor observability: no built-in request/response logging. Once the job queue runs it's gone; only diagnostic is external-call telemetry (endpoint + timing only, no request/response body). Any monitoring must be built from scratch.
- Poor scalability of *reach*: an AL job-queue integration typically does one thing → one service. Organisations soon want fan-out (email someone, trigger another process) which AL-only doesn't give cheaply.
- AL still limited for very old/legacy formats & instrumentation.

<!-- ingested: Creating Power Automate flows for Business Central that actu | 2026-07-26 -->

<!-- ingested: NAV TechDays 2019 - Unlocking new integration potential for | 2026-07-26 -->
### Master-data sync via Azure Event Grid + BC Admin API (NAV TechDays 2019 — Dmitry [sic? MVP, St Petersburg] & Chandrasekhar [sic? MVP, Auckland/Theta NZ])

**Admin API (Automation of environment mgmt)**
- BC admin API bumped to **v2** early Nov (of talk era); URL shape `.../admin/v2.0/applications/businesscentral/environments` [sic? verify path on Learn].
- Auth: needs OAuth token. MS ships a .NET helper lib to fetch it, but from AL (no .NET) call the token endpoint directly via HttpClient. Talk used **password grant** (username+password+client_id+resource); secret/key grant also possible.
- App registration in Azure AD: create app → get Application (client) ID → set client type **public** + redirect URI → grant BC API permission (read or read/write). Write access needed to create/delete environments.
- Token short-lived (~3–5 min); refetch per call.
- Environment ops: `GET .../environments` list; **PUT** (not POST) to create — body JSON with country/localization, ring/version, environment type (Production|Sandbox); if no version specified, latest applied. `DELETE .../environments/{name}` to remove. Create/delete async (status `preparing`/`removing`).
- **Automation APIs** (separate set) manage companies, extensions, publish config packages.

**Event Grid as middle-tier broker for BC→N-system sync**
- BC has no native Event Grid connector — publish via **custom topic** using plain HTTPS POST from AL (HttpClient): content-type `application/json`, header carries topic access key, POST to topic endpoint URL.
- Event Grid message required header fields: **topic**, **subject**, **eventType**, **eventTime**, **id**; **data** body author-defined (send only changed/needed fields, not whole record).
- topic/subject are your own grouping scheme (e.g. topic=BusinessCentral, subject=Customer). eventType = create/modify/delete.
- Prefer **one topic + subjects** over many topics; billing is per-message not per-topic. Pricing: first 500k ops free, then ~$0.60 per 1M ops.
- **Message size cap: 64 KB** at GA (was 1 MB in preview). For larger payloads use **claim-check pattern**: Azure Function stores full payload in Blob storage, Event Grid carries a small reference (tenant/id/token); consumer fetches blob by token.
- **Delivery/retry**: Event Grid retries a down endpoint up to **24h** (configurable back-off intervals, e.g. 5 min); after 24h routes to **dead-letter** (blob) for manual replay. It's push-only — consumers cannot pull from Event Grid on demand.
- Design: keep events self-contained (one event = full context, no cross-event dependencies). Consumers = Logic Apps filtering on subject/eventType/language, then POST into target BC via its **published API** (standard or custom API on subsidiary) — so target company needs no Event Grid code, just an API.

**BC-side implementation pattern shown**
- Reused **Data Exchange Definition** to select/export which fields go into the JSON payload — add a field = config a new mapping line (incl. fields from other extensions), no redeploy. Import side can also use data-exchange defs with optional-field handling so a custom field absent on target is ignored.
- **Message version** field (e.g. 1.0/2.0) tags payload so consumer logic only processes matching versions → avoids breaking existing consumers when schema grows.
- Automate publishing by extending BC **Workflows**: workflow event on record create/modify/delete (with field-level filters, e.g. only when Name changed) → run data-exchange export → raise integration event → POST to Event Grid. Avoids hand-coding OnModify subscribers per table.
- JSON built with AL JsonObject; buffer table collects fields → JSON array.
- Note: sync in demo was one-way (master→subsidiary); a delete in master **recreates** the record in subsidiary if missing (upsert semantics).
- Translation of field values (e.g. localized COA names) done in the Logic App via Cognitive Services Translator; translator takes single values not JSON, so payload fields concatenated with pipe delimiter then split on response. Language code (e.g. `ru`) looked up from translator languages API.

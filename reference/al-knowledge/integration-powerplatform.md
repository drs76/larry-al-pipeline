<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Power Automate, Power Platform ALM, web hooks

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 6. Developer APIs — permissions, approvals, documents (28.x, API v2)

### Power Automate flows for BC (mibuso — AJ Ariyaratnam [sic? "AJ andari" from captions — verify; DSWi COO/MVP])
- Flow types: **automated cloud flow** (fires on trigger event), **instant cloud flow** (on-demand button, incl. mobile Power Automate app / manual trigger with user inputs), **scheduled cloud flow** (recurrence, e.g. weekly Monday 10:01).
- BC connector licensing: BC connector + standard M365 connectors (email etc.) included with M365 licenses at no extra cost for BC SaaS. **BC on-prem needs separate Power Automate licensing** (not free).
- ~500 connectors available; ~200+ standard. Can also call any custom API endpoint.

**API pages, not web services**
- Power Automate / Power Apps require **API pages**, not the classic web-service (SOAP/OData-page-export) endpoints used for Power BI.
- Microsoft ships ~40-44 standard API endpoints (v2.0). Custom/extended tables need own API page.
- Fast scaffold: VS Code **AL Language** + "AL development tools" ext → right-click → **New AL file wizard** → Page wizard → set page type API → fill APIPublisher / APIGroup / APIVersion / EntityName / EntitySetName → pick fields. Generates full API page in seconds.
- GUI alternatives (no AL): appsource apps **Simple Object Designer** (Eric Hougaard [sic? "Eric hugard"]) and **DataBraider** (Spare Brained Ideas) create/expose API pages from BC UI; one can export the page into an extension.

**Gotcha: ODataKeyFields / SystemId**
- Wizard-generated API pages omit an important property. Manually add a **SystemId** field to the repeater (`field(systemId; Rec.SystemId)`) and set page property **ODataKeyFields = SystemId**.
- SystemId (guid) is the immutable key the connector's **Row ID** parameter expects — not the natural primary key (e.g. customer No.). Without it, Row-ID-based Get record can't resolve records.

**Connector actions gotchas**
- **Get record vs Find record**: `Get record` requires the Row ID = SystemId guid, which you usually don't have. Users repeatedly fail feeding the natural key (No.) into Row ID → error. Use **Find record / Find one record** instead: set **filter** (Advanced params → Show all), e.g. `number eq '<value>'`, to look up by natural key.
- **Trigger doesn't expose record fields**: an on-create trigger ("when a record is created") only carries the Row ID, not field values. Must add a **Get record** step first before dynamic field values appear in later nodes.
- **Company not resolved**: BC connector returns company **id (guid)**, not name. To show friendly company name, call the **automation API `companies`** (automation/company set) and use its `displayName`, mapping by Body Company Id.
- **New designer is unreliable** — some connector/action properties (dynamic dropdown of table fields) don't populate. Switch to **classic/old designer** when field dropdowns fail.
- **Standard MS API bug**: field captions differ from BC (No.→ number, Name→ displayName). Known data bug: customer **`balanceDue`** field returned wrong/duplicate value (returned Balance not Balance Due) — verify against Microsoft Learn/compiler. Recommendation: **build your own API endpoints per project** rather than trust standard ones; multiple purpose-specific API pages over the same table is fine.

**Permissions & multi-company**
- BC connector **respects BC permissions** — runs as the calling Entra ID user; can't read/write fields the user can't in BC UI. (Mirroring data elsewhere bypasses this.)
- Company is a **mandatory** connector parameter and tables are per-company → no clean single-flow solution for many companies; workaround is pushing data to Dataverse (company-agnostic) and sourcing from there.

**On-prem setup**
- Expose **OData v4** endpoint: open/port-map the OData port (default 7048), FQDN or A-record, and a **trusted CA TLS cert** (Let's Encrypt or commercial). **Self-signed certs do not work** for any Power Platform / Power BI web service.
- Some v3 connector actions unavailable on-prem (only v2/preview/beta). Entra ID SSO simplifies on-prem auth.

**Calling API page actions**
- Custom API pages can expose **bound actions/methods** (AL procedures); flow triggers the action (e.g. email all open invoices for a customer) via one manual button + customer-No input.

**Limits / misc**
- BC API connector rate limit ~**100 connections/minute** (per presenter's recollection; verify current throttle limits).
- Flows live in a **Power Platform environment tied to a user account**, independent of BC environments; deleting a BC company/environment does not delete flows. Deleting the M365 user account deletes their user-owned flows. Put production flows in a shared/default environment, not personal.
- Cross-tenant deployment/versioning of flow solutions is fragile — export/import between tenants often needs parameter fixups; same-tenant copy is fine.
- Templates library + Microsoft "Power Automate in a Day" free instructor-led courses. Co-pilot Studio (formerly Power Virtual Agents) chatbots can call Power Automate → BC; building the chat experience needs a Copilot Studio license (dev/trial plan to experiment).

<!-- ingested: BC TechDays 2022 - ALM Accelerator for Power Platform [CoE S | 2026-07-26 -->
### ALM for Power Platform + BC integration (mibuso TechDays 2022 — Michael Megel [sic? "Michael Miguel/amigo" from captions, Cosmo Consult — verify], ALM Accelerator for Power Platform)
- Power Platform apps (canvas apps, Power Automate flows) need same ALM discipline as AL apps: source control, 3 environments (dev/test/prod), automated deploy.
- **Dataverse solution** = Power Platform equivalent of an AL app: a wrapper (publisher, prefix, unique name, version) around components (canvas apps, flows, environment variables, connection references, permission/security roles, dataverse tables).
  - Managed solution = sealed, install-only, cannot re-export — use for transport to test/prod. Unmanaged = editable, for dev.
  - Solutions have NO dependency mechanism like AL apps; all referenced components must already exist in the target environment.
  - Bundling flow+app in one solution preserves the inter-dependency across transport (vs manual export/import which breaks it).
- **BC connector in flows** binds to fixed environment name + company name (+ API + entity). Hardcoding these blocks transport across environments.
  - Fix: **environment variables** (key/value pairs, e.g. type Text) make solutions configurable per target; reference them via connector's Add Dynamic Content. Only works when connector lives inside a solution.
  - Exclude the current (dev) values from the exported solution so target env supplies its own.
  - **Connection references** abstract the concrete BC connection; must be reconfigured in each target env at import.
- **GOTCHA — custom connectors don't support environment variables** (as of talk). A canvas app using the BC custom connector stays bound to the *original* (dev) environment even after transport — writes silently land in the wrong BC environment. Fix planned for 2023 wave 1.
  - Workaround: use **BC virtual tables** (dataverse-surfaced physical BC tables) as the data source instead of the custom connector — these respect environment config. Flows can still use environment variables normally.
- **Virtual tables (BC↔Dataverse) constraints** (from Q&A):
  - One dataverse environment's virtual tables point to a single BC company only.
  - Require matching base currency to set up.
- Flow deploy needs an activation user / proper owner set in target env; with many flows you must specify activation order.
- ALM Accelerator for Power Platform: open-source, part of CoE (Center of Excellence) Starter Kit, built by Microsoft PowerCAT team; installed via CoE CLI (`coe` [sic? "soe/Siri CLI" from captions]). Automates export-solution-to-git, validation pipeline (PR→managed solution imported to validation env), and deploy pipelines. **Azure DevOps only** at time of talk — no GitHub support.
- Branching model mirrors environments: main branch↔production, solution branch↔test, developer branch↔dev; each solution lives in its own repo folder with its own pipelines triggered by changes to that folder.

### Web hooks / external business events (BC platform)

**Web hook v1 (API-page based) — do NOT use**
- Every API page you create auto-registers a web-hook subscription capability for all record events (insert/modify/delete) on that page — often without the developer realising.
- On every global insert/modify/delete the platform reads the subscription table checking for interested parties → heavy **global-trigger performance overhead** on tenants with many API pages.
- Only record events can be surfaced; subscriptions **expire every 3 days** and must be renewed.
- Cannot use system tables for the APIs; API pages built as **query objects** don't trigger. Workaround to suppress registration: make the OData/API key a composite key so the page isn't registered.
- Payload was only the record's primary key.

**External business events (v2) — recommended, still Preview at talk**
- Not tied to API pages; partners can raise a business event **anywhere in business logic**. Handled at platform level, so no per-record global-trigger overhead — event fires only when its procedure is called.
- Fires only if the transaction **commits** (built-in async, like the job-queue pattern) — devs don't have to enforce commit discipline manually.
- Payload can carry more than just the PK (define parameters on the event), though presenters still recommend the callback pattern: payload carries system ID + company ID, external side calls back the BC API (`$get` by system ID as rowId) to fetch full record.
- Why still Preview: MS lacks a clean way to **deprecate/duplicate** an event without breaking integration contracts; they ship only a small set of stable MS events to avoid breaking changes before GA ("within the year" at talk). Partners CAN add their own business events now.

**Authoring a custom business event (AL)**
- Extend an event-category enum to add your own category (app-level).
- Define the event as a procedure with business-event metadata: event name (exact string subscribers use), display name, description, category, and a **required-permission** declaration. [sic? attribute name — likely `[ExternalBusinessEvent(...)]`; verify against compiler/Learn]
- Collect all business events into a dedicated codeunit; call them like any procedure from anywhere in the transaction.

**Setup / permissions (MS Learn overstates this)**
- The long enablement article on Learn is NOT required; no Dataverse connection needed — works standalone in BC. (Presenters got MS to agree docs need updating.)
- Subscriber (named user or service account) needs: **External Event Subscriber** permission set, plus **read** access to the external business event definition table. That's all.
- Required-permission check happens at **subscription time**: BC verifies the subscribing user has the declared permission before it will deliver any data — the security gate for what the external service can see.

**API surface (API v2 / runtime)**
- Discovery: `GET .../api/v2.0/$metadata` shows two endpoints — `externalEventSubscription` and `externalBusinessEventDefinitions`. [sic? exact entity set names — verify]
- `GET .../api/microsoft/runtime/1.0/externalBusinessEventDefinitions` [sic? path/version] lists ALL events (MS + partner) with appId, event name, **event version**, payload shape, display name, description, category, publisher, app version.
- Create subscription: POST to the subscription endpoint with company name/ID (omit company to subscribe to all companies), event name, appId, notificationUrl, clientState (token echoed to the receiver for validation).
- **Gotcha:** missing `eventVersion` in the subscription payload returns a misleading *permission* error, not a validation error. Get the version from the event definition.
- Unsubscribe: DELETE `.../externalEventSubscription(<id>)` with `If-Match: <etag>` header AND a body of an **empty JSON object `{}`** (omitting body errors). Returns 204. Get the subscription ID from the create response or the list endpoint; etag from the list.
- Notifications are **batched**: multiple events in a short window arrive as an **array** in one callback POST — receiver must loop. (Power Automate BC connector shows N separate runs; raw HTTP/web-hook connector shows 1 run with N-element body.)
- `clientState` is NOT included on delivered event notifications. To attach per-subscription metadata, encode it in the notification URL query string.

**Delivery / retry semantics**
- Fire-and-forget, decoupled: BC only cares that the receiver returns **200** (ack = "received", not "processed"). Non-200 → BC retries (observed up to ~19 retries; no config/setup to change retry count). BC never learns whether the downstream actually succeeded — error handling is the receiver's responsibility.
- BC cannot *consume* external web hooks (its APIs all require auth; notification endpoints are auth-free by nature). Use a middle layer that subscribes to the external web hook and calls the BC API.

**Monitoring (business events)**
- In-product pages: **Business Event Subscriptions** (current subscriptions, incl. creating user), **Business Event Notifications** (timestamps, retry counter, platform execution info), **Business Event Log** (subscribe/unsubscribe/notification history). No execution codeunit is visible — dispatch is all platform-side.

**Power Automate / integration-layer notes**
- BC standard connector for business events: **no service-to-service auth** — requires a named user (there's a MS backlog idea to add S2S; vote for it). Also breaks/goes "out of shape" when you try to parameterise connector bodies with environment variables → hard to ship as a solution.
- Workaround: use the generic **HTTP + Web Hook** trigger connector instead. It supports managed OAuth/S2S auth (register an app), lets you define subscribe endpoint + body, auto-generates the callback URL per enable, and define an unsubscribe endpoint that extracts the subscription ID from the subscribe response (again DELETE with empty body). No mapping-shape issues.
- Company selector became available on the PA trigger only recently (mid-preview) — evidence the feature is still moving.
- Many teams moving integration from Power Platform to **Azure Integration Services (Logic Apps)** mainly for **security** (strong IP filtering not possible in low-code/serverless), and for full telemetry/monitoring control (Logic Apps can push to App Insights; Power Automate can't correlate).
- Business events are stated as **production-ready and scalable** despite Preview label — presenters ran them at large scale successfully.

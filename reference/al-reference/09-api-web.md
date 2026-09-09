<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# API pages / web services, interfaces, permission sets

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 23. API Pages / Web Services (BCQuality: web-services)

- **Address API records by `SystemId`, not a renamable business key** — business keys change; SystemId is stable.
- **Version by adding a new `APIVersion`, never by mutating a published one** — mutating breaks live integrations.
- **Read only committed data** from APIs that must not expose in-flight writes (`ReadIsolation`).
- **Expose business operations as bound actions, not writable status flags** — a writable `Status` field lets callers set invalid states directly.
- **Lock down write operations on read-only API pages** (`Editable = false` / `InsertAllowed`/`ModifyAllowed`/`DeleteAllowed = false`).
- **Declare every required property** on a `PageType = API` page (`APIPublisher`, `APIGroup`, `APIVersion`, `EntityName`, `EntitySetName`, `DelayedInsert`).

<!-- ingested: Extending Dynamics 365 Business Central with Virtual Tables | 2026-07-26 -->
### Dataverse integration, virtual tables & business events (mibuso BC TechDays 2024-06)

**Four ways to integrate BC with Dataverse:** data sync (batch-job replication), data events, virtual tables, business events. Config hub for all of them: **Dataverse Connection Setup** page. Connection is per-company; one Dataverse environment per company.

**Data Sync**
- Bidirectional replication via job-queue batch jobs; data physically stored in *both* BC and Dataverse.
- Standard `Customer` and `Vendor` both map into the single Dataverse `account` table.
- Central config = **Integration Table Mapping** (table-level rules) + field mapping. Can run full sync or modified-only; per-field enable/disable; per-mapping direction control (send-only vs bidirectional).
- **Coupling / uncoupling** = matching a BC record to a Dataverse record on defined criteria.
- Ownership model: choose **Team** (recommended, uses Dataverse business units) vs Person (must map each salesperson to a user).
- **Manual creation of table mapping + field mapping in the client is new in BC24** — older versions must define mappings in AL code. Gotcha: migrating C/AL→AL and moving fields into the 50000 range breaks existing mappings on pre-BC24; must re-map in code.
- Extending data sync to custom tables requires an **integration table** = an AL table that mirrors the Dataverse entity's schema. Don't hand-write it — generate with **AL Table Proxy Generator** (`.exe` shipped inside the AL Language VS Code extension folder). Point it at project, symbol/package path, Dataverse URL, and target entity; it fetches entity metadata and emits the AL table.
  - From **AL Language v13+**, the proxy generator needs two new params: **client ID** and **redirect URI**. Microsoft removed the built-in Entra app (security), so you must register your own Entra app and pass its client ID.
- Wiring custom sync in AL: subscribe to `OnLookupCRMTables` [sic? verify event name] to point the coupling lookup at your integration-table page; enable deep linking between the BC table and the Dataverse table; then register table mapping + field mapping (map on a key field, use a `ModifiedOn` field for change detection).
- Validation runs on write-back: if a Power App writes to a Dataverse table synced to BC and the BC `OnValidate`/`OnInsert` fails, the record is created in Dataverse but sync fails — error surfaces **in BC** (sync log), not in the Power App.

**Virtual Tables**
- Surface BC data in Dataverse via **API pages/APIs at query time** — Dataverse calls BC's API on demand. **No data stored in Dataverse** (no storage consumed).
- Requires installing the **Business Central Virtual Table** app from AppSource (free); it provisions several managed solutions in the Dataverse env. Enable virtual tables in Dataverse Connection Setup ("virtual tables and business events" path in assisted setup); virtual tables are off by default.
- Individual API pages must be explicitly enabled as virtual tables (all APIs disabled by default) — enabling schedules a batch job.
- Respects BC business logic: writes from a Power App / model-driven app trigger BC validation (e.g. end-mileage < start-mileage rejected; invalid lookup values rejected) with the error shown in the app.
- **Not every API page suits a virtual table**: a header+lines composite API page (embedded lines) loses the lines when surfaced as a single virtual table — the system keeps only the header. Prefer flat header and line API pages.
- **Synthetic relationships** (newer feature): link a native Dataverse table (or a Data Sync table) to one or more BC virtual tables, defined in Dataverse Connection Setup → synthetic relations. Related virtual-table records then show under a real Dataverse record. Has feature telemetry.

**Webhooks (contrast)**
- Push model: external system **subscribes** to a resource (a specific API page); BC pushes on any data change.
- On subscribe, BC performs a **handshake** — replies to the notification URL with a validation token that the endpoint must echo back to prove it's listening.
- Subscription **expires after 3 days**; external system must refresh (e.g. cron) before expiry.
- Fires on *every* insert/modify/delete (like change log); notification payload carries only the **changed resource + change type**, NOT which fields changed — consumer must call back to BC to fetch the actual data.
- Optional **clientState** in the subscription body acts as a shared secret so the anonymous endpoint can reject calls that don't present it.
- Internals: subscription creates a record in system table `API Webhook Subscription` [sic? verify]; changes recorded in `API Webhook Notification` [sic? verify]; a task-scheduler background task dispatches the notification.

**Business Events ("webhooks on steroids", preview)**
- Notify external systems of specific *business actions* (e.g. order released), not raw data changes. Also subscription-based, **but no 3-day expiry and no handshake** — subscription persists until manually deleted.
- Payload can carry as much data as the AL author includes, so consumers usually need no callback. Cannot send records or complex types — only primitives; serialize JSON to text if needed.
- Fired **after the transaction commits**; multiple business events raised in one transaction are **bundled into a single notification** (e.g. two loan lines → one notification, not two). Note: Power Automate may trigger twice on a bundle (possible bug).
- **Standard business events**: shipped in Microsoft's external-events app (introduced ~2 releases prior), grouped into 5 categories — accounts payable, accounts receivable, sales, purchasing, opportunities. Naming is inconsistent across the product: "external events", "business events", "external business events".
- **Authoring a custom business event in AL:**
  - Extend the event-category enum to add your own category.
  - Declare the event as an **`ExternalBusinessEvent`** [sic? verify exact attribute/keyword against compiler] with name, display name, category, and a **version**.
  - Versioning rule: never mutate a published business event (e.g. to add a param) — **obsolete the old one and publish a new version** to avoid breaking existing subscriptions.
  - Raise it from your own `OnAfter…` subscribers (e.g. after loan/return actions).
- **Subscribing (REST):** GET available events from the external-business-events endpoint; POST subscription must include the **app ID** that owns the event, the event name, the notification URL, and the **event version** (defaults to empty if omitted — a subscription with empty version won't receive a v1 event; version must match exactly). In-client: **Business Event Subscriptions** page lists subscribers + activity log; **Refresh business events** action re-fetches event definitions after code changes.
- Consuming in Power Platform: Power Automate BC connector trigger *"when a business event occurs"* (preview) or the Dataverse connector *"when an action is performed"* (GA) — custom + standard events both appear.

**Telemetry for business events** — four signal event IDs: subscription created, subscription deleted, triggered successfully, failed to send. Custom dimensions expose event name, event version, and the subscribing external system (available on create/delete signals; the *triggered* signal does NOT record the target system). Event ID `40` [sic? verify] = subscription created.

**Licensing:** business events need no extra BC license (Power Automate side may need its own).

**Option/choice fields across languages:** option values sync as their underlying integers, so BC↔Power Apps sync is language-independent; translations are maintained separately per side (Power Apps calls options "choices").

## 24. Interfaces (BCQuality: interfaces)

- **Prefer an interface with enum-backed implementation over a `case` statement** for variant behaviour — new variants add an enum value + implementation, no edits to a central `case`.
- **Assign a codeunit to an interface variable** for injectable, testable dependencies.
- **Set `DefaultImplementation` on the enum** so an unmapped value still resolves to a usable interface.

**Interface additions (2024w2):**
- **`interface IExpress extends IShipping`** — extend an interface to add methods without breaking
  existing implementors of the base. Implementors of the extended interface must implement the
  **combined** method set; an enum implementing only the base still works (it implicitly implements the
  base — don't re-list it).
- **`is`** — Boolean test whether an interface instance's underlying codeunit implements another
  interface. Left side must be an interface variable/parameter or a **variant** (inspects the variant's
  codeunit).
- **`as`** — cast an interface to another interface type. GOTCHA: **errors on an invalid cast** —
  always guard with `is` first.
```al
if Provider is IExpressShippingProvider then
    (Provider as IExpressShippingProvider).ExpressDispatch();
```
- System Application ships a generic **`IUnknown`** base interface — accept `IUnknown`, then `is`/`as`
  to the real type for generic interface-handling code.

## 26. Permission Sets (PTE0004 — every extension needs one)

PerTenantExtensionCop makes a missing permission set an **error**: `PTE0004: Table <id> '<name>'
is missing a matching permission set`. Every table the extension adds must be covered by a
permission set **in the same extension**. Ship one from the start — retrofitting is the most
common analyzer failure. File suffix: `.PermissionSet.al` (§2).

Verified BC28 syntax (compiles clean under PTECop):
```al
permissionset 50103 "PTE My Feature"
{
    Assignable = true;                       // user-assignable in the UI; default is false
    Caption = 'My Feature', MaxLength = 30;

    Permissions =
        table "PTE My Setup" = X,            // X = execute (the table OBJECT)
        tabledata "PTE My Setup" = RIMD,     // Read/Insert/Modify/Delete (the DATA)
        codeunit "PTE My Mgt" = X,
        page "PTE My Setup Card" = X;
}
```
Rules:
- **`table … = X` and `tabledata … = RIMD` are BOTH needed per table** — object execute and data
  access are separate grants. PTE0004 is about the tabledata coverage.
- Letters: `R`ead `I`nsert `M`odify `D`elete for `tabledata`; `X` (execute) for objects
  (table/codeunit/page/report/query/xmlport). Grant the minimum the feature needs — a read-only
  lookup table doesn't need `IMD`.
- Object id from the extension's range; name ≤30 chars like any object (the old 20-char
  permission-set limit is gone in BC28 — verified by compile).
- **Compose** with `IncludedPermissionSets = "Other Set";` instead of repeating permissions.
- **Extend someone else's set** (e.g. grant your objects to a base role) with:
  ```al
  permissionsetextension 50104 "PTE My Feature - Basic" extends "D365 BASIC"
  {
      Permissions = tabledata "PTE My Setup" = RIMD;
  }
  ```
- Add objects to the permission set **in the same change that creates them** — the referee now
  compiles with PTECop, so a new table without coverage fails the build.
- Legacy XML permission files (`extensionsPermissionSet.xml`) are obsolete — AL objects only.

<!-- ingested: · Entitlement object | 2026-08-16 -->
### Entitlement object

- `entitlement <Name> { ... }` — declares the maximum permissions a user may hold, based on purchased license or Entra role. Online BC only (v18.0+). No object ID; identified by name.
- Effective permissions = intersection of (entitled) ∩ (assigned permission sets). Entitlement alone grants nothing.
- `ObjectEntitlements` lists permission sets. Only permission sets **from the same app** may be referenced — one app cannot widen or redefine another app's entitlements.
- VS Code snippet: `tentitlement`.

**Type values**

| `Type` | `Id` holds | Use |
|---|---|---|
| `Role` | Entra role GUID | Entra role mapping; pair with `RoleType = Delegated` or local |
| `PerUserOfferPlan` | Partner Center plan Service ID (string) | Marketplace transactability, per-user plan |
| `Unlicensed` | — (no Id) | User not licensed via a Marketplace offer plan; custom/side-by-side licensing |
| `Group` | Entra group **object** ID | Group access to transactable app without buying a license |
| `Application` | Entra app **client** ID | S2S vendor access without a license |
| `ApplicationScope` | scope string, e.g. `'API.ReadWrite.All'`, `'Automation.ReadWrite.All'` | S2S by granted scope |

```al
entitlement "Delegated Admin agent - Partner"
{
    Type = Role;
    RoleType = Delegated;
    Id = '00000000-0000-0000-0000-000000000007';
    ObjectEntitlements = MyApp_PartnerFullAccessPermissionSet;
}

entitlement BC_PerUserOfferPlan
{
    Type = PerUserOfferPlan;
    Id = 'MyOfferPlan';
    ObjectEntitlements = "MyOfferLicensePermission";
}

entitlement BC_Unlicensed
{
    Type = Unlicensed;
    ObjectEntitlements = "MyFreeLicensePermission";
}
```

**Checking entitlements at runtime**

- Indirect check via record permission properties — cheapest freemium gate:
  - `Rec.WritePermission()` true ⇒ user entitled *and* permitted to write ⇒ treat as licensed.
  - only `Rec.ReadPermission()` ⇒ unlicensed tier.
  - neither ⇒ inconclusive (permission may simply not be assigned) — do not infer license state.
- Direct check via `NavApp`:
  - `NavApp.IsUnlicensed(): Boolean` — user holds this app's `Unlicensed` entitlement.
  - `NavApp.IsEntitled('<EntitlementName>'): Boolean` — entitlement defined in the current app.
  - `NavApp.IsEntitled('<EntitlementName>', '<AppId GUID>'): Boolean` — entitlement defined in another app (e.g. System Application id `63ca2fa4-4f03-4f2b-a480-172fef340d3f` for `'Dynamics 365 Business Central Essentials'`).

**Freemium pattern** — layer permission sets, then bind each tier to an entitlement:

```al
permissionset 50101 MyFreeLicensePermission
{
    Assignable = false;
    Permissions = table MyTable = X,
                  tabledata MyTable = R;
}

permissionset 50102 MyOfferLicensePermission
{
    Assignable = false;
    Permissions = tabledata MyTable = RMID;
    IncludedPermissionSets = "MyFreeLicensePermission";
}
```

- Note `Assignable = false` on entitlement-backed permission sets — they are granted through the entitlement, not hand-assigned to users.
- Marketplace transactability binding of entitlements to offers arrived in 2023 wave 2.
- Sign-in / authorization failures caused by entitlement gaps surface in Authorization Trace telemetry.
- Real examples live in BCApps `src/System Application/App/Entitlements/`.

<!-- ingested: · Permissionset object | 2026-08-16 -->
### permissionset object

- `permissionset` object available BC 2021 wave 1 (v18.0)+. Snippet: `tpermissionset`.
- Building blocks. Assignable sets = admin-assignable via Permission Sets page. Nonassignable sets = hidden from UI, used only for composition.
- Name length limit: **20 chars when `Assignable = true`**, 30 chars otherwise. Over limit → compiler error `AL0305`.
- Properties: `Assignable`, `Caption`, `Permissions`, `IncludedPermissionSets`, `ExcludedPermissionSets`.
- `IncludedPermissionSets` pulls in another set's permissions; `ExcludedPermissionSets` subtracts.
- Permission letters on `tabledata`: R/I/M/D (read, insert, modify, delete). Case-insensitive in practice (`RIm` valid). Codeunits use `X` (execute).

```al
permissionset 50134 "Sales Person"
{
    Assignable = true;
    Caption = 'Sales Person';

    Permissions =
        tabledata Customer = RIMD,
        tabledata "Payment Terms" = RMD,
        tabledata Currency = RM,
        tabledata "Sales Header" = RIM,
        tabledata "Sales Line" = RIMD;
}

permissionset 50135 MyPermissionSet
{
    Assignable = true;
    Caption = 'My PermissionSet';
    IncludedPermissionSets = "Sales Person";

    Permissions =
        tabledata Vendor = RIm,
        codeunit SomeCode = X,
        codeunit AccSchedManagement = X;
}
```

**Gotchas**

- `permissionsetextension` changes are **additive only** — any extension can escalate privileges on a set you ship. Only make a set extensible if elevation is acceptable.
- Entitlement = collection of permission sets defining a meaningful user role; distinct from assignable permission set.

**Tooling**

- VS Code command `al.generatePermissionSetForExtensionObjects` (BC 2022 wave 2+) generates/updates a permission file for the active project — creates new file or merges into an existing one. Run it after adding objects; forgotten permissions are a common ship bug.

<!-- ingested: · Permissionset extension object | 2026-08-16 -->
### permissionsetextension object

- Available BC 2021 wave 1 (v18.0)+.
- Adds permissions to existing AL-defined permission set. **Additive only** — cannot remove permissions.
- Ships with extension: install grants perms, uninstall removes them. No manual admin assignment needed.
- Snippet: `tpermissionsetextension`.

```al
permissionsetextension 50140 "Extended Sales Doc" extends "Sales Person"
{
    Permissions = tabledata Currency = ID;
}
```

- Permission letters on tabledata: R/I/M/D (here `ID` = Insert + Delete). See Permissions property / "Permissions on database objects".

**Gotcha — privilege escalation by extension**

- Because extension is additive and applies automatically on install, a permission set extension can elevate privileges on a deliberately narrow permission set. Admin may not expect installing an app to widen existing roles.
- Design rule: a permission set extension should only add permissions for objects belonging to its own app. Keeps blast radius inside the app.
- Corollary for base permission sets you author: assume anyone can extend them; do not rely on a permission set staying narrow. Guard with `Assignable` property where relevant.

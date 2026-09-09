# bc-security

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: Securing Business Central / Customer-Dri | 2026-07-27 -->
### Securing Business Central — secretless auth, Purview auditing, network isolation

- **Microsoft Secure Future Initiative (SFI)** — three principles: secure by design, secure by default, secure operations. Six pillars, 28 objectives. Session focuses on two: *protect identities & secrets* and *protect networks*.
- Internally BC removed all stored credentials (storage account keys, SQL user/pass) across its Azure backend, moving to Entra ID auth only.

#### Secretless auth to BC APIs (managed identity + federated credentials)
- Client-secret pitfalls: can be stolen/leaked, need manual rotation + secure storage, risk of hardcoding.
- Recommended: **managed identity** on an Azure caller resource → auto-creates a service principal in Entra; grant it granular Azure RBAC; resource fetches short-lived tokens from an internal endpoint.
- To call BC APIs (S2S), you still need an **Entra app registration** with BC API permissions, but replace the client secret with a **federated identity credential (FIC)** that trusts a managed identity. No secret stored.
- Two managed identity kinds: **user-assigned** (persists, attach to multiple resources) and **system-assigned** (lifecycle tied to its resource — deleted with it). Managed identities do **not** expire (no 2-year expiry like secrets); only the issued token is short-lived.
- Flow: caller resource (e.g. Azure VM) with assigned managed identity → build a **client assertion** from the managed identity token → pass to confidential client → Entra validates against the app's FIC config → returns access token for BC.
- Customer side: add the partner's app (client ID) under Entra apps, grant consent, and scope access further via BC **permission sets** (e.g. read-only).
- Uses standard MSAL code; partner tenant ID = app tenant, resource tenant ID = customer tenant.
- **Limitation:** calls *from* BC outbound (AL) still require client secret — multi-tenant SaaS has no per-tenant identity, so FIC not available there. Managed identity only works for callers *in Azure*; not available on-prem or non-Azure callers.

#### Auditing via Microsoft Purview
- BC automatically emits auditable events to **Purview** (tenant-wide audit portal). Record type filter for Business Central exists in the Purview audit search.
- Event categories include: administer environment, configure extension, administer user, configure Copilot — each with sub-activities (e.g. administer-environment event → created/renamed/copied/scheduled/updated activities). Full list on Microsoft Learn.
- Automation pattern shown: Entra app (FIC, no secret) with Microsoft Graph `AuditLog.Query.Read.All` [sic? verify exact permission name] → two Azure Functions (submit query / fetch results by query ID) → Logic App on 24h recurrence that alerts (email) when a matching event (e.g. environment renamed) appears.

#### Network isolation — service tags
- BC has a dedicated **service tag** `Dynamics 365 Business Central` (reserved IPv4 + IPv6 ranges, distinct from generic Azure cloud tags) since 2023. Ranges are reused from a pool; list changes only on new region onboarding or capacity exhaustion.
- Use in NSG rules / on-prem firewalls to allow only BC-originated traffic (e.g. allow TCP 443 from the BC service tag).
- **Gotcha (temporary):** an Azure networking change moved the BC service tag from GA to "development" mode, so it is not selectable in the portal picker. Workaround: reference the tag name directly via PowerShell or ARM template (the rule still works).
- Obtain the IP ranges two ways: (1) Azure REST **service tags list** API (`Microsoft.Network` service tags endpoint — requires auth; sample used a Logic App system-assigned managed identity with RBAC read on the subscription); (2) Microsoft's published service-tags **JSON file** URL (no auth). Filter the JSON for the BC tag.
- Each tag entry has a **changeNumber** (version). Automate firewall updates only when changeNumber increases (store last-applied version as a tag on the target resource; compare, then PATCH firewall rules).

#### Service tags on storage accounts — doesn't work
- Storage account network firewall supports **IPv4 only** (no service tag, no IPv6).
- Even manually populating BC IPv4 ranges fails when the caller's VNet is in the **same or paired region** as the storage account: Azure routes traffic over the internal network, so the storage firewall sees an **internal IP**, not the public BC IP. (Confirmable via storage diagnostic logs.)
- Virtual network rules (allow-listing BC's subnet) also fail: BC moves environments across clusters → new VNet → not allow-listed.
- **Recommended workaround:** front the storage with an **Azure Function**. Azure Functions *do* support service-tag firewall rules — set deny-all + allow `Dynamics 365 Business Central` tag. Function survives cluster moves; backing storage can be fully private (private links). No IP-range automation to maintain.

#### General hardening takeaways
- Go secretless with managed identities where the caller is in Azure; otherwise use FIC on an Entra app.
- For Azure resources (SQL, Storage, Service Bus, Cosmos DB): **disable local authentication** to force Entra ID only — this is how SFI KPIs measure success.
- SAS URLs still allowed but max validity now **7 days** (was longer when SAS was backed by storage account keys).
- Disable **anonymous blob access**.
- Add firewall rules as a second defense-in-depth layer. **Network Security Perimeter** (Azure feature, in preview) aims to simplify this.
- Use **PIM** for just-in-time elevation; avoid persistent elevated access.
- BC docs at `aka.ms/bcsecurity` [sic? verify exact URL] currently document what you *can't* do; being revamped with these samples.
- BC vulnerabilities qualify for the Microsoft Dynamics **bug bounty** program.

<!-- ingested: Microsoft Presents: Security & Privacy 101: best practices f | 2026-07-27 -->
### Security & privacy fundamentals (Microsoft talk)

- Security model = protect + detect + respond, not just a perimeter wall. Adopt "assume breach": assume attacker already inside; plan detection and eviction, not only prevention.
- Priority split (rule of thumb from MS response-centre CVP): ~50% inventory/asset management, ~30-40% fundamentals (authn, encryption), ~10-20% empathy + attacker mindset.

### Asset inventory
- Cannot protect what you don't know exists. Keep an up-to-date list of every machine/VM/license/software.
- Reduce attack surface: kill unused VMs and forgotten test machines (a stale test box with live creds was a real breach pivot point).
- Patch everything; automate updates (winget on Windows, softwareupdate/tooling on Mac). Unpatched RCE vulns stay exploited for years.

### Authentication & secrets
- MFA everywhere; at least 2FA. Prefer FIDO hardware keys (e.g. YubiKey) or authenticator apps over SMS (SMS is weakest but still better than nothing).
- Passwordless + password manager where possible.
- Store secrets in a dedicated secret store, never in code or plaintext files. Have a rotation plan for leaked/compromised secrets.
- Removing a secret from source does NOT remove it from git history — rotate the actual secret. Attackers grep history for "removing password" commits and reuse them.

### Pipeline / code security
- Use static + dynamic analysis: CodeQL, credential scanners (CredScan [sic?] — verify tool name) to block secrets entering code.
- Restrict who can push to production; don't allow prod access from everyday personal laptops.

### Encryption
- Encrypt at rest, in transit, and (for sensitive domains) in use. Microsoft data is encrypted at rest by default — don't disable it.
- "In use" options: Always Encrypted for SQL [sic?] (encrypts in RAM); verify exact feature name.
- Use TLS certs (e.g. Let's Encrypt) for domains you own.
- Bring-your-own-key / customer-managed key (CMK) supported for sensitive industries.

### GDPR & data governance
- GDPR grants rights: be informed/consent, view, edit, delete, export your data. BC satisfies most of these natively via UI / export; consent obtained at sign-up via service agreement.
- Cross-boundary data flow (e.g. BC tenant in Denmark but Power Platform env elsewhere) is valid but triggers a mandatory privacy notice + recorded consent before the feature can be used.
- 2020 Schrems II [sic?] ruling invalidated EU→US transfer agreements. Microsoft's response: EU Data Boundary (EUDB) — a Microsoft policy, not law. Provision all linked services (BC, Power Platform, etc.) inside EUDB and Microsoft keeps them GDPR-compliant. Note: not all European countries are in the EUDB.
- Compliance certs (third-party audited): ISO 27001 (info security mgmt), ISO 27701 (privacy mgmt) [sic? — captions said 2701/2771], SOC 2 (encryption, access control, redundancy, availability, monitoring/incident response). Verify exact ISO numbers.

### Customer-managed key (CMK) — BC offering
- Layered encryption: customer key in customer's Key Vault encrypts the storage key kept alongside data in the Azure Storage account.
- Storage account fetches the key via managed identity from a shared account granted by the Key Vault admin.
- Result: Microsoft cannot decrypt customer data without access to the CMK; customer can rotate/revoke the key at any time. Legal requirement in some industries.

### Least-privilege access (how Microsoft operates)
- Engineers access prod/customer data only from locked-down restricted devices (limited web/network/software) using dedicated accounts for audit trail.
- Access requires justification, approval by a small approver group, and auto-expires after a short window.
- Customer Lockbox: puts the customer in the approval chain — customer is notified of a Microsoft access request and can approve/deny it.

### Internal review process (reusable pattern for partners)
- Three stages, same flow for privacy and security: (1) preliminary risk assessment at design start, (2) feature review at completion, (3) annual full-service review for external auditors.
- Preliminary assessment outcomes: go / needs changes / stop (violates guidelines). "Stop" ≠ bad idea — reflects the usability-vs-privacy/security trade-off; lean to privacy/security.
- Security feature review uses a threat model (categories: elevation of privilege, repudiation, denial of service, etc. — STRIDE-style) → prioritise risks → mitigation plan → verify in code.
- Privacy feature review uses a data flow diagram (map services, trust/geographic boundaries, data flowing between) + a data inventory: list each data element, sample it, classify (personal data vs system data like correlation IDs), record which services store/handle it and where (EU?), then judge compliance.
- Practical gotcha: OAuth tokens are only base64-encoded and often contain personal data (name, email). Don't forward user tokens across boundaries — use service-to-service auth / managed identities (on-behalf-of) instead.

### Responsible AI principles (Microsoft)
- Accountability: user stays in control; human approval gate before AI takes action (e.g. AI must not auto-create/post sales invoices).
- Transparency: output explainable; disclose that AI generated the answer.
- Reliability & safety: genuine purpose, consistent/predictable output for same input, monitoring + feedback.
- Fairness: no bias/stereotypes. Inclusiveness: accessible to all users.
- Privacy & security: data passed to the model must be handled with same rigour.
- Apply in UI (show how response was generated, allow edit, final approval, feedback) AND in backend prompt engineering/architecture.

### Attacker & customer mindset
- Secure by default (UK NCSC definition): make things as secure as possible without the user configuring anything; don't force users into settings for security.
- When forced to choose security vs usability, choose security — but don't tank a working app over a low-priority issue.
- Phishing: AI makes phishing emails realistic (fewer typo/bad-URL tells). Watch for URL masking (display text ≠ real link) and email spoofing (good providers flag it). Spear phishing uses scraped public data (e.g. Instagram vacation posts) for targeted lures.
- Red team / offensive security: think like an attacker against your own systems — port scanning, website scanning; commission a pen test if resources allow.

### Partner takeaways
- Keep an up-to-date asset inventory. Appoint privacy/security SMEs to write internal guidance/training. Run a lightweight privacy/security review per feature (data flow diagram + threat discussion) and act on the outcomes.

<!-- ingested: Microsoft Presents: Authorization techniques you might have | 2026-07-27 -->
### Authorization techniques (security groups, S2S, guest users, GDAP, device users)

**Baseline BC auth model**
- Authentication in Entra ID (identity), then two authorization layers: (1) entitlement to features via license/subscription (Premium, Essential, admin roles); (2) restriction to operations via permission sets.

**Security groups (Entra ID groups, reused in BC)** — three uses:
- *Environment access*: link a security group on the environment in BC Admin Center; only direct + indirect members can sign in. Admins bypass the restriction. Admin Center warns if the linked group was renamed/deleted.
- *Permission set assignment*: create a security group record in BC (Security Groups page → New → pick Entra group), assign permission sets to it. All members licensed for BC inherit those sets automatically. Users page shows which security group granted a set.
- *Bulk license assignment* (Entra feature, not BC): assign licenses to a group; only **direct** members inherit (nested groups reportedly don't work for licensing — unverified). Set each user's **usage location** or license assignment fails. Entra "licensed users" view shows access path as indirect + source group. In BC the user just looks normally licensed.
- Over-assigning: if group has 100 members but only 50 licenses assigned, only 50 get the license; the rest don't (no loophole). A user does not consume two licenses of the same type from two groups.

**Service-to-service (S2S) auth** — added v17, expanded after.
- For system-to-system integration (e.g. web shop → BC APIs), no user present, so no interactive re-auth prompt. OAuth client-credentials flow.
- Entra setup: register an app; add a client secret (or certificate); under API permissions add Business Central → **Application** permissions (not Delegated, which is the user-delegation flow). Scopes: `API.ReadWrite.All` [sic? verify exact scope name] (all BC APIs), `Automation.ReadWrite.All` [sic?] (setup APIs — install extensions, import config packages), `AdminCenter.ReadWrite.All` [sic?]. Grant admin consent.
- BC setup: Microsoft Entra Applications list page → New → paste the Entra app **client ID**, describe, enable, assign permission sets (app is treated like a user).
- Entitlement for an app comes from the checked API-permission scopes, not from a license or admin role.
- API operational limits are **per user/per app**. No cap on number of registered Entra apps, so registering multiple apps + rotating multiplies throughput.
- Installing extensions via S2S: reportedly possible with Automation or API scopes (presenters not fully certain — verify).

**Guest / invited users (Entra B2B)**
- Invite external user by email in customer's Entra (optionally auto-send invite). Invitee accepts, becomes a user of type **Guest** in the customer tenant.
- Guest's UPN is not their email; format encodes their home org, e.g. `alias_microsoft.com#EXT#@customerdomain` — lets you see who they really are.
- Guest logs in with their native (home-org) credentials. Assign a BC license to the guest like any user; in BC they appear as a normal user (the `Authentication email` field actually shows the UPN).

**GDAP (Granular Delegated Admin Privileges)**
- Replaces old DAP (deprecated/dead — stop using). Granular in: **duration** (e.g. 90 days, optional auto-extend), **roles** (grant only needed Entra roles, e.g. BC admin role, Cloud App Administrator for consenting to Entra apps), and **which partner employees** may act (partner selects security groups on the admin relationship).
- Flow: partner creates admin-relationship request in Partner Center (name, duration, roles, auto-extend) → customer receives email link to M365 admin center → customer approves → partner assigns security groups of employees who can use it.
- Delegated-admin logins appear in BC as **anonymized** users (privacy); Admin Center shows they logged in and hold the delegated-admin license.
- Gotcha: don't mix GDAP privileged accounts with guest users — reportedly breaks. Old DAP failed to recognize a user who was both guest and delegated admin.
- Limitation: cannot scope a partner to a *specific environment* (BC admin role sees all environments). Per-partner/per-environment isolation is on the roadmap (est. ~end of 2026 — unverified).

**Device users (concurrent/pool licensing)** — added v15; scheduled tasks as device users added recently.
- For shared devices (scanners, POS). Buy N device licenses; up to N concurrent sign-ins. Extra users wait until a slot frees. Example: 100 scanners, 33 in use per shift → buy 33 device licenses.
- Setup: create an Entra security group with a **specific reserved name**; members are treated as device users. Do **not** assign licenses to these users individually.
- (On-prem differs: has a Device Users page in BC; cloud does not — cloud is purely license + named security group.)
- Traceability: device users still log in as themselves → appear as individual entries on BC Users page, and App Insights telemetry carries the user ID. Admin Center → active sessions lets you close a stuck/open session after a shift ends.

**Troubleshooting auth failures**
- Read the error message (includes a session ID). Some causes are outside BC's visibility (e.g. missing Entra usage location).
- Use the session ID in App Insights / Application Insights telemetry to find the exact missing permission, group, or role.

**On-prem note**: security groups reportedly work on-prem (a claim they can't connect to Entra was disputed — verify).

<!-- ingested: BC TechDays 2023 - Ease permission management in your applic | 2026-07-27 -->
### permission-management (BC 2022 wave2 / 2023 wave1)

**Composable permission sets** — a permission set can include other permission sets (nesting).
- Copy permission set options: flat copy / clone / **copy by reference** (reference keeps included set live, not flattened).
- Include another set with `IncludedPermissionSets` in AL, or via UI on the user's assigned set. Building a set that contains others = composed set.
- To make a set includable/assignable, use `Assignable = true` and `Access = Public` [sic? verify property names against compiler].

**Inherent permissions** (2023 wave1) — developer elevates user permissions in code context, only on your OWN app objects (cannot grant into other apps' objects, security reason).
- Two forms: grant within a **method** scope, or grant at **object level** (metadata property) so object is out of permission control entirely.
- Object-level: `InherentPermissions` and `InherentEntitlements` properties on table/object [sic? confirm exact property names]. e.g. give every user insert on a log table, read on a setup table.
- Use to remove buffer tables, impl codeunits, reports etc. from permission sets → cleaner sets, fewer admin errors, protects critical code paths (init) from missing-permission login failures.
- Effective Permissions page shows `Source = Inherent` for these (shipped in a later minor).
- MS reduced the `Login` permission set using inherent permissions — vastly smaller vs v21.4.

**Exclude permissions** — subtractive model: final set = included permissions − excluded permissions.
- Cannot express "deny" as an ACL; only subtract from a set. Excluding a whole set removes each of its permissions.
- UI: add an exclude line on a permission entry, or exclude an entire included set (parent shows as *partial*).
- **Exclude from wildcard** (2022 wave2): exclude specific pages/reports/objects from sets that grant wildcard (`*`) execute — grant-all-except pattern.

**Security groups on BC environments**
- `Update users from Microsoft 365` action now respects a security group set on the BC environment — syncs only users in that group; enables setup before first login (previously user had to log in to be created).
- Create AAD security group (Azure/M365 admin) → set as environment's user security group in BC admin center → update removes plans from users not in group.
- **Nested security groups** supported — group a group under the access group; members get access without direct membership.
- **Security Groups page** in BC: map AAD groups (SaaS) or Windows groups (on-prem) to BC permission sets. Move user between groups → changes their BC permissions. Optional; can mix group-based + directly-assigned (hybrid).
- Blank out default permissions in **License Configurations** so licensed users get no direct permissions (permissions come only via group).
- On-prem: Windows groups only, no AAD security group support (raise BC idea for it).

**User groups deprecated** — redundant now (nesting replaces composition; security groups replace Windows-group linking). Lived wrongly in base app.
- Migration wizard via Feature Management: options **assign permissions to members** (flat) or **convert to permission set** (keeps structure — recommended). Converts all at once.

**Telemetry (App Insights)** — permission errors signal: which customers/apps/objects hit errors. Also tracks permission-set changes (which set, which app changed it, field-level diffs).

<!-- ingested: BC TechDays 2022 - Permissions revisited | 2026-07-27 -->
### permission-sets: composition & exclusion (TechDays 2022 "Permissions revisited")

- Permission system layers (all must pass): license (on-prem) / entitlements (SaaS, protects IP owner), system constraints (e.g. read-only replica blocks non-read ops via the permission system), admin-granted permissions, plus optional test permission sets to simulate an extra layer.
- **Composed permission sets**: a permission set can include other permission sets, not just raw permissions. Nesting has no depth limit. Enables role → duty → task → permission hierarchies.
- Moved to metadata in **2021 wave 1 (v18)**, but back then includes were *flattened* on import — no real nesting retained.
- **v20** stores real nesting via system tables: `Tenant Permission Set` [sic? verify name] holds permissions, plus a `Permission Set Relation` [sic? verify] table for includes/excludes. Hierarchy retained at runtime.
- New permission-set editor UI: middle list = include/exclude individual permissions; bottom-left = include/exclude permission sets; right split view = resulting hierarchy + inclusion status (Full / Partial / Excluded); fact box shows permissions added by selected set.
- `Expanded Permissions` [sic? verify object name] table/page = flattened result of all includes/excludes. Reached via **View all permissions** action.

### permission exclusion semantics (set theory)

- **2022 wave 1**: added ability to exclude. `Tenant Permission` [sic?] gained a `Type` field (Include / Exclude); relations between permission sets also have Include/Exclude type.
- Calculation = set subtraction, NOT skip. Compute union of all included permissions → one list; union of all excluded → second list; subtract second from first per-element.
- Consequence: excluding a permission set removes **every permission that set contains** from the final result, regardless of where/how that set sits in the tree. Excluding something not present = no effect.
- Behaviour changed from v20's implementation, which was a *skip* during traversal (fragile — broke if tree restructured). New behaviour is structure-independent: internal shape of a set doesn't affect the result.
- Exclusion is **not a deny**: it only removes within *this* permission set. User can still gain the permission from another assigned set. (Avoids the counter-intuitive deny problem where adding a set reduces access.)
- Duplicate includes don't stack — inclusion is set membership, not a count.
- Worked examples: exclude a set that itself excludes X → the exclusion list is computed fully first (so the re-added X survives in the final result). e.g. D=(3,4,5); exclude R where R=(A∪B) minus 5 = (3,4) → result = {5}.
- Guidance: excluding a large shipped set (e.g. D365 Read out of D365 Premium) removes too much. Instead make a *small* set containing only the permissions to drop, then exclude that. It can take ~15 permissions to grant an edit ability but only 1 to remove it (all are required).
- Metadata: `IncludedPermissionSets` and new `ExcludedPermissionSets` [sic? verify property names]. No "excluded permissions" property — intentionally omitted; wrap perms in a small set and exclude that instead.

### copying permission sets

- Copy action now offers three modes:
  - **Flat / flat copy** — old behaviour, flattens to a raw permission list. Discouraged.
  - **Copy by reference** (recommended default) — new set *includes* the source set, so future Microsoft/partner additions flow through; you then add your own excludes on top. Solves the stale-copy upgrade problem where copied sets missed newly required permissions.
  - **Clone** — exact clone of includes/excludes and permissions.
- Export to XML updated to include permission-set relations; tagged version 2.0. Old XMLs still import (version auto-detected, single action). Tenant export adds a related-scope marker to record whether it came from a system permission set.

### inherent permissions (attribute)

- Method attribute [sic? verify name, e.g. `InherentPermissions`] elevates permissions during that method's execution — permission no longer needs to be in the assigned permission set. Available for **cloud scope** now (was on-prem-only since v20).
- Only elevates for **your own objects/extensions** — cannot alter permission setup of other extensions.
- `InherentPermissionsScope` [sic? verify] controls grant: Both (default), Permissions only, or Entitlement only.
- Scope propagates *down the call stack* to methods you call, BUT is stripped when an **event is raised** (you can't know what subscribers will attach). An event subscriber can re-declare inherent permissions on itself.
- Example use: login needed indirect Read on G/L Entry only to derive a default work date from the latest entry in demo setup — now attributed instead, so no G/L Entry permission needed.
- When to use: small dedicated tasks, ideally methods that call nothing else; critical paths that must never fail on any user (init tables on first login, feature-enabled checks). Not for large processes — don't circumvent security.
- Trade-off: admin/business owner loses the ability to revoke that permission for that method scope.

### roadmap (as of talk)

- Break down big sets (D365 Basic/Premium) into scenario-sized sets.
- **Inherent permissions on object** — removes ability to set up security on that object at all (e.g. setup tables); use sparingly.
- Troubleshooting tool to find which permission set grants a given permission.
- More telemetry/audit on set assign/remove (already emits telemetry when sets added/removed from users).

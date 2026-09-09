<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# PTE conventions, signature verification, obsoletion, extra rules

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 16. PTE Conventions

- **Suffix**: `PTE` on all new objects — `PTEDocumentLinkAZMgt`, `PTEDocumentLinkAZSetup`, etc. Never `TNP`.
- **Guard pattern** — every ABS operation starts with:
  ```al
  if not PTEDocumentLinkAZSetup.Get('DEFAULT') then
      exit;
  if not PTEDocumentLinkAZSetup.IsEnabled then
      exit;
  ```
- **Download intercept**: set `IsHandled := true` ONLY after successful ABS retrieval. If `PTEBlobName = ''`, exit without touching `IsHandled` — falls through to existing DB blob logic.
- **Migration rules**:
  - Do NOT `Commit()` per row. Chunk via `Codeunit.Run` (one atomic transaction per chunk) or use `DataTransfer`/`ModifyAll` — see §10 and §21.
  - On upload failure: do NOT clear DB blob field — surface error, leave DB blob intact
  - Set `PTEMigrated := true` only on confirmed successful upload
  - `PTEMigrated` is set only by migration codeunit — never set it in `OnBeforeInsert`
- **Object IDs**: ranges are per-project. PTE extensions default to `50100..50199`. Check the project's `app.json` or handover prompt for the assigned range before writing any object. Do not use IDs outside the assigned range.
- **Large / multi-line text on a page**: use the `WikiViewerPTE` control add-in (`usercontrol(...; WikiViewerPTE)` + a `SetContent()` call) **if that add-in exists in your project** (project-specific, not a platform control), not a native `field()` with `MultiLine = true`. AL has no "visible rows" property, so a MultiLine field stays visually cramped; WikiViewerPTE renders markdown in a scrollable container. Push content via `SetContent()` at the same lifecycle point where visibility is set.

---

## 18. Verifying platform API signatures (don't guess)

Training data on BC/AL platform APIs is frequently wrong or stale (e.g. `AOAI Operation Response` does **not** expose token-count getters — only `IsSuccess`/`GetStatusCode`/`GetResult`/`GetError`). Before writing AL against an unfamiliar **system** codeunit/enum (anything outside the project's own `src/`), verify the exact signatures from the compiled symbols:

```sh
unzip -o "<project>/.alpackages/Microsoft_System Application_<ver>.app" -d /tmp/alsym
```

The `.app` is a zip containing `SymbolReference.json`. Its top-level `Codeunits`/`Tables`/`EnumTypes` arrays are usually **empty** — real objects are nested recursively under `Namespaces[].Namespaces[]…`. Walk it (Python, open with `encoding='utf-8-sig'` — a BOM is present) to find the object, then read its `Methods`/`Values` for exact names, parameter types and return types.

**Better still — actually compile.** Use the **dotnet AL tool** (`~/.dotnet/tools/al`) — the
canonical toolchain here, and what the build pipeline (`run-build.py`) uses as the referee:
```sh
~/.dotnet/tools/al compile /project:"<project dir>" /packagecachepath:"<project dir>/.alpackages"
```

**A bare compile is NOT what VS Code shows.** VS Code loads the cop analyzers; without them the
compile misses whole diagnostic classes (PTE0004 missing permission set is an **error** under
PerTenantExtensionCop; AA02xx style/tooltip/overflow warnings under CodeCop/UICop). To match the
Problems panel, add the analyzers (they ship inside the dotnet tool):
```sh
A=$(dirname $(find ~/.dotnet/tools/.store -path "*net10.0*" -name "Microsoft.Dynamics.Nav.CodeCop.dll" | head -1))
~/.dotnet/tools/al compile /project:"<dir>" /packagecachepath:"<dir>/.alpackages" \
  "/analyzer:$A/Microsoft.Dynamics.Nav.CodeCop.dll" \
  "/analyzer:$A/Microsoft.Dynamics.Nav.UICop.dll" \
  "/analyzer:$A/Microsoft.Dynamics.Nav.PerTenantExtensionCop.dll"   # + AppSourceCop for AppSource apps
```
Needs a populated `.alpackages/` symbol cache. If it's empty, download symbols via the tool's own
**MCP server** (`~/.dotnet/tools/al launchmcpserver --transport http --port <p> <project dir>`,
then its `al_downloadsymbols` tool) — again exactly the pipeline's path.

> Do **NOT** use `alc` from the VS Code AL extension (`~/.vscode/extensions/ms-dynamics-smb.al-*/bin/…`).
> It's per-extension-version, drifts from the pinned toolchain, and isn't what the referee runs —
> a pass under one and a fail under the other is wasted confusion. `~/.dotnet/tools/al` only.

Compiling catches real bugs a read-through misses (e.g. a missing `using System.Visualization;`
for the `BusinessChart` add-in).

## 22. Breaking Changes & Obsoletion (BCQuality: breaking-changes)

- **Never delete or rename a published table field / public member.** Deprecate through the Obsolete lifecycle: mark `ObsoleteState = Pending` with `ObsoleteReason` + `ObsoleteTag`, ship for a release, then `ObsoleteState = Removed` and write the removal upgrade code.
- **Do not change the signature of a published procedure** — add a new overload instead.
- **Add new enum values only at the end** (extensible enums) — inserting mid-list renumbers and breaks dependents.
- **Choose access modifiers deliberately** — `internal`/`local` by default; `public` is a forever contract. Don't widen access to expose sensitive data through a public API.
- **Don't build on code already marked obsolete.**

<!-- ingested: Microsoft Presents: Obsolete Move, Future of delocalization | 2026-07-26 -->
### ObsoleteState Pending/Moved — move tables & fields between apps (mibuso, Microsoft engineering 2024-06)

- New `ObsoleteState` values `Pending` and `Moved` (alongside existing `Pending`/`Removed`) let you relocate a table or field to another app **without upgrade code and without copying data**. During extension sync the platform renames the underlying SQL table/column in place instead of copy-migrating. Verify exact enum member spelling (`PendingMove`/`Moved`? vs `ObsoleteState = Moved` with a separate move flag) against the compiler — captions garbled it. `[sic?]`
- Two new companion properties: `MovedFrom` and `MovedTo`, holding the **app ID** of the source/target extension. `MovedTo` (with a pending state) is set on the object in its current app to signal an upcoming move; `MovedFrom` is set on the copy in the destination app once moved. `[sic?]` verify exact property names.
- Properties apply to **tables and fields**. A field can move independently of its table — e.g. table moves down into a sub-app while one field stays behind via a table extension, or vice versa. Syntax is identical for down/sideways/up moves.
- Move directions all work the same mechanically: down (parent app → sub-app), sideways (between two unrelated apps, no dependency needed), up (sub-app → parent).
- **A move is a breaking change.** Once annotated moved, the symbol is gone from the source app — anyone depending on the source app that does NOT also depend on the destination app breaks (missing table/page/etc.). Manage via dependencies.
- The moved-out object must be **left behind as a legacy stub** in the source app: no code needed, but you must keep all SQL schema elements (fields, keys) intact so AppSource cop can verify the schema didn't change during the move. Changing schema + moving simultaneously is disallowed (would be breaking).
- Annotating a pending move raises a **code cop warning**; suppress with `#pragma` once handled.

### `propagateDependencies` — shield consumers from componentization

- app.json `propagateDependencies: true` makes an app re-export all its own dependencies to anything depending on it. Lets you split a monolith into sub-apps and have existing consumers keep working with their single original dependency, as long as every piece moved stays within that app's declared dependency set.
- Propagation is **one level only** — it does not transit through a chain. If app A propagates deps and B depends on A, B sees A's deps; but C depending on B does not automatically see them. Design the componentization boundary accordingly.
- The platform `application` package (app.json `application` version property) already uses propagated deps across base/system/Business Foundation, so Microsoft can shuffle tables/fields among first-party apps non-breakingly.
- **Guidance: depend on the `application` version property, not directly on Base Application / Business Foundation**, so first-party moves don't break you. If a symbol goes missing, read its `MovedTo`/`MovedFrom` to find the app ID you now need a dependency on.

### Upgrade / publish ordering for moves (production)

- Correct sequence: **publish ALL apps first (in dependency order), then sync all, then install all.** Publishing all first lets the platform see the full picture before any rename.
- A **half-done move is a corrupt state**: if the destination app isn't installed, the source table was already renamed away so its data is inaccessible (symbol gone) though the rows still exist in SQL. Finish installing the destination app to recover. No platform guardrail warns you mid-flow (as of 2024-06).
- VS Code publish does publish+sync+install in one step (dev-only code path), so moves appear to "just work" there; cloud/sandbox/production require the manual 3-phase order.
- Move properties were **first-party only** at time of talk, to be opened to partners gradually.
- Cleanup of legacy stubs is deferred: since this was a new feature, moved objects weren't expected to be removable before ~v31. (Separately, v26 planned to remove SQL schema of items obsolete-removed in v23 and earlier.)

### Namespaces as prep for moves (suggestion, not required)

- Namespaces are unrelated to the move mechanism but useful when refactoring toward it: when extracting a table extension or segmenting features, place objects in the target namespace so the eventual move is not also a rename (renaming the original object would itself be breaking). Namespaces are optional and **immutable once set** — no rename support yet.

## 25. Additional performance / error / security rules (BCQuality)

**Performance (§10 companions):**
- `IsEmpty()` for existence checks — never `Count() > 0` or `FindFirst`.
- `ModifyAll` / `DeleteAll` instead of a per-row `Modify`/`Delete` loop (mind: triggers/subscribers/media fields can silently regress these — pass `RunTrigger` deliberately; `DeleteAll` skips `OnDelete` unless you pass `true`).
- `Get` (full primary key) over `FindFirst`; `FindFirst` is the wrong tool for a keyed single-row read.
- `SetCurrentKey` with a key that covers both filter and sort.
- **Guard event subscribers with a cheap check before any DB call** — a subscriber fires on every publish; do the early-exit first.
- `FindSet(true)` takes an UpdLock on the read — use the plain `FindSet()` for read-only iteration; don't hold locks while waiting for the user.
- `SetLoadFields` before filters; reading an unlisted field after triggers a JIT reload — omit filter-only fields.
- **Membership checks over large sets: `Dictionary of [K, Boolean]` + `ContainsKey` (hash, ~O(1)), never `List` + `Contains` (linear scan → O(n×m) inside a record loop).** A List is only right when order/duplicates matter and the set is small.

**Error handling (§12 companions):**
- **A throw in a table-event subscriber rolls back the whole batch** — an `OnAfterInsertEvent` subscriber that `Error()`s aborts the user's insert. For non-critical side-effects (e.g. an external upload), fail soft (log + exit), don't `Error`.
- Prefer `ErrorInfo` with recommended actions over a plain `Error` for recoverable failures; set `ErrorInfo.ErrorType = Internal` for defects you want in telemetry but not in the user's face.
- `TestField` for a conditional presence check; `FieldError` only for an already-failed validation (it never evaluates a condition).

**Security (§14 companions):**
- `IsolatedStorage.SetEncrypted` over `Set` for sensitive values.
- Prefer **OAuth2 over API keys** for external HTTP; use the SecretText-aware `HttpClient` surface and `SecretStrSubstNo` so secrets never materialise as plain `Text`.
- Procedures that read/write IsolatedStorage, or `RecordRef.Open` a **caller-provided** table, must **not** be `public`.
- Validate URLs sourced from table fields before calling them; don't set `ValidateTableRelation = false` on user-editable fields.

<!-- ingested: Microsoft Presents: Fortifying Business Central - Secure You | 2026-07-26 -->
### Securing AL code — STRIDE threat modeling & secrets (mibuso, Derek 2025-10)

**Secret text data type**
- Use `SecretText` for any credential (API keys, passwords, tokens). Value stays hidden during debugging — cannot be read out in the debugger.
- Use when moving credentials out of isolated storage / Key Vault into an HTTP call, JSON payload, or control add-in.
- JSON: can now write a `SecretText` value into a JSON object without exposing it (inject secret into the JSON) — recently added [sic? verify exact `JsonObject`/`JsonValue` API for SecretText on Microsoft Learn].
- Control add-ins accept `SecretText`, BUT JavaScript still runs client-side — user can debug their browser and read the value. SecretText does not protect against that.
- Never hardcode secrets as string literals, labels, or resource files — git history retains them until purged. (MS red-team found valid-for-years creds this way; static analysis now blocks check-in of even fake creds.)

**Isolated storage — data scope**
- Default scope is `Module` (implicit). Always set scope explicitly for readability, even if Module.
- Scopes, narrowest→widest granularity: `Module` (default, whole extension module), `Company` (only within that company), `User` (only the saving user retrieves), and combinations (Company+User = most fine-grained). Always still bound to the extension.
- Extension B cannot read extension A's isolated storage unless A exposes it via a public procedure.
- Access isolated storage only from `internal`/`local` procedures to prevent unauthorized cross-extension access.
- `SetEncrypted` [sic? verify method name] to encrypt stored value — limit ~215 chars.
- Mark sensitive procedures `NonDebuggable` (not isolated-storage-specific — any code handling secrets) as a backstop if a dev falls back to plain `Text`.

**Azure Key Vault**
- App Key Vault is AppSource-only — NOT available to PTEs.
- Store app-specific secrets (not per-tenant/per-environment secrets) there.
- Advantage over isolated storage: manage secret lifecycle centrally — set expiration dates, force/automatic rotation of keys/certs, without entering each tenant.
- Access via App Key Vault Secret Provider [sic? verify `AppKeyVaultSecretProvider` / codeunit name], configured in app.json.

**Entitlements & permissions**
- Entitlement ≈ license (Essentials, Premium). Defines max possible access.
- Extension with NO entitlement object → all its objects get full implicit access: codeunits/pages get direct Execute; tables get direct Read/Insert/Modify/Delete/Execute.
- If you specify even one entitlement (e.g. Essentials only), any license not listed (e.g. Premium) gets NOTHING for those objects. Specify all needed licenses.
- Access requires the INTERSECTION of entitlement AND permission set — having only one grants no object access.
- Use security groups to manage permissions centrally.

**Inherent permissions / entitlements (`InherentEntitlements`, `InherentPermissions`)**
- Grant temporary elevated permission to a procedure at runtime (actions beyond the calling user's permissions) — e.g. a proc granting indirect Read to a ledger table.
- Apply only at the highest/outermost level of the call stack where the permission is actually used — inherent permission propagates down into any procedure you call from there. Scattering it makes permission origin untraceable and audits/maintenance a nightmare.
- Legit use: foundational objects/procs every user must reach regardless (e.g. Copilot capability codeunit). Do NOT leave them on just because it eased testing — easy to forget and ship (info-disclosure / privilege-escalation risk).

**STRIDE threat categories (apply per AL feature/dataflow)**
- Spoofing — impersonation. AL gotcha: don't pass `TenantId`/`UserId` as params to an external call; read them from AL platform in-code so a caller can't inject someone else's ID.
- Tampering — unauthorized data modification. Gotcha: a `Before`-publisher event (e.g. OnBeforePostSalesDocument) that lets subscribers MODIFY the record before a deliberate action gives an injection point — pass data without allowing mutation unless required.
- Repudiation — untraceable actions. Mitigate with Change Log, Monitor Sensitive Fields, telemetry (accept storage/perf cost — logs are the only proof).
- Information disclosure — e.g. username/password fields on a page as plain `Text` with no ExtendedDatatype masking; reachable via `?table=<id>`. Add ExtendedDatatype (Masked), remove stray inherent perms.
- Denial of service — self-inflicted via table locks (`repeat..until` over a large filtered set while locking) or hammering an external service into rate limits, blocking other tenants.
- Elevation of privilege — inherent-permission proc mistakenly wired to a public page action.

**Design checklist**
- External calls: what auth (OAuth token / cert / API key > basic), where are creds stored (isolated storage/Key Vault, NOT database/resource/literal).
- Prefer OAuth + isolated storage over username/password in the database.
- Principle of least privilege everywhere; don't hand out SUPER; audit inherent entitlements/permissions on objects.
- Managed identity from within BC to call Azure services / SQL is NOT currently supported (as of 2025-10) — no code cop/linter flags these security issues either.

## 27. Reference repos & patterns

- **Microsoft BCApps** — `github.com/microsoft/BCApps`, the official System/Base App source. Best ground truth for idioms: interface + implementation examples, event publisher/subscriber usage, facades, no. series (`src/System Application/`, `src/Business Foundation/`).
- **alguidelines.dev** — standard AL design patterns. Handy ones: **API Register Fieldset** (track request fields via a temp Field table + `RegisterFieldSet(FieldNo)` in `OnValidate`), **Command Queue** (`interface ICommand { procedure Execute() }` + Push/Pop), **Delegate API Operation** (return `false` from `OnInsertRecord`/`OnModifyRecord`/`OnDeleteRecord` to cancel the default).

<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Events & subscribers, error handling, archiving, upgrade codeunits

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 11. Events & Subscribers

Declaring an integration event (in publisher codeunit):
```al
[IntegrationEvent(false, false)]
local procedure OnBeforeDoThing(var Rec: Record "Document Link"; var IsHandled: Boolean)
begin
end;
```

Calling with IsHandled pattern:
```al
procedure DoThing(var Rec: Record "Document Link")
var
    IsHandled: Boolean;
begin
    IsHandled := false;
    OnBeforeDoThing(Rec, IsHandled);
    if IsHandled then
        exit;
    // default logic continues here
end;
```

Event subscriber codeunit (alguidelines: subscriber codeunits contain ONLY subscribers).
Both examples below are REAL, verified against BC28 symbols — table 1173 "Document Attachment":
```al
codeunit 50106 PTEDocAttachSubs
{
    // (a) TABLE SYSTEM EVENT — implicit on every table. Names end in ...Event
    //     (OnBeforeInsertEvent / OnAfterInsertEvent / OnBeforeModifyEvent / OnAfterDeleteEvent …),
    //     params are (var Rec; RunTrigger). There is NO IsHandled on system events.
    [EventSubscriber(ObjectType::Table, Database::"Document Attachment", 'OnAfterInsertEvent', '', false, false)]
    local procedure DocAttach_OnAfterInsertEvent(var Rec: Record "Document Attachment"; RunTrigger: Boolean)
    begin
        // side-effect work; do NOT Error() here — a throw rolls back the user's insert (§25)
    end;

    // (b) PUBLISHED INTEGRATION EVENT — exists only if the publisher declares it; parameters bind
    //     BY NAME, so copy them exactly as published (here the first param is named
    //     DocumentAttachment — declaring it as `Rec` fails with AL0282 "member not found").
    [EventSubscriber(ObjectType::Table, Database::"Document Attachment", 'OnBeforeExport', '', false, false)]
    local procedure DocAttach_OnBeforeExport(var DocumentAttachment: Record "Document Attachment"; var IsHandled: Boolean)
    begin
        if DocumentAttachment.PTEBlobName = '' then
            exit;   // fall through to base logic — don't touch IsHandled
        // serve the file from ABS…
        IsHandled := true;   // ONLY after successfully completing the action
    end;
}
```

EventSubscriber signature:
```al
[EventSubscriber(ObjectType::<type>, <ObjectRef>, '<EventName>', '<ElementName>', SkipOnMissingLicense, SkipOnMissingPermission)]
```
- `SkipOnMissingLicense` and `SkipOnMissingPermission`: both `false` in most cases
- `<ElementName>`: empty string `''` for table/codeunit events; field/action name for page events
- **Integration-event parameter names must match the publisher's declaration exactly** (binding is
  by name, not position). Verify against symbols (§18) — never guess names OR parameters.
- For download intercept: blob field empty → exit without setting `IsHandled` → falls through to existing logic

---

## 12. Error Handling

```al
// TryFunction wrapper — public method returns Boolean, private does the work
procedure UploadBlob(BlobName: Text; var DataStream: InStream): Boolean
begin
    exit(TryUploadBlob(BlobName, DataStream));
end;

[TryFunction]
local procedure TryUploadBlob(BlobName: Text; var DataStream: InStream)
var
    ABSBlobClient: Codeunit "ABS Blob Client";
    ABSOperationResponse: Codeunit "ABS Operation Response";
    ABSOptionalParams: Codeunit "ABS Optional Parameters";
begin
    // Any Error() or unhandled exception here = TryFunction returns false
    ABSOperationResponse := ABSBlobClient.PutBlobBlockBlobStream(BlobName, DataStream, ABSOptionalParams);
    if not ABSOperationResponse.IsSuccessful() then
        Error(ABSOperationResponse.GetError());
end;

// Calling side
if not UploadBlob(BlobName, DataStream) then
    Error(UploadFailedErr, GetLastErrorText());
// ⚠ PRIVACY: GetLastErrorText() may carry customer content (filenames, field/record values)
// from the underlying failure. Surfacing it raw in an Error/telemetry is a privacy finding
// (BCQuality privacy/getlasterrortext-customer-content-in-errors). For a user-facing failure
// prefer a controlled message; if you must include diagnostics, log them via a telemetry
// channel you control (Session.LogMessage with a defined DataClassification), not the raw text.

// Dialog functions
Error('Something went wrong: %1', ErrorText);          // throws, stops execution
Message('Migration complete: %1 records', Count);       // info dialog
if not Confirm('Delete all records?', false) then       // yes/no, default=false
    exit;
```

**`[ErrorBehavior(ErrorBehavior::Collect)]`** — lets a procedure keep running past `Error()` calls and collect them instead of aborting. Load-bearing where paired with `HasCollectedErrors()` / `GetCollectedErrors()` / `ClearCollectedErrors()`; removing the attribute while leaving those calls is an invalid state.
- ✓ Capture messages BEFORE `ClearCollectedErrors()` — after clearing, `GetLastErrorText()` returns `''`:
  ```al
  foreach Err in GetCollectedErrors() do ErrTB.AppendLine(Err.Message);
  ClearCollectedErrors();
  LogError(Staging, ErrTB.ToText());        // ✓ has the messages
  ```
- ✗ `LogError(Staging, GetLastErrorText())` after `ClearCollectedErrors()` silently logs a blank message.
- If collected errors seem to "loop", suspect a cursor/`Commit()` issue (a `FindSet` cursor invalidated by `Commit()`), not the Collect attribute.

---

<!-- ingested: Microsoft Presents: User friendly error handling in AL | 2026-07-26 -->
### ErrorInfo object — actionable & collectible errors (mibuso 2024-06)

- `ErrorInfo` = structured "recipe" for building an error dialog. Prefer over long param lists: set only the props you want (all have defaults), any order; Microsoft can add props without breaking changes.
- Core props/methods: `Message`, `Title`, `DetailedMessage`, `SystemId`, `RecordId`, `AddAction(...)`, `AddNavigationAction(...)`, `CustomDimensions`.
- **Actionable error** = user can recognize + understand + repair/report. Build with title + message + action button.
- `AddAction(caption, codeunitId, methodName, tooltip)` — "fix-it" action. `methodName` referenced by name (string), must exist; the method takes an `ErrorInfo` param (contract). Runs custom fix logic. Supports custom dimensions. [sic? verify AddAction signature/overloads]
- `AddNavigationAction(caption, pageId, tooltip)` — "show-it" action. Just opens page number, no method needed, no custom dimensions. Docs call these **fix-it** vs **show-it** actions.
- Pass state to fix action via `SystemId` (preferred over `RecordId` — easier to handle) or `CustomDimensions` (untyped property bag), read inside the action procedure.
- Web client renders same `ErrorInfo` by context: field-`Validate` → inline actionable error; action/dialog-triggered → dialog.
- **Tooltip**: last param of add-action methods → tooltip on the error button. Tooltips can now also be set on **table fields** (not only page controls); Copilot chat pane harvests field tooltips for context — write good tooltips + captions.
- **DetailedMessage**: NOT shown to end user; lives in error dialog's Copy Details / Share to Teams/Outlook / generate-email. Auto-enhanced with session IDs, UTC timestamps, AL call stack, custom dimensions. Use for technical/support info (e.g. feed `GetLastErrorText` from an HTTP failure). Keep concise.

### TestField auto-actionable (platform)

- Platform now auto-adds a navigation action to `TestField` errors — no AL code needed.
- Conditions all must hold: target page resolvable via record's `DrillDownPageId`/`LookupPageId` [sic? captions garbled "drill down page ID and card page ID" — verify], user has read+execute permission on that page, destination record ≠ current record, destination page ≠ current page. Link is pre-filtered to the correct record.

### Collectible errors (since 2021)

- Continue execution while collecting errors, then show all together; avoids error-after-error round trips.
- Design: reuse existing error-raising code (no behavior change when not collecting), avoids accidental commits, `Codeunit.Run` semantics preserved.
- Mark an error collectible: set `ErrorInfo.Collectible := true` (also honored by `TestField`/`FieldError` when passed an `ErrorInfo`).
- Enable collect scope: `[ErrorBehavior(ErrorBehavior::Collect)]` attribute on the method. [sic? verify attribute name/enum]
- Platform collects instead of throwing; at scope end still errors (default ugly dialog) unless handled.
- Handling: run via `Codeunit.Run`; on failure call `HasCollectedErrors()`, `GetCollectedErrors()` → list of `ErrorInfo`, iterate. `ClearCollectedErrors()` (or bool param on GetCollectedErrors) to suppress default platform dialog. [sic? verify exact method names]
- Common pattern: push collected `ErrorInfo` into a temp Error Message record → Error Message page.

### Error Message Management module (older collect path)

- Logs errors to Error Message record. Use if already on this module. Extension "Error Messages with Recommendation" adds title/recommended-action/status/subcontext fields + a fix workflow.
- Implement interface (error-message-fix [sic? verify name]) with 3 procs: set-error-message-properties, on-fix-error (fix logic, has access to error message record, runs in separate transaction), on-success-message. Extend the governing enum so platform maps error → fix.
- BaseApp helper: `AddSubContextToLastErrorMessage` [sic?] gets last error message + raises event; use a tag to uniquely identify the message in the subscriber.
- **Limitation**: cannot yet retrieve `AddAction` actions from `ErrorInfo` via error message management path — actions lost when combining.

### Behavior / troubleshooting notes

- Error actions run **modally**, shown AFTER transaction rollback → no locks held while user fixes; user re-runs the action afterward (not a paused flow).
- Page **709** = Error Message Register (posting + job queue errors); shows last-modified-by on committed error message records.
- Help & Support page: app/platform version, last known error, enable additional (detailed) logging → captures every SQL call; combine with Copy Details session ID + telemetry for root cause.
- Guidance: replace plain `Error(text)` with `ErrorInfo`; make most errors collectible so callers can batch them.

## 20. Archiving & ledger-application gotchas

- **Extension fields survive archiving for free**: BC's `ArchiveManagement.StoreSalesDocument` calls `TransferFields` from `Sales Header` → `Sales Header Archive`. Mirror your tableextension fields on the archive table with **identical field IDs/types** and they copy automatically — no manual assignment.
- **Set the final status in-memory before archiving**: in an `OnBeforeDeleteEvent` the record still exists; mutate `Rec` fields (e.g. status = `Lost`) in memory (no `Modify()` needed) before `StoreSalesDocument(Rec, false)` — `TransferFields` captures the in-memory value.
- **`CustEntrySetApplID.SetApplId` — re-read the entry after calling it**: SetApplId writes `Applies-to ID` via an internal local; the caller's var ref stays **stale** (holds the old DB value `''`). You MUST `Get()` the entry again before your own `Modify()`, or `Modify` silently clears `Applies-to ID` from the DB. Also, SetApplId only sets the **first** parameter — set the second entry's `Applies-to ID` manually to the same GUID, else posting errors "did not specify which entry to apply".
- **Detailed CLE `Transaction No. = 0`**: BC creates DCLEs with `Transaction No. = 0` for some original-system applications. Init `MaxTransNo := -1` (not `0`) when scanning for the latest application (`0 > 0` silently skips them); pair payment/invoice DCLEs by **`Application No.`** (unique per `Apply()` call), not `Transaction No.`.

## 21. Upgrade Codeunits (BCQuality: upgrade)

Only relevant for versioned/AppSource apps that ship schema or data changes.

- **Put upgrade logic in a codeunit with `Subtype = Upgrade`.** `OnUpgradePerCompany` / `OnUpgradePerDatabase` triggers should call helper procedures, not inline the logic.
- **Gate with upgrade tags, not version checks.** Register every tag via an `OnGetUpgradeTags`-style subscriber; check `UpgradeTag.HasUpgradeTag(...)` and set it after. Version-number branching is fragile.
- **Detect first install:** `if DataVersion() = Version.Create('0.0.0.0')` — skip data upgrades on a fresh install.
- **`DataTransfer` for bulk column updates on large tables** — set-based, fast. BUT it writes at the DB layer and does **not** fire `OnValidate` / `OnModify` / `OnAfterModifyEvent` subscribers. Safe for new fields/tables; for a pre-existing field with load-bearing validation use `Modify(true)` or document the intentional bypass.
- **`InitValue` does not back-fill existing rows** — only new records get it; existing rows need explicit upgrade code.
- **Guard every DB read in upgrade code** (`if Rec.Get(...) then`) — data may not exist yet.
- **Do not raise errors that block the upgrade** — log telemetry and continue; a thrown error can wedge the tenant mid-upgrade.
- **No external calls (HTTP, etc.) inside upgrade codeunits.**
- **Skip non-essential runtime work** when `GetExecutionContext() = ExecutionContext::Upgrade`.
- **Schema-breaking changes** (primary-key / field-type) are safe **only on tables with no existing data** (new in the same change); otherwise ship an upgrade procedure.

<!-- ingested: AL error handling | 2026-08-16 -->
### Error handling overview (Learn hub page)

- Core error-handling methods:
  - `Error()` — show error dialog, abort AL execution (rolls back transaction).
  - `ErrorInfo` data type — richer error object: classify error, attach support/telemetry info, drive actionable-error UI. Pass to `Error(Message: ErrorInfo)`.
  - `ClearLastError()` — clear last error from memory.
  - `GetLastErrorText()` — text of last error.
  - `GetLastErrorCode()` — error classification/code.
  - `GetLastErrorCallStack()` — call stack where last error was raised.
  - `GetLastErrorObject()` — last `System.Exception` object.
  - `Dialog` data type — dialog window; `Error` is a Dialog-family method.

- Strategy → mechanism map:
  - Run codeunit, branch on failure → `if not Codeunit.Run(...) then` (Run returns Boolean; rolls back the codeunit's writes).
  - Catch errors raised by AL code → `[TryFunction]` try methods.
  - Catch .NET interop exceptions → try methods, **on-premises only** (no .NET interop in cloud).
  - Bulk validation without a dialog per failure → error collection (`ErrorInfo` + collectible errors) instead of hard `Error()`.
  - Errors in Page Background Tasks → page trigger `OnPageBackgroundTaskError`.
  - Log an error inside a transaction that will roll back → logging in the same session is lost by rollback. Write it from a **background session** (StartSession) or send to telemetry (`LogMessage` / `Telemetry.LogError`), both of which survive rollback.

- Runtime auto-emits error telemetry to Application Insights on every user-facing error dialog: three streams — error-message quality, error dialogs shown (incl. AL location raising it), permission errors. Useful for alerting on error spikes.
- Own telemetry via the Telemetry AL module: `Telemetry.LogError`.

- Related sub-topics on Learn worth reading: failure modeling / robust coding practices, understanding the error dialog, UX guidelines for errors, actionable errors, collecting errors, try methods, error message best practices.

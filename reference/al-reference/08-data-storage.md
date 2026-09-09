<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Streams & blobs, isolated storage, Azure Blob Storage

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 13. Streams & Blobs

```al
var
    TempBlob: Codeunit "Temp Blob";
    ReadStream: InStream;
    WriteStream: OutStream;

// Buffer data into TempBlob
TempBlob.CreateOutStream(WriteStream);
CopyStream(WriteStream, SourceInStream);

// Read back from TempBlob
TempBlob.CreateInStream(ReadStream);

// Read a BLOB table field into a stream (CalcFields required first)
Rec.CalcFields("Document Content");
Rec."Document Content".CreateInStream(ReadStream);

// Write a stream into a BLOB table field
Rec."Document Content".CreateOutStream(WriteStream);
CopyStream(WriteStream, SourceInStream);
Rec.Modify(true);

// Check if BLOB field has data
Rec.CalcFields("Document Content");
if Rec."Document Content".HasValue() then
    // process
```

**Embedded resources (ship files inside the `.app`).** Declare a resource **root folder** in app.json;
reference a resource by its full name = path from the root + filename. Multiple root folders allowed
but the resource name must be **unique across the whole extension**.

```json
"resourceFolders": [ "res" ]     // app.json — without this the file is NOT packaged
```
With root `res` holding `encoding.txt`, the resource name is **`'encoding.txt'`** — the root
folder is NOT part of the name. Get it wrong (or omit `resourceFolders`) and the file is
silently missing from the `.app`; the failure only shows at runtime as
*"A resource matching '…' could not be found in app '…'"*. Runtime-verified BC27.
```al
// Read directly (2025w1) — no stream handling. ⚠ default text encoding is MS-DOS — pass encoding.
Txt  := NavApp.GetResourceAsText('config/app.json', TextEncoding::UTF8);
JObj := NavApp.GetResourceAsJson('config/app.json', TextEncoding::UTF8);
// Stream form (also NavApp.GetResource(name, stream) — 2024w2)
NavApp.GetResource('images/logo.png', InStr);
// List with glob pattern matching (2025w1)
NavApp.ListResources('data/*.txt', ResourceList);
```
Limits (2025w1): single resource **16 MB**, all resources **250 MB**, resource name **250 chars**, max
**256** resources/app. Resources are **read-only** and accessible **only from the owning extension**
(share by exposing a stream in code). Cloud uploads are malware-scanned; the target server is the final
arbiter of allowed extensions.

---

## 14. Isolated Storage (Secrets)

```al
// In the setup table — store Shared Key securely
var
    StorageKeyTok: Label 'PTEAZKey_', Locked = true;  // Locked = true prevents translation

procedure SetSharedAccessKey(KeyValue: SecretText)
begin
    IsolatedStorage.Set(StorageKeyTok + Rec.Code, KeyValue, DataScope::Module);
end;

[NonDebuggable]
procedure GetSharedAccessKey(): SecretText
var
    ReturnValue: SecretText;
begin
    if IsolatedStorage.Contains(StorageKeyTok + Rec.Code, DataScope::Module) then
        IsolatedStorage.Get(StorageKeyTok + Rec.Code, DataScope::Module, ReturnValue);
    exit(ReturnValue);
end;

procedure HasSharedAccessKey(): Boolean
begin
    exit(IsolatedStorage.Contains(StorageKeyTok + Rec.Code, DataScope::Module));
end;
```

Rules:
- `DataScope::Module` — key visible only to this extension
- `Locked = true` on label tokens — prevents xliff translation
- `[NonDebuggable]` on any method that reads the secret
- Key prefix + record Code = unique per setup record

⚠ **Scope must be identical across every `Set`/`Get`/`Contains`/`Delete` for a key.** A `Get`/`Contains` without an explicit `DataScope` defaults to `DataScope::Module`; if the value was written with `DataScope::Company`, the read silently returns not-found (setup fields show blank after republish) even though the data exists. Pick one scope per key and use it in every call.

---

## 15. Azure Blob Storage (ABS)

### app.json dependency

```json
{
    "id": "<guid>",
    "name": "System Application",
    "publisher": "Microsoft",
    "version": "28.0.0.0"
}
```
> `id` is the public **System Application** app GUID (a fixed Microsoft value) — take it verbatim
> from the symbol package's `app.json` or [BCApps](https://github.com/microsoft/BCApps); the ABS
> `"ABS Blob Client"` etc. live in that module.

### Init + auth

```al
var
    ABSBlobClient: Codeunit "ABS Blob Client";
    SSAuthorization: Codeunit "Storage Service Authorization";
    Authorize: Interface "Storage Service Authorization";

procedure InitialiseContainer(Setup: Record PTEDocumentLinkAZSetup)
begin
    Authorize := SSAuthorization.CreateSharedKey(Setup.GetSharedAccessKey());
    ABSBlobClient.Initialize(Setup.StorageAccount, Setup.ContainerName, Authorize);
end;
```

### Upload

```al
var
    ABSOptionalParams: Codeunit "ABS Optional Parameters";
    ABSOperationResponse: Codeunit "ABS Operation Response";

ABSOperationResponse := ABSBlobClient.PutBlobBlockBlobStream(BlobName, DataStream, ABSOptionalParams);
if not ABSOperationResponse.IsSuccessful() then
    Error(ABSOperationResponse.GetError());
```

### Download

```al
ABSOperationResponse := ABSBlobClient.GetBlobAsStream(BlobName, DataStream, ABSOptionalParams);
if not ABSOperationResponse.IsSuccessful() then
    Error(ABSOperationResponse.GetError());
```

### Delete

```al
ABSOperationResponse := ABSBlobClient.DeleteBlob(BlobName, ABSOptionalParams);
if not ABSOperationResponse.IsSuccessful() then
    Error(ABSOperationResponse.GetError());
```

### Blob naming label

```al
var
    BlobNameLbl: Label '%1/%2/%3/%4.%5', Comment = '%1=SetupCode, %2=TableCaption, %3=RecordKey, %4=FileName, %5=Extension';

BlobName := StrSubstNo(BlobNameLbl, Setup.Code, Rec.TableCaption, Format(Rec.SystemId), FileNameNoExt, FileExt);
// Example result: DOCLINK/Document Link/{guid}/Invoice_123.pdf
```

---

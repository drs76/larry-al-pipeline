---
bc-version: [all]
domain: error-handling
keywords: [tryfunction, return-type, boolean, AL0244]
technologies: [al]
countries: [w1]
application-area: [all]
---

# A `[TryFunction]` takes no explicit return type

## Description

A procedure marked `[TryFunction]` returns an implicit `Boolean` (true on success,
false if it errored). Declaring any explicit return type raises `AL0244`. Wrap the real
work and expose the result via `var` parameters.

## Best Practice

```al
[TryFunction]
local procedure TryPutBlob(BlobName: Text; var Source: InStream)
begin
    // may Error(); caller gets false
end;
```

## Anti Pattern

```al
[TryFunction]
local procedure TryPutBlob(BlobName: Text): Boolean   // ✗ AL0244 — no return type allowed
begin
end;
```

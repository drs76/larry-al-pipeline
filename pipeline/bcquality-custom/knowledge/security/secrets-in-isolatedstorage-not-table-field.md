---
bc-version: [all]
domain: security
keywords: [secret, isolatedstorage, secrettext, nondebuggable, credentials, table-field]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Secrets live in IsolatedStorage as SecretText — never as a table field

## Description

Credentials (shared access keys, API keys, connection secrets) must be stored in
`IsolatedStorage` with `DataScope::Module` and moved as `SecretText`, with the accessor
procedures marked `[NonDebuggable]`. Storing a secret in a table field exposes it via
the database, RapidStart, pages, and telemetry, and cannot be a `SecretText` type.

## Best Practice

```al
[NonDebuggable]
procedure SetSharedAccessKey(Key: SecretText)
begin
    IsolatedStorage.Set(KeyTok + Rec."Code", Key, DataScope::Module);
end;
```

## Anti Pattern

```al
field(10; SharedAccessKey; Text[250]) { }   // ✗ secret in a table field — exposed and unencrypted
```

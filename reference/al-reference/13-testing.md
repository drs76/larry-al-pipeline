<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# AL test codeunits

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 32. Testing (AL test codeunits)

Test codeunit = `codeunit` with `Subtype = Test`; test methods carry `[Test]`; UI/handler procedures
are wired with `[HandlerFunctions('Name,Name2')]`.

**Mock outbound HTTP without a live service (2025w1).** Decorate a handler with `[HttpClientHandler]`
and attach it via `[HandlerFunctions]`. The handler's **Boolean return decides mock vs real**:
`exit(true)` issues the ORIGINAL request to the real endpoint; `exit(false)` returns your mocked
response.
```al
[Test]
[HandlerFunctions('MyHttpHandler')]
procedure TestCallsService()
begin
    // ... exercise code that makes HTTP calls ...
end;

[HttpClientHandler]
procedure MyHttpHandler(Request: TestHttpRequestMessage; var Response: TestHttpResponseMessage): Boolean
begin
    // branch on the request — ONE handler services every call in the test (e.g. GET and DELETE)
    if Request.HasSecretUri then
        exit(true);                       // ⚠ SecretText URI hides path/query — let it through or handle blind
    Response.HttpStatusCode := 200;
    Response.ReasonPhrase := 'OK';
    Response.Content.WriteFrom('{"ok":true}');
    exit(false);                          // use the mock
end;
```
GOTCHAs: an **empty handler still blocks** the call and returns a mock (default return is `false`) —
you must `exit(true)` to let a request through; when attached, **all** HTTP calls in the test route to
the single handler; can't set cookies or redirection status codes in the mock. Gate CI with the test
codeunit property `TestHttpRequestPolicy` (allow-all / allow-only-handled / **block** all unhandled
outbound) so automated runs never hit real endpoints.

```al
// Test-only: accept self-signed / local-service certs. NEVER in production.
HttpClient.UseServerCertificateValidation := false;
```

**VS Code test running** does NOT use AL Test Runners → no AI/data-driven suites and test-runner
setup/teardown events may not fire; isolation comes from the codeunit's **`TestIsolation`** property
(defaults to codeunit level). See AL-KNOWLEDGE §3 for the Testing Explorer / Page Scripting workflow.

---

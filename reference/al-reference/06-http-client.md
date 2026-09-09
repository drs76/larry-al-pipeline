<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# HttpClient, RestClient, mocking, JSON/YAML test utils

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 10. Record Operations & Performance

### HTTP client mocking in tests (TestHttpClientHandler)

- New test feature: intercept HTTP requests sent through any HttpClient and mock the response — entirely within AL, no external mock service / rerouting.
- Handler procedure signature: takes a **TestHttpRequestMessage** and **TestHttpResponseMessage** [sic? verify type names], decorated with `[HttpClientHandler]` attribute [sic?].
- Register on the test method via `[HandlerFunctions('MyHandler')]`, same as other handler funcs.
- Request object exposes request type (GET/POST), path, and query parameters — dispatch on these to mock multiple endpoints in one handler.
- Populate response: set body content, `HttpStatusCode` (e.g. 400/404), and reason phrase to simulate errors.
- Independent of the RestClient codeunit — the handler works at the platform level with no test-package dependency; mocking RestClient interfaces is an alternative choice, not required.

<!-- ingested: Http Communication Best Practices | 2026-07-26 -->
### HTTP client — outbound calls, headers, RestClient (mibuso 2024-06)

**Default call pattern & error checks**
- `Get`/`Post`/`Put`/`Send` return a `Boolean` = "did a response come back at all", NOT "was it successful". `false` = DNS failure, no server, firewall block, host down, etc. Always test it.
- On `false`, also check `HttpResponseMessage.IsBlockedByEnvironment` [sic? verify property name] — even though no response content/headers exist, this Boolean is populated. If it's the cause, raise a specific error telling the user the app is blocked.
- On success, test `HttpResponseMessage.IsSuccessStatusCode` (200-range = success: 200 OK, 201 Created, 204 No Content). For a specific expected code, test `HttpStatusCode` directly. On failure show status code + reason phrase.
- Read body via `Content` property (`HttpContent`): `ReadAs(text)` or `ReadAs(instream)` for binary.

**Blocked-by-environment mechanism (sandboxes only)**
- Sandboxes copied from production have all apps switched OFF for outbound HTTP, to prevent copies from hitting real production endpoints.
- Controlled by a record in table `NAV App Setting` [sic? auto-caption garbles it — verify exact table name/id on Learn], field `Allow HttpClient Requests` [sic? verify]. Effectively the only field.
- No record → user is prompted Allow/Block, Once/Always. "Once" options create NO record (re-prompt next time). "Always" options create the record with the field true/false; thereafter no prompt.
- Gotcha: opening the record from Extension Management page auto-creates it (defaulting to blocked) → no more prompt, just silent block until you set the field true there.
- Copying prod→sandbox clears the table. You may create the record yourself in install code to self-allow.

**Send vs Get/Post/Put**
- `Get`/`Post`/`Put` are convenience wrappers around `Send`. Internally they build an `HttpRequestMessage` and call `Send`. Serious integrations usually use `Send` directly (needed to set request-level headers).

**Headers — three levels**
1. `HttpClient.DefaultRequestHeaders` (an `HttpHeaders`) → `.Add(name, value)`. Applied to EVERY request from that client instance. Use for static values (user agent, basic auth).
2. Request message: `HttpRequestMessage.GetHeaders(headers)` — returns headers as a **var/byref** param plus a Boolean (awkward API; no direct `.Headers.Add`). Applied to that one request only; client combines these with default headers.
3. `HttpContent` headers — for content headers only (see below).
- Some headers allow multiple values (e.g. Accept-Language), some only one (Content-Type). Adding a 2nd value to a single-value header → error "cannot add the value because content-type does not support multiple values". Adding same-name twice on a multi-value header yields one header with comma-joined values.
- Use `SecretText` for authorization/token values (hides from debugger). Note: request wire content is still plaintext — always use HTTPS.
- SecretText header quirks: `HttpHeaders.Keys` returns key names (text). `GetValues(name)` returns `List of [Text]`; if the value was secret it errors — use `GetSecretValues`. No "get secret keys" function; use `Contains` / a `ContainsSecret`-style check. Response headers are ALWAYS plain text.

**Content-Type / HttpContent gotcha**
- Behind the scenes `HttpContent` wraps .NET's abstract `HttpContent`; AL instantiates it as a `StringContent`, which defaults Content-Type to `text/plain` even before you write anything.
- Each `WriteFrom(text)` / `WriteFrom(secrettext)` / `WriteFrom(instream)` creates a fresh string content and RESETS Content-Type back to `text/plain`.
- Therefore: **write content FIRST, then set Content-Type.** And because Content-Type already exists (single-value), you must `Remove` it before `Add`. Correct order: `WriteFrom(...)`; `GetHeaders(contentHeaders)`; `contentHeaders.Remove('Content-Type')`; `contentHeaders.Add('Content-Type','application/json')`.
- Content-Type can ONLY be set on `HttpContent`, never on `HttpClient`/request — else "misused header name".
- Header object is a .NET reference type: after `GetHeaders` and mutating it, no set-back/push needed.

**Performance / lifetime**
- Instantiating a new `HttpClient` (local var) is ~90% slower than reusing a global instance — but only measurable at ~10,000 calls; the network round-trip dominates, so it rarely matters per-request.
- .NET HttpClient is designed long-lived; the expensive internal `HttpMessageHandler` holds a connection pool. In raw .NET, new-client-per-request causes port exhaustion (ports stay open ~4 min per TCP spec; ~65k outbound ports total). BC handles this for you via an internal HttpClientFactory + delegating handler that pools the message handler — AL devs don't hit port exhaustion.
- Recommended pattern: for occasional calls a fresh client is fine; for loops/sync, use a codeunit with a **global** `HttpClient`, an `Initialize` fn that sets default headers once, and multiple send calls. Avoid SingleInstance codeunit — its cached client never picks up DNS changes (no `PooledConnectionLifetime` control in AL) until the user logs out/in.

**Redirects / cookies**
- Location header (with 301/302) is auto-followed by AL HttpClient; cannot be disabled in AL (unlike .NET). BC bound-action responses may return a Location header pointing to the created/updated record.

**RestClient module (System Application, since v23)**
- Wraps HttpClient + all HTTP objects; one-line calls with success/blocked checks handled internally.
- Examples: `RestClient.Get(url)` → `HttpContent` codeunit → `.GetContentAsText()`; `RestClient.Post(...)`; `HttpContent.Create(text, 'application/json')`; `GetContentAsJson()` → JsonToken → `.AsObject()`; `RestClient.PostAsJson(url, jsonobject)` returns JsonToken (auto sets application/json, no manual content-type); `GetContentAsBlob()` → TempBlob codeunit; post a TempBlob for binary/PDF.
- Objects: RestClient, HttpRequestMessage, HttpResponseMessage, HttpContent, a Method enum, an HttpClientHandler interface, and authentication interfaces (basic, OAuth2 client-credentials).
- **Permissions/telemetry gotcha:** RestClient lives in System Application, so out-of-the-box the *System Application* makes the call → the block prompt names "System Application", granting it opens outbound HTTP for ALL apps using RestClient, and telemetry goes to Microsoft not your AppInsights.
- **Fix:** implement the `HttpClientHandler` interface in YOUR app. Its single `Send` procedure receives the client, request, response and just does `HttpClient.Send(request, response)`. Initialize RestClient with your handler → the call is attributed to your app (correct prompt + telemetry).
- Same handler enables test mocking: a test handler implementation skips the real send and instead sets status code, reason phrase, response JSON, and returns success — lets you fake positive/negative (404, invalid body) responses to test your integration code without a live server.
- RestClient works on-premise too. Current limitation: no cookie support (must fall back to raw HttpClient for cookies).

### JSON/YAML test utilities

- New JSON utility methods to build/replace properties on a JsonObject from templates.
- **YAML support** — JsonObject can read from a YAML multi-line string (parses YAML into JSON). Verify method name `[sic?]`.
- **`WriteWithSecretsTo` [sic?]** — embeds a `SecretText` value into a JSON object, producing a new `SecretText` for the whole payload so the secret (e.g. token) is never exposed in debug/logs. Verify exact name against compiler.

### Directory.AppProps.json + dotnet build tool (preview)

- **`Directory.AppProps.json`** [sic? verify exact filename] — MSBuild `Directory.Build.props`-style shared file at repo root; supplies common values across many app.json files (monorepo). Defines variables (e.g. `major`/`minor`/`build`/`revision` combined into `version`).
- Reference a variable in app.json via `$(version)` token syntax. If a property is present in app.json it wins; if absent, taken from the props file's `properties` section (e.g. shared `publisher`, base URL). Can also inject `preprocessorSymbols`/configuration; empty resolved strings are dropped.
- **dotnet tool**: `dotnet tool install Microsoft.Dynamics.BusinessCentral.Development.Tools --interactive --global --prerelease` [sic? verify package id] — gives an `al` CLI (`al compile --project ...`) that resolves the same props file, usable in pipelines and alongside VS Code. Cross-platform (Linux/macOS/Windows).
- Extra commands: `al GetPackageManifest` [sic?] prints the resolved manifest from a built .app (shows merged publisher/privacy/URLs). The tool replaces app.json values before compile, so at compile time everything is resolved as if inline.
- Preview only — don't use props file in production pipelines yet; format may change.

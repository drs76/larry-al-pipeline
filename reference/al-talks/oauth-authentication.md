# oauth-authentication

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2022 - OAuth revealed | 2026-07-27 -->
### OAuth for Business Central (TechDays 2022, Arend-Jan Kauffmann)

- OAuth = authorization framework: lets a third-party app get *limited* access to an HTTP service. Two directions: external app → BC API, or AL code → external (SharePoint, Graph mail, OneDrive).
- Not secure by default; only as secure as correctly applied. Access tokens are not encrypted secrets — decode-only — so leaked tokens = full access until expiry.

**Four roles**
- Resource server — BC, exposes data via HTTP APIs.
- Client application — external third-party app wanting access (not the BC web client).
- Resource owner — the BC user granting access.
- Authorization server — Azure AD (Entra ID), issues tokens.

**App registration vs service principal**
- App registration = the *definition* (name, publisher, redirect URIs, secrets, required API permissions, exposed APIs). Lives only in its home directory.
- Service principal (Azure portal menu: **Enterprise applications**) = an *instance* of the app registration. Analogy: app registration is the codeunit source, service principal is the loaded instance. Granted permissions live on the service principal, not the app registration.
- Home-directory service principal is auto-created with the app registration (portal makes 2 Graph calls; via Graph API you make both yourself).
- Single-tenant: everything stays in home directory. Multi-tenant: app registration stays home, but service principals get created in *other* directories the first time a user/admin consents there. Multi-tenant requires a verified publisher.
- BC itself is a multi-tenant app registration in Microsoft's directory exposing APIs; consenting to it creates BC's service principal in the customer directory.

**Permissions: scopes vs roles**
- Scope (a.k.a. **delegated permission** in portal UI) = app acts *on behalf of a signed-in user*. Requires matching BC user account for that user.
- Application role (**application permission** in portal) = app acts as *itself* (own app account, no user). Requires an application-type account in BC. Only an admin can grant (like creating a new user account).
- Scope/role names are URIs: prefix identifies the app registration, suffix is the permission. Examples: `api://.../user_impersonation` [sic? verify exact BC scope string], Graph `Mail.Read`, `Mail.ReadWrite`, `Mail.Send`. BC exposes `user_impersonation` (scope) and `api.readwrite.all` [sic? verify casing/name] (app role).
- Static permissions = declared upfront on app registration (required for client-credentials/application permissions). Dynamic permissions = requested at authorize-time in the scope param, not pre-declared (allowed for delegated).

**Consent flows**
- User consent = one user grants for own account. Admin consent = admin grants for whole org (tick "consent on behalf of your organization"); individual users then not prompted. Application-role grants require admin consent always.

**Access token (JWT)**
- JSON Web Token, base64url-encoded (URL-safe, `=` padding stripped), 3 dot-separated parts: header.payload.signature. Payload is plain JSON — decode at jwt.io/jwt.ms. Not secret.
- Signed with private key of a cert; receiver verifies with public key → tamper-proof. Can decode *and* sign JWTs in AL code.
- Contains: audience (target resource, e.g. BC API), user, tenant id, scope/role, issue + expiry time. Tenant id is in the token, so not needed in the API URL.
- Lifetime ~60 min (sometimes 70–75). Refresh token valid 90 days, and using it issues a new 90-day refresh token — rolling window. But tenant policies requiring periodic interactive login (e.g. every 2 weeks) break refresh-token background use.

**Authorization Code grant flow** (delegated / on-behalf-of user, interactive)
- Two Azure endpoints under `login.microsoftonline.com/<tenant>/oauth2/v2.0/`: `/authorize` (browser, interactive) and `/token` (backend API call).
- Step 1: open `/authorize` in browser with client_id, `response_type=code`, redirect_uri, scope. User logs in + consents (first time only).
- Step 2: Azure redirects to redirect_uri with `?code=...&session_state=...`. Auth code valid **10 minutes**. session_state usable only for single sign-out, not sign-in.
- Step 3: app POSTs to `/token` (content-type `application/x-www-form-urlencoded`) with `grant_type=authorization_code`, code, client_id, redirect_uri (must match the one that produced the code), scope, client_secret → gets access token.
- Multi-tenant / unknown user: use `organizations` (not a domain, not `common`) as tenant segment; `common` also allows personal accounts (unsupported).

**Client Credentials flow** (service-to-service, app account, no user)
- Single POST to `/token`: `grant_type=client_credentials`, client_id, client_secret, scope, and *must* use the specific tenant domain (not `common`/`organizations`). Returns access token directly.
- Requires app-role (application) permission declared statically + admin consent, AND an application-type user record in BC linked to the app registration's client id (else "invalid credentials").

**Device code flow** — for devices without their own browser (e.g. VS Code publishing to BC sandbox: shows a code to paste in browser).

**Public vs confidential clients / redirect URI**
- Redirect URI registered under a *platform* type; type decides whether a secret is needed.
- Web platform = confidential client (runs on server, can keep a secret; auth code travels browser→server→token endpoint, so secret defends against interception attack). Secret required.
- SPA / mobile / desktop = public client, cannot keep a secret (don't store secrets on desktop — even Teams got caught storing tokens as cleartext). Desktop apps open their own browser window so the auth code never leaves the app — no secret needed.
- `localhost` is the only non-HTTPS redirect URI allowed; all others must be HTTPS. One app can have multiple redirect URIs.

**Secrets vs certificates**
- Portal "secret" = a password (Graph API `addPassword`). Max lifetime 24 months. Never store in code; recommended only for dev/test.
- Prefer certificates: sign request with private key, key never travels the network. Supported in .NET and callable from AL.
- Note: client-credentials still sends the secret in the request body — same exposure concern as basic auth's header; cert-based auth is what actually improves on basic auth.

**C# / AL notes**
- For OAuth in C#, use NuGet `Microsoft.Identity.Client` (MSAL): build public/confidential client with client id + secret, call `AcquireTokenInteractive` or `AcquireTokenForClient` [sic? verify method names].
- AL can create the app registration + self-signed cert via Graph API entirely in code, avoiding asking the user for a foreign client id/secret.

**Practices (Q&A)**
- Distributed app across multiple customers: use a *separate* app registration per customer directory so one leaked secret doesn't expose all. Single shared registration only when you fully own/host the code.
- Multiple internal apps (e.g. several Azure Functions) needing identical permissions can share one registration.
- Token buffering: keep token in memory up to ~60 min; Azure doesn't mind frequent token requests and prefers that over persisting tokens where they can leak. Avoid storing tokens in setup-table fields.

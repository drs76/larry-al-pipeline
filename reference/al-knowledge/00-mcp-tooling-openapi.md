<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# mcp-tooling-openapi

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

<!-- ingested: From OpenAPI to Copilot: Auto-Generating MCP Tools for VS Co | 2026-08-19 -->
### Generating MCP / Copilot tools from an OpenAPI spec

Source: BC TechDays session (Lippert / Fenster), Aug 2026. Not BC-specific, but relevant to BC tooling that fronts a REST backend.

**Two ways to expose tools to VS Code Copilot**
- Standalone MCP server (local or remote) — protocol-standard, usable by any MCP client (VS Code, other editors, agents).
- VS Code extension using the **Language Model Tool API** — tools live inside the extension, not an MCP server. TypeScript, registered via the VS Code extension API. Tighter integration, distribution is free (install extension = get tools), but only works in VS Code.
- End user sees no difference in the chat tool picker; the icon differs (extension vs MCP server).

**MCP tool shape (protocol)**
- Tool listing returns name, title, description, and a JSON input schema with required params.
- Tool call = JSON request with tool name + arguments; response is JSON content. Structurally the same as a REST call — which is why OpenAPI → MCP generation works mechanically.
- Spec also covers resources, sampling, elicitation — tools are only one part.

**Pipeline demoed: OpenAPI → TypeScript client → tools**
1. ASP.NET Core web API. Recent `dotnet new` templates already emit an OpenAPI doc and map it to a route; add Swagger UI package only for the graphical view.
2. Enable `GenerateDocumentationFile` in the csproj so XML doc comments on controller actions/params flow into the OpenAPI descriptions (suppress the missing-comment warning).
3. Scaffold VS Code extension with the Yeoman generator. Entry point `extension.ts` (`activate`), metadata + contributions in `package.json`.
4. Install `openapi-generator-cli` [sic? exact npm package name — verify] and add `openapitools.json` with two generator configs: one emitting a TypeScript client (fetch or axios flavour), one emitting the language-model tools into a separate output dir using a **custom template directory**.
5. Custom templates are **Mustache** — loop over the spec's operations and emit one `registerTool` call per operation, instantiating the generated API class and returning the response to Copilot.
6. Language model tools must also be declared in `package.json` (name, description, input schema) to be visible. Demo used a companion script that reads the spec and writes those entries, wired up as an npm script so regeneration is one command.
7. On API change: rerun the npm script → client + tools + package.json entries all refresh in seconds.

**Practice notes**
- Not every endpoint should become a tool. Keep an exclusion list — destructive endpoints (deletes, bulk imports) stay out unless guarded.
- Description quality in the OpenAPI spec directly determines tool-selection accuracy. Invest in operation and parameter descriptions; document error/response codes so the agent can self-troubleshoot.
- For third-party APIs you don't control, add an intermediate enrichment step (or author the spec yourself) before generating.
- Auth belongs in the generated client, never in chat — no secrets passed as tool arguments.
- Naive generation = 1 endpoint → 1 tool. Combining several endpoints into one tool means hand-written logic and gives up full auto-generation.

**Too many tools**
- Many extensions each contributing tools → context-window pollution and worse tool selection. Less severe with large-context models, still a token cost.
- MCP servers mitigate with dynamic tool discovery (a meta/search endpoint). VS Code's Language Model Tool API has **virtual tool clustering** [sic? feature name — verify in VS Code docs] which groups similar tools and pre-selects likely ones.
- No sensible fixed tool-count limit; risk depends on how *similar* tools are, not how many.

**MCP apps (rich UI in chat)**
- Default MCP tool output is text — poor for graphs, dashboards, tabular analysis.
- MCP apps let a tool return an HTML interface rendered inline in Copilot chat, with two-way communication back to the backend (clickable, not a static image).
- C# has an MCP SDK NuGet package for building MCP servers. MCP app support was still an open PR as of Aug 2026, but existing SDK methods suffice.
- Server setup: `AddMcpServer` [sic? exact method name — verify], declare the extra `ui` capability, HTTP transport.
- Tools are declared like controllers: a class whose methods carry an `[McpServerTool]` [sic?] attribute with description text on method and parameters.
- An MCP-app tool returns normal content **plus structured JSON content**; the HTML resource's JavaScript consumes that JSON to render.
- The HTML is registered as an **MCP server resource** at a URI; requesting that URI returns the dashboard page.

**Legacy APIs**
- Generation needs a machine-readable contract. SOAP/WSDL is arguably better described than REST, so generation is theoretically possible — no known off-the-shelf generator was named.

### MCP / agent security

- Threat model for locally-run MCP servers and agent tools: arbitrary code execution on the dev machine, filesystem destruction, credential exfiltration. `npx some-mcp-from-a-blog-post` is the modern "download and run an exe".
- Real incidents cited: an agent recursively deleting a user's home directory (Claude Code bug report, Oct 2025); an agent dropping a production database despite an explicit freeze instruction.
- **Permission bleed:** an agent inherits whatever the user has. Changing your Azure CLI subscription (`az account set`) on the host silently gives an already-running agent session production access. Same class of problem as over-permissioned humans.
- **Docker sandboxes** (micro-VMs for coding agents) as mitigation. Own filesystem, network, env, processes, optional Docker daemon.
  - Only the folder you explicitly share is visible; rest of the host filesystem is unreachable. Reference material can be mounted read-only.
  - Separate credential store — host `az login` / selected subscription do **not** leak in. Agent works in exactly the subscription you set inside the sandbox.
  - Outbound network denied by default; a preconfigured allowlist covers common dev hosts (GitHub, Azure, AWS). Blocked and allowed calls are visible in the sandbox log — usable as an audit of what your MCP servers actually contact.
  - **Credential injection:** a sandbox "kit" declares service domains plus a header template; the proxy strips the placeholder token the MCP server holds and injects the real secret on outbound calls to those domains. The MCP server never sees the real credential, so a malicious server can't exfiltrate it. Secret supplied on the host as a sandbox secret.
  - Kits are declarative (name, description, allowed network domains, service domains + injected headers, install steps) and compose: `sandbox run copilot` with an AL kit, Azure CLI kit, Azure DevOps kit. AL kit installs .NET then `dotnet tool install` of the BC development tools (which include the AL MCP server) — scoped to the sandbox, not machine-global.
- **PAT risk:** long-lived, over-scoped personal access tokens handed to an MCP server are the easiest exfiltration target. Microsoft's own Azure DevOps and GitHub MCP docs show env-var PAT auth for CI/automation, so a lookalike "PAT-auth" MCP server on a public repo is a plausible credential-harvesting vector.
- **Data-privacy question (payroll-type scenarios):** the correct answer is OAuth/SSO so the MCP server inherits the *user's* permissions, not a shared service key. There is no reliable content-level gate stopping an MCP from returning PII — prompt instructions can be talked around. Control the tool surface and token scopes instead.
- **Load/DoS:** an MCP is no more dangerous than the REST API behind it in kind, but far faster — an agent can issue thousands of writes a minute where a human could not. Rate/throughput considerations are a real design input.

<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Coding agents in AL, agent testing, BC MCP server

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 29. Coding Agents in AL (AI development toolkit)

The AL API for building/deploying custom agents as extensions. Get the latest AL VS Code
extension → **New Project → `agent` template** (working sample + README). Source:
Microsoft dev session `reference/transcripts/coding-bc-agents-al-devkit.md`. Verify signatures
against the platform (§18) — the API is new and evolving.

**Agent type = the blueprint** (defines identity + default settings). Three parts:
1. **Enum extension on the Agent Metadata Provider enum** — a new value; the agent's main identifier. Its implementation ties the type to your interface implementations.
2. **Copilot Capability enum extension** — a unique name + caption; acts as the on/off feature switch users see.
3. **Interface implementations** (below) — behaviour.

**The three agent interfaces:**
- **Agent Factory** — *default* (create-time) settings: first-time-setup page, binds the Copilot capability, default profile, default permissions.
- **Agent Metadata** — *runtime* settings that can change over an agent's life: summary page, override the message-review page, agent initials, etc.
- **Task Execution** — behaviour during message processing: input/output message **validation**, the **user-intervention suggestions** shown, and context-specific settings. Methods carry an **agent user ID** so behaviour can differ per instance.
  - Message validation use-cases: relevance-check/discard unrelated input messages; add warnings to inputs; post-process outputs (e.g. append an email signature); switch context (e.g. currency) by page ID.

**Types vs instances.** A type is the blueprint; **instances are actual BC users** (each has its
own permissions, profile, user settings, instructions). Interface methods take the agent user ID
so you can branch per instance.

**Setup page.** New page type **`ConfigurationDialog`** — purpose-built for agent setup. Left =
the standard **agent setup part** (name, on/off toggle, AI-usage disclaimers); right = your custom
settings. To back it:
- Make a **tracking table** whose **primary key is the user security ID** (same key agents use); hold your custom settings there.
- The page works against a **temporary record** — only persist on OK/accept.
- The setup part exposes a **setup buffer** record (ID, active, …); the **Agent Setup codeunit** auto-creates the agent when you save, and you set the agent's **instructions** on it.

**Creating agents programmatically** — alternative to the setup page (tie to an action/workflow;
must run in a user session). Use the **Agent codeunit** — also the place to change config
dynamically: display name, profile, permissions, etc.

**Instructions** can be (re)loaded any time, but the common pattern is to load at agent creation
**from a resource** (`.txt` in the app) so they're easy to store/display.

**KPI pages** — any Card Part page assigned as the agent's KPI page shows metrics on avatar hover
(same wiring style as the setup page).

**Tasks vs messages** (assigning work):
- **Task** = a unit of work bound to one agent instance; has a title; triggers processing. Build with the **Agent Task (builder)** codeunit.
- **Message** = bound to a task. **Input** messages give context beyond instructions (instructions say *process invoices*; message says *which* invoice). Agent replies with **output** messages. Multi-turn: add more input messages to continue.
- Flow: get the instance (from your setup table) → **Task Builder** → create a message → build → `Create` → task waits for user approval, then executes.
- **Attachments** (PDFs → text-extracted): via the **Message Builder** (`AddAttachment`) before creating the task.
- **External ID** field/method on messages — tie a message to an email thread etc. so you can find and continue it.

**Triggering tasks** — embed task creation anywhere in AL: a page-extension action (e.g. add to
Sales Order list), an event subscriber, a process. Manage running tasks via the **Agent Task
codeunit** (stop/restart).

**Getting results** — two ways:
- **Poll** the **Agent Task** record's `Status` field (completed/stopped/…) then query BC for the result. Fine for unit tests / non-production.
- **Agent-session-gated events**: fire code only when running inside an agent session. Use the **Agent Session codeunit** `IsAgentSession` (optionally check the user ID for a specific instance) so a subscriber runs after the agent acts in the UI.

**Exposing an agent to other apps.** By default the AL agent API only touches agents defined in
*your own* app (security isolation). To let another app drive yours, add a **public codeunit with
public functions** (e.g. a `MyAgent Public API` codeunit exposing `Deactivate`) — those become the
sanctioned cross-app surface.

### Troubleshooting agents

Source: `reference/transcripts/bc-agent-troubleshooting.md`. An agent's decision at each step is a
function of five inputs: **instructions** (the blueprint), **available tools** (context-specific,
e.g. what's callable on the current page), the **virtual UI** (how the agent "sees" BC), **task
messages** (which record to act on), and **step history**. When it's stuck, one of those is wrong.

From **Agent Tasks page → View Log Entries** you get every step (assistance requests flagged).
**View Details** on a step opens the full decision context:
- **Decision** — what it chose + details (e.g. the assistance-request text).
- **What the agent saw** — a textual dump of the page: page ID/name, page type, editable flag, description, and every element (actions + descriptions, **fields**). Browser-search it to confirm whether a field is even present/editable.
- **What tools the agent had access to** — its capabilities at that point (helps calibrate instructions).
- **What data the agent memorized** — current memory (e.g. the order total it kept to judge risk).
- **What messages the agent had access to** — everything visible to it so far.
- Fact boxes: **Page stack** (which pages were open — the agent opens/closes pages to navigate; e.g. Role-Centre → Sales Order Card) and **settings** (currency/formatting used for output messages — check here when the final message is wrong).

**Most common root cause is an AL mistake, not the LLM.** In the demo the agent couldn't find a
`risk` field: "What the agent saw" showed the field absent → it was **never added to the profile /
PTE**, and a `reason` field was present but **not editable**. Debugging flow: reproduce → *What the
agent saw* → is the field there and editable? → if not, fix the **profile/permission set (§26)** or
page, not the instructions. If the field is present, then it's an instruction/context problem.
- Best permission-troubleshooting tool is the **Agent Log Entries** (pages navigated, actions invoked, errors like a missing permission on a custom table). To change an agent's permissions you must **disable it first**, then re-enable.

### How the runtime works (mental model)

Source: *Under the Hood* eps 13–14 (`reference/transcripts/under-the-hood-*.md`). Useful for
predicting agent behaviour; none of it is partner-controllable.
- The agent drives BC through the **logical client API** [sic?] — the same JSON page/field/action layer that renders the web/mobile clients. The LLM is shown a *logical* view of the current page (fields, actions, tooltips) plus a small tool set: **set a field, invoke a page action, close the current page, and a "note" scratch-memory tool**. No new UI plumbing was invented for agents.
- The loop is one big **execute-task** prompt that grows as steps accumulate; ~20 prompts total, with cheap ones (summaries, some grounding) on **mini models** and execute-task on the **full model** (currently GPT-4.1 [sic]; o1/GPT-5 gave more latency, no accuracy win).
- **Guardrails you get for free:** input-analysis prompts scan incoming messages for harmful content + **prompt-injection/jailbreak**; output checks cover language + number/date formatting + **grounding** (a separate evaluator LLM confirms generated content matches what the agent actually saw — anti-hallucination); **loop detection** nudges a stuck agent (runtime acts as the user) then escalates to human intervention; validation errors are fed back for a retry.
- **Memory is current-task only** today (visited pages + auto-remembered search results + note-tool contents); cross-task "teaching" memory is in development.

### Profiles & permissions (agent-specific)

- The agent runs as the **intersection** of the invoking user's permissions AND the agent's own permission set — never more than the user. Trim Edit/Delete you don't need.
- A tighter **profile** = less UI to reason over = higher accuracy. A profile can be blanked (properties that clear all actions / all fields / all saved views) and elements added back via **configuration** — including fields from third-party extensions, and things code exposes that the UI doesn't.

### Azure OpenAI in the AI development toolkit (Copilot/PromptDialog AL)

For your own Copilot features (not agents), the toolkit's Azure OpenAI surface changed:
- **`SetManagedResourceAuthorization`** [sic?] has a new overload that **omits the partner subscription details** (old overload obsoleted); completions via `AzureOpenAI.GenerateChatCompletion`.
- New **Azure OpenAI Policy Parameters** codeunit [sic?]: content-filter level enum (low = default, medium supported, high not) and **XPIA / prompt-shield** injection detection (tag the input, set XPIA detection = true).

### Exporting / importing agents (ALM)

- Agent **definition** exports as an **XML** file — one agent from the agent card (**Export Agent Definition**, Design submenu) or several from the agent list. Contains name, display name, permissions used, and instructions; **not** the instruction history (download that separately — see §28).
- **Import Agent Definition** → wizard → select the XML (supports multiple agents). Preview shows per-agent new-vs-replace, resulting instructions, and a **Validation Status** column (warnings/errors). Agents import **inactive** — activate after review.
- Migration gotcha: if the source **profile doesn't exist in the target**, the imported agent gets **no profile** and can't navigate the UI — fix post-import.

## 30. Testing & evaluating agents in AL

Agents are non-deterministic, so you don't write exact-match tests — you write **evaluations**
that measure accuracy/quality/safety over data-driven inputs, run deterministically against a
non-deterministic agent. Source: *Getting started with Agent testing* 1–3
(`reference/transcripts/agent-testing-*.md`). All names below are from auto-captions — verify
against Microsoft Learn / the sample app.

**Dependencies.** Take a dependency on the **AI Development Toolkit – Evaluation** app; it pulls in
the **AI Test Toolkit** (UI), the **Agent Test Library** (~27 helper methods), and the standard
test libraries.

**Three artefacts per test app:**
1. **YAML data sets** — inputs + expected output. Sections: `suite setup`, then a test with `name`/`description`/`turns` (always multi-turn syntax, even for one turn). Per turn: **turn setup** (create/simulate data in AL before the agent acts), **query** (the arriving message — from/title/body, attachments via `resources` or an AL-generated report streamed in via a named action type + free-format action data), **expected data** (which of the 3 outcomes — message-to-review / records-to-review / user-intervention — plus expected suggested-action codes and a free-format payload to check created records). **Placeholders** compute dates off the BC **work date** so nothing is hardcoded.
2. **AL test codeunits** — loop the turns and verify. ~3 lines fetch the agent from the test suite (so the same tests run against different agents/models/instructions via a picker).
3. **Suite config (XML)** — wires data sets ↔ codeunits and registers with the eval tools; an **install codeunit** loads the YAML/config resources and imports them via **AI Test Suite Management**.

**Agent Test Library keywords** (async ones suffixed `…AndWait`): `RunTurnAndWait` (mocks message
arrival — parses the query, imports attachments, handles user-intervention by reading it from input
and calling the unblock method), `FinalizeTurn` (stores the result, logs task/steps/inputs/expected/
errors, checks for a next turn), `GetExpectedData`, `WaitForTaskToComplete` [sic?] (when you invoke
the agent from AL/an action). Agent eval context via an **AI Test Context**-style codeunit exposing
`GetAgentUserSecurityId` [sic?].

**Scoring — do NOT use hard `assert`s** for output validation. Accumulate failures into an **error-
reason** text and return `true`/`false`; the text surfaces in the UI log-entry fact box with
navigation to the failing step. `FinalizeTurn` output is downloadable (serialised task/steps/inputs/
expected/errors) → upload to **Azure AI Foundry** for **LLM-as-judge**, or feed back to an agent to
improve tests/instructions.

**Gotcha — build your own master data.** The model has *memorised* the demo company (knows customer
10000 = Cannon Group, item numbers), so tests over demo data don't prove real behaviour. Create your
own customers/items in setup with the standard test libraries; set only the test-relevant fields,
default the rest; **clean up after every test**.

**Categorise & run.** P0 = fast happy-path, run often; P1 = edge cases/regressions; **load** tests =
oversized data, run sparingly; **variation** tests = same scenario, shifted context. **CI/CD:** the
**Test Runner for AL Test** PowerShell module (on the BC image at
`Applications\TestFramework\TestRunner`, token auth) points at a **sandbox** — **sandbox-only, no
on-prem/Docker images**. Shipped sample: the **Sales Validation Agent** test.

## 31. BC MCP server (exposing BC to external AI)

The Model Context Protocol server exposes BC to any MCP client (Copilot Studio, M365 Copilot chat,
VS Code, …). Two distinct servers: the **data/app MCP server** (over API pages) and the **Admin
Center MCP server** (tenant ops). Enable in BC via **Feature Management → all users** (preview).
Source: `reference/transcripts/mcp-*.md`, `bc-copilot-studio-integration.md`.

**What it exposes.** API **pages** (built-in + your custom ones), including their **bound actions/
methods** (surfaced like OData bound actions — not just CRUD). The **default** config is read-only
over *all* API pages, implemented as **3 dynamic tools**: `search` (semantic find), `describe`
(fields/types + OData filter/select syntax), `invoke`. The LLM chains them.

**28.2 update (April 2026) — supersedes earlier "not yet" notes:**
- **All Microsoft-published API *groups*** are now exposable (analytics, automation APIs, e-document,
  intercompany, subscription billing, e-invoicing, …) — no longer just API v2 **core**. New config
  action **"Add tools by API group"** bulk-adds every API in a group (each still togglable read-only
  vs modify).
- **API *queries* are now exposable** — set object type = **query**, pick the object ID (e.g. the
  Power-BI-app analytics queries: GL account category, finance, inventory); the server auto-selects
  the **highest** API version. These are the same analytics queries behind BC's Power BI apps —
  aggregation power that CRUD API pages lack. Point the agent at the analytics-API docs
  (aka.ms/bcintegration) as **knowledge** for KPI understanding.

**Authoring an MCP configuration** (the `MCP Configurations` page):
- Pick **Available tools** (which API pages) and per page set read-only vs modify/delete; a master **allow create/update/delete** toggle (off = everything read-only). Set **Active**.
- **Dynamic tool mode** — preload all tools vs on-demand `search`. **Discover additional objects** — let the client reach pages not in the list (more surface = higher error rate; consider limiting to API v2).
- **Tool count matters:** Copilot Studio caps ~**70 tools**, and each page counts **twice** (read + modify).

**AL lever — `AboutTitle`/`AboutText` on your API objects.** The tool name is derived from purpose +
object type/ID; the **description embeds the page's AboutText**, and `describe` adds field names/
types. Rich AboutText measurably improves the agent's tool choice. Suggested flow: have an LLM draft
about-text from the fields, proofread, add to metadata.

**Enhanced server (2026 RW1):** config **validations** (flags stale/uninstalled-app APIs, warns on a
missing parent API like a sales line without its header, with **Apply recommended action**);
**import/export configs as JSON** across environments; a **connection string** under Advanced;
change-auditing to **Microsoft Purview** + partner telemetry on incoming calls; **Resources** — a
tool can return an **embedded file reference** instead of inlining big data, handed to host-side
code execution (e.g. Copilot's Python interpreter) rather than running on BC; ~50 new standard APIs.

**Admin Center MCP server** (separate): over the Admin Center API, same Entra auth. Add in VS Code as
an **HTTP MCP server** by URL. Use for listing environments/updates, diagnosing failed upgrades
(reads the failure, can recommend *clear failed upgrade* / uninstall-replace PTE), copying
environments, scheduling updates. **Preview limits:** no destructive ops (delete/rename env, uninstall
apps), no security-group or linked-Power-Platform settings.

**Auth.** Authenticated like an API — the session runs under the **calling user's permissions/
entitlements** via Entra/OAuth. VS Code + Copilot Studio are pre-authorised; other hosts need an
**Entra app registration**. (A `bcmcp` proxy sample existed to bridge non-Copilot-Studio hosts; being
retired as native host auth ships.)

**Copilot Studio wiring:** add tool → **Model Context Protocol** → search "Business Central" →
"Business Central MCP server (preview)" → set **environment + company** (Configuration blank = default
read-only). Billed as Copilot Studio usage (Copilot credits); Power Platform usage rights are included
in the BC licence.

---

<!-- ingested: Microsoft Presents: MCP Server for Developers | 2026-07-29 -->
### BC MCP server — architecture & config

- **What it is**: Business Central exposes an MCP server so external LLM hosts (VS Code, Copilot Studio, Claude Code, GitHub Copilot CLI, Teams) can call BC as tools. Standard MCP primitives: tools, resources, prompts (+ elicitation). Most clients implement tools well; resources/prompts support varies.
- **Online only**: MCP server supported for BC online, not on-prem (dynamic search needs semantic vectors unavailable on-prem).
- **Remote vs local**: BC MCP is used as a *remote* MCP over HTTP — no install, just a connector. Auth via MCP protocol; authorization stays BC permissions.
- **Auth**: OAuth 2.1 compliant (per MCP spec ~Nov 2025); BC's OData/API stack updated for OAuth 2.1. VS Code and Copilot Studio are pre-authorized (work out of box).
- **Third-party clients (Claude Code, GitHub CLI)**: Dynamic Client Registration (DCR) is deprecated/deemphasized (security concerns). With Entra ID you must: (1) register an app in Entra ID, (2) enable public client flow, (3) add a localhost redirect URI (so local CLI agent receives the auth code at redirect). Store client IDs in the BC MCP config page for reference. Connection string format differs slightly per client (Claude Code needs client ID + callback port; GitHub CLI uses differently-named headers — check their docs).

### BC MCP — tools from API pages & queries

- **API pages as tools**: every *published* API page becomes a tool if added to a configuration. Default config (if none set up) = all API pages available read-only. Permissions still govern everything.
- **API queries as tools**: added support so agents get set-based aggregation/summation/multi-table joins instead of the LLM pulling many pages and doing math in-memory/Python. Same principle as AL: let SQL do set ops; one query = one call returning all needed aggregates.
- **Tool descriptions** come from existing metadata: API page uses caption + `about` text; queries gained an `about` text property (new). The property must have *content* — empty about text = poor description. Tip: run a small agent over the codebase to auto-generate `about` text for all API pages/queries (helps humans too).
- **Orphan/child APIs**: BC pre-processes about text to inject hints — e.g. an invoice-lines API tool description tells the agent to first get the ID from the sales-invoice API (same header-dependency problem as OData exposure).

### BC MCP — embedded resources (large results)

- Tool results can return as an **embedded resource** (a file reference) instead of a text block. Only the reference enters the model context, not the full payload — avoids blowing the context window.
- Resource size limit ~**5 MB** [sic? verify limit] vs tiny effective limit when returning as text.
- Agent passes the file reference to a Python code-execution tool (e.g. in Copilot Studio) so data analysis / stats happen in Python, not the LLM.
- File-reference approach used by Copilot Studio and VS Code; VS Code writes a *temporary* file that may need extra permissions for code-execution tools to read.

### BC MCP — dynamic tool mode

- **Problem**: tool list consumes context; clients cap tool count (Copilot Studio hard limit = **70 tools**, errors past that).
- **Dynamic tool mode**: instead of exposing each API as a tool, BC exposes three system tools — **search**, **describe**, **invoke**. Agent searches for relevant APIs, describes to learn usage, invokes to run. No limit on number of APIs in the config.
- Discovers both API pages *and* API queries.
- **Requires** enabling **semantic metadata indexing** on the Feature Management page (indexes page objects). Without it, falls back to keyword search (worse). Semantic vectors are why it's online-only.
- **Static vs dynamic tradeoff**: dynamic gives LLM more freedom but needs strong instructions/knowledge files (agent can't see all tools up front) and a smarter/pricier model. Static exposes a fixed tool list — cheaper model works.
- **Optimization workflow**: run dynamic mode → use telemetry to record which tools/queries actually get used → build a static configuration (or promote a generated query to an API query) with exactly those → switch to a cheaper model.

### BC MCP — configuration page

- Search "MCP" to find the MCP configuration page. Multiple configs allowed; each config = a scoped tool set; different agents connect to different configs.
- Server-feature toggles per config: **API tools** (published APIs → tools) and **data query tools** (see below); can enable/disable each.
- **Must disable/deactivate a config before editing it** — active agents using it will start failing. Alternative: use the **Copy** action to make a test copy, edit/test there, then apply to the original (avoids breaking other clients).
- **Export/Import** configs (share as files).
- **Validation on activate**: flags issues (API page/query not installed on system; child tool like invoice-lines present without its parent sales-invoice tool) and offers a recommended action to apply.
- Each config provides a **connection string** for clients; paste into `mcp.json` for VS Code.

### BC MCP — data query tool set (preview/upcoming, not shipped)

- New tool set ("data query MCP") for open-ended data Q&A where you can't predict needed pages/queries. Exposes ~5 tools: find BC tables, traverse the table graph (table→table relations), get table schema/fields, compile a query, execute a query.
- Agent gathers context then **generates an AL query on the fly** — a short-lived/dynamic query, compiled and executed, never published to the environment; created then destroyed. Results returnable as text or embedded resource.
- Read-only; writing directly to tables not allowed. BC permissions (direct read permissions) still fully apply.
- Needs a strong model to write AL queries; can attach the **MS Learn MCP server** (AL query samples/docs) and instruct the agent to consult it on compile failure.

### External MCP agents vs internal BC agents

- **External (MCP)**: run in any host, less control, run as *your own user/permissions*. Best when the agent spans multiple systems (billing, ticketing + BC) or needs an external orchestrator; publishable to multiple channels.
- **Internal BC agents**: full access to entire BC UI (anything a user can do in the web client). Have a dedicated **agent user**; effective permissions = intersection of agent permissions ∩ your permissions (safer). Different billing model. Best for DBU-native UI workflows.
- **Company scoping**: connection string currently specifies the company name; MCP configs believed shared across companies [sic? presenters unsure — verify]. Because new MCP spec is moving *stateless*, a stateful "set company" tool won't persist across calls — may require a company parameter on every tool. Under exploration.

### Gotchas

- API tools currently limited to **API pages and API queries** — no codeunit-based APIs ("for now").
- Models may under-fill tool parameters: an agent asked to return all 30 exposed fields may return only 6–10; weaker models (e.g. GPT 4.1) sometimes ask the user for required params instead of supplying them. Mitigate via instructions + better model.
- Debug via standard App Insights telemetry — a tool-invocation event fires per call (telemetry still expanding).

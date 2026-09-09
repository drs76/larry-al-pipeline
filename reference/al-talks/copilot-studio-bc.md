# Copilot Studio + BC, extensions, autocomplete critique

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: What's new in Microsoft Copilot Studio a | 2026-07-27 -->
### Copilot Studio + Business Central integration

- Copilot Studio: end-to-end tool to design, publish and manage agents; "Copilot" and "agent" labels now used interchangeably in the UI.
- Build paths: pre-built agents, templates, from-scratch (visual canvas), or pro-code via the **Microsoft 365 Agent SDK** [sic? verify name on Microsoft Learn].
- **Generative orchestration** setting (buried in agent settings): "use generative AI orchestration for agent response". Enabling it lets the agent decide which tool/knowledge source to call from the user prompt. Default off historically — turn on for autonomous behaviour.
- **Suggested prompts** (starter questions) configured per agent; surface as get-started suggestions in the published channel.

### Agent building blocks

- **Knowledge** — ground the agent in trusted sources: public URLs (e.g. MS Learn), uploaded files (CSV, policies), SharePoint, databases. Agent answers cite source links. Test mode has an **activity map** showing runtime path (which knowledge source / tool was hit).
- **Tools** — where BC data enters. Options: pre-built connectors (incl. the Power Platform **Business Central connector** — same component as Power Platform, all its actions available), custom connectors, agent flows, prompts, skills, REST API, MCP.
- **Orchestrator** — either generative orchestration (autonomous) or **topics** for explicit controlled step sets. **Triggers** (recently added) let an agent run autonomously off events, e.g. incoming email, like a Power Automate trigger.
- **Channels / UX** — publish targets: Microsoft 365 Copilot (extends existing M365 Copilot with your custom agent), plus third-party channels (Google Business Messages, Apple Messages for Business).

### BC connector specifics

- Connector actions (e.g. find/read records) call BC APIs per environment. Demo hardcodes environment; production should use **environment variables** so connections aren't hardcoded across deployments.
- **"Run under user" / user-permission execution**: BC connections in the Copilot context run under the *asking user's* permissions, not a service/super account. If the user lacks BC permission, the call fails. Differs from classic Power Platform where the run account was ambiguous.
- Custom APIs built in AL extensions are exposed through the same BC connector. Custom connectors also supported.

### Prompts and flows as tools

- **Prompt tool**: wraps an LLM call as a tool. Supports templates or from-scratch; define input variables with sample data to test in isolation; choose output format (text or JSON for integration); select the model. Give each tool a description telling the orchestrator when to invoke it.
- **Agent flows**: rule-based/structured workflows (Power Automate-style) embedded in the agent, e.g. create order, create approval, notify manager. A flow can contain a BC connector action — so BC reachable directly OR via a flow.
- Flow inputs can be **"dynamically filled with AI"** — Copilot infers the parameter (e.g. equipment name) from conversation context to start the flow.

### Enhance / manage

- Enhance via **Azure AI Foundry**: bring vector indices, Azure AI Search, 1,900+ models (pro-code).
- Built-in **analytics/activity tab** in Copilot Studio: usage insights, CSAT, errors, escalations.
- Management via **Power Platform admin center** [rolling out]: lifecycle, access control, staged rollout of agents.

### Recent features

- **Agent store** (GA): marketplace for Microsoft and custom agents; install/share; agents undergo validation to be listed.
- **Multi-agent orchestration** (public preview / rolling out): one agent can call another; nested agents.
- **Deep reasoning in prompts**: prompt tool can use a deep-reasoning model from Azure AI Foundry — described as the **o1** model [sic? captions said "01"; verify].

### MCP + Business Central

- BC exposing an **MCP server** (pre-production/pre-prod URL at time of talk — not yet shipped). Turns BC into an MCP source answering natural-language ERP questions (items, customers, orders, quotes) and taking actions (create quote/order).
- MCP raises the integration abstraction: instead of specifying exact API queries/params, the LLM converts intent ("show me latest quotes from BC") into concrete API calls using MCP + tool definitions and BC API metadata (e.g. infers sales-quote API, sort for "latest", top-N).
- Standard MCP servers (BC + other Dynamics products like CRM) selectable when adding a tool in Copilot Studio. Announced at Build: Dynamics products (CRM, BC) expose MCP servers.

### Native BC agents vs Copilot Studio (Q&A)

- Native BC agent platform (e.g. the **Sales Order Agent**) is built in AL/extensions, runs inside BC — currently *unrelated* to Copilot Studio agents.
- Plan: BC-native agents will surface in Copilot Studio, and makers can extend around them. Use BC-native for in-product processes (BC as system of record); use Copilot Studio when automating *across* products.

### Licensing (presenters disclaimed expertise — verify)

- A Business Central license does **not** include Copilot Studio rights — pay extra. Some Power Platform usage rights included, but not Copilot Studio.
- Copilot Studio billed per **message**: message packs or pay-as-you-go. BC scenario more complex — messages depend on agent design / MCS messages per turn. Read the licensing terms.

<!-- ingested: Microsoft Presents: Bring your Copilot extension to Microsof | 2026-07-27 -->
### Bring your Copilot extension to Microsoft cloud (toolkit, BC AI resources, MCP)

**Copilot toolkit / developer tools for Copilot in BC**
- Toolkit builds *interactive* ("classic") Copilot features, as distinct from autonomous agents; both expected to converge into one common toolkit over time.
- Handles plumbing (LLM calls, connection setup, UI pieces, system-module helpers, telemetry) so devs focus on value-add.
- Docs/learning entry point: `aka.ms/StartCodingWithAI` [sic? — verify exact aka.ms slug].
- Samples on GitHub BCTech repo (`aka.ms/bctech` [sic?]), including an Azure OpenAI / Copilot-feature sample.

**Business Central AI resources (BC AI resources)**
- Moving from private preview (invite-only) to public preview this release.
- Lets AppSource publishers call LLMs via Microsoft-managed Azure OpenAI resources — no need to procure/manage your own Azure OpenAI subscription for production.
- Microsoft bills the customer directly for AI consumption; customer gets a single bill across ISV solutions.
- Choice model: use BC AI resources (recommended default, production) OR bring your own Azure OpenAI subscription. Typical pattern: own subscription for dev/test, BC AI resources for production. Same app/source, switched by environment context.
- Even when using BC AI resources you must still supply *your own* Azure OpenAI subscription — used only as proof you accepted Azure OpenAI usage terms, not for billing.
- API to select managed path: `SetManagedResourceAuthentication` [sic? verify — auto-caption]; bring-your-own uses `SetAuthorization` [sic? verify] on the Azure OpenAI module, plus specify model.
- Detect environment in AL via a context object to branch prod vs non-prod (use own sub if not customer production) [exact object/method name not stated — verify].
- Microsoft handles scaling, throttling, load balancing, regional instances, deployment updates.
- Content safety on managed path: blocking policies, harm filters (hate/violence/sexual/self-harm), jailbreak detection, cross-prompt-injection protection.
- Privacy: your prompts are your IP; not used to train AI/Copilot.

**Billing model**
- Shared currency across Microsoft = Microsoft Copilot Studio (MCS) messages.
- Metered by tokens = input + output tokens summed. Token ≈ between a character and a word; test tool reports tokens used.
- Mapping chain (per Microsoft docs table): standard SKU → 10 responses = 50 messages, i.e. 1 response = 1.5 messages. For AI tools (BC AI resources path): 1 response = per 1,000 tokens, model-independent, rounded up.
- Pay-as-you-go ≈ 1 US cent per message; prepaid/message-pack quota gets a discount.
- Example: GPT-4 std SKU, 10,000 tokens = 10 responses = 15 messages = ~15 US cents. 4,500 tokens rounds to 5,000 = 5 responses = 7.5 messages = ~7.5 cents.
- Quota sources: free base quota from BC license → prepaid quota (discounted) → pay-as-you-go.
- Copilot & AI Capabilities page gets new "Billing type" column showing who bills: license/base, Microsoft (BC AI resources), or publisher ("custom billing"). Billing covers only LLM/AI consumption; publishers still charge separately for app usage via AppSource.

**Models**
- GPT-4.1 family positioned as developer-focused ("new API"); Microsoft moving all integrations to latest OpenAI models over the summer.
- Toolkit gives an abstraction to request "latest" model instead of pinning a version.
- Gotcha: newer model ≠ strictly better — behaves *differently*, not back-compatible; prompt behaviour/accuracy can regress silently on version bump. Real case: email-drafting prompt lost detail/accuracy after a model version change; caught by tests, fixed by prompt tweak.
- Key takeaway: good test coverage matters more than a pretty prompt; migration is safe only with tests.
- GPT-4.1-mini migration cited as low-drama vs past migrations, but still run tests.
- BC stance: stay model-aware. Model-routing/abstraction layers (Azure/AWS auto-pick-best-model) suit chat/categorization, not BC's specific prompts.
- Model list on BC AI resources is shorter than full Azure AI Foundry list; more may be enabled over time.
- Design pattern: use a powerful model for core processing, a cheaper/faster model to validate responses (hallucination check) before doing work.

**Copilot test toolkit (AI Test Toolkit)**
- AL extension, runs in sandbox only, shipped on AppSource; source in BCApps repo under AI test toolkit subfolder.
- End-to-end Copilot feature testing: define test suite, data-driven input (dataset per suite or per test case), iterate rows to drive test cases, run whole suite, view stats including token consumption.
- Evaluate results by: human eval, evaluation functions/methods in test cases, or Azure AI Foundry.
- Gotcha: toolkit applies additional system prompts when running through it, which can differ from your own-subscription path — test *both* subscription scenarios.

**Azure AI Foundry (for BC dev)**
- Playground to prototype prompts before building in BC — validate intent expressibility first.
- Use for harmful-content/safety evaluation and response-alignment checks.
- Generate large test-case sets (500–700+) covering phrasing variety and user biases.

**MCP (Model Context Protocol)**
- Standardizes how LLM features describe their skills, near real-time, so a host can discover and call them.
- Demo: BC chat has fixed built-in skills (e.g. "show latest quotes from Alpine" resolves quote=sales quote, Alpine=customer). Adding an MCP server config exposes a new skill; chat then discovers it, calls it, folds the result into conversation context (demo: hard-coded beer list, but could be any integration).
- Direction: let ISVs contribute skills to core Copilot experiences (chat, sales-line suggestions) via MCP — not yet GA, "come talk to us."

**Roadmap / asks**
- More flexible test-tool UI (inline, larger than single dialog).
- Image input (models like GPT-4.1 are multimodal; dedicated vision models for deep image analysis) and reasoning (o-series) models.
- Better telemetry/feedback loops for troubleshooting prompts and understanding customer prompts.
- Semantic search by similarity — building first for metadata, later for data (e.g. user says "product", data has "item").
- Telemetry signals + comms when Microsoft changes models, to avoid breaking production extensions.

**Accuracy/cost guidance**
- Billing scales with data volume, model, and retries, but costs are small; a good feature costs far less than lost productivity even with retries.
- No 100% accuracy; "good enough" is partner/scenario-defined — target ~85–95%. Copilot keeps user in control, so they can edit weak suggestions without re-calling the LLM. Monitor for users retrying often (signals a problem).

<!-- ingested: Copilot is just a fancy autocomplete… | 2026-07-27 -->
### GitHub Copilot for AL — completions, edits, agent, inline

**Fancy autocomplete (inline completions)**
- Context sent to model = current file (name + as many lines before/after cursor as fit) plus up to **4 additional open tabs**. Line selection within a large file is effectively random (not the whole file); tab selection is also random, not relevance-ranked.
- Token limit for the request is **8,192 tokens**; if the current-file context fills it, no extra tabs are sent.
- Only *open, active/edited* tabs count — never closed files. No memory between completions, no code analysis, no talk to compiler/language server (so it can't see existing warnings).
- Practical rule: keep ≤4 relevant tabs open; close others (`Close Others`/`Close to the Right`) to sharpen suggestions.
- Completions model is switchable: Copilot icon → Configure Code Completions → change model. Newer/better model is often not the default at first.
- Findings on the 4-tab limit were reverse-engineered via Fiddler intercepting the HTTPS prompt before it leaves the machine; undocumented, may change. Observed quirk: request metadata sometimes tags the language as Perl.

**Edits mode**
- Like chat but can modify files. Key advantage: **you control the context** — pull in exactly the files the model should see; it won't touch files you didn't add.
- For AL, switch model to a Claude/Anthropic cloud model (Sonnet 3.5/3.7/4) — reported markedly better for AL than GPT models.
- Enable Claude models in **GitHub settings** (github.com → Copilot features), not VS Code settings; org-licensed users need an admin to enable.
- Reliably messes up object IDs — fix manually. Start a **new session per logical step** (click +): shorter context = faster and more accurate; large context degrades accuracy.
- Keep AL files small for edits: >500 lines becomes painful, aim <300 lines.

**Agent mode**
- Like edits but has tools: search/read codebase, find references/definitions, check file errors, get diffs, run terminal commands. Fetches its own context, so you feed less.
- Can generate AL from scratch (empty project) or extend by analogy to existing objects; output is a starting point, not production-ready (empty triggers, over-use of globals, wrong file placement in multi-root workspaces).
- Downside: may wander into unintended files (README, docs). For tight control prefer edits.

**Inline Copilot (Ctrl+I)**
- Operates only within the current selection — good for editing one procedure inside huge legacy files (thousands of lines) where edits/agent are slow/error-prone.
- No context control: falls back to the 4-open-tabs rule.
- Also usable in the terminal: generate shell/git commands (e.g. interactive rebase) and small PowerShell scripts.

### Copilot instructions / memory files (AL)
- `.github/copilot-instructions.md` is prepended to every request — use as persistent memory for coding standards (naming ≤30 chars, event subscriber brackets, variable ordering, explicit record parameters, begin/end only for compound statements).
- Useful for teaching post-cutoff AL features the model doesn't know, e.g. `JsonObject` typed getters `GetText`/`GetInteger`/`GetBoolean` `[sic?]` (verify exact method names against Microsoft Learn/compiler) — otherwise the model keeps using older `.Get(...)` patterns.
- Reusable prompts go in `.github/prompts/`; invoke with `/` (slash) in the Copilot pane.
- Limitation (as of talk): must live in the repo; no centralized/linked memory, and no directory-scoped instruction files in Copilot yet.
- Commit-message generation can be steered via a dedicated VS Code setting for commit instructions.

### Cursor vs VS Code + Copilot (AL)
- Cursor = fork of VS Code focused on AI features; roughly ~2 steps ahead, Copilot keeps catching up. No strong reason to switch if org already pays for Copilot.
- Cursor extras noted: `/generate cursor rules` builds rule/memory files from a conversation; rule files support types **manual**, **always** (= copilot-instructions equivalent), **auto-attached (glob pattern match)**, and **agent-requested** (description the agent may choose to load). Auto-attach by file pattern (e.g. test-only rules) is the feature wanted in Copilot.
- Cursor terminal has "Add to chat" to pipe terminal errors into the prompt; model selector lets you hide unused models.
- **Next Edit Suggestions**: evolution of autocomplete that jumps the cursor to the next edit location (Tab to jump), works mid-line and propagates edits (e.g. rename both sides). Available in VS Code too — enable via settings search "next edit suggestions".

### Model choice & prompting (AL)
- For AL, default to Claude — reported consistently best. For mature languages (C#, Python, TS) rotate models when one gets stuck (Claude ↔ o3): different models give different implementations.
- Why Copilot is weaker for AL than C#/Python: far less open-source AL training data — not code quality. Corollary: testable, SOLID, small single-purpose procedures with interfaces produce tests resembling C# tests the models saw, so Copilot writes better AL tests. It cannot write good tests for untestable legacy code.
- Prompt quality drives completion quality. `prompt boost` extension: start a prompt with "boost this prompt" to expand a casual prompt into a structured one. `[sic?]` extension name — verify in VS Code marketplace.
- Break work into single steps; asking for many changes at once fails. Take control of context (pull in target + reference files) as the top lever for better output.
- Code review: GitHub Copilot code review reportedly weak for AL as of talk; CodeRabbit noted as better for AL (accepts custom instructions). Custom instructions for Copilot code review need the enterprise SKU.

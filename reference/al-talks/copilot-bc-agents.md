# ISV docs in Chat, autonomous BC agents, trust & AI-powered extensions

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: Bring ISV docs to Chat with Copilot, and | 2026-07-27 -->
### Copilot chat — ISV docs & metadata search (BC TechDays talk)

**Chat core capabilities (recap)**
- Two modes: (1) find relevant records — chat guesses the target page, builds a normal BC filter on it, returns results with citations you can verify by opening the page; (2) answer product questions from Microsoft Learn docs.
- Learn-doc answers query the documentation source directly (not Bing), then run grounding checks.
- Best queries name the page type, desired filters, and sort order. Follow-up/clarifying questions supported.
- Newer: chat can build analysis views (opens via button); chat is aware of a page's Copilot actions and can surface them for discoverability.

**Chat with your own ISV documentation**
- Set a help URL in `app.json` pointing at your docs; passed to chat for every deployed extension in the environment.
- On a doc-relevant ask, chat does a Bing search scoped to those URLs, then applies same grounding checks as Learn docs. Combines Learn + your docs in one answer; falls back to links if it can't compose a satisfying answer.
- Requirements/gotchas:
  - Docs must be indexed by Bing → URL must be public (auth'd docs won't work out of the box).
  - HTML/text crawl best; PDF works partially; images don't work.
  - Redirects from short URLs are NOT followed.
  - Scoped root path max 2 levels deep.
  - Avoid uncommon URL chars (e.g. pipes); keep alphanumeric/ASCII.
  - Rollout: sandbox first (toggle on Copilot & agents capabilities page to enable Bing search), production targeted for release wave 2 (late 2025 per talk).

**Semantic metadata search (platform)**
- Distinct from data/modern search (which searches table data). Metadata search = search over entities (pages/reports) from base app + extensions. Powers Tell Me, Report Explorer, and Copilot chat entity mapping.
- Problem with today's string/token match: synonyms ("clients" vs "customer") need manual `additional search terms` in page metadata — doesn't scale, poor multilingual support.
- New approach = hybrid ranking combining: text similarity + semantic (vector embedding) similarity + other signals (e.g. page bookmarked).
- Embeddings map query + page metadata to same vector space; rank by cosine similarity (dot product suffices since most models are unit-magnitude). Contextual embedding models (BERT-style) capture word sense; multilingual models give cross-language search for free.
- Embedding weakness: pages with thin metadata get noisy embeddings and pollute results (e.g. bare "Invoice" page keeps matching), and embeddings handle acronyms/technical terms poorly — hence hybrid, not pure vector.
- Benefit: chat better maps intent to partner/extension entities it doesn't know natively; works when the query never names the BC entity.
- Rollout: opt-in via Feature Management; enabling kicks off background indexing, then chat switches to semantic metadata search. Also planned for Tell Me and Report Explorer.

**Preparing extensions for chat / AI**
- Chat works only on list pages backed by a real source table (NOT temporary or virtual tables).
- Chat operates on tables/records but uses PAGE metadata for navigation.
- Response/output format = defined by a `Brick` field group on the underlying table. Chat can pull extra fields on request or when relevant.
- Fields ignored by chat: JSON, Media, Blob field types, and any field with no tooltip.
- Metadata to provide:
  - Table fields: caption (only if field name isn't self-explanatory) + tooltip (1–2 lines).
  - Table: define a Brick field group for default chat response format.
  - Page fields: captions + tooltips — page metadata OVERRIDES table metadata, so missing table caption/tooltip can be supplied on the page.
  - Page: set `UsageCategory` (makes page searchable), caption, 1–2 `AdditionalSearchTerms`, and `AboutText` — AboutText is the most important, short 1–2 lines describing what the page is for.
  - Extension: help URL in `app.json`.
- Chat obeys standard BC permissions — can't touch pages/tables the user can't access.
- Extra-field pull-in can be disabled per profile by turning off personalization for that profile.

**MCP (Model Context Protocol) in AL — LAB/experimental, subject to change**
- Client-server protocol to feed context to an LLM; positioned as "LLM-first" vs OpenAPI/Swagger (less token clutter/noise). By Anthropic; docs at modelcontextprotocol.io.
- Primitives: resources (files/data), tools (LLM-invokable functions), prompts. Focus is tools.
- Proposed AL surface: system table `Copilot Chat Tool` [sic? verify name against compiler] holding MCP server name + endpoint, plus keys (company, user, page, likely profile) to scope which server loads per conversation.
  - Optional implementation codeunit for runtime control of connection; can override/whitelist which of the server's advertised tools chat may use.
  - Can supply auth/custom headers, and a status message shown in chat while the server runs.
  - Can unload internal platform tools (e.g. remove built-in doc provider so a custom provider like DeepWiki doesn't compete).
- MCP tool params: define a summarized-conversation string param to receive current user intent, or simple primitives (e.g. a boolean auto-populated by the chat orchestrator, "set true if about X"). Chat regenerates the final message applying its formatting → consistent output + keeps guardrails.
- Guardrails retained for MCP path: harmful-content detection on request out and response back; off-topic detection is a non-disableable skill.
- Enabling scenario: MCP can reach non-public/local docs if the MCP server is publicly reachable from SaaS and bridges to local content (demo used ngrok to proxy SaaS→local).
- Custom knowledge sources (à la Copilot Studio SharePoint sources) NOT supported in initial release; under consideration. [sic? verify `Copilot Chat Tool` table/field names against compiler + Microsoft Learn — from auto-captions.]

<!-- ingested: Microsoft Presents: Autonomous agents in Business Central | 2026-07-27 -->
### BC autonomous agents — architecture & development

- Agents represented as **users** in the User table: type = special agent type, but have display name, username, permission sets, profile. User-card-like agent card page.
- Every agent record tied to an underlying user record → permission sets and profiles apply normally.
- **Instructions** stored on the agent record — natural-language description of the agent's job (the core of an agent). Not editable via card page for shipped agents.
- Agent = goal-oriented: you state *what*, not *how*; the LLM decides steps.
- Agents operate BC by driving the same **logical UI API** (JSON) a browser client uses. They log in as a separate async session (not inside a user's session), navigate pages, set fields, press buttons. Can read/act on **any field on a page — including extension fields — as long as it has permission**; doesn't matter that the field isn't on the base page.
- **Restrict what an agent sees via a dedicated profile / Role Center** → fewer pages/fields/actions = more reliable, less chance of wandering. Recommended to build a purpose-built profile.

#### Data model
- **Agent Task** = unit of work. Table record. Creating a task is what makes an agent act; an agent with no task does nothing.
- Tasks may have no input/output (instructions self-contained) or be **multi-turn conversational** (sequence of input/output messages).
- **Task Messages**: type = input or output. Output messages always created by the agent; input by AL code. Have a status (e.g. can trace a `discarded` message).
- Multi-turn requires **reusing the same task** — find the existing task and append a message rather than creating a new one. Context/memory is per-task. Agent Task record has a text field to link to an external ID (e.g. Outlook conversation ID) for correlation.
- **Log entries**: detailed per-step audit (page operations = any UI interaction, output-message creation, user interventions). More granular than the timeline; used for troubleshooting/auditing. Timeline is the end-user view.

#### User access & permissions (security)
- Agents have a **user-access** list = row-level security over the shared agent/task/message tables. A user not granted access to an agent cannot see that agent or its tasks even though data lives in shared tables (enforced by platform, incl. AL FINDSET).
- Access can be view-only (help with tasks) or include configure rights.
- **Effective permissions at run time = intersection of the agent's permissions AND the permissions of the user who created / last assisted the task.** Prevents privilege elevation (a user can't make the agent do what the user itself can't).
- Agent tied to a **Copilot capability**; disabling that capability disables all its agents.

#### Application vs platform split (running a task)
- **Agent application (AL, your code) responsibilities:** channel integration (e.g. read mailbox / send email — platform does NOT handle email or any channel); decide new task vs continuation (correlate via external ID); insert input message; set task **status = ready** to hand off; build the profile/permission sets; setup page + setup data; build instructions; process reviewed output messages (send them, then set message status ready→sent to avoid double-send).
- Setting status=ready is non-blocking, can run in a UI session; no dispatch needed from AL.
- **Platform responsibilities:** schedule/run ready tasks in background (subject to concurrency quota per environment); **scan new input messages for harmful content — if detected, task is blocked/stopped**; drive the UI via logical API executing instructions; auto-handle user interventions (review requests, help-needed, permission-blocked steps); create output messages + handle review flow; the whole task-pane/timeline UX.

#### Registering an agent (AL — APIs subject to change, verify against compiler/Learn)
- Extend enum `Agent Metadata Provider` [sic?] with your value; implement interfaces `Agent Factory` [sic?] and `Agent Metadata` [sic?] (an `Agent Validation` [sic?] interface exists with a default impl). Example implemented both metadata+factory in one codeunit.
- Metadata supplies: initials (separate initials for setup-available vs already-set-up state, enabling multiple instances e.g. SO1/SO2), setup page ID (distinct first-time vs subsequent setup), summary page ID (KPI page), whether to show the "+" activate avatar (e.g. hide if one instance already exists), and the tied Copilot capability. Can override the agent-task-message review page with your own.
- Before an agent record exists, the avatar shows dashed + "+"; activating runs the setup page and creates the record.

#### Playground (developer-only)
- Agents list → Playground menu: create a no-code "Playground Agent" on the fly, assign permission sets + profile + initials, activate, paste instructions, create a task manually. No app redeploy — instructions are just data, so iterate fast.
- Observed: abstract instructions ("ensure all sales orders comply") let the agent solve efficiently (3 steps, read data straight off the list page) vs over-directed step-by-step instructions (33 steps, opened every card). Prefer stating goal over procedure.
- Feedback-driven refinement of instructions is a planned direction (not yet implemented).

#### Sales Order Agent (public preview, English-speaking markets first)
- Monitors a shared mailbox; per email: identify contact→customer, check item availability, draft sales quote (fills requested delivery date, lines), draft customer reply with quote PDF attached, send on confirmation, convert to sales order on customer acceptance.
- Multi-turn: customer replies on the **same email thread** land on the same task (thread → task correlation). Handles add/remove/change-qty and clarifying questions for vague inquiries.
- Human-in-the-loop review configurable: review all / first / none. Unregistered-sender or off-topic emails get a warning; a warning also fires if a new message arrives while a step awaits review (discard the stale drafted step, confirm the newer message, resume).

#### Payables Agent (private preview, ~20 partners)
- Monitors mailbox for PDF invoices; extracts data via **Azure Document Intelligence** [sic?: "Azure document intelligence"]; creates draft purchase / e-document; maps lines to GL accounts from company accounting history/policy; PDF previewable side-by-side in BC.
- Account mapping done by LLM (planned: UI confidence indicator; planned: match against purchase orders). Approach: infer accounts by scanning similar past invoices.

#### Misc / roadmap / commercial
- Agents run as normal user sessions → thousands of users + ~10 agents is fine; not a perf concern of its own. But LLM latency + large pages/many steps = heavy token prompts → treat agents as background, not click-and-wait. Concurrency/AI quota (TPD) limits parallel tasks.
- Built-in BC approval workflows still gate agents: agent (as a user) blocked on e.g. Post until approved, then continues.
- Third-party interop planned via **A2A (agent-to-agent) protocol** — e.g. Copilot Studio agent ↔ BC agent. BC agents live in BC (AppSource delivery, integrated timeline) rather than Copilot Studio.
- Agents interact via pages/UI only — no per-table function registration. For large data or aggregation, build custom pages (they did build a custom item-availability page for the sales agent for efficiency/reliability). Agent can use page filters/search.
- Customizing shipped-agent instructions: not currently extensible, planned.
- **Pricing:** no per-agent license; usage billed by messages. Rough figures cited (verify on Microsoft Learn): incoming mail ~2¢, outgoing mail ~2¢, quote created ~5¢, order created ~5¢. Any licensed user can interact with agents.
- Agent playground private preview ~July 2026; public preview targeted ~October 2026 (per talk).

<!-- ingested: Microsoft Presents: Building Trust in AI: The Development of | 2026-07-27 -->
### chat-with-copilot-grounding-and-trust

- Chat with Copilot in BC has two request types: **knowledge questions** (answered from Microsoft Learn / product docs, returned with citation markers linking to source) and **data questions** (queries against the user's company data).
- Preview was English-only at time of talk; other immersive Copilot features (e.g. sales-line suggestions) already multilingual as of the 24.2 release [sic? verify version]. Multi-language chat planned but not shipped.
- No customer/tenant data is used to train the LLMs.
- Copilot **respects the calling user's permissions** — it only surfaces metadata for objects the user can see and only returns records they can access via the UI. Cannot be used to bypass permission sets.

### hallucination-handling

- LLMs by design will not admit lack of knowledge; they complete/fabricate. Core design goal of chat is to force an honest "I can't help" instead of a confident wrong answer.
- Real failure examples seen during development: fabricated procedures that *sound* right because docs contain structurally similar (but different) instructions (e.g. inventing how to reverse a sales credit memo from a sales invoice). Also "correct-by-luck" answers ungrounded in any doc (e.g. release a sales order via Home group → Release, right answer but no doc source existed at the time).
- Data-side fabrication example: asking inventory for a non-existent item ID returned an invented count plus a clickable-but-broken record link (bookmark/record ID didn't exist).
- Mitigation flow for knowledge: acquire trusted knowledge (docs), then verify the LLM's answer actually addresses the question before returning. If ungrounded, return helpful links rather than a fabricated procedure.

### data-query-pipeline

- Unambiguous data request path: (1) classify intent / whether a matching skill exists; (2) pass installed table metadata (base app + extensions) to LLM and extract the target entity → resolve to a table (e.g. Sales Header [sic? "sales headed" in captions — verify]); (3) LLM generates filters + sort (e.g. sort by posting date, filter status posted/released); (4) retrieve records; (5) return with explanation.
- Ambiguous named-entity requests (e.g. "overdue balance for Adatum" where the LLM can't tell Adatum is a customer) fall back to the existing **search company data** function that scans commonly-used tables.
- On any pipeline failure (can't resolve data type, can't build filters because required fields aren't on the page, or query returns no rows) the code must explicitly tell the LLM there were no results and to apologise — never hand it an empty query object, which triggers fabrication.
- Every data answer ships an **explanation** of how it was derived (which table, which filter/sort field) so users can trust/verify the figure. Explanation is shown under the expandable References section (not always inline). Example: "top customer" is inferred by sorting on the Sales (LCY) field descending.

### making-extensions-copilot-ready

- Copilot sees an extension only through **page metadata**: fields present on pages/lists, captions, tooltips/about text. If a user would struggle to find data via the UI, so will Copilot.
- Developer action: give fields meaningful captions and tooltips, and surface fields on the relevant pages/lists. Cryptic names (a field literally called "115") make Copilot unable to reason about the data.
- No API today to extend/register custom chat skills [sic? verify current state on Learn]; you influence Copilot purely by describing your app well via metadata.
- Custom/third-party documentation cannot be fed to chat; external knowledge is sourced only from Microsoft Learn.
- Localized-only captions: those non-English captions are what get passed to the LLM; generally works but should be tested, consider English fallback captions.
- Tooltip/caption inheritance: defining on the table should ideally suffice (page inherits), but at time of talk the lookup was page-oriented and being optimized — safest to ensure the metadata is discoverable.

### limits

- No complex data aggregation (e.g. aggregate sales across all customers/countries, sales-by-month over years) — chat can't do it; direct users to the **Analysis assist** / natural-language analysis feature instead.
- Feedback: thumbs up/down captured (category on thumbs-down: inaccurate / offensive / other); free-text field and output capture were in progress, not yet available to extension developers.

<!-- ingested: Copilot Development: AI-Powered Extensions for Business Cent | 2026-07-27 -->
### Copilot toolkit — promptdialog & AI module (BC 2024 wave1)

- Copilot toolkit = signature UI (`promptdialog` page + copilot actions), AI module (`System.AI` namespace in system application), capability registration, telemetry helpers.
- Scope: BC online only (Docker allowed for dev/testing); generative AI only; single-turn (input→output), non-conversational. Chat pane is NOT buildable with the toolkit.
- Responsible AI baked in: human always reviews/approves output. Either show result for review before saving, or if saved first, provide undo that fully rolls back committed changes.

### promptdialog page type
- New page type; core of the signature UI. Renders 3 states (input / generating / output) from ONE page via areas.
- NOT extensible by design — prevents third parties altering responsible-AI guards; also aids debugging since LLM output is statistical/non-deterministic, so ownership of instructions must be clear.
- Areas: `area(Prompt)` for input (fields, page parts, controls); `area(Content)` for output. No repeater allowed in output — put records in a sub-page shown as a page part.
- System action area (promptdialog-specific): `Generate` action is a platform action; on input screen shows as Generate, on output screen as Regenerate (same underlying code). Regenerate resends same system+user message.
- `PromptMode = Generate` starts page directly in generating mode (skip input) — used when all needed data already in BC.
- Save via page close trigger (OnQueryClosePage), check OK vs Cancel — same as normal pages. Keep/Discard action captions are renamable.
- Progress indicator: update user during long generation (data retrieval/processing/post-processing) instead of the normal progress dialog API.
- `InstructionalText` property [sic? verify exact property name] on prompt fields — placeholder hint text.
- Prompt guides: `promptguide` action + prompt-guide area with captioned example prompts (triggers) to seed user input.
- Page caption can use `DataCaptionExpression` [sic? verify] to echo the user's prompt.
- History supported — navigate back through prior prompts/outputs.

### Discoverability / surfacing
- Sparkle image option on actions; sparkle field option (for menus); "copilot action" (prominent next-action button, e.g. bank rec page) placed via new `Prompting` area in actions.
- Copilot actions supported on list pages, list parts, worksheets, and startup dialogs at time of talk; card page support was in progress.

### AI module (System.AI) key objects
- `AzureOpenAI` codeunit: `SetCapability`, `SetAuthorization`, generate methods (chat completion), `GenerateChatCompletion` returns assistant message; `GetLastMessage` [sic? verify names against System.AI on GitHub].
- `AzureOpenAIOperationResponse` [sic?] — full LLM response.
- Model types: chat completion, text completion (text completion expected to be deprecated), embeddings.
- `AzureOpenAIChatMessages` [sic?] — build system + user prompt.
- Chat completion parameters: set temperature (0 = non-creative/deterministic), max tokens. JSON mode: new property `SetJsonMode(true)` [sic? verify] added in 24.2 — forces pure JSON output, but you must ALSO state "respond in JSON" in the system prompt.
- Chat roles: user, assistant, tool, system [sic? verify enum].

### Capability registration
- Extend enum `Copilot Capability` [sic? verify object name]; in install codeunit check if registered, then call register capability passing the enum, GA-or-Preview status, and a learn-more URL.
- Each extension adding a capability must register it itself — registration does not cascade to dependent extensions.
- Admin page "Copilot & AI Capabilities" gives transparency + on/off control per capability.

### Prompt engineering patterns shown
- LLM has no memory and no BC context — resend full system instructions + data every call.
- Structured output: instruct model to reply in XML or JSON; parse into a temporary table (XMLBuffer etc.), show in sub-page, insert to DB only on Keep. Post-process to strip stray fences/markers (e.g. ```xml).
- System-prompt template order: goal/task → steps → rules/constraints → output format. Add "no comments", "respond only in JSON".
- Reinforce ignored instructions with an emphasis block ("these are important, follow them") when model drifts.
- Send only the minimum data (e.g. session durations, not full descriptions) to cut tokens and improve results.
- Field-mapping use case: send only table field list + Excel headers (not the data) and ask LLM to map — robust generic Excel import.

### Function/tool calling
- Register AL functions as tools: describe function name + parameters to the model; model selects function and fills parameters; toolkit auto-executes the matching AL function and returns result.
- In AL: add a tool (instead of/alongside system message); check if response is a function call, get result; optionally feed result back to LLM for a natural-language final answer, or show raw result.
- Cannot register all BC functions — token limit constrains how many tool definitions fit.

### Tokens
- Toolkit has token-counting APIs; counting differs per model (separate methods per model, e.g. 3.5 vs others). Model context limits ~4k up to ~128k tokens depending on model.

### Embeddings / semantic search
- Full-text search only matches literal terms; semantic search matches meaning ("furniture" → desks/chairs).
- Send text to embedding model → get vector; compute cosine similarity between query vector and each item vector; filter e.g. similarity < 0.8 out. Enables answering beyond exact user wording.

### Testing AI features (Microsoft practice)
- Do test-driven dev: after validating prompt in Azure OpenAI Studio, write tests before next dev phase.
- Accuracy tests (prompt output can vary run-to-run; catch regressions when tweaking prompt).
- Grounding tests (e.g. verify item attributes actually appear in generated marketing text).
- Quality / end-to-end + red-teaming (harm, bias, jailbreaks).
- Test framework was WIP, to be shared on GitHub.

### Content-safety gotcha
- Azure content-safety filters can block prompts on flagged wording (e.g. "beer party" was refused); rephrasing ("evening party") passed.

### Roadmap notes (as of talk, ~24.x)
- Managed/shared AI resources: private preview (BC-managed AI, sign-up) — removes need to bring your own Azure OpenAI resource.
- Copilot actions coming to card pages.
- Plan to merge chat experience with promptdialog.
- promptdialog input language: English only at time of talk (marketing text supported ~7 languages); more languages planned.
- Private/self-hosted LLM redirection not supported — toolkit wraps Azure OpenAI endpoints directly (unless via managed subscription).

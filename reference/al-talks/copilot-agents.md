# Autonomous agents, prompt engineering, Copilot autofill/summarize

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: OpenClaw - aka entering the era of truly autonomous agents | 2026-07-27 -->
### OpenClaw / autonomous agents (community talk)

Context: mibuso talk (Freddy Kristensen [sic? — verify spelling], Finn Petersen [sic?]) on OpenClaw [sic? — product name from auto-captions, verify], an open-source autonomous AI agent framework. Origin lore (WhatsApp relay → renamed `claw`/`multi`/OpenClaw) is anecdote — skip. Durable dev facts below.

**What it is**
- Open-source agent that *acts* (writes/runs/installs software, scrapes web, reads email), not just a chatbot. Runs continuously on an always-on machine, not on your working laptop.
- You interact with / teach it via a chat channel (Telegram, WhatsApp, voice), not an IDE. The persona teaching it is an end user, not a developer.
- Each agent has a workspace of plaintext markdown files: a "soul"/identity file, a user file (facts about you), per-agent tool allow-list, memory, and "dreams."
- Memory strategy: agent compacts daily experience into smaller long-term files ("dreaming"); some skills use a "memory palace" approach. Memory scoping is an unsolved/hard problem with competing skill approaches.
- Heartbeat: scheduled/cron-like trigger to run tasks at set times.

**Hosting / setup**
- Runs on macOS, Ubuntu (incl. VM), Windows (recently added — previously discouraged), Raspberry Pi 4/5, or one-click hosts (Hostinger [sic?]). Windows enterprise support added ~Build with per-folder read-only/write/hidden permissions and "auto mode" for permission grants.
- Mac Mini popular because unified RAM (shared CPU/GPU memory) lets it run local LLMs; low power/noise.
- Recommended safe start: OpenClaw inside a VM (VMware Workstation Pro / Fusion Pro, now free). Take VM snapshots before experiments; roll back on failure. Share a host folder into the VM to hand it tasks.
- Install: paste a shell command from installer; it checks node/npm versions and prerequisites. Choose an AI model (OpenAI/Anthropic), a chat channel (Telegram easiest), and skills.
- Telegram setup: create a bot via BotFather to get credentials + pairing code.
- Default skills include a hidden weather skill. Brave Search usable as search backend (free tier, needs API key).
- Backup: have the agent push its workspace to a GitHub repo (needs a scoped token). Lets you inspect/edit the agent's "brain" as plaintext and track evolving memory/skills.

**Cost control**
- Token spend real: reported ~$5–$25/day on default cloud model.
- Hybrid models: run cheap/free local model (Ollama, ~20GB+ downloads) for light tasks like the heartbeat; reserve cloud model for heavy reasoning. Switching heartbeat to Ollama cut cost to ~$0.30/day in one case. Model choice is configured above the workspace level.

**Security (take seriously)**
- Agent inherits the permissions/identity it runs as — on your own machine it can do anything you can. Do NOT run on your company/work laptop for experiments.
- Prompt-level "don't obey others" instructions are insufficient — use hard/physical guardrails (separate machine, VM, Docker sandbox).
- One agent per customer/tenant on separate machines/VMs so credentials can't leak across security boundaries. Agents on the same box can read each other's data.
- Use scoped access tokens (limited GitHub/cluster access) rather than broad admin.

**Skills**
- Skill format standard: `agentskills.io` [sic? — verify domain]. A skill is just a folder containing `skill.md` (plaintext). Standard authored by Anthropic; used across Claude/Codex/etc.
- Marketplace: clawhub.io [sic? — verify] and skills.sh / skills.md [sic?] for examples. Publishing requires an account aged ~5 days.
- "Skill workshop": teach the agent interactively, then have it save the lesson as a reusable skill; it shows a draft skill before committing for future runs.
- To author a skill reliably, point the agent at `agentskills.io` for the spec plus a reference skill (e.g. an existing GitHub skill) + the relevant API docs.

**Business Central relevance**
- OpenClaw's MCP client cannot connect to Business Central today because it lacks OAuth support for MCP. A PR adding OAuth to OpenClaw's MCP was open at time of talk — watch for merge. [Verify current state against the OpenClaw repo / MS Learn.]
- BC's MCP surface does not expose everything the UI does — some operations unavailable via MCP.
- Speaker opinion (not fact): in-BC agents are constrained — no tool install, no external MCP, forced to BC's model, limited to in-BC data — and may be superseded by external agents an end user can teach without a developer. Treat as opinion.

**Agent-tooling landscape (comparison)**
- Claude Code / Codex / Cursor: run on your laptop (LLM in cloud, job local); can install tools + MCP servers; user is an engineer; hybrid model choice. Phone-continuation exists but requires laptop left on.
- GitHub Copilot coding agents: run in the cloud (no laptop needed); triggers = issue opened / PR opened / PR sync / PR merge / schedule; predefined tool set, cannot add MCP/tools; always a cloud model.
- OpenClaw differentiator: always-on host, taught by a non-developer via chat, full MCP-server access, hybrid models.

**Applied examples (patterns, not verified)**
- Autonomous CRM: agent reads email, scrapes sites, extracts data (incl. PDF extraction step), files each lead as a GitHub issue → CRM-as-markdown-in-GitHub. Used agent-dedicated email service ("agent mail" [sic?]).
- Long-running code review: custom skill reviews a multi-app AL project (app + test app), emits executive summary, object counts/ranges, and recommendations; can also extract a repo's "coding philosophy" to feed forward into generating/reviewing other apps. Reverse-engineering old C/AL→AL apps floated as a use case.

### Verify before trusting
- Product/marketplace/spec domains (`agentskills.io`, `clawhub.io`, `skills.sh`, `skills.md`), the name "OpenClaw", "Moldbook", presenter names, and "Microsoft Scout" all come from auto-captions — confirm spelling/existence independently.
- BC MCP OAuth PR status: check the actual repo and Microsoft Learn.

<!-- ingested: Microsoft Presents: Prompt Engineering: From Concept to Real | 2026-07-27 -->
### Prompt engineering for BC Copilots (Microsoft session)

**Message roles**
- Three roles: system (aka meta/system prompt — controls the LLM), user, assistant.
- In AL: add system message + add user message; the assistant response is added automatically. `[sic?]` exact method names not shown — verify against Microsoft Learn / compiler.

**Iterating a prompt (worked example: email → intent)**
- Progression to get usable output: (1) plain instructions → verbose natural-language response, unusable in AL; (2) name explicit actions/intents (e.g. `create sales quote`, `get order status`) → predictable keyword; (3) demand JSON output → parseable; (4) sub-instructions to split item name vs features; (5) an explicit example response format to force features into an array not key-value pairs.
- Test against a wide range of inputs — a prompt that works on one example often fails on the next. Adding a concrete example fixes cases that instructions alone don't.
- `create sales quote` / `get order status` are conceptually AL functions to be called. Caption transcript says "sales code" — that is a caption garble for **sales quote** `[sic?]`.

**Function calling (tool calling)**
- Preferred default over hand-rolled JSON instructions. Give the model function definitions (name, optional description, parameters) → model knows capabilities + arg schema.
- Output is JSON-formatted by default; no need to specify format in system prompt. Drastically shrinks the system prompt.
- Define parameters incl. arrays (items, features), and mark mandatory fields (e.g. customer info + item name) as the bare minimum for the action.
- Response comes back as a tool_calls entry of type function with an arguments object.
- In AL: specify tools (e.g. add tool), plus system + user prompt. `[sic?]` verify exact AL API (Chat Completions / AOAI tool API).
- Keep function list small: ~8 functions is a practical upper limit; more degrades the model's ability to choose correctly unless functions are very distinct.

**Safety — the "magic function" pattern**
- Models always want to respond; "if harmful, do not respond" tends to still produce output. Instead redirect all unsupported/harmful intents to a dedicated `magic function`.
- Handle magic-function calls in AL (throw controlled error / generic reply). Extract an `intent` param for telemetry (what unsupported things users ask).
- Use magic function for both harmful content AND any out-of-scope intent. Sets explicit boundaries for what the copilot supports.

**Grounding / validation (under the hood of shipped features)**
- Marketing Text: merges attributes with prompt, then a validate-answer function grounds the output — checks numbers/facts in generated text against actual table values (e.g. length 100cm); unmatched number = hallucination. Retries up to 5 times, else calls magic function and returns "sorry".
- Sales Line Suggestions: LLM extracts intent/keywords → classify (item search / document search / unsupported→magic function) → entity search against the DB. Validates that requested items actually exist before responding. CSV attachments: LLM picks relevant columns, extracts product info, feeds same intent-extraction path.

**Model config parameters**
- Temperature: 0–2 (default ~1, model-dependent). Low = more deterministic (never fully) — use 0 for comparison/extraction (bank rec, intent extraction) to avoid hallucination. High = creative; Marketing Text uses ~0.7. Near 2 = incoherent. Set in chat completion params.
- Max tokens: caps OUTPUT tokens only. Context window (input+output) e.g. GPT-4o ~128k. Typical max output ~32k. Reasoning-model thinking tokens count against max output too. Low limit truncates output.
- Frequency penalty: penalty grows with each reuse of a word → gradually reduces overuse. 0–2, default 0.
- Presence penalty: hard penalty on first use → discourages any reuse. 0–2, default 0.
- Recommend leaving both penalties at 0 when temperature is 0 (they can suppress words from your grounding data).

**Prompting techniques**
- Zero/one/few-shot: add examples w/o fine-tuning. More examples help more on complex tasks; benefit is model-dependent. Start with zero, add examples only if accuracy insufficient.
- ReAct (reason+act): model reasons then calls tools/functions, iterates — good for multi-step, verification, real-time data, data-driven choices.
- Structured output: guarantees a fixed (JSON) format; function calling is a subset. In BC either set JSON mode = true (prompt MUST contain the word "JSON" or the platform throws an error) or use add tool. `[sic?]` verify AL set-JSON-mode API name.
- Chain of thought: provoke non-reasoning models with "think step by step". Can embed CoT inside a function param (e.g. a `detailReason` field emitted before the `intent` field) so the model reasons then possibly corrects its intent — used in agents. Note: OpenAI models generate but do NOT return reasoning tokens; DeepSeek/Gemini expose them.

**Grounding BC data — gotchas**
- Models know BC/ERP generally but not YOUR environment/config.
- Opaque item IDs (e.g. `item 2023 FG EU`) mean nothing to the model — supply friendly name/description.
- SKU: in BC it also includes location code (item no. + variant + location), not just item/variant as elsewhere — spell this out.
- Decode coded fields: e.g. document type 3 = Credit Memo — provide the mapping; don't assume the model knows enum values.
- Provide field captions, units, business rules.
- Terminology mapping: jobs = projects (renamed, used interchangeably); BC uses "vendor" not "supplier" — tell the model synonyms external users may use.
- Currency: when summarizing customer/transaction data, include the currency per transaction, else totals are wrong. Model has no exchange rates — if you omit them it invents rates (its training data), factually wrong.

**Hallucination / factual accuracy**
- Model fills any gap in the prompt. In finance-heavy ERP this is dangerous.
- Mitigations: ask model to cite document ID/reference then sanity-check in AL; validate the answer against BC before showing it; instruct "only use information provided; if unsure, call magic function". Trust but verify every response.

**Token limits / large data**
- GPT-4 ~128k tokens ≈ ~90k words, but more tokens → lower quality, higher latency, higher cost. Rough cost rule-of-thumb quoted: ~1¢ per extra 1k prompt tokens, ~3¢ per 1k completion tokens per request.
- GPT-4 accuracy benchmark: high at 8K–32K tokens, noticeable dip beyond. Use tokens efficiently.
- Big-data pattern (e.g. item search over many items): don't dump the whole table. (1) LLM extracts keywords/intent from user query, incl. synonyms/alternate terms/plurals (bike↔bicycle); (2) pre-filter items in AL using those keywords (OR filters on name/description); (3) send only the filtered subset back to LLM to rank/pick best match. Also apply to sequenced prompts — split calls so each gets only what it needs rather than resending huge context.

**Maintainability & testing**
- Treat prompts as executable specs / code; keep in source control; pin "this prompt works with this model + this config + this BC version."
- Model drift is real even within a model family (not just 4.0→4.1): a 4.0 iteration once returned marketing text ~20× longer; a newer CSV response silently added a confidence column and broke AL parsing.
- Newer models take instructions more literally (4.1 vs 4.0) — can drop performance; re-tune prompt on every model change. Aim for latest model but never assume the old prompt keeps its accuracy.
- Re-run full test suite on: model switch (mandatory), config change, AND any product change (e.g. jobs→projects rename can break a copilot with no LLM change).
- Run tests daily/weekly via automated pipelines + telemetry; alert on accuracy drop. Convert every bug into a test case.
- Use the BC Copilot test tool: one feature vs hundreds of input test cases with expected outputs. Keyword-extraction features → assert exact output in AL; free-text features (marketing text) → need separate evaluation (can't assert exact string).
- Azure OpenAI deployment has a version-upgrade setting: always-latest / upgrade-at-end-of-life / no-auto-upgrade. Patches otherwise apply automatically.

**Misc tips**
- Markdown is the preferred prompt format internally — fewest tokens vs JSON input, and models parse it well (# = title levels).
- You can ask Copilot itself to refine/enhance your prompt.
- Azure AI Foundry "generate prompt": feed 1–2 sentences → get a full end-to-end prompt (steps, output format, examples) to validate a use case fast. Foundry chat playground doesn't handle function calling well; team uses Insomnia for testing tool calls.
- Multi-language: keep prompts in English (models perform best in English) but instruct the response language (e.g. German/Danish for marketing text); non-English accuracy improving, close to English for GA'd features.

Source: mibuso YouTube, auto-captions — identifiers unreliable; "sales code"→sales quote, verify AL API names against Microsoft Learn/compiler.

<!-- ingested: Microsoft Presents: Data-Driven Copilot Experiences in Busin | 2026-07-27 -->
### Copilot Autofill & Summarize (BC) — platform data-driven experiences

**Status/availability**
- Both features public preview (as of talk, 2026). BC online desktop only. Trial, sandbox, production all supported.
- English fully supported; other languages available but may under-perform.
- Work on custom pages/fields out of the box but **not directly extensible in AL yet**.
- On by default for all users; admins disable via Copilot capabilities page. Each ships a distinct permission set, so admins can scope to selected users.

**Autofill**
- Data-entry assist. Invoke via sparkle icon; fills empty fields on the current FastTab scope where invoked.
- Pipeline: gather page/user/role/field metadata → query multiple suggestion providers in parallel per field → AI ranks/grounds → surface single best suggestion (plus alternates in UI).
- Suggestion providers (~5-6): most-recently-used value, most-frequently-used value, intelligent lookup selection, AI-generated, web search (Bing, shipping later this wave).
  - Most-recently-used: no LLM, purely BC data, tracks last-access recency per record.
  - Most-frequently-used: company-wide scope, respects permissions, no LLM.
  - Lookup selection: uses LLM to pick best from a finite option set (lookups + option fields). Filters on finite lookups respected.
  - AI-generated: foundational model knowledge, risk of fabrication → grounded against BC data.
- Limitations: boolean and date fields not yet supported (expansion planned). No suggestion returned when providers/AI judge suggestions not relevant — deliberate (no bad values forced).

**Summarize**
- Adds a **summary fact box** on card + document pages showing top 3 role-tailored important/urgent items; "show more" expands to additional bullets.
- Interactive: clicking a bullet highlights the source field/fact box or opens the related page; can expand collapsed FastTabs. Refresh regenerates after data edits. Integrates with chat pane for follow-up actions.
- Pipeline: collect user role → gather entity data (fields, fact boxes, related high-aggregate pages) → LLM derives insights → score by context → emit top-3 interactive markdown.

**Summarize data sources (what AL devs control)**
- Fields visible on the page; for document pages, subpage/line parts also sent. Respects permissions, personalization, customization.
- Fact boxes: sent as related data, but excludes system fact boxes (links, notes) and fact boxes with a `Provider` property [sic? — verify property name] (those indicate selected line on document pages).
- Related statistics pages: derived from page actions that have a `RunObject` property [sic? — verify]. Filtered to page names containing "statistics"/"stats" for performance + because they carry aggregated/analytical data. Filters defined on the action are respected (e.g. action filtered to the card's customer → only that customer's data sent).
- User info: from user settings; **role** is the key input for role-tailored summaries.

**AL dev guidance (influence quality via metadata)**
- Features are not AL-extensible, but metadata heavily drives accuracy/performance.
- Write descriptive English tooltips, field/page descriptions, and teaching tips — AI draws context from these.
- Use role-tailored profiles: improves results, security, segregation of duties.
- `AboutTitle`/`AboutText` teaching-tip (onboarding) properties are page-level only; no plan to add table-level equivalents.

**Responsible AI** — built on six principles: fairness; reliability & safety; privacy & security; inclusiveness; transparency; accountability. Thumbs up/down feedback feeds iterative summary evaluation.

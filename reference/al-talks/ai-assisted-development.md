# ai-assisted-development

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: AL Development in the AI Era | 2026-07-27 -->
### AI-assisted AL development (Cursor / Copilot vibe coding)

**Context is the lever, not the prompt**
- Bare prompts ("create setup structure") yield generic, often wrong AL. Feed structured context instead.
- Recommended context stack: business requirements (PRD), a technical *development plan*, and coding-standard rules.
- Cursor *rules* = files under `.cursor/rules/` auto-injected into every agent request as context. Author them from AL best-practice sources (e.g. AL patterns site) covering naming, folder structure, patterns.
- Generate a development plan from the PRD first; regenerate it after adding rules so it adopts your folder conventions and phased breakdown.
- Models have a training cutoff — they don't know newer AL features or niche APIs; you must supply that knowledge explicitly.

**Feeding missing knowledge (RestClient example)**
- Models default to `HttpClient` and don't know the `RestClient` module `[sic?]` (verify: System Application `Rest Client` codeunit family) because web docs are sparse; agent tried, searched web, failed, reverted.
- Workaround shown: (1) transcribe a webinar to text for the *conceptual* how-to, (2) ask the agent to generate architecture/workflow/public-model docs *from the System App source itself*, (3) feed both back → agent reimplements correctly, collapsing calls to ~1 line.
- Then have the agent write a reusable rule ("always use RestClient, with do/don't examples") so future projects reuse it.

**Workflow discipline**
- Work in phases: setup tables/pages → master data import → business logic → custom APIs → tests.
- Keep chats short; start a new chat per feature — long chats confuse the model.
- Commit per AI iteration. When a long fix-loop finally works but code is bad: ask agent to summarize failures, regenerate the dev plan, roll back to a prior commit, reimplement with new knowledge.
- Maintain a "learnings" file the agent appends to (what worked/failed) and reads next run.
- Escape the "please fix" loop by pasting relevant Base App code into the agent as reference.

**Where AI is weak in AL**
- Business logic and BC internals: picks wrong events (e.g. used `OnAfterPostSalesDoc` [sic?] then referenced already-finalized sales header/lines), forgets requirements mid-task, no accounting knowledge (deposits/refunds), doesn't know new features unless told.
- Adding a field to Item Ledger Entry: agent doesn't grasp it must flow via Item Journal Line → posting; needs a developer.
- **Security blind spot (gotcha):** generated custom API exposed customer balances with no data filtering — every customer could read all customers' data, and API access can imply broad BC data access unless a scoped permission set is assigned. AI won't add this; you must.

**Where AI is strong**
- API/integration boilerplate, test code, documentation generation.
- Semantic search over the pre-indexed Base App in the agent tab (find code without knowing keywords).

**Tests**
- "Tests can't be better than your code" — don't fix failing tests with AI; failing tests reveal where generated code is wrong. Read and fix the implementation manually.

**Model selection in Cursor**
- Choose model per call. Thinking models (plan-then-act) — pricier/slower — for complex features and dev-plan generation; classic models for generic code. Presenter's default for AL: Claude Sonnet `[sic?]`; Gemini for docs/generic; OpenAI models rated weaker at AL (anecdotal).
- Cursor $20/mo subscription includes most models; premium (e.g. o3) costs extra.

**IDE symbol awareness**
- Complaint: Copilot/agents hallucinate standard BC methods that don't exist.
- Latest VS Code Copilot can reference *symbols* (installed app symbol files) in chat, reducing made-up methods. Cursor lacked this at talk time — workaround is keeping Base App open and pasting code manually.

**Why models are poor at AL (rationale)**
- LLMs trained on GitHub; AL has orders of magnitude fewer repos than Python. AL syntax is now decent, but business-logic/base-app knowledge is under-represented. Microsoft reportedly consumes third-party models rather than training BC-specific ones (unverified claim).

**Human-side technique for correct design (contrast approach)**
- Deposit/keg modeling done "by hand": kegs = items flagged as deposit, linked via a unit of measure; deposit lines created on sales order *release* and removed on *reopen*; deposit line VAT = 0 (but purchase VAT still applies); use posting groups for GL routing; store deposit amount on Item Ledger Entry (not Value Entry) via Item Journal Line + subscriber, because Sales Amount is itself a flowfield.
- Useful one-liner discovered: force sub-form totals refresh after inserting lines on release — `[sic?] force totals calculation` (verify exact API on sales sub-form).
- Demo data via a `.rdlc`/resource file read at install: `NavApp.GetResource` [sic?] as text, parse with JSON object helpers (`Get Boolean/Integer/Text`) — presenter used a markup/JAML-like resource for readability.

**Conclusion**
- Best results = blend: human functional design + AI code generation. AI generates; a developer ("captain") owns the design, business logic, security, and ships the result.

**Related tool (open source)**
- "BC code interpreter" (GitHub, author's): natural-language data insights over BC. Generates Python run in an Azure Function; discovers relevant BC APIs, pulls+combines data, returns charts. No raw data sent to LLM — only API results interpreted. `[sic?]` verify repo name.

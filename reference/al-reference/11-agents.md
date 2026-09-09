<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# AI agents in BC — functional concepts & setup

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 28. AI Agents in Business Central (functional context — not AL syntax)

Platform knowledge for extensions that touch or complement BC's agentic features. For the
**AL coding API** (agent types, interfaces, task/message codeunits) see **§29**. Sources:
Encore webinar + Microsoft's official dev sessions 2026-02 (`reference/transcripts/bc-agents-*.md`)
+ Microsoft Learn (actively updated — verify specifics there before relying on them).

**Model.** An agent = a confined AI role for ONE business process. Two delivery modes:
pre-built agents from Microsoft (Payables Agent, Sales Order Agent; more coming) and
build-your-own via the **Agent Designer** inside BC (new — previously required Copilot
Studio outside BC).

**Setup pattern (all agents).** An agent is set up like a user: its own **profile** (the UI
it sees), its own **permission set** (minimum for its task), and a **user access list**
(which humans monitor its human-in-the-loop pane). Effective permissions are ALSO bounded
by the interacting user's permissions — layered security. Everything is logged per task,
including Copilot credit consumption.

**Billing.** 1 Copilot credit ≈ 1 US cent. Payables Agent: 50 credits/document + 5/line.
Agent Designer shows per-case credit burn while stepping through — tighter instructions =
cheaper agent.

**Payables Agent** (GA mid-2026):
- Dedicated email address; invoices arrive from internal finance forwarding and/or selected vendors directly.
- OCR reads the invoice → draft purchase invoice; matches (or optionally creates) the vendor; resolves **vendor item references** to BC item nos.; suggests G/L accounts; matches to existing POs.
- Agent-created values are flagged with an info icon + rationale; corrections made at review are **remembered for next time**.
- Human-in-the-loop review before anything posts; KPIs (time saved, emails handled) on the agent icon.

**Sales Order Agent:**
- Customer emails in natural language (or PO PDF/image attachment) → multi-turn email exchange → sales quote with **customer-specific pricing** (honours BC price lists/discounts, e.g. qty breaks) → converts to order on customer confirmation.
- Checks inventory, unit of measure, item attributes/variants; optional capable-to-promise (quote incoming supply, not just on-hand).
- Config: shared mailbox; respond to registered/unregistered senders; **autonomy levels** (validate-everything → fully autonomous quote generation); daily email cap (spam guard, default 100); email signature (rich-text).
- Pausable — intended to switch on for peak periods.
- **2026 updates:** attachment analysis (PDF + images incl. photographed invoices — classifies relevant/reviewed/unsupported); rich-text custom **email signature**; per-sender-type autonomy (registered vs unregistered each get review-all / review-first-in-thread / fully-automatic); **capable-to-promise** earliest-ship-date calc for out-of-stock items; **skip-quote** autonomy (uncheck "review sales quote" → creates the order directly for registered senders when stock allows); natural-language instructions to unblock mid-task ("use the Berlin chair instead").

**Expense Agent** (NEW pre-built — fills BC's historic no-expense-management gap):
- Receipt → reimbursement: AI OCR (incl. handwritten) extracts merchant/amount/date → auto-categorise → itemise (e.g. split a hotel folio, per-diem by location) → groups into a default **expense report** → user reviews → submit. Auto currency conversion to home currency.
- **Three intake channels:** M365 Copilot chat, a shared mailbox, and a **dedicated web app for non-BC users** (Entra sign-in; drag-drop receipts). All route through an **expense-agent service** that writes to BC's expense app module via API.
- **Rules vs Policies:** Rules = strict numeric caps (max amounts, daily/fixed rates) in a BC table, 100% enforced; Policies = language-based conditions (business-class eligibility, hotel star limit), approval-driven (still rolling out).
- **Approvals:** submit → *pending approval* (submitter locked out) → approver notified (email/Copilot chat), has a "For my approval" tab, can approve or send back with a comment. State syncs to BC.
- **Licensing quirk:** submitters need **no BC licence** (billed via Copilot credits); managing/submitting = Team Member; posting = Essentials/Premium; **approvers MUST hold a BC licence** even when approving from the web app (GL consequences). Config: search "expense agent" in Tell Me → set agent email, load initial setup data (categories, posting groups), import **Expense Users** (has a "can approve" flag; supports expense teams).

**Payables Agent — 2026 updates:** preview in US/UK/AU/NZ moving to worldwide GA; agent-created vendors get **Blocked = All** (respects onboarding due diligence — must unblock before proceeding); autonomy dial can **skip the initial email review** (straight to PDF analysis). Roadmap: better vendor matching, 2-/3-way PO matching, e-invoice sourcing, in-agent approvals, auto-posting, payment suggestions.

**Credit consumption & billing (admin).** Copilot credits are Microsoft's shared AI currency; a BC licence grants free monthly credits, overage via **pay-as-you-go** (Azure subscription) or pre-purchased packs. **View Consumption Data** on the agents list works for custom *and* Microsoft agents (per-entry: timestamp, credits, capability, agent user, action). **Agent Tasks** list has a per-task *Copilot credits consumed* column, drillable to per-step charges. Viewing consumption needs the **Agent Diagnostics** permission set or SUPER — **Agent Admin is not enough** (it only enables/configures agents). PAYG setup is a multi-step Azure/Power-Platform-admin flow (resource group → billing plan with product = Copilot Studio → PAYG environment → link the Dataverse env to BC via **Environments → Link**); full steps in `reference/transcripts/agent-billing-pay-as-you-go.md`.

**Agent Designer** (build-your-own, in-BC; positioned as proof-of-concept tooling):
- **Instructions are the product.** Natural language, as concise as possible, refined iteratively (history kept — revert/tweak). Use an indented-bullet hierarchy for step-by-step behaviour, and open by giving the agent a **role** ("You are the ... for ..."). Instructions compile into **tasks & steps**; edit those only for fine-tuning — fix behaviour at the instruction level first.
- Your instructions run as a subset of a larger hidden Microsoft governing prompt (compliance + prompt-injection protection).
- Step-through testing per case: agent's decision, what it saw, tools available, memory, credits burned at each step.
- Three interaction tools: **user intervention** (agent needs help), **user review** (validate my work), **response action** (outbound email/chat).
- Train while testing: thumbs up/down on agent-created data feeds the next iteration — feedback loop matters.
- Ships with a sales-validation template. Demoed customs: project assistant (creates project + WBS phases/tasks from the customer's project history), materials-consumption agent (creates assembly BOMs from shop-floor consumption reports).
- Web-client authoring is **preview, sandbox-only**; deploy-as-extension to production comes later. Automated agent **evaluation** (score results across instruction iterations) is coming.

**Writing agent instructions (Microsoft's own practice).** The instructions ARE the agent —
get them right before touching tasks/steps.
- **Less is more.** Modern models don't need every step spelled out — outline only the important steps of the business process. Over-specifying lowers accuracy.
- **Role-based prompting** first: open with who the agent is and its goal ("You are the accounts-receivable agent…"). Sets context, improves accuracy.
- Structure Microsoft uses: a **Guidelines** section (rules applying to *all* tasks — comms/email formatting, e.g. "never post a draft credit memo before user review", "if the customer has no email/number, check the customer list") + a **business-specific** section per task (numbered process steps).
- **Instructions always win over task messages** (platform gives them higher priority). Put the reusable process in instructions; use task messages only for what *varies* per task (which invoice, which customer). Don't repeat the process in every task.
- **Sub-steps in instructions become timeline captions.** The begin/end timeline messages are platform-controlled (title settable via SDK); the sub-steps between come from how you structure the instructions.
- **Agent size:** no fixed rule. One agent can do multiple tasks if they're different enough; if adding instructions drops accuracy, split into multiple agents. One task can chain to another ("…when done, suggest money-raising opportunities").
- **Page-specific instructions:** instructions can be scoped to load only when the agent is on a given page. Syntax seen as Liquid-style (`{% if page = … %} … {% endif %}` per the runtime team) — verify exact form against Microsoft Learn before using.
- **Accuracy levers:** bold/UPPERCASE emphasis and strong wording ("you MUST NOT…"), numbered steps, richer error messages + tooltips (the agent reads and recovers from them), and **smaller profiles** (less UI to navigate = higher accuracy). Treat the agent as a usability tester — if a human struggles with an unintuitive task, so will the agent.
- Instruction **history** is versioned — a version is saved automatically **every time a task runs** (not per keystroke), plus a manual **Save to History** (nameable). Revert via history if a change hurts accuracy. **Download** one version to disk, **Download Selected** several as a **zip** (for external diffing — the client has no built-in diff). History is **NOT** included in agent export — download it separately to preserve it.

**Document reading.** PDFs/images attached to a task go through **Azure Document Intelligence**
for text extraction — the LLM then reasons over the extracted text (e.g. reads invoice lines, a
described "broken leg / 30cm scratch"). It is **text extraction only, not machine vision** — the
agent won't count objects in a photo. For true vision you'd wire a different tool.

**Two integration paths — native BC agents vs Copilot Studio.** Native BC agents (§29) live
inside BC, act as a user over the UI, target back-office/core-ERP automation. **Copilot Studio**
agents (Power Platform, low/no-code, usage-billed via credit packs — no extra BC user licence
for consumers) are for cross-system front-office / conversational experiences and reach BC data
two ways: the **Power Platform connector** (→ BC APIs) or the **BC MCP server** (→ BC APIs). The
MCP server lets any MCP client (Copilot Studio, M365 Copilot chat, VS Code, …) consume BC over the
open **Model Context Protocol**. Roadmap: calling native BC agents *via* MCP from Copilot Studio.
**AL relevance:** the API pages you build (§23) are what MCP exposes — see **§31** for authoring and
scoping MCP configurations.

**Relevance when writing AL:** agent-created records carry provenance (the info-icon
rationale); agents operate through profiles + permission sets you may need to extend
(§26 — grant an agent's permission set access to your extension's tables or its drafts
fail); subscribers on document tables fire during agent processing too — keep them cheap
and never hard-`Error` on non-critical side effects (§25), or you abort the agent's draft.

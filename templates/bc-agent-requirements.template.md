# Business Central Agent — Requirements Gathering Workbook

*Customer discovery & scoping for a BC AI agent engagement — 2026-07-08*

**Purpose.** A structured discovery tool to run *with* a customer to decide **whether** an AI agent
fits their Business Central process, **which** kind of agent to build, and **what** is needed to
build it. Work through it in a workshop; capture answers in the tables. By the end you should have
enough to choose a delivery path and produce a build backlog.

**How to use it.**
- Sections are ordered as a conversation: opportunity → path decision → detailed requirements →
  security → testing → cost → sign-off.
- Do **Part A** and **Part B** in the first session; they decide everything downstream.
- Skip the requirement sections that don't apply to the chosen path (Part B tells you which).
- Everything is a working draft — Microsoft's agent features change fast; verify version-specific
  detail against Microsoft Learn before committing dates or limits to the customer.

**Key framing for the customer.** A Business Central agent is a **confined AI role for ONE business
process**, set up like a *user* — it gets its own login profile (the UI it can see), its own
permission set (the minimum for its job), and a list of humans who monitor it. It acts through BC's
normal screens, everything it does is logged, and a human reviews its work before anything commits.
It is not a chatbot bolted on the side; it is a co-worker with tightly drawn boundaries.

---

## Part A — Opportunity & business case

*Goal: confirm there is a real, valuable, agent-shaped process here before designing anything.*

### A1. The process

| # | Question | Capture |
|---|----------|---------|
| A1.1 | What single business process do you want to automate? (one process per agent) | |
| A1.2 | Who does it today, and roughly how long per case / per day? | |
| A1.3 | What triggers the work — an email, a document arriving, a scheduled run, a user action in BC? | |
| A1.4 | What does "done" look like for one case? (a posted invoice, a sales quote sent, an expense report submitted…) | |
| A1.5 | Volume: how many cases per day / week / month? Any seasonal peaks? | |
| A1.6 | What is the pain today — cost, delay, errors, backlog, staff time on drudgery? | |
| A1.7 | What is the value of fixing it? (hours saved, faster cycle time, headcount avoided, fewer errors) | |

### A2. Agent-fit check

An agent is a good fit when the process is **repetitive, rules-based, document- or message-driven,
and tolerant of a human review step**. Score each:

| Criterion | Y / N / Partly | Notes |
|-----------|----------------|-------|
| Repetitive and high-frequency (worth automating) | | |
| Follows describable rules a person could write down | | |
| Driven by inbound documents or messages (email, PDF, form) | | |
| A human can review output before it commits (tolerates human-in-the-loop) | | |
| Mostly lives *inside* BC (data + actions are in BC) | | |
| Low cost of an occasional wrong draft (caught at review) | | |

> **Red flags** (push back or rescope): needs real-time decisions with no review window; requires
> true machine *vision* (counting/measuring objects in a photo — the agent extracts *text* only, it
> does not "see"); spans many disconnected systems with complex orchestration; the rules can't be
> articulated; regulatory process where an unreviewed AI action is unacceptable.

### A3. Baseline & target metrics (define now, measure later)

| Metric | Baseline (today) | Target (with agent) |
|--------|------------------|---------------------|
| Cases handled per day | | |
| Avg. handling time per case | | |
| Error / rework rate | | |
| Cycle time (trigger → done) | | |
| Staff hours per week on this task | | |

---

## Part B — Delivery path decision

*Goal: pick the cheapest path that meets the need. Do NOT default to a custom build.*

### B1. The four paths

| Path | What it is | Best when |
|------|-----------|-----------|
| **1. Pre-built Microsoft agent** | Payables, Sales Order, or Expense agent — configure, don't build | The process matches one of the three (see B2). Fastest, cheapest. |
| **2. Agent Designer (in-BC, no code)** | Build-your-own with natural-language instructions inside BC | Bespoke process, standard BC data/pages, no custom AL needed. Note: currently **preview, sandbox-only** for authoring; production deploy-as-extension is maturing — confirm current status. |
| **3. Custom AL-coded agent** | Agent built as an AL extension (agent template + interfaces) | Needs custom tables/pages, programmatic task creation, tight validation, cross-app exposure, or shipping as a product. |
| **4. Copilot Studio agent + BC data** | Power Platform agent reaching BC via connector or the BC **MCP server** | Cross-system / front-office / conversational experience that spans beyond BC; consumers who shouldn't need a BC user licence. |

> Paths are not exclusive. A common shape is a **native BC agent (2 or 3)** for the back-office work,
> with **BC data exposed via MCP (4)** to a conversational front end.

### B2. Pre-built agent triage

If the process matches one of these, strongly prefer configuring the pre-built agent over building.

| Pre-built agent | Does | Match? |
|-----------------|------|--------|
| **Payables Agent** | Invoice email → OCR → draft purchase invoice; matches/creates vendor, resolves vendor item refs, suggests G/L, matches POs; human review before posting. Learns from corrections. | |
| **Sales Order Agent** | Customer email / PO PDF → multi-turn exchange → sales quote with customer-specific pricing → order on confirmation; checks inventory/UoM/variants; capable-to-promise. | |
| **Expense Agent** | Receipt (incl. handwritten) → OCR → categorise → itemise → expense report → approval workflow; intake via Copilot chat, mailbox, or a web app for non-BC users. | |

If a pre-built agent fits, jump to **Part C-1** (config requirements) and skip C-2/C-3.

### B3. Path decision — record the outcome

| Decision | Answer |
|----------|--------|
| Chosen path (1 / 2 / 3 / 4 / hybrid) | |
| Why this path (fit, cost, timeline, control) | |
| Paths rejected and why | |
| Open questions blocking the decision | |

---

## Part C-1 — Requirements: pre-built agent configuration

*Only if Path 1. Gather the config the customer must supply.*

| Area | Question | Capture |
|------|----------|---------|
| Mailbox | Which shared mailbox / dedicated email will the agent use? | |
| Senders | Which vendors/customers send in? Respond to registered only, or unregistered too? | |
| Autonomy | Desired autonomy level per sender type (review everything → review first-in-thread → fully automatic)? | |
| Caps / guards | Daily email cap (spam guard, default 100)? Skip-quote / skip-review conditions? | |
| Master data | Vendor/customer records, item references, price lists & discounts, G/L accounts, posting groups ready? | |
| Expense-specific | Categories, posting groups, Expense Users list (with "can approve" flag), rules (numeric caps) vs policies (language-based)? | |
| Approvals | Who approves? (note: **approvers MUST hold a BC licence**; submitters may not need one) | |
| Signature | Rich-text email signature content? | |
| Provenance | Who reviews agent-flagged values / corrections (fed back as learning)? | |

---

## Part C-2 — Requirements: the agent's behaviour (custom — Paths 2 & 3)

*The instructions ARE the agent. This is the most important section for a custom build.*

### C-2.1 Role & scope

| Question | Capture |
|----------|---------|
| One-sentence role: "You are the ___ agent for ___." | |
| What is explicitly **in** scope for this agent? | |
| What is explicitly **out** of scope? | |
| Could this be **one** agent, or should it split into several? (split if adding steps drops accuracy) | |
| Does one task chain into another? (e.g. "when done, suggest…") | |

### C-2.2 The process steps

Capture the process as the customer describes it. Keep to the **important** steps — modern models
don't need every micro-step, and over-specifying *lowers* accuracy.

| Step | What happens | Decision / rule | Data read | Data written |
|------|--------------|-----------------|-----------|--------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| … | | | | |

### C-2.3 Guidelines (rules that apply to every case)

Business-wide rules the agent must always follow (comms style, guardrails, fallbacks). Examples:
"never post a draft credit memo before user review"; "if the customer has no email, check the
customer list first."

| # | Guideline |
|---|-----------|
| 1 | |
| 2 | |
| 3 | |

### C-2.4 Edge cases & exceptions

| Situation | What should the agent do? |
|-----------|---------------------------|
| Missing / ambiguous data | |
| Duplicate or conflicting record | |
| Amount / quantity outside normal range | |
| Can't complete the task | |
| Suspected bad / malicious input | |

---

## Part C-3 — Requirements: data, documents & systems

| Area | Question | Capture |
|------|----------|---------|
| Trigger data | What data/message arrives to start a case? Structure? | |
| Documents | Are PDFs/images involved? (Extracted via Azure **Document Intelligence** — **text only, not vision**. Handwriting OK; counting objects in a photo is NOT.) | |
| BC data read | Which tables/pages must the agent read? | |
| BC data written | Which records does it create/update? Any custom tables? | |
| Master data quality | Is the master data it relies on clean and complete? | |
| External systems | Anything outside BC involved? (drives Path 4 / MCP / custom tools) | |
| Output | Where do results go — a record, an email reply, a chat message? | |

---

## Part D — Human-in-the-loop & autonomy

| Question | Capture |
|----------|---------|
| Which of the three interaction points are needed: **user intervention** (agent needs help), **user review** (validate my work), **response action** (outbound email/chat)? | |
| At which step(s) must a human review before commit? | |
| Who are the monitoring users (the access list)? | |
| Desired autonomy now vs. later (start supervised, loosen over time)? | |
| Can the agent be paused (e.g. on/off for peak periods)? | |
| How is the agent unblocked mid-task (natural-language nudge)? | |

---

## Part E — Security, permissions, profiles & licensing

*The agent runs as the **intersection** of the invoking user's permissions AND its own permission
set — never more than either. A tighter profile also means higher accuracy (less UI to reason over).*

| Area | Question | Capture |
|------|----------|---------|
| Permission set | What is the **minimum** set of tables/objects the agent needs? (trim Edit/Delete not needed) | |
| Custom objects | Does the permission set need access to your extension's tables/drafts? (or the agent's actions fail) | |
| Profile | Which role-centre/profile should the agent see? Can it be trimmed to only the pages/fields it needs? | |
| Field presence | Are all fields the agent must set actually **on the profile/page and editable**? (No.1 cause of agent failures) | |
| Data classification | Any sensitive/PII data in scope? Handling constraints? | |
| Licensing | Who needs BC licences? (e.g. Expense: approvers must be licensed; submitters may not) | |
| Governance | Who owns enabling/disabling the agent (Agent Admin) vs viewing consumption (needs **Agent Diagnostics** or SUPER)? | |

---

## Part F — Integration & exposure (if Path 3 / 4 / hybrid)

| Question | Capture |
|----------|---------|
| Does another app / front end need to drive this agent? (needs a public API codeunit surface) | |
| Expose BC data to external AI via **MCP server**? Which API pages? Read-only or modify? | |
| MCP client target (Copilot Studio, M365 Copilot chat, VS Code…)? Tool-count budget (Copilot Studio caps ~70; each page counts twice)? | |
| Rich **AboutTitle/AboutText** on API objects planned? (measurably improves the AI's tool choice) | |
| Auth model for external hosts (Entra app registration needed)? | |

---

## Part G — Testing & acceptance

*Agents are non-deterministic — you don't write exact-match tests, you write **evaluations** that
measure accuracy/quality/safety over representative inputs.*

| Question | Capture |
|----------|---------|
| What does "good enough to go live" mean? (target accuracy %, which outcomes must be right) | |
| Representative test cases: happy paths (P0), edge cases (P1), oversized/load, context variations? | |
| Source of test master data? (build your own — the model has *memorised* the demo company, so demo-data tests don't prove real behaviour) | |
| Acceptance criteria per scenario (message-to-review / records-to-review / user-intervention + expected records)? | |
| Who signs off go-live? | |
| Environment for eval runs (**sandbox only** for the test runner — no on-prem/Docker)? | |

---

## Part H — Cost & Copilot credits

*Agents consume **Copilot credits** (≈ 1 US cent each). Tighter instructions = cheaper agent.*

| Question | Capture |
|----------|---------|
| Estimated cases/month × credits/case = expected monthly credit burn? (Agent Designer shows per-case burn while testing) | |
| Free monthly credits from BC licence vs. expected overage? | |
| Overage model: pay-as-you-go (Azure subscription) or pre-purchased packs? | |
| Who owns the PAYG / billing setup (multi-step Azure / Power Platform admin flow)? | |
| Budget ceiling / alert threshold? | |

---

## Part I — Constraints, risks & non-goals

| Item | Capture |
|------|---------|
| Hard constraints (compliance, data residency, deadlines) | |
| Preview-feature risk (authoring sandbox-only, features shifting) — acceptable? | |
| Explicit non-goals (what this agent will NOT do — manage scope) | |
| Dependencies / blockers (data readiness, licences, environment access) | |
| Rollback / fallback if the agent underperforms | |

---

## Part J — Summary & next steps

| Item | Outcome |
|------|---------|
| Process | |
| Chosen path | |
| Value case (baseline → target) | |
| Key requirements (top 5) | |
| Open risks | |
| Success metrics | |
| Immediate next steps & owners | |
| Sign-off (name / date) | |

---

## Appendix — Glossary

- **Agent** — a confined AI role for one business process, set up like a BC user (profile +
  permission set + monitoring users).
- **Agent Designer** — in-BC, no-code tool to build agents from natural-language instructions.
- **Instructions** — the natural-language definition of the agent's behaviour; the primary product.
  Split into *Guidelines* (all-task rules) and per-task process steps. Higher priority than task messages.
- **Task / Message** — a task is a unit of work for one agent instance; input messages give
  case-specific context; the agent replies with output messages.
- **Human-in-the-loop** — the review step before an agent's work commits; three interaction points:
  user intervention, user review, response action.
- **Autonomy level** — how much the agent does without review, dialable per sender type / condition.
- **Document Intelligence** — Azure OCR/text-extraction the agent uses on PDFs/images (**text only,
  not machine vision**).
- **MCP server** — Model Context Protocol server exposing BC (over API pages) to external AI clients.
- **Copilot credits** — Microsoft's AI usage currency (~1 US cent each) that agents consume.
- **Profile** — the trimmed UI the agent sees; smaller = more accurate.
- **Permission set** — the minimum object access the agent has; effective rights = intersection with
  the invoking user's rights.

---

*Grounded in Microsoft BC agent guidance current to mid-2026 — verify version-specific
limits and preview status against Microsoft Learn before relying on them with the customer.*

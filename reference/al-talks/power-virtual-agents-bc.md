# power-virtual-agents-bc

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2023 - How to connect Power Virtual Agent and Bu | 2026-07-27 -->
### Power Virtual Agents + Power Automate + Business Central

- Pattern: chatbot (Power Virtual Agents, now Copilot Studio) → Power Automate flow → Business Central API. Bot collects input, flow reads/writes BC, response returned to chat. Lets external users create BC records (e.g. sales orders, customers) via conversation without direct BC access.

**Power Virtual Agents structure**
- Conversation organised into **topics**. Advice: many small topics, redirect between them, over one giant bot — easier to maintain.
- Each topic starts with a **trigger** = phrases that start it. Recommend 5–10 trigger phrases so NLU generalises.
- Nodes: ask question (multiple-choice, or free "user response"), show message, redirect to topic, call action (Power Automate), transfer conversation (creates case in connected case-management app).
- Rename node variables — not always needed downstream but essential to track state in complex bots.
- Email question type validates email format (`@` + domain).
- Built-in Lesson 1/2/3 trial topics good starting examples.
- Analytics tab: session outcome, customer satisfaction score, drop-off node per topic.

**Adaptive Cards**
- Built at adaptivecards.io [sic? — verify domain] — free with Microsoft account, drag-drop inputs, outputs JSON.
- Paste card JSON into a PVA node; inputs auto-become bot variables (input/output) usable downstream.
- Each input field JSON defines: type, id (the variable name used to map into BC), required flag, error/placeholder text.
- Card cannot read BC data directly. To populate a dropdown/lookup you must define a **data source** and feed it into the chatbot separately — no live DB read. Extra work + a limitation for validation/lookups.
- Purpose is visual/grouping multiple questions in one card; not required — can fall back to sequential question/answer nodes.

**Power Automate → BC actions**
- Flow for a bot is created via the node's **Call an action** → new flow; gives fixed input/output shape matching PVA — cannot author from scratch for the bot.
- BC connector actions used: **Create record**, **Find record** (Get records). Common params: Environment, Company, API category **v2.0** [sic? — confirm exact BC connector version label], Table.
- Sales order = header + lines. Order of ops in demo: Create record (Sales Orders, needs Customer ID) → Find record (Items, filtered) → Create record (Sales Order Lines).
- Find record filter query uses OData syntax, e.g. `number eq '<value>'` [sic? — verify field/operator against BC API]. Filter is where you scope what the end user may reach.
- Sales order line create loops (Apply to each) over found item IDs → supports multiple line items automatically.
- Amount fields available include with/without tax (e.g. amount including tax) [sic? — confirm exact field names].
- Return values to bot: initialize string variables, Set variable from BC fields (order no, display name, amount), Compose a final combined message, output the Compose result as the flow's single return value → bot inserts it as a message.

**Behaviour / gotchas**
- BC item lookup is case-sensitive by default; typing must match casing unless the field's "not case sensitive" setup is changed.
- Ambiguous name (multiple items/customers sharing name fragment) → design bot to ask for a more specific name (the "complex" flow variant).
- Parallel requests: each order triggers a separate flow run; runs don't overlap IDs. Presenter claims tested handling of a few hundred concurrent requests. Number-series contention still a theoretical BC bottleneck at very high volume.
- Error handling lives in the Power Automate flow (configure steps); surface error to user or admin.

**Deployment / channels**
- Publish button pushes all changes live to every connected channel at once.
- Native channels: Teams (no extra install), Power Pages / Power Portal (add chatbot component, scope to all or specific pages). Also Skype, Facebook, Telegram, and **custom website via iframe embed code**. Channel list is limited but covers common cases.
- ALM: export solution to move bot + flows across environments (dataverse solution). Connections/naming may need re-pointing per environment; global variables can be included.

**Licensing**
- BC connector from Power Platform needs a **premium** Power Automate/Power Apps license.
- Power Virtual Agents needs its own separate license; presenter recalls ~2000 sessions included, +$100 per extra 1000 sessions [sic? — verify current Copilot Studio pricing/session terms].

**In-BC chatbot idea (Q&A)**
- Embedding the bot inside the BC client: use a control add-in ~1×1 px with high z-index + HTML overlay, bound high in the page hierarchy, to surface the chat as an overlay; wire error-code→message mapping via Dataverse. Dataverse integrates natively; BC less so but workable.

_Source: auto-captions — verify all BC connector action names, API version label, OData filter syntax, adaptivecards.io URL, and licensing figures against Microsoft Learn / the connector UI._

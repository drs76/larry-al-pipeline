# copilot-studio

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: Develop Copilot experiences with Power P | 2026-07-27 -->
### copilot-studio

- Copilot Studio (Power Platform) = tool to bring BC data into conversational Copilot experiences; not BC-only, feeds M365/Office/Dynamics copilots.
- Pricing: consumption-based — build free, pay per message/AI consumption once bot is live. Model choice affects cost (GPT-4 pricier/slower than GPT-3.5). Model now selectable per prompt.
- Quick start: search "Copilot Studio" → "Try a demo" → give a website URL (e.g. learn.microsoft.com) → chat bot answers grounded on that site. No account needed for demo.
- Grounding a bot only on a website still hallucinates (demo invented a nonexistent "cancel" action on posted credit memo). Mitigate with topics, instructions/prompts, and your own curated data.
- **Bot build blocks:**
  - *Knowledge sources* — websites, uploaded docs, and (preview) Dataverse tables.
  - *Topics* — logical flow units triggered by user intent; define step-by-step conversation. Recommended core topics: greeting, end-conversation, escalate-to-live-agent, plus one per business process.
  - *System topics* — built-in default topics (greeting/end) exist even with no custom topics.
  - *Generative answers* — enable in settings to let copilot generate responses from provided knowledge source.
  - *Actions/plugins* — same connectors as Power Automate, including a Business Central connector; call custom BC APIs to read/write data.
  - *Entities + slot filling* — extract required inputs from user before proceeding.
  - *Trigger phrases* — multiple per topic; add many phrasings, test with varied users/languages.
- **Pattern shown (time registration):** BC connector topic triggers on intent → action calls a Power Automate flow → flow runs a GPT prompt (Azure OpenAI) to parse natural-language input into structured data (return as table or JSON) → adaptive card confirm → write back to BC via custom API. Prompts are testable in a playground with sample input.
- Channels: publish one bot to Teams, web, custom portals, Power Pages, Power Apps, etc. Bot logic is shared across channels.
- Power Pages + BC integration was in public preview (~6 mo before talk) for external data-exposure portals; bots work out-of-box on those pages.
- **Dataverse as knowledge (preview):** add Dataverse table (e.g. Contacts) as knowledge + enable generative answers → data Q&A over synced data. Preview supports native Dataverse tables only; virtual tables not yet supported.
- Getting BC data into Dataverse: enable BC's Dataverse sync (setup guide, choose environment). Sync feature covers a limited fixed set of entities both ways; virtual tables expose more entities out-of-box. Guidance: if starting fresh, prefer virtual tables; use APIs + platform tools for custom/non-standard entities.
- **Custom BC data → Copilot Studio:** expose via custom AL API pages/extension, then call through the BC connector action/plugin (same as Power Automate). This is the general "bring your own data" path.
- **Permissions/auth:** configure bot authentication so calls run under a user token — BC/Dataverse permissions then apply and restrict returned data. Without auth (anonymous, e.g. public website bot) there is no per-user permission enforcement. Default Teams/Office auth available, or configure a custom app.
- **Languages:** English default; add languages in settings + supply a resource/translation file for UI strings. Panelists believed a bot must be trained per-language (English-only training won't reliably answer other languages) — `[sic?]`, unverified. Note: OpenAI officially lists English-only; Microsoft has expanded language coverage across portfolio, and BC AI features are localized across all languages since v24.2 `[sic?]` (verify version).

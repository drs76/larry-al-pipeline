<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# AI resources, agent platform, billing & models

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 5. AI Resources & Agent Platform (billing / models / geo)

*(Coding APIs for Copilot/agents are in AL-REFERENCE §29; this is the resource/billing layer.)*

- **BC AI resources** went private → **public preview** (all publishers) 2025 w1, adding
  **consumption-based direct billing** of customers by Microsoft. *(BC AI resources 2025 w1)*
- **Managed resources are SaaS + production only.** Dev/test/troubleshooting and any non-SaaS
  (container/on-prem) **must use your own Azure OpenAI** subscription (BYO). BYO only needs an
  approved/EULA-accepted subscription for the compliance check — no deployed models required.
- **Models:** managed = **GPT-4o / GPT-4o-mini** only; **no embeddings/fine-tuning** (semantic-search-
  like capability planned); reasoning models (o1/o3-mini), DeepSeek, Gemini are **BYO only**. **No
  RAG / data source** (e.g. Azure AI Search) from the toolkit at all.
- **Content safety differs prod vs dev:** managed applies a **blocking** content-safety policy
  (hate/violence/sexual/self-harm + jailbreak + basic XPIA) and **appends a meta-prompt** → managed
  output can differ slightly from BYO dev output. **Always retest in a sandbox before deploying.**
- **Deprecations:** managed model deprecations fire a **telemetry signal** (App Insights) with
  **stricter deadlines than AL deprecations**; MS auto-migrates you to the new model.
- **Data residency:** calls stay in-geo when a deployment exists; when none exists the tenant admin can
  **disable cross-geo calls** on the Copilot and agent capabilities page. MS doesn't train on / retain
  customer data.
- **Copilot Studio:** one agent can mix an MCP-server tool (scopable to one entity), a connector tool,
  a custom prompt and a Power Automate flow — the orchestrator picks per request; agents take web /
  BC-docs knowledge sources; publish to channels Teams, M365 Copilot chat, WhatsApp, Messenger, email,
  SMS. *(Copilot Studio integration)*

---

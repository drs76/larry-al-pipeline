# semantic-kernel

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Semantic Kernel: from Zero to Hero | 2026-07-27 -->
### Semantic Kernel (SK) — Microsoft AI dev kit

- Open-source SDK from Microsoft for building AI agents / integrating LLMs; the pro-code (full-code) tier of BC AI, below out-of-box Copilot features and Copilot Studio (low-code). Not embedded in AL — write in C#, Python, or Java, then call from AL (e.g. host as Azure Function, call over HTTP from BC).
- Goals it targets: provider-independence (Azure OpenAI, OpenAI, Google Gemini, Amazon Bedrock, offline), scalability, agentic patterns, RAG memory, predictable per-token cost (no per-message packages like Copilot Studio).
- NuGet package: `Microsoft.SemanticKernel` [sic?] — core; verify exact package IDs against NuGet/Learn. Java lacks OpenTelemetry logging support; otherwise on par.

#### Kernel + chat completion
- Core object = **kernel**, created via a builder: `Kernel.CreateBuilder()` [sic?], add services, then `.Build()`. Verify method names against SK docs.
- Add chat completion service per vendor, e.g. `AddAzureOpenAIChatCompletion(...)` vs `AddGoogleAIGeminiChatCompletion(...)` [sic?] — switching provider is a one-line change (model ID + API key). Verify exact method names.
- LLM is stateless out of box — no memory across calls. To keep context, maintain a chat/session history object (`ChatHistory` [sic?]) and pass it each turn, until you hit the context-window limit.

#### Memory / RAG
- Long docs exceed context window → use retrieval-augmented generation: embed doc → vectors → vector store → semantic search at query time.
- SK abstracts this via **Kernel Memory** (package `Microsoft.KernelMemory` [sic?]); a `KernelMemoryBuilder` [sic?] needs an embedding model + an LLM. Verify names.
- Ingest is roughly one line (import document path); query returns answer plus source references (from the ingested doc, not the internet).
- Pluggable vector stores: file system (`SimpleFileStorage` [sic?] — dev only), SQL Server / Azure SQL (vector support in recent release — cheap, recommended for large corpora), Azure AI Search (powerful but costly), Qdrant (3rd party). Verify store class names.

#### Plugins / functions (tools)
- Three ways to give the model tools:
  1. **Prompt templates** — `.txt` prompt + JSON config declaring description/params (e.g. `{{today}}` param syntax [sic?]). Presenter rarely uses.
  2. **Native functions** — C# method decorated `[KernelFunction]` [sic?] with `[Description]` on the method AND each parameter (model uses descriptions to pick the tool). Register via `kernel.Plugins.AddFromType<T>()` [sic?]. Verify attribute/method names.
  3. **Logic Apps** — expose workflow's OpenAPI/Swagger JSON; SK auto-discovers callable workflows via `ImportPluginFromOpenApiAsync(url)` [sic?]. Workflow must start with an HTTP "when a request is received" trigger. Lets low-code devs add tools (e.g. BC connector workflows) without C#.
- Tools do NOT count against user-prompt size / prompt token limit — attached separately. But many tools DO cost latency: model must reason over all tool descriptions to select one.

#### Agents & orchestration
- SK **Agent Framework**. Supported agent types: Azure AI (Foundry) agent, ChatCompletion agent (code-defined), OpenAI Assistant agent, Copilot Studio agent, Bedrock agent.
- Each agent = name + description + instructions (prompt) + its own kernel instance → different agents can bind to different models (e.g. one GPT-4.1, one Gemini) in the same app.
- Orchestration patterns:
  - **Sequential** — output of agent 1 feeds agent 2, etc.
  - **Concurrent** — same input fanned to all agents in parallel, outputs merged.
  - **Group chat** — collaborative conversation among agents + optional human-in-loop.
  - **Handoff** — a main/router agent receives the task and routes to specialist agents by task type; specialists can hand back to router. Human-in-loop via an interaction callback function.
- Handoff quality depends heavily on prompt quality; hardest pattern to get right.

#### BC integration pattern (real example)
- AL prompt-dialog page builds a prompt containing YAML of available API pages: enumerate page metadata of type API, their fields, serialize to YAML, pass as context. Model then knows which standard/custom APIs exist.
- Separate system prompt (stored in Key Vault, not code) teaches the model how to format API URLs (standard vs custom), apply OData filters, handle dates/errors. Model then composes multi-query API calls → richer than stock Copilot chat.
- Best practice: keep prompts OUT of code (Key Vault / external), so you can tune without redeploy — mirrors how Microsoft ships BC Copilot prompts.

#### MCP (Model Context Protocol)
- Open protocol (from Anthropic) becoming standard; client registers an MCP server once, then calls any target system through it. BC MCP support = work in progress; usable today from GitHub Copilot, Copilot Studio, etc.
- Two transports: **stdio** (local servers), **HTTP + SSE** (remote servers).
- SK consuming MCP: add MCP client factory package [sic? verify], create MCP client with URL+transport, list tools, expose to model. Demo used Playwright MCP server (browser automation) driven by an SK agent.

#### Offline / cost
- Fully offline supported: swap `AddAzureOpenAIChatCompletion` for `AddOllamaChatCompletion` [sic?] (Ollama), or use **Foundry Local** to run open-source models locally — near-zero cost.
- Cost tracking: Azure OpenAI emits telemetry; enable it and group by IP/tenant to attribute per-customer spend. Presenter has an ARM template on GitHub for this.
- Two token limits per session: per-interaction prompt size (subscription-bounded, not model-bounded) and overall throughput. For many concurrent users, deploy multiple model instances and route requests (e.g. via Azure API Management) — Microsoft does this under the hood.
- Debugging orchestration: enable SK logging → traces to Application Insights; otherwise test + prompt-tune. No dedicated multi-agent test tooling.

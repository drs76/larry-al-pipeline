# azure-openai-integration

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2023 - Smarter Apps in Less Time: Copilot and Ch | 2026-07-27 -->
### Azure OpenAI vs OpenAI
- OpenAI = the company/API that built GPT; Azure OpenAI = same underlying models served through Azure with Microsoft's infra, security, and content filtering added on top.
- Access: OpenAI is instant on signup; Azure OpenAI required a waitlist (two, historically — one for the service, one for GPT-4). [sic? waitlist status is time-sensitive, verify current on Microsoft Learn]
- Deploy in Azure Portal: create Azure OpenAI resource (pick region + resource group + pricing tier), then open **Azure OpenAI Studio** to create/deploy named model *deployments*. Multiple deployments of the same model allowed, each with its own capacity/quota.
- Region matters: some models available only in certain regions; you can run instances in several regions to spread quota.

### Two chat endpoints
- **Completions** endpoint takes a single `prompt`. This is what BC Copilot uses.
- **Chat** endpoint takes a `messages` array (role/content objects) instead of a flat prompt; response content is read from `choices[].message.content` rather than the completions-style field. Same URL, different params/response shape.

### BC built-in Azure OpenAI codeunit
- System app codeunit `Azure AI Usage` [sic? presenter's caption — verify exact name/ID against the System Application; a general-purpose Azure OpenAI wrapper codeunit exists but was `internal` at time of talk]. Access was `internal`, expected to open up later.
- Speaker chose NOT to use the built-in codeunit in production because it can't scale around the Azure OpenAI **rate/token quota limit**: it only lets you name a model and send a prompt, no load balancing.

### Prompt engineering
- Prompt = instructions to the model; treat like instructions to an intern.
- Structure: start with a role ("You are a …"), then instructions, then context, then input/output examples. **Repeat the required output format again at the end** — with a long prompt the model tends to forget an instruction stated only at the top.
- For deterministic/structured output set **temperature = 0** (range 0–2; higher = more random/risky). Also raise max length so output isn't truncated.
- To force parseable output: explicitly state "always return a JSON object in this exact format", show the format, and add "don't include any comments" — models otherwise wrap JSON in prose.
- Token limits apply to input **and** output combined. GPT-3.5 ~4k tokens, a 16k variant, GPT-4 8k/32k. ~1 token ≈ 4 characters. Larger context = higher cost and latency.

### Chat-to-schedule-job-queue pattern (demo)
- Natural-language chat in BC that creates Job Queue Entries. Flow: user text → BC control add-in → codeunit calls Azure OpenAI with a stored system prompt → parse returned JSON → insert job queue records.
- System prompt was stored in **blob storage** and loaded at call time.
- Domain knowledge (how BC job-queue scheduling works, date-formula rules) was pasted into the prompt as context from blog docs so the model emits valid values.
- Add explicit constraints the model keeps violating, e.g. "next run date formula" and "run on <weekday>" fields cannot both be set on one entry — instruct the model to split into two separate job queue entries instead. Also: don't invent object type/number if unknown; politely say "I don't know".
- Include few-shot request/response examples to raise output reliability.

### Embeddings & vector search (grounding on your own data)
- Because prompts have token limits you can't paste a whole knowledge base. Instead embed data and retrieve only relevant chunks (RAG).
- Embeddings map text chunks to vectors of numbers; semantic search finds nearest vectors (meaning-based, not keyword). OpenAI embedding dimension ≈ 1536 [sic? presenter said "one thousand five hundred thirty-two" — 1536 is the real ada-002 dimension; verify].
- Flow: chunk source text → embed → store in vector DB. At query time: embed the question, nearest-neighbour search the vector DB, inject the matching chunk into the prompt, let the LLM answer from it.
- Demo used **Supabase** as a cloud vector store. PDFs can be indexed too, but tables rendered with dot-leaders crawl poorly, so table cells may be lost on extraction.

### Azure OpenAI "on your data" (preview at time of talk)
- Playground feature: add a data source (e.g. Azure Blob Storage) + an Azure Cognitive Search instance to auto-index it, then chat over it with near-zero code.
- Can deploy the result as an Azure web app with user permissions.
- Presenter's caveat: preview, unstable, slow on large data — a starting/test point, not production-ready at the time.

### Scaling in production — Azure OpenAI SDK for .NET + Azure Functions
- Used **Azure.AI.OpenAI SDK for .NET** (beta at the time) inside an **Azure Function** instead of the BC codeunit. SDK connects to both Azure OpenAI and standard OpenAI. [sic? confirm package name `Azure.AI.OpenAI`]
- Reason: chat-with-data generates far more requests than one-off item-description calls; the built-in codeunit can't scale past the quota. A Function fronts multiple Azure OpenAI instances behind one endpoint and load-balances requests to dodge per-instance token limits.

### Incremental data ingestion tip
- To keep the vector DB current, re-index on a schedule (speaker: once/day via a separate script).
- Mentioned the **bc2adls** extension to export BC data (as Delta files, only changed records) to storage for incremental crawling into vectors. [sic? "MBC to a DLS" in captions = bc2adls; verify]

### GitHub Copilot notes (AL)
- Copilot Chat / "Copilot X" required signup and, at the time, the **Insider/preview** build of VS Code (or standard Visual Studio); needs a GitHub Copilot paid license.
- Inline AI edit shortcut: **Cmd+I** (Mac) / **Alt+I** (Windows) inside a file to generate/modify code in place.
- "Explain this code" panel available on selection.
- Copilot's AL quality improved as more AL devs used it. Context it uses for suggestions: the active file plus a few other open tabs and recently opened files — keep relevant AL files open for better completions.

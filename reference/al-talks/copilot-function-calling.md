# Function calling in AL with Azure OpenAI

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: Prompt engineering and functional callin | 2026-07-27 -->
### Function calling in AL (Azure OpenAI)

- Function calling lets an LLM invoke developer-defined AL functions/APIs based on natural-language user input — LLM returns which function to call plus extracted arguments; the toolkit then auto-invokes your code and hands back the result.
- Implement the `AOAI Function` [sic?] interface (verify exact name on MS Learn) with three methods: `GetName`, `GetPrompt`, `Execute`.
  - `GetName` returns the function name — must match the `name` in the function prompt exactly.
  - `GetPrompt` returns the function definition object (name, description, parameters). Keep prompts as IP: store in isolated storage (per-tenant extension) or Key Vault (AppSource app), not hardcoded.
  - `Execute(arguments)` is called automatically when the model picks that function. Receives the required (and any optional) args the model extracted. Return type is Variant — can return record, text, code unit, etc.
- Always validate model output in `Execute`: check required args are present, reject empty strings, confirm referenced records exist before use. Model can hallucinate/omit values.

### Wiring the call

- Setup: set capability, set authorization, add each function as a tool (e.g. via `AddTool` [sic?] — verify), then set system message, add user query, call `Generate` [sic?].
- Tool choice: `Auto` (default) lets model pick any registered function OR return free text — you must check whether the response is a function call vs generative text and handle each. Setting a specific function forces that function every time regardless of query (usually wrong for multi-intent copilots).
- Passing context to a function: add a global var + setter on the function's code unit; call the setter just before `Generate`. The same instance is reused when `Execute` fires, so it sees the context.

### Function definitions (the schema)

- Each function has: name, optional description, parameters (properties with type + optional description), and a `required` list.
- Description max length ~1024 chars (undocumented). Complex "when to call which function" logic works better in the system prompt than in descriptions.
- Declare `required` properties so the model guarantees extraction (e.g. company name + item array, with item name required inside the array). Optional args (e.g. quantity) can default in code.
- Response is structured/JSON by definition — no need to prompt for output format; defining the function schema enforces it.

### System prompt structure

- Three components combine: system prompt (context + instructions), function definitions (capabilities + I/O contract), user prompt (raw input).
- System prompt sections used in the demo: context (what the AI is for), safety instructions (redirect harmful content to a catch-all function), task instructions (which function to call for which input pattern).
- Prompt tips: be concise (tokens = cost); use examples to fix misbehaviour (e.g. splitting item name vs feature — "two red bicycle" → name=bicycle, feature=red); bold or star text for emphasis; ask Copilot to refine your prompt.
- Model handles non-English user input fine; for generative-text features tell it to reply in the user's language. For function calls language is largely irrelevant since output is JSON args.

### Magic / catch-all function pattern

- Define a catch-all function ("magic function") for anything unsupported or harmful; system prompt routes unrecognised/harmful input to it. Gives a controlled boundary over free-text input.
- Give it an `intent` string property (or an enum of categories like `harmful`/`not-supported`) so you can branch on why it was hit and show different errors.
- Red-teaming finding: redirecting harmful content to a function works better than instructing the model "don't respond" — the LLM tends to respond anyway, so a function call is a more reliable guardrail.
- Azure OpenAI applies default content filters even with no safety instructions; the built-in BC default system prompt adds a stricter safety layer (may be too restrictive for some industries — supply your own safety prompt then).

### Notes / gotchas

- Large catalogs (e.g. 150k items) cannot be passed in the prompt — extract keywords from the model, then use your own search or embeddings to resolve to records.
- Models are not fine-tuned for BC; you use your own Azure OpenAI deployment (GPT-3.5-turbo / GPT-4 / GPT-4-turbo) from AI Studio.
- Telemetry: user input and model responses are treated as customer content, so Microsoft does not log them. You may log non-content signals like which function was called or the intent enum — never the raw query. Partner telemetry lives in the partner's own subscription.
- Parallel function calling (Azure OpenAI feature, not yet in the BC SDK at time of talk): one user turn can trigger multiple function calls (e.g. get-weather twice + search-hotel twice for two cities).
- AI module ships in the System Application (BCApps repo). Jailbreak/system-prompt bypass is mitigated by red teaming but not fully preventable.

_Source: caption-derived; verify `AOAI Function` interface name, `AddTool`/`Generate` method names, and the 1024-char description limit against Microsoft Learn or the compiler._

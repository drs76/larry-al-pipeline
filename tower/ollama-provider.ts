import { createProvider, openAICompletionsApi } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

// Larry LAN ollama via nginx HTTPS proxy. Migrated to the 0.81 complete-provider
// form (createProvider + openAICompletionsApi) so pi sends tools NATIVELY again —
// the legacy provider-config form regressed after pi 0.81 and leaked tool calls
// as `<function=…>` text (search/kb tools never executed). Ollama returns proper
// tool_calls for these qwen models, so native send restores tool use.
const BASE = "https://larry.home.arpa:11443/v1";

const mk = (id: string, name: string, ctx = 32768, max = 16384) => ({
  id,
  name,
  api: "openai-completions" as const,
  provider: "ollama",
  baseUrl: BASE,
  reasoning: false,
  input: ["text"] as ("text" | "image")[],
  cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
  contextWindow: ctx,
  maxTokens: max,
});

export default function (pi: ExtensionAPI) {
  pi.registerProvider(createProvider({
    id: "ollama",
    name: "Ollama (Larry)",
    baseUrl: BASE,
    auth: {
      // Keyless local server: no prompt, always resolves a dummy key so the
      // provider counts as configured.
      apiKey: {
        name: "Ollama (local, keyless)",
        async resolve() {
          return { auth: { apiKey: "ollama" }, source: "keyless local server" };
        },
      },
    },
    models: [
      mk("qwen3-coder:30b", "Qwen3 Coder 30B"),        // default coder (Go/C#/general)
      mk("al-coder-qwen3", "AL Coder Qwen3"),           // qwen3-coder:30b + baked AL SYSTEM
      mk("al-coder-qwen36", "AL Coder Qwen36"),         // older/weaker AL derivative
      mk("al-coder-north-mini", "AL Coder NorthMini"),
      mk("north-mini-code-1.0", "NorthMini Code 1.0"),
    ],
    api: openAICompletionsApi(),
  }));
}

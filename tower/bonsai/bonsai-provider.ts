import { createProvider, openAICompletionsApi } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

// Ternary-Bonsai-27B on Larry (llama-server, OpenAI-compat) — pi chat brain.
// Mode B time-share: `bonsai on` (see bonsai-control.ts) evicts the ollama coder
// and serves here; idle >15min auto-stops it. So run `bonsai on` before chatting.
//
// Migrated to the 0.81 complete-provider form (createProvider + openAICompletionsApi)
// alongside ollama-provider — the legacy form regressed after pi 0.81.
//
// Ternary-Bonsai is a Qwen3 derivative: its default chat template runs in THINKING
// mode, so llama-server puts the whole answer in `reasoning_content` and leaves
// `content` EMPTY — pi renders content, so replies show blank. Force thinking off
// via compat.chatTemplateKwargs (native field; replaces the old before_provider_request hack).
const BASE = "https://larry.home.arpa:8444/v1";  // nginx TLS proxy → 127.0.0.1:8091

export default function (pi: ExtensionAPI) {
  pi.registerProvider(createProvider({
    id: "bonsai",
    name: "Bonsai (Larry)",
    baseUrl: BASE,
    auth: {
      apiKey: {
        name: "Bonsai (local, keyless)",
        async resolve() {
          return { auth: { apiKey: "bonsai" }, source: "keyless local server" };
        },
      },
    },
    models: [
      {
        id: "ternary-bonsai-27b",
        name: "Ternary-Bonsai 27B",   // 52 tok/s; thinking forced off below
        api: "openai-completions" as const,
        provider: "bonsai",
        baseUrl: BASE,
        reasoning: false,
        input: ["text"] as ("text" | "image")[],
        cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
        contextWindow: 8192,
        maxTokens: 4096,
        compat: { chatTemplateKwargs: { enable_thinking: false } },
      },
    ],
    api: openAICompletionsApi(),
  }));
}

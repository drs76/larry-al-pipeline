import { createProvider, openAICompletionsApi } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

// OpenRouter provider for the pipeline's cheap-cloud MID tier (CODER_BACKEND=mid,
// see setup/pipeline/war-plans/mid-tier-routing/). One key, many models. Built in
// the pi-0.81 complete-provider form (createProvider + openAICompletionsApi) so
// tool calls send NATIVELY — the legacy form leaks them as <function=…> text and
// the coder never writes files (see reference_pi_081_provider_fix).
//
// EGRESS: this reaches a third-party cloud. The pipeline only ever invokes it via
// run_mid(), which is gated by egress_policy.allowed("openrouter") — customer AL
// (local-only) can never route here. Do NOT wire this provider into an
// ungated/interactive path for work code.
const BASE = "https://openrouter.ai/api/v1";

const mk = (id: string, name: string, ctx = 131072, max = 16384) => ({
  id,
  name,
  api: "openai-completions" as const,
  provider: "openrouter",
  baseUrl: BASE,
  reasoning: false,
  input: ["text"] as ("text" | "image")[],
  // Cost tracked on the OpenRouter dashboard, not here; zero keeps pi's budget UI quiet.
  cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
  contextWindow: ctx,
  maxTokens: max,
});

export default function (pi: ExtensionAPI) {
  // Register ONLY when the key exists. pi resolves every registered provider's auth
  // up front, so a provider that throws in resolve() does not degrade to "unavailable
  // model" — it aborts the whole run: `pi --list-models` and even a plain `pi -p` die
  // with `ModelsError: API key auth failed for provider openrouter`, taking the local
  // bonsai/ollama models down with it. A keyless box must simply not have this
  // provider (asking for it then fails with a clear unknown-provider error).
  if (!process.env.OPENROUTER_API_KEY) return;

  pi.registerProvider(createProvider({
    id: "openrouter",
    name: "OpenRouter (mid tier)",
    baseUrl: BASE,
    auth: {
      apiKey: {
        name: "OpenRouter API key (OPENROUTER_API_KEY)",
        async resolve() {
          const key = process.env.OPENROUTER_API_KEY;
          if (!key) {
            throw new Error(
              "OPENROUTER_API_KEY not set — the mid tier needs an OpenRouter key " +
              "(https://openrouter.ai/keys). Put it in ~/.config/zsh/local.zsh.");
          }
          return { auth: { apiKey: key }, source: "OPENROUTER_API_KEY env" };
        },
      },
    },
    // Primary + A/B alternates. Swap via MID_MODEL (openrouter/<id>) — no code change.
    models: [
      mk("deepseek/deepseek-chat", "DeepSeek-V3 (mid default)"),
      mk("moonshotai/kimi-k2", "Kimi K2"),
      mk("z-ai/glm-4.6", "GLM-4.6"),
      mk("deepseek/deepseek-v4-flash-0731", "DeepSeek V4 Flash (0731)"),
    ],
    api: openAICompletionsApi(),
  }));
}

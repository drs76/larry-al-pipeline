import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";

const SEARXNG_URL = process.env.SEARXNG_URL ?? "https://searxng.home.arpa";

interface SearxResult {
  title: string;
  url: string;
  content?: string;
}

export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "web_search",
    label: "Web Search",
    description: "Search the web via local SearXNG instance",
    promptSnippet: "Search the web for current information",
    promptGuidelines: [
      "Use web_search when the user asks about current events, docs, or anything not in local files/training data.",
    ],
    parameters: Type.Object({
      query: Type.String({ description: "Search query" }),
      count: Type.Optional(Type.Number({ description: "Max results (default 5)" })),
    }),
    async execute(_toolCallId, params, signal) {
      const url = new URL("/search", SEARXNG_URL);
      url.searchParams.set("q", params.query);
      url.searchParams.set("format", "json");

      const res = await fetch(url, { signal });
      if (!res.ok) {
        return {
          content: [{ type: "text", text: `SearXNG error: ${res.status} ${res.statusText}` }],
          isError: true,
        };
      }

      const data = (await res.json()) as { results: SearxResult[] };
      const results = data.results.slice(0, params.count ?? 5);

      if (results.length === 0) {
        return { content: [{ type: "text", text: "No results found." }] };
      }

      const text = results
        .map((r, i) => `${i + 1}. ${r.title}\n${r.url}${r.content ? `\n${r.content}` : ""}`)
        .join("\n\n");

      return { content: [{ type: "text", text }], details: { count: results.length } };
    },
  });
}

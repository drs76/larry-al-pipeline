import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";
import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";

// Local hybrid (BM25 + vector) KB search over the AL/BC markdown knowledge bases,
// served by `kb serve` on Larry (setup/tooling/kb_core.py). Everything stays on the LAN:
// the query embeds via Larry, vectors live in Larry's local-disk sqlite store — no egress.
//
//   KB_REMOTE        base URL of the kb serve instance (default http://larry.home.arpa:8848)
//   token, in order: env KB_REMOTE_TOKEN, then file ~/.pi/.kb-token (one line, chmod 600)
// Never hard-code the token here — this file is committed to the setup repo.
const KB_REMOTE = process.env.KB_REMOTE ?? "http://larry.home.arpa:8848";

function token(): string {
  if (process.env.KB_REMOTE_TOKEN) return process.env.KB_REMOTE_TOKEN;
  try {
    return fs.readFileSync(path.join(os.homedir(), ".pi", ".kb-token"), "utf8").trim();
  } catch {
    return "";
  }
}

interface KbHit {
  corpus: string;
  path: string;
  heading?: string;
  snippet?: string;
  score?: number;
}

export default function (pi: ExtensionAPI) {
  pi.registerTool({
    name: "kb_search",
    label: "KB Search",
    description:
      "Hybrid (BM25 + vector) search over the local AL/Business Central knowledge bases: AL syntax " +
      "reference, AL platform knowledge, curated AL patterns (event subscribers, HTTP, IsolatedStorage, " +
      "posting), BC-agent transcripts, and the MS BCQuality do/don't rules. Returns ranked {corpus, path, " +
      "heading, snippet}. Prefer this over guessing a BC API/signature — the snippets carry real, correct AL.",
    promptSnippet: "Search the local AL/BC knowledge bases for correct patterns and API signatures",
    promptGuidelines: [
      "Use kb_search before writing AL when unsure of an exact event signature, codeunit name, or pattern.",
      "Optional corpus filter: al-reference, al-knowledge, al-patterns, transcripts, bcquality, memory.",
    ],
    parameters: Type.Object({
      query: Type.String({ description: "Natural-language or keyword query" }),
      corpus: Type.Optional(Type.String({ description: "Limit to one corpus (optional)" })),
      n: Type.Optional(Type.Number({ description: "Max results (default 6)" })),
    }),
    async execute(_toolCallId, params, signal) {
      const tok = token();
      const headers: Record<string, string> = { "Content-Type": "application/json" };
      if (tok) headers["Authorization"] = `Bearer ${tok}`;

      let res: Response;
      try {
        res = await fetch(new URL("/search", KB_REMOTE), {
          method: "POST",
          headers,
          body: JSON.stringify({ query: params.query, corpus: params.corpus ?? null, n: params.n ?? 6 }),
          signal,
        });
      } catch (e) {
        return { content: [{ type: "text", text: `kb_search: cannot reach ${KB_REMOTE} (${e})` }], isError: true };
      }
      if (!res.ok) {
        return { content: [{ type: "text", text: `kb_search error: ${res.status} ${res.statusText}` }], isError: true };
      }

      const hits = (await res.json()) as KbHit[];
      if (!hits.length) {
        return { content: [{ type: "text", text: `No results for "${params.query}".` }] };
      }
      const text = hits
        .map((h, i) => `${i + 1}. [${h.corpus}] ${h.heading ?? h.path}\n   ${h.path}\n   ${h.snippet ?? ""}`)
        .join("\n\n");
      return { content: [{ type: "text", text }] };
    },
  });
}

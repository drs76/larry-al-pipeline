#!/usr/bin/env python3
"""kb-search MCP server — exposes the local hybrid KB search (kb_core) to Claude Code.

Minimal hand-rolled MCP stdio transport (newline-delimited JSON-RPC 2.0) — no `mcp`
package dependency, matching the repo's hand-rolled style. Registered in .mcp.json.
Everything stays local: search embeds the query via Larry and reads the local sqlite index.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tooling dir
import kb_core

PROTO = "2024-11-05"
TOOL = {
    "name": "kb_search",
    "description": (
        "Hybrid (BM25 + vector) search over the local markdown knowledge bases: AL syntax "
        "reference, AL platform knowledge, BC-agent transcripts, the large AL knowledge dump, "
        "the MS BC/AL quality knowledge base (do/don't rules across security, performance, UI, "
        "events, style, ...), and the Claude memory-wiki. Returns ranked {path, heading, snippet} — open the path "
        "to read full context. Local + no egress. Prefer this over grep for conceptual lookups."),
    "inputSchema": {
        "type": "object",
        "properties": {
            "query":  {"type": "string", "description": "Natural-language or keyword query"},
            "corpus": {"type": "string", "description":
                       "Optional: limit to one corpus (al-reference, al-knowledge, transcripts, al-merge, bcquality, memory)"},
            "n":      {"type": "integer", "description": "Max results (default 8)"},
        },
        "required": ["query"],
    },
}

def reply(mid, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": mid}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg) + "\n"); sys.stdout.flush()

def handle(req):
    m, mid = req.get("method"), req.get("id")
    if m == "initialize":
        proto = (req.get("params") or {}).get("protocolVersion") or PROTO
        reply(mid, {"protocolVersion": proto,
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "kb-search", "version": "1.0.0"}})
    elif m == "tools/list":
        reply(mid, {"tools": [TOOL]})
    elif m == "tools/call":
        p = req.get("params") or {}
        args = p.get("arguments") or {}
        if p.get("name") != "kb_search":
            reply(mid, error={"code": -32601, "message": f"unknown tool {p.get('name')}"}); return
        try:
            res = kb_core.search(args["query"], corpus=args.get("corpus"), n=int(args.get("n", 8)))
            if res:
                text = "\n".join(
                    f"[{r['score']}] {r['corpus']}  {r['path']}\n  {r['heading']}\n  {r['snippet']}"
                    for r in res)
            else:
                text = "No results. If nothing is indexed yet, run `kb index`."
            reply(mid, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as e:
            reply(mid, {"content": [{"type": "text", "text": f"kb_search error: {e}"}], "isError": True})
    elif m == "ping":
        reply(mid, {})
    elif mid is not None:                 # unknown request → method-not-found
        reply(mid, error={"code": -32601, "message": f"method not found: {m}"})
    # notifications (no id, e.g. notifications/initialized) → no response

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue
        try:
            handle(req)
        except Exception as e:
            sys.stderr.write(f"kb-search-mcp error: {e}\n")

if __name__ == "__main__":
    main()

# KB-SEARCH — local hybrid search over the markdown knowledge bases

A retrieval layer for the markdown KBs (Karpathy "LLM-wiki" pattern, adapted to this stack).
Instead of grep + reading whole files, an agent asks a natural-language question and gets ranked
chunks back. **Everything stays on the LAN — no egress:** the query and each chunk are embedded
by Larry (`mxbai-embed-large`), and the vectors + BM25 index live in a single sqlite store.
Inspired by the "LLM Knowledge Bases" idea (Ben Holmes / Karpathy); the QMD-style search layer is
the piece we were missing.

> 🧭 **Host: Larry.** The sqlite store and `kb serve` run on **Larry's local disk**; every dev
> machine (Deb, WSL, ThinkPad) is a **client** that queries it over HTTP. The store used to live on
> Deb on the NFS mount — that corrupted under a concurrent serve+index (2026-08-06); the DB now
> stays on the serving host's own disk in WAL mode. See EN-8 in
> `reference/larry-tower-build-and-architecture.md`.

## Pieces

| File | Role |
|------|------|
| `setup/tooling/kb_core.py` | engine: chunk → embed (Larry) → sqlite (FTS5 BM25 + vector blobs) → hybrid search (reciprocal-rank fusion) |
| `setup/tooling/kb` | CLI wrapper (`kb index` / `kb search` / `kb stats` / `kb corpora`) |
| `setup/tooling/kb-corpora.yaml` | which corpora are indexed |
| `setup/tooling/kb-search-mcp/server.py` | MCP server exposing `kb_search` to **Claude Code** (registered in repo `.mcp.json`) |
| `~/.pi/agent/extensions/kb-search.ts` | pi tool `kb_search` (wraps the `kb` CLI) for **pi / probe** sessions |
| `~/.local/share/kb/kb.db` (on Larry) | the index — Larry local disk, WAL, gitignored + regenerable (`KB_DB`) |

## Use

```bash
kb index                 # build/refresh all corpora (idempotent — re-runs re-embed nothing unchanged)
kb index --corpus memory # just one corpus
kb search "how does telemetry work in BC" -n 6
kb search "interface implements pattern" --corpus al-merge --json
kb stats                 # chunk/file counts per corpus
```

From **Claude Code**: the `kb_search` MCP tool is available in this repo (via `.mcp.json`).
From **pi**: load `-e ~/.pi/agent/extensions/kb-search.ts` (or add it to the default extension set).

## Serving — Larry hosts, everyone else is a client (`kb serve`)

The sqlite store lives on **Larry's local disk**; every other machine queries it over HTTP.
Larry runs `kb serve` (systemd **user** service `kb-serve.service` + linger, `http://larry.home.arpa:8848`,
bearer-token auth). A client sets **`KB_REMOTE`** and `search` / `stats` / `corpora` go over HTTP —
the CLI, the MCP server, and the pi extension all inherit it (same `kb_core` functions). `index`
and `serve` refuse to run in `KB_REMOTE` mode. **Deb is a client too** and no longer holds a local
store.

**The token has two homes and they must agree.** `KB_REMOTE_TOKEN` wins when it is in the
environment; when it is not, `kb_core.py`, the pi `kb-search` extension and `al-rag` all fall back
to **`~/.pi/.kb-token`** (one line, chmod 600). Maintaining only one of them is how deb ended up
serving HTTP 200 from `local.zsh` and HTTP 401 from `~/.pi/.kb-token` on the same box — interactive
zsh worked while the MCP server, pi and every non-interactive caller failed silently.

```bash
# server (LARRY) — env in ~/.config/kb/serve.env: KB_DB=~/.local/share/kb/kb.db (LOCAL disk),
# KB_EMBED_URL=http://localhost:11434/v1/embeddings (local ollama), KB_SERVE_TOKEN, HOST/PORT.
systemctl --user status kb-serve            # firewalld: 8848/tcp opened

# client (Deb / WSL / ThinkPad / Windows) — needs a checkout of setup/tooling; NO kb.db.
# NEVER paste the token by hand: the script fetches it over ssh without printing it, writes
# BOTH destinations from one fetch, and verifies each separately. Re-run after any rotation.
bash tower/handoff-scripts/kb-client-setup.sh
kb search "how does telemetry work in BC" -n 6
```

Needs `ssh larry` to resolve — a keypair on Larry **and** a `Host larry` block in `~/.ssh/config`
(`User dav`). Without the alias, ssh sends the local account name and Larry refuses it; the script
now tells you which of the two it is.

**Diagnose against `/stats`, never `/health`.** `/health` takes no auth, so it answers
`{"ok": true}` to a client whose token is dead — which is exactly why two boxes looked wired for
weeks while every authenticated call failed.

Endpoints: `GET /health` (open), `GET /stats`, `GET /corpora`, `POST /search {query,corpus,n}`
(all token-gated when `KB_SERVE_TOKEN` is set). LAN-only, no TLS — don't expose off-LAN.
The pi ext honours `KB_BIN` for the `kb` script path on clients where the repo lives elsewhere.

> **Migrating a client off Deb:** just point `KB_REMOTE` at `larry.home.arpa:8848` (same token).
> Deb, WSL, and ThinkPad all use the identical two env vars now.

## Add a corpus

Edit `kb-corpora.yaml` — add a block with `desc` and `paths` (files or dirs; dirs are walked for
`*.md`; paths may be absolute, `~`, or repo-relative). Then `kb index --corpus <name>`.

## Environment knobs

- `KB_EMBED_URL` (default `https://larry.home.arpa:11443/v1/embeddings`; **on Larry itself** the serve/refresh use `http://localhost:11434/v1/embeddings` — local ollama, no proxy hop), `KB_EMBED_MODEL` (`mxbai-embed-large`)
- `KB_DB`, `KB_CORPORA`, `KB_REPO_ROOT`, `KB_MAX_CHUNK`, `KB_EMBED_BATCH`
- `KB_BIN` — for the pi extension, path to the `kb` script when the repo lives elsewhere (WSL / ThinkPad client)
- `KB_REMOTE` / `KB_REMOTE_TOKEN` — thin-client mode: query a remote `kb serve` over HTTP instead of local sqlite
- `KB_SERVE_HOST` / `KB_SERVE_PORT` / `KB_SERVE_TOKEN` — server side (`kb serve`); token gates all but `/health`
- TLS: the store trusts the system CA and drops only Python 3.13's `VERIFY_X509_STRICT` (the HomeLab
  CA lacks a keyUsage extension). `KB_EMBED_CA` points at a CA file; `KB_INSECURE=1` is a LAN-only escape hatch.

## Hygiene — `kb-lint` (the "lint" op)

`setup/tooling/kb-lint` runs a deterministic hygiene pass over the Claude memory-wiki:
dead wikilinks, wikilink drift (underscore/hyphen, dropped type-prefix), orphan notes, and
MEMORY.md index drift. Report-only by default:

```bash
kb-lint                  # report (touches nothing)
kb-lint --fix-links      # rewrite drifted [[links]] to their canonical `name` slug
kb-lint --append-missing # append index stubs for un-indexed notes (never rewrites curated rows)
kb-lint --semantic       # also run `probe` (pi + Larry) to flag stale/contradictory notes — advisory
```

MEMORY.md is never blindly regenerated — its hand-curated titles/order would be lost.

## raw → wiki discipline (ingest)

The pattern keeps three layers stacked, never collapsed:
- **raw/** — immutable sources. Here: `setup/reference/transcripts/` (BC-agent video transcripts).
- **wiki/** — LLM-synthesized pages. Here: `AL-REFERENCE.md` / `AL-KNOWLEDGE.md`, built from the
  transcripts (see `setup/tooling/al-knowledge-export.sh` for the ingest/ETL step).
- **index/search** — this layer.

Keeping raw sources means the synthesized pages can be **re-generated** when the schema improves,
without re-gathering. `kb index` is idempotent (per-chunk content hash) — unchanged sources
re-embed nothing, so a nightly refresh is cheap.

## Nightly refresh (on Larry)

A systemd **user** timer on **Larry** at 03:30 (`~/.config/systemd/user/kb-refresh.{service,timer}`,
`Persistent=true` so a missed run catches up) runs `kb index` (idempotent — unchanged sources
re-embed nothing) with the same `serve.env` (local DB + local ollama). WAL mode lets this write run
while `kb-serve` keeps reading — the two coexist safely (they did **not** on the old NFS store; that
was the corruption, EN-8). Linger is enabled (`doas loginctl enable-linger dav`) so it fires logged
out. On-prem equivalent of the video's cloud-scheduled enrichment.

**Why Larry now (not Deb):** the store + `kb serve` live on Larry, and Larry embeds locally — so the
refresh is a single-box operation with no cross-host write (the thing that corrupted the old NFS
DB). Larry also mounts the corpora sources read-only (`/mnt/rojaws/{localDev/setup,refs}`), so it
sees everything the index needs.

> **Caveat — the `memory` corpus is not on Larry.** The Claude memory-wiki lives under Deb's
> `~/.claude/...`, which Larry doesn't have, so the Larry index carries **0 memory chunks** and
> memory is currently not searchable via KB. (No pruning risk — it was never indexed there.) Two
> follow-ups: (a) clone the memory repo (`drs76/claude-memory-localdev`) on Larry at the expected
> path to make it searchable; (b) `kb-lint` (memory-wiki hygiene) stays a **Deb** concern — run it
> from Deb, not the Larry refresh, since that's where the memory-wiki is.

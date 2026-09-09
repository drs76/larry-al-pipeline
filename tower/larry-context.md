# Larry — Local AI Inference Server

Self-hosted inference tower serving LLMs over LAN. *(Updated 2026-08-07.)*

## Hardware
- **GPU**: AMD Radeon RX 7900 XTX 24GB VRAM
- **OS**: Rocky Linux 10, headless, SSH only
- **Stack**: Ollama **0.33.2** + ROCm

## Access
| Service | URL |
|---|---|
| Ollama API (HTTP) | `http://larry:11434` |
| Ollama API (HTTPS) | `https://larry.home.arpa:11443` |
| Larry Dashboard | `https://larry.home.arpa/dash` (basic-auth) |
| SSH | `dav@larry` (doas for root ops) |

DNS: `larry` or `larry.home.arpa` — resolves on local LAN via Pi-hole on Nemesis.

## Ollama API Usage
```
Base URL: http://larry:11434
Compatible with OpenAI-style /v1/ endpoints
```

## Available Models (`ollama list` 2026-08-07)
| Model | Best For | Size |
|---|---|---|
| `qwen3-coder:30b` | **Default pipeline coder** (alw/gow/csw; fast, ~80 tok/s) | 18GB |
| `al-coder-qwen3` | Interactive AL (`alcode`; Modelfile SYSTEM wrap — pair with `alrag` for API grounding) | 18GB |
| `qwen3:32b` | General reasoning/chat | 20GB |
| `deepseek-coder-v2:16b` / `deepseek-r1:14b` | Code / reasoning (reasoners DESCRIBE, don't drive tools) | 9GB |
| `qwen2.5-coder:14b` | Code incl FIM/completions | 9GB |
| `devstral` | Agentic coding eval | 14GB |
| `gemma4:26b` | Vision (image+text) | 17GB |
| `ornith:35b` | **BROKEN — ROCm cold-load hang, do not use**; `ornith:9b` OK | 21GB |
| `al-coder-qwen36` / `al-coder-north-mini` / `north-mini-code-1.0` | Legacy AL coders (weak/slow for AL — superseded by qwen3-coder) | ~17–18GB |
| `al-coder-tuned` | QLoRA AL finetune experiment (hallucinates APIs; RAG beats it) | 9.3GB |
| `mxbai-embed-large` | Embeddings (kb hybrid search, RAG) | 0.7GB |

**`al-coder-*` models** have a BC AL developer system prompt baked in (Modelfile SYSTEM). Note: a baked SYSTEM is INERT when an agent/harness sends its own system message — put AL rules in the prompt/AGENTS.md, not just the model.

## AL build pipeline (Pi / Claude Code — primary AL automation)
`/mnt/rojaws/localDev/setup/pipeline/run-build.py` (prefer `alw build`) — automated AL build: handover → coder writes AL → scoped al-mcp downloads BC28.2 symbols (`al_downloadsymbols globalSourcesOnly`, no auth/server) → `al compile` → deterministic normalizers (using-placement, string-prop quoting, canonical app.json from handover) → keep-best/no-regress fix loop. Coder backend pluggable via env **`CODER_BACKEND=pi`** (local ollama via Pi harness, free) or **`claude`** (Claude Code, Pro-sub quota). Replaces the old LibreChat-agent approach (which had auth/2FA/context-prune problems). Run on Larry; needs ollama + al-mcp + (for pi) `~/.npm-global/bin/pi` + `~/.pi/ollama-provider.ts`, or (for claude) `~/.npm-global/bin/claude` logged in.

## LibreChat — RETIRED 2026-06-30
Fully retired (`docker compose down`; volumes kept on Larry but unused). Chat/agents replaced by pi + Claude Code; extension analysis by `bcw analyse`. Historical config in `setup/archive/librechat/`.

## AL Project Paths on NFS Share
```
/mnt/rojaws/WorkDevGuideLines/   ← guidelines, pipelines, AL projects
/mnt/rojaws/Code/AL/             ← AL extension projects (promoted)
/mnt/rojaws/localDev/projects/   ← prototypes
```

## Extension Analysis
`bcw analyse /mnt/rojaws/path/to/extension` — deterministic collector + egress-gated analyst (Larry-first), writes WIKI + performance docs. See `setup/pipeline/BCW.md`.

## SSL (larry.home.arpa)
- Local CA on Deb (`~/certs/ca/`) — key never leaves Deb
- Cert: `/etc/nginx/ssl/larry.crt` + `larry.key` on Larry
- Renewal: re-sign on Deb with `larry/larry.ext`, scp to Larry, `doas systemctl reload nginx`

## Using Larry from Another Claude Project
Add to `CLAUDE.md`:
```
Read /mnt/rojaws/localDev/larry-context.md for Larry (local AI inference server) details.
```

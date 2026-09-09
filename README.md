# Larry setup & AL pipeline — source of truth

> **Show-and-tell:** [`WORKFLOWS-OVERVIEW.md`](WORKFLOWS-OVERVIEW.md) — one-page tour with mermaid
> diagrams (architecture, egress gate, build loop, planning tiers) for a non-project audience.

This repo is the single home for how the **Larry** AI tower is built and how the
**AL coding pipeline** (pi/Larry + Claude) runs on top of it. Setup plans, infra
config, pipeline code, templates, and reference docs all live here.

> **Start here:** [`pipeline/PROJECT-LIFECYCLE.md`](pipeline/PROJECT-LIFECYCLE.md) — start-to-finish
> for a new project (interview → handover → Larry → build → review → promote), across **AL, Go, and
> C#/Azure Functions**, driven from the terminal. For the AL deep-dive with diagrams see
> [`pipeline/AL-CODING-WORKFLOW.md`](pipeline/AL-CODING-WORKFLOW.md).

## Layout

| Folder | Contents |
|---|---|
| **`tower/`** | Larry build + infra: [`ai-tower-build-plan.md`](tower/ai-tower-build-plan.md), [`ssl-setup-larry.md`](tower/ssl-setup-larry.md), [`larry-context.md`](tower/larry-context.md), and the live nginx proxies — `nginx-larry.conf` (Ollama HTTPS `:11443`) and `nginx-almcp-proxy.conf` (al-mcp `:5003`). Reproduce elsewhere: [`wsl-setup.md`](tower/wsl-setup.md) (mirror the dev box in WSL2 as a **Larry client**) · [`windows-setup.md`](tower/windows-setup.md) (native Windows Server Larry client, no WSL; optional docker host) · [`windows-host-setup.md`](tower/windows-host-setup.md) (native Windows **workstation** Larry client, **PowerShell-only** — no WSL/WezTerm; Git Bash for the CLIs) · [`coop-setup.md`](tower/coop-setup.md) (**standalone** C# box with its own GPU/ollama) · [`coop-update.md`](tower/coop-update.md) (catch an existing COOP up to the latest pipeline). |
| **`nomad/`** | The NOMAD self-hosted stack — [`nomad-context.md`](nomad/nomad-context.md). |
| **`dashboard/`** | The Larry maintenance web app (`https://larry.home.arpa/dash`) — [`dashboard/README.md`](dashboard/README.md). Deployed to `/opt/larry-dashboard` on Larry via `dashboard/deploy-dash` (the one deploy ritual; `--check` diffs repo vs deployed). |
| **`pipeline/`** | The build pipelines for all three languages. **Start:** [`PROJECT-LIFECYCLE.md`](pipeline/PROJECT-LIFECYCLE.md). Per-language CLIs: [`ALW.md`](pipeline/ALW.md) (AL) · [`GOW.md`](pipeline/GOW.md) (Go) · [`CSW.md`](pipeline/CSW.md) (C#/Functions). Orchestrators `run-build.py` / `run-build-go.py` / `run-build-cs.py` ([`RUN-BUILD.md`](pipeline/RUN-BUILD.md)). Validator-peer review + pi coms: [`COMS.md`](pipeline/COMS.md). AL deep-dive: [`AL-CODING-WORKFLOW.md`](pipeline/AL-CODING-WORKFLOW.md). **Analysis** (not codegen): [`BCW.md`](pipeline/BCW.md) — analyse a customer BC/AL extension → WIKI + performance/UCI docs, Larry-first + egress-gated. |
| **`templates/`** | [`larry-handover.template.md`](templates/larry-handover.template.md) — the handover skeleton `alw new` copies. [`bc-agent-requirements.template.md`](templates/bc-agent-requirements.template.md) — blank BC-agent discovery workbook that `/bc-agent` prefills. |
| **`reference/`** | [`AL-REFERENCE.md`](reference/AL-REFERENCE.md) — AL syntax/patterns/gotchas, read by every handover. [`AL-KNOWLEDGE.md`](reference/AL-KNOWLEDGE.md) — companion: platform/runtime, DevOps (AL-Go), dev tooling, AI-resource billing, and BC business-feature awareness (the world around the language). [`bench-results/README.md`](reference/bench-results/README.md) — **evidence index**: what the benchmark programme proved about escalation and routing, which rung to arm, and what stays off. Pre-registrations live beside it as `exp-*.md`. [`DOC-STYLE.md`](reference/DOC-STYLE.md) — the house handbook style (`/handbook` writes to it). [`AL_RULES.md`](reference/AL_RULES.md) — **generated, do not edit**: the AL house ruleset the Windows box loads into every Claude session, emitted by `pipeline/al_rules_gen.py` from `al-reference/00-gotchas.md` + `01-syntax-style.md` + the hand-written [`tsg-addendum.md`](reference/tsg-addendum.md). Re-run the generator after any ingest; `--check` exits 1 when a source has moved. |

## Tooling (`tooling/`) — tracked here, symlinked into place

Canonical copies live in this repo; each machine symlinks them into the expected location:

> **Never hardcode the repo path in a tracked file.** These files are symlinked onto
> machines that keep the clone in different places — `~/larry-setup` on the Windows
> workstation and the WSL clients, `/mnt/rojaws/localDev/setup` on the dev box — so a baked
> path is right on one machine and wrong on every other. The CLIs resolve it at runtime
> (`SETUP_DIR="${SETUP_DIR:-…}"`, first of `$SETUP_DIR` · `~/larry-setup` ·
> `/mnt/rojaws/localDev/setup`); the prompts and skills write `$SETUP_DIR/...` and carry a
> one-line resolver near the top saying the same thing. Export `SETUP_DIR` to override.

| File | Symlinked to |
|---|---|
| `tooling/alw` | `~/.local/bin/alw` — the workflow CLI (defaults point here via `RUN_BUILD`/`TEMPLATE`) |
| `tooling/al-route.md` | `~/.pi/agent/prompts/al-route.md` — the pi `/al-route` triage prompt |
| `tooling/{spec,handover,warplan,scout,cs-route,go-route,al,fable,handbook}.md` | `~/.pi/agent/prompts/` — **symlinked** (all prompts; no copy drift). `/spec` (deep) · `/handover` (light) · `/warplan` (failure-mapped, hard projects — Claude plans, pi executes) · `/scout` (decision-first, tier above /warplan: chart a too-big-to-plan effort as a local-markdown map of DECISION tickets, resolve one/session, then hand off to `/spec`·`/warplan`·`/handover`; chain = scout → warplan → build) · `/al` (BC/AL expert Q&A over the cwd repo: AL-REFERENCE + BCQuality + compiler grounded, read-only) · `/fable` (adopt the Fable 5 operating doctrine for the session; mirrors `/mnt/rojaws/localDev/HANDOVER.md`; Claude side via `~/.claude/commands/fable.md`) · `/handbook` (engineering handbook in the house style, see `reference/DOC-STYLE.md`) |
| `tooling/{warplan,scout,spec,wizard,to-questionnaire,writing-for-agents}-claude.md` | `~/.claude/commands/{warplan,scout,spec,wizard,to-questionnaire,writing-for-agents}.md` — **symlinked**: the Claude Code versions (Claude is the intended planner). pi's versions delegate here via `anon claude` (egress-gated); if blocked they draft locally and ledger every unknown |
| `tooling/{al,fable,handbook,al-syntax}.md` | `~/.claude/commands/` — **symlinked to both** pi and Claude (same file serves both; al-syntax is Claude-only) |
| `tooling/bc-agent.md` | `~/.pi/agent/prompts/bc-agent.md` **and** `~/.claude/commands/bc-agent.md` — **symlinked to both**. `/bc-agent [folder] [prefill\|plan\|both]`: scan a folder of customer material → prefill the **BC Agent Requirements** workbook (gaps flagged `❓ TBC`) and/or build an agent delivery plan; grounded in AL-REFERENCE §28–31, fills `templates/bc-agent-requirements.template.md`. **NDA/PII → run on Larry (local); never egress customer data.** |
| `tooling/ste.md` | `~/.pi/agent/prompts/ste.md` **and** `~/.claude/commands/ste.md` — **symlinked to both**. `/ste [write\|rewrite\|review] [strict\|flavored] <file>`: ASD-STE100 Simplified Technical English, the *sentence* layer of the house doc style (`/handbook` is the *structure* layer) |
| `tooling/ste/SKILL.md` | `~/.claude/skills/ste-writing/SKILL.md` — **symlinked**: the auto-triggering Claude skill (fires on "make this read less like AI"). Link `ste-lint.py` + `ste-recurring-errors.md` into the same dir |
| `tooling/anon` | `~/.local/bin/anon` — egress-policy gate + anonymisation hook (`policy`/`scrub`/`run`) |
| `tooling/bcw` | `~/.local/bin/bcw` — BC Extension Analysis CLI (`analyse`/`collect`) |
| `tooling/probe` | `~/.local/bin/probe` — local read-only investigation (pi + Larry, no egress) |
| `tooling/md2pdf` | `~/.local/bin/md2pdf` — markdown → styled A4 PDF in **house purple**, page numbers, footer from the first H1. Pre-renders ```` ```mermaid ```` fences into real diagrams via `mmdc`. The converter half of the `doc-convert` toolchain, beside pandoc and pymupdf. **The single canonical copy** — see [`tooling/md2pdf-handover.md`](tooling/md2pdf-handover.md) |

`md2pdf` picks its PDF engine itself: **WeasyPrint** where it imports (Linux clients),
**headless Edge** where it does not (the Windows workstation has no GTK3 runtime).
Diagrams follow the engine — PNG under WeasyPrint, which cannot render the
`<foreignObject>` mermaid-cli emits; SVG under Edge. Override with
`MD2PDF_ENGINE=weasyprint|edge` and `MD2PDF_MERMAID=png|svg`. No `mmdc` on PATH means
fences print as source with a warning, never a failure. Windows is the one machine that
cannot symlink it — it uses `~/.local/bin/md2pdf.cmd` (PowerShell) and a `md2pdf` sh
shim (Git Bash), both calling the repo copy directly.

Re-link on a new machine — resolve the repo first, then everything below is
machine-independent:
```sh
SETUP_DIR="${SETUP_DIR:-$([ -d "$HOME/larry-setup" ] && echo "$HOME/larry-setup" || echo /mnt/rojaws/localDev/setup)}"
ln -s $SETUP_DIR/tooling/alw ~/.local/bin/alw
ln -sf $SETUP_DIR/tooling/anon ~/.local/bin/anon && chmod +x ~/.local/bin/anon  # symlink, not copy
ln -sf $SETUP_DIR/tooling/md2pdf ~/.local/bin/md2pdf
for f in al-route cs-route go-route spec handover warplan scout al fable handbook; do
  ln -sf $SETUP_DIR/tooling/$f.md ~/.pi/agent/prompts/$f.md
done
for f in warplan scout spec wizard to-questionnaire writing-for-agents; do
  ln -sf $SETUP_DIR/tooling/$f-claude.md ~/.claude/commands/$f.md
done
for f in al fable handbook al-syntax; do
  ln -sf $SETUP_DIR/tooling/$f.md ~/.claude/commands/$f.md
done
ln -sf $SETUP_DIR/tooling/bc-agent.md ~/.pi/agent/prompts/bc-agent.md   # /bc-agent for pi
ln -sf $SETUP_DIR/tooling/bc-agent.md ~/.claude/commands/bc-agent.md     # and Claude Code
ln -sf $SETUP_DIR/tooling/ste.md ~/.pi/agent/prompts/ste.md              # /ste for pi
ln -sf $SETUP_DIR/tooling/ste.md ~/.claude/commands/ste.md               # and Claude Code
mkdir -p ~/.claude/skills/ste-writing                                                    # + auto-triggering skill
for f in SKILL.md ste-lint.py ste-recurring-errors.md; do
  ln -sf $SETUP_DIR/tooling/ste/$f ~/.claude/skills/ste-writing/$f
done
```

## Related, outside this repo

- **`~/.config/nvim/lua/config/alw.lua`** — the `<leader>aw` Neovim menu (lives in the nvim config repo).
- **`~/.pi/ollama-provider.ts`** — pi's provider extension. Per-machine (the baseUrl differs:
  Larry uses localhost, dev/laptop use the HTTPS proxy), so intentionally NOT tracked here.
- **AL projects** live in `/mnt/rojaws/localDev/projects/` (prototypes) and
  `/mnt/rojaws/Code/AL/` (promoted/refined) — not here; this repo is setup only.

## The pipeline in one line

`alw route` triages an ask; `alw new` scaffolds a prototype; `alw build [N]` runs
Larry (free) then optionally escalates to Claude after N stalled rounds; `alw promote`
ships it to `Code/AL`. The **AL compiler is the referee** — no LLM grades the code.

---

## License

Copyright (C) 2026 Dave Sinclair.

This program is free software: you can redistribute it and/or modify it under the
terms of the **GNU General Public License, version 3** as published by the Free
Software Foundation. See [LICENSE](LICENSE) for the full text.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Copyleft is deliberate: anyone may use, study, modify and redistribute this, but
derivatives must stay under the same licence and ship their source. It cannot be
folded into a closed product.

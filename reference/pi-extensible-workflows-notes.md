# pi-extensible-workflows — video notes (2026-07-31)

Source: Andrea Baccega, "Pi Extensible Workflows: Full Guide"
(youtu.be/qAiivspEHmU) · repo: https://github.com/vekexasia/pi-extensible-workflows
Transcript captured via yt-dlp auto-captions; distilled here. NOT AL knowledge —
do not route through ingw tiers.

## What it is

A pi extension implementing Claude-style scripted workflows: a tiny DSL
(`agent`, `shell`, `prompt`, `parallel`, `pipeline`, `phase`, `checkpoint`,
`withWorktree`) embedded in JS, so orchestration is code and only the
probabilistic steps are agents. Actively developed.

## Core ideas (and how they map to our stack)

| Video concept | Our equivalent / gap |
|---|---|
| Deterministic loop drives agent (`until tests pass, max N`) | run-build.py fix loop — same philosophy, ours is Python outside pi |
| Sub-agent results never land in main context | **Gap worth stealing**: our pi fix rounds run as one long agentic session → the 32k overflow wedge (`pi stream wedge`). Fan each fix round to a fresh short-lived agent = wedge avoidance by construction |
| Deterministic merge/cleanup phase ("makes no point to spin up an agent for this") | our normalizers (using-directives, string-props, AL0282 guard) — same doctrine |
| develop-until-approved (coder model + different reviewer model, feed findings back, max retries) | pi coms validator-peer review (gow/csw `--review`) — theirs is packaged as a reusable workflow function |
| Per-role tool/extension/skill exclusion → **system prompt cut ~50%** | **Biggest win available**: our coder runs load every extension (searxng, kb-search, coms…). On a 32k num_ctx model that's stolen budget — trimming leaves more room for AL-REFERENCE topic injection |
| Model aliases per role (reviewer=big, developer=mid, summarizer=cheap-no-tools) | matches our route-by-size lesson (qwen36 small / qwen3-coder large) |
| Run budgets: soft cap (injects "wrap up" msg) + hard cap (truncate) | we only have timeouts; soft-cap idea is nicer than SIGKILL |
| Journal → pause/resume/rerun with completed steps cached | our runs restart from zero on crash |
| JSON-schema-constrained workflow output | our `--mode json` manifest discipline |
| Bundle workflow + real code into a binary (API calls in code, agent for reasoning, creds stay out of the model) | bcw / probe already follow this shape |

## Assessment for us

Not a drop-in: run-build.py already IS a deterministic workflow harness and is
proven; rewriting it inside this extension buys little and adds a fast-moving
dependency. The transferable items, cheapest first:

1. **Role-scoped extension/tool trimming for pipeline pi calls** — slim system
   prompt on coder runs (no searxng, no kb-search MCP, no question tool).
   Direct token win on 32k models; nothing to install, `pi` flags/config only.
2. **Short-lived agents per fix round** instead of one long session — attacks
   the open stream-wedge bug at the design level.
3. Soft budget cap ("wrap up" injection) before hard timeout in run-build.
4. Extension itself worth a play for *interactive* multi-agent work on deb
   (issues → parallel worktrees → merge), where we have no harness at all.

Raw transcript: scratchpad only (not kept). Re-pull via
`yt-dlp --write-auto-subs` if needed.

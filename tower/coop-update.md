# COOP update — catch up since the original COOP bundle

Runbook to bring an existing **COOP** box up to date with everything added to `larry-setup`
after the first COOP guide. Written for **Claude executing on COOP (WSL2)**. COOP is the
standalone C#-first build box (own ollama + `csw`); this does **not** change that — it pulls
the new pipeline and flags the **one breaking change** that affects COOP.

> Prereq: the original setup is done (see `tower/coop-setup.md`). If COOP was never set up, do
> that first, then return here.
>
> **Letting Claude drive it?** Point Claude on COOP at the companion brief
> [`coop-update-claude.md`](coop-update-claude.md) (imperative, confirm-before-change).
>
> **Delivery:** COOP has **no repo access**, so the update ships as **`coop-update.zip`** that
> extracts over the existing `~/larry-setup` (which is a plain file tree, not a git clone).

---

## 0. Apply the update zip

```sh
# with coop-update.zip in your home dir — extract OVER the existing tree (overwrites changed files,
# adds new ones; your local .anon/ and handovers are untouched):
unzip -o ~/coop-update.zip -d ~/larry-setup
# refresh the CLIs COOP uses:
cp ~/larry-setup/tooling/csw ~/.local/bin/ && chmod +x ~/.local/bin/csw
```

The zip brings the new pipeline: an **egress policy gate**, an **anonymisation
hook**, BCQuality knowledge wiring, build metrics/leaderboard, SARIF diagnostics, a class-routed
fix-strategy, `handover_lint` (auto-run by `csw build`), model pre-warm, and more. Most is opt-in.
**One is breaking — do §1.**

> **Zip currency:** the delivery zip must be **regenerated from `setup/`** to include
> `pipeline/handover_lint.py` + the updated `run-build-cs.py`/`csw` — an older bundle predates them
> and `csw build` will fail importing the lint module. Regenerate before shipping (see
> [[reference-coop-setup]] for the file manifest).

---

## 1. ⚠ BREAKING — the egress policy will kill COOP's Claude escalation

New this weekend: every Claude call funnels through an **egress gate** (`pipeline/egress_policy.py`,
now imported by `run-build-cs.py`). It is **deny-by-default**: the default profile `local-only`
**blocks all Claude calls** and **disarms escalation** at startup.

COOP is a **12 GB** box — its 14B drafts lean on **Claude escalation** (`csw build <p> N`) for the
hard tier. Under the new default, that escalation silently refuses and the build stays on the local
model. **COOP must opt in.**

COOP is a standalone box using the colleague's **own** Claude account on **non-work** code, so the
right profile is **`personal`** (raw Claude allowed). Add to `~/.bashrc`:

```sh
echo 'export EGRESS_POLICY=personal' >> ~/.bashrc && source ~/.bashrc
```

Verify the gate now allows Claude:
```sh
ln -sf ~/larry-setup/tooling/anon ~/.local/bin/anon && chmod +x ~/.local/bin/anon   # symlink, NOT copy (imports pipeline/ by real path)
anon check          # personal -> ALLOW ; local-only -> BLOCK
```

> If the colleague ever puts **work / client** code on COOP that mustn't go to Anthropic, drop a
> per-repo `~/<repo>/.anon/config.yml` with `policy: local-only` (or `enterprise-anon`) — it
> overrides the env for that repo only. See §3 and `tooling/anon-claude-hook.spec.md`.

---

## 2. Re-confirm the 12 GB model override (default changed)

The pipeline default coder model changed to **`qwen3-coder:30b`** — which **does not fit COOP's
12 GB**. COOP already overrides this in `~/.bashrc` (from the original guide); confirm it's still
there, or escalation/write will try to load a 30B and spill to CPU:

```sh
grep -E 'PI_CODER_MODEL|COMS_.*_MODEL' ~/.bashrc
#   PI_CODER_MODEL=ollama/qwen2.5-coder:14b
#   COMS_VALIDATOR_MODEL=ollama/qwen2.5-coder:14b
#   COMS_RELAY_MODEL=ollama/qwen2.5-coder:14b
ollama ps           # after a build: PROCESSOR should read 100% GPU
```

---

## 3. New capabilities (opt-in) — enable what's useful for COOP

| Feature | What it does | COOP action |
|---|---|---|
| **Egress policy** (§1) | gates Claude egress per box/repo | **required**: `EGRESS_POLICY=personal` |
| **Anon hook** (`tooling/anon`) | `scrub`/`run` — scrub sensitive tokens + fail-closed secret gate before sending a repo to Claude; reversible | optional — only if COOP hosts work/client code. `anon run "<task>"` runs Claude on a scrubbed mirror and applies the reverse-mapped diff back |
| **BCQuality knowledge** | injects curated BC/AL rules into the coder + review prompts (fail-open: no clone → no change) | optional; AL-oriented, neutral for C#. To enable: clone BCQuality where the pipeline expects (see `pipeline/bcquality-integration.md`) |
| **Build metrics + leaderboard** | one JSON line per build → `build_leaderboard.py` | automatic, local, no action |
| **Fix-strategy (class-routed)** | `FIX_STRATEGY=auto` (now the **default**) picks snippet vs rewrite per error class. Force one with `FIX_STRATEGY=snippet` (local Fast-Apply SEARCH/REPLACE, no cascade) or `=rewrite` | automatic; force `snippet` only if the 14B keeps breaking files on rewrites |
| **handover_lint** | `csw build` now **lints the manifest first** and refuses a build on a defective handover (catches fixture defects before spending a build). Bypass with `LINT=0` | automatic — if a build stops before writing with a lint error, fix the handover or `LINT=0 csw build …` |
| **Forward-fix + pre-warm** | Claude fixes forward without reverting on parse-unmask; coder model pre-warmed before write | automatic |
| **`REVIEW_BACKEND=claude`** | stronger Claude behaviour reviewer (`csw build … --review`) | optional; **egress-gated** — needs `EGRESS_POLICY=personal` |
| **SARIF diagnostics / AL LSP** | structured compiler diagnostics + AL navigation | AL-only; not used by `csw` |
| **`md2pdf` + `/doc-convert`** | markdown → styled PDF with mermaid diagrams rendered, and PDF/docx/xlsx ingest | optional, local, no egress. COOP is WSL2 Linux, so it uses WeasyPrint — install per `coop-setup.md` §6. Without `mmdc` the diagrams print as source text rather than failing |

---

## 4. Verify COOP end-to-end

```sh
csw help
# with escalation, on a smoke project — proves the policy lets Claude close:
csw build coop-smoke 2      # pi does 2 rounds on the 14B, then Claude closes
```

Expect the banner to print `Egress policy: personal` and `Escalation: ARMED …` (not
`DISARMED by egress policy`). If you see DISARMED, `EGRESS_POLICY` isn't set — redo §1.

---

## TL;DR for COOP

1. `unzip -o ~/coop-update.zip -d ~/larry-setup` + refresh `csw`.
2. **`export EGRESS_POLICY=personal`** in `~/.bashrc` — or Claude escalation is dead (deny-by-default).
3. Confirm `PI_CODER_MODEL=ollama/qwen2.5-coder:14b` is still set (default is now a 30B that won't fit 12 GB).
4. Optional extras: `anon` hook (work code), `FIX_STRATEGY=snippet`, BCQuality, `REVIEW_BACKEND=claude`.
5. `csw build coop-smoke 2` → banner shows `personal` + `ARMED`, build passes.

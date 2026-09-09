# ThinkPad setup — native Linux Larry client (ollama → pi | claude)

**Goal:** stand up the dev pipeline on the **roaming ThinkPad (Debian, native Linux)** as a
**thin client of Larry** — pi and Claude Code drive builds, LLM inference happens on **Larry over
the LAN**. No local GPU, no local ollama, no model pulls.

```
 ThinkPad (Debian, native Linux)       LAN                    Larry (Rocky 10, RX 7900 XTX)
 ┌─────────────────────────┐                                  ┌──────────────────────────┐
 │ alw / gow / csw          │                                  │ nginx :11443 (HTTPS)     │
 │   └ pi ──────────────────┼──► https://larry.home.arpa:11443 ┼─► ollama :11434          │
 │   └ claude (escalation) ─┼──► api.anthropic.com (public CA) │   qwen3-coder:30b, etc.  │
 └─────────────────────────┘                                  └──────────────────────────┘
```

**Same role as the WSL box** (`wsl-setup.md`) — owns **no** inference, reuses Larry's full-fat
30–35B models over the HTTPS proxy. **NOT COOP** (`coop-setup.md` = standalone GPU box). Difference
vs WSL: this is **native Linux on real LAN hardware**, so the whole Windows/WSL networking layer is
gone — no `.wslconfig`, no mirrored networking, no `/mnt/c`. Two things still make or break it (DNS +
CA trust), then drop in pi, Claude, and the tooling.

> **Audience:** Claude Code on the ThinkPad. Steps marked **[HUMAN]** need the operator (copying the
> CA cert). Everything else is scriptable. Run verify gates before moving on. Shell = **zsh** with
> `ZDOTDIR=~/.config/zsh` — env goes in **`~/.config/zsh/.zshenv`**, NOT `~/.zshrc` or `~/.bashrc`.

---

## 0. The two things that make or break this

Native Linux removes the WSL networking pain, but the LAN-trust crux is the same:

1. **DNS** — the ThinkPad must resolve `larry.home.arpa` (served by Pi-hole on Nemesis). This
   just works **while on the home LAN** with Pi-hole as the DNS server (DHCP-assigned). **Roaming
   caveat:** off the home network there is **no Larry** — pi/local builds won't reach it. Claude
   escalation still works anywhere (public CA).
2. **TLS** — pi talks to `https://larry.home.arpa:11443`, which uses the **HomeLab CA** (self-signed
   root). The box must trust that CA (`update-ca-certificates`) **and** Node must use the system
   trust store (`NODE_OPTIONS=--use-system-ca`).

If a later step fails, it's almost always one of these two. See **Troubleshooting**.

---

## 1. Base tools

```sh
sudo apt update && sudo apt install -y build-essential git curl unzip \
  python3 python3-venv ca-certificates zsh
```

Make zsh the login shell and point `ZDOTDIR` at `~/.config/zsh` (mirrors the dev box layout — the
default `~/.zshrc` is a leftover skeleton, real config lives under `~/.config/zsh`):

```sh
chsh -s "$(command -v zsh)"                 # log out/in to take effect
mkdir -p ~/.config/zsh
# bootstrap: the one file zsh reads before ZDOTDIR — sends it to ~/.config/zsh
echo 'export ZDOTDIR="$HOME/.config/zsh"' | sudo tee /etc/zsh/zshenv
touch ~/.config/zsh/.zshenv                 # all our env exports land here
```

> Everywhere below that says "append to `~/.config/zsh/.zshenv`", then `source` it (or open a new
> shell). This is the file that persists PATH/env across sessions.

---

## 2. Reach + trust Larry — the crux

### 2a. DNS resolves

```sh
getent hosts larry.home.arpa      # must print Larry's LAN IP
```

Empty → not on the home LAN, or Pi-hole isn't this box's DNS server. Check `resolvectl status`
(the active DNS server should be the Pi-hole IP). Do not proceed until this resolves.

### 2b. Install the HomeLab CA — [HUMAN to supply the cert]

pi/Node reject Larry's cert until the box trusts the HomeLab CA root (`ca.crt`). The operator copies
the **public** `ca.crt` onto the ThinkPad (the CA *key* stays on the Deb box — never copy that).
Native Linux, so `scp` it over the LAN or bring it on USB:

```sh
# e.g. from the deb box:  scp deb.home.arpa:/path/to/ca.crt ~/  — then:
sudo cp ~/ca.crt /usr/local/share/ca-certificates/homelab-ca.crt
sudo update-ca-certificates          # should report "1 added"
```

Verify the full chain over the proxy — the real test that DNS **and** TLS both work:

```sh
curl -sS https://larry.home.arpa:11443/api/version      # -> {"version":"..."} with NO -k flag
```

Succeeding **without `-k`** means the CA is trusted. If it needs `-k`, the cert isn't in the trust
store — fix before continuing.

---

## 3. Node + pi + provider

```sh
# Node 22+ — pi ≥ 0.75 requires Node ≥ 22.19.0; Debian stable ships 20, use NodeSource
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v                              # v22.x

# npm global prefix on PATH (matches the dev box layout)
npm config set prefix "$HOME/.npm-global"
npm install -g @earendil-works/pi-coding-agent
```

Copy **`~/.pi/ollama-provider.ts`** from the repo — `cp ~/larry-setup/tower/ollama-provider.ts ~/.pi/`
(baseUrl points at Larry's HTTPS proxy — do NOT change to localhost, there is no local ollama).

> **pi 0.81 migration (2026-07-22) — mandatory.** The repo file uses the 0.81 complete-provider
> form (`createProvider(openAICompletionsApi())`). The old legacy `registerProvider("ollama", {…})`
> form **breaks native tool-calling on pi ≥ 0.81**: local qwen models emit tool calls as
> `<function=…>` text and `web_search`/`kb_search` never run. Always deploy the repo copy — do not
> hand-write the legacy form.
>
> **Already have an older install?** First ensure **pi ≥ 0.81** (`npm i -g @earendil-works/pi-coding-agent@latest`) —
> the `createProvider` form errors with `undefined (reading 'streamSimple')` on pi 0.80.x and takes the
> provider offline. Then `cd ~/larry-setup && git pull` and
> `cp tower/ollama-provider.ts ~/.pi/ && cp tower/bonsai/bonsai-provider.ts ~/.pi/`, restart pi.

```ts
import { createProvider, openAICompletionsApi } from "@earendil-works/pi-ai";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const BASE = "https://larry.home.arpa:11443/v1";

const mk = (id: string, name: string, ctx = 32768, max = 16384) => ({
  id, name, api: "openai-completions" as const, provider: "ollama", baseUrl: BASE,
  reasoning: false, input: ["text"] as ("text" | "image")[],
  cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
  contextWindow: ctx, maxTokens: max,
});

export default function (pi: ExtensionAPI) {
  pi.registerProvider(createProvider({
    id: "ollama",
    name: "Ollama (Larry)",
    baseUrl: BASE,
    auth: { apiKey: { name: "Ollama (local, keyless)",
      async resolve() { return { auth: { apiKey: "ollama" }, source: "keyless local server" }; } } },
    models: [
      mk("qwen3-coder:30b", "Qwen3 Coder 30B"),      // default coder (Go/C#/general)
      mk("al-coder-qwen3", "AL Coder Qwen3"),         // AL coder (Business Central) + al-rag
      mk("al-coder-qwen36", "AL Coder Qwen36"),
      mk("al-coder-north-mini", "AL Coder NorthMini"),
      mk("north-mini-code-1.0", "NorthMini Code 1.0"),
    ],
    api: openAICompletionsApi(),
  }));
}
```

Node must use the system CA store (so pi trusts Larry), and PATH must find the npm globals + local
bins. Append to **`~/.config/zsh/.zshenv`**:

```sh
cat >> ~/.config/zsh/.zshenv <<'EOF'

# ---------- Node / pi ----------
export NODE_OPTIONS="--use-system-ca"
export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:$PATH"
EOF
source ~/.config/zsh/.zshenv
```

Register the extension permanently in `~/.pi/agent/settings.json` so plain `pi` loads it — no `-e`
flag on every run (merge into the existing file if pi already created one):

```json
{
  "extensions": ["~/.pi/ollama-provider.ts"],
  "defaultModel": "qwen3-coder:30b"
}
```

Without this, `pi` starts with **"Warning: No models available"** — the provider file does nothing
until pi is told to load it.

Verify pi sees Larry's models over the proxy:

```sh
pi --list-models                     # must list qwen3-coder:30b etc.
pi -p "reply with exactly: OK"       # end-to-end: default model -> Larry over HTTPS
```

### 3a. Bonsai chat provider

Ternary-Bonsai-27B is the interactive-chat brain on Larry (`llama-server` behind nginx
`:8444`), time-sharing the GPU with the ollama coder. Builds never read these defaults —
every runner passes an explicit `-e`/`--model` plus `-ne`. Wire it the same as the coder:

```sh
cp ~/larry-setup/tower/bonsai/{bonsai-provider.ts,bonsai-control.ts} ~/.pi/
# then add both to "extensions" in ~/.pi/agent/settings.json:
#   ["~/.pi/ollama-provider.ts", "~/.pi/bonsai-provider.ts", "~/.pi/bonsai-control.ts"]
pi --list-models                     # bonsai/ternary-bonsai-27b now listed
```

`bonsai-control.ts` gives `/bonsai on|off` inside pi and auto-wakes the server, but it drives
the larry-dashboard API and needs its basic-auth creds — `LARRY_DASH_AUTH="user:pass"` or
`~/.pi/.larry-dash-auth` (chmod 600). Without them it prints a "no dashboard creds" message and
you start Bonsai from the dashboard by hand; `curl` to `:8444` returns **502** while the unit is
stopped (nginx up, backend down) — that is idle auto-stop, not a broken install. Same creds make
VRAM eviction work from this box during builds (`pipeline/bonsai_vram.py`). Details:
`tower/bonsai/bonsai-context.md`.

To match the workstation's chat defaults, set `"defaultProvider": "bonsai"` and
`"defaultModel": "ternary-bonsai-27b"` in the same file. Builds ignore both — every runner
passes an explicit `-e` and `--model`.

### 3b. OpenRouter (cheap cloud tier) — optional, **egress**

```sh
cp ~/larry-setup/tooling/openrouter-provider.ts ~/.pi/     # add to "extensions" as above
echo 'export OPENROUTER_API_KEY="sk-or-..."' >> ~/.config/zsh/local.zsh   # untracked, not .zshenv
```

Reaches a third-party cloud. The **pipeline** path (`CODER_BACKEND=mid`) is gated by
`egress_policy.allowed("openrouter")`, so a `local-only` repo can never route there — but an
**interactive** `pi --provider openrouter` is not gated by anything. Never chat customer AL to it.

`~/.config/zsh/local.zsh` is sourced from `.zshrc`, i.e. **interactive shells only** — a runner
launched from cron or a non-interactive script won't see the key.

> The provider registers itself **only when `OPENROUTER_API_KEY` is set**, and that guard is
> load-bearing. pi resolves the auth of every registered provider up front, so the earlier
> version — which threw a helpful error from `resolve()` — did not degrade to an unavailable
> model, it aborted the process: with no key, `pi --list-models` and even a plain `pi -p` died
> with `ModelsError: API key auth failed for provider openrouter`, taking bonsai and ollama down
> with them. Keep the guard.

---

## 4. Claude Code

```sh
curl -fsSL https://claude.ai/install.sh | bash    # native installer -> ~/.local/bin/claude
claude --version
```

Sign in interactively once (`claude`, follow the auth prompt). Claude talks to `api.anthropic.com`
(public CA — no HomeLab cert needed). This is the escalation backend when local rounds stall, and
works **on or off** the home LAN.

---

## 5. Setup repo + workflow tooling

The dev box runs tooling straight out of `/mnt/rojaws/localDev/setup`. Here that path doesn't exist —
clone the source-of-truth repo and point the workflow env at it:

```sh
git clone git@github.com:drs76/larry-setup.git ~/larry-setup    # or https:// if no SSH key
```

Put the CLIs on PATH and the pi prompt-templates in place. **Symlink, do not copy** — copies
were the original advice here and they silently rotted: a `git pull` updated the repo while
`~/.local/bin/alw` and the prompt copies stayed a month behind (missing `handover_lint`, the
handover path-placeholder substitution, and the `/scout`·`/al`·`/handbook` prompts). Symlinks
make `git pull` the only update step.

```sh
mkdir -p ~/.local/bin ~/.pi/agent/prompts ~/.pi/agent/extensions ~/.claude/commands

# workflow CLIs + local tools (anon = egress gate, kb/al-rag = KB thin client)
for f in alw gow csw anon bcw probe kb ingw al-rag kb-lint; do
  ln -sfn ~/larry-setup/tooling/$f ~/.local/bin/$f
done
chmod +x ~/larry-setup/tooling/{alw,gow,csw,anon,bcw,probe,kb,ingw,al-rag,kb-lint}

# pi prompts
for f in al-route cs-route go-route spec handover warplan scout al fable handbook bc-agent; do
  ln -sfn ~/larry-setup/tooling/$f.md ~/.pi/agent/prompts/$f.md
done

# Claude Code slash-commands. The *-claude.md variants install under the bare name
# (Claude is the intended planner for /warplan, /scout, /spec, /wizard, …).
for f in warplan scout spec wizard to-questionnaire writing-for-agents; do
  ln -sfn ~/larry-setup/tooling/$f-claude.md ~/.claude/commands/$f.md
done
for f in al fable handbook al-syntax bc-agent; do
  ln -sfn ~/larry-setup/tooling/$f.md ~/.claude/commands/$f.md
done

# pi extensions (web + KB search)
ln -sfn ~/larry-setup/tooling/searxng-search.pi-ext.ts ~/.pi/agent/extensions/searxng-search.ts
ln -sfn ~/larry-setup/tooling/kb-search.pi-ext.ts      ~/.pi/agent/extensions/kb-search.ts

find ~/.local/bin ~/.pi/agent/prompts ~/.claude/commands -xtype l    # must print nothing
```

Point the tooling env at `~/larry-setup` and set the working coder model. The `alw` script defaults
to `ornith:35b` (**broken** — ROCm cold-load hang) and to `/mnt/rojaws/...` paths, so override both.
Append to **`~/.config/zsh/.zshenv`**:

```sh
cat >> ~/.config/zsh/.zshenv <<'EOF'

# ---------- Larry workflow (ThinkPad client) ----------
export RUN_BUILD="$HOME/larry-setup/pipeline/run-build.py"        # AL
export RUN_EDIT="$HOME/larry-setup/pipeline/run-edit.py"          # AL edit flow (alw edit)
export RUN_BUILD_GO="$HOME/larry-setup/pipeline/run-build-go.py"  # Go
export RUN_BUILD_CS="$HOME/larry-setup/pipeline/run-build-cs.py"  # C#
# Per-language templates — a shared $TEMPLATE makes gow/csw pull the AL template.
export TEMPLATE_AL="$HOME/larry-setup/templates/larry-handover.template.md"
export TEMPLATE_GO="$HOME/larry-setup/templates/go-handover.template.md"
export TEMPLATE_CS="$HOME/larry-setup/templates/cs-handover.template.md"
export PROJECTS_DIR="$HOME/projects"
export PROTOTYPES_DIR="$HOME/projects/prototypes"
export CODE_AL="$HOME/projects/al"        # local promote target (no /mnt/rojaws/Code/AL when roaming)
export PI_CODER_MODEL="ollama/qwen3-coder:30b"                    # NOT ornith:35b (broken)
export COMS_VALIDATOR_MODEL="ollama/qwen3-coder:30b"
export COMS_RELAY_MODEL="ollama/qwen3-coder:30b"
# KB hybrid search: no local index here, query Larry's `kb serve` over HTTP.
# (The index moved off deb to Larry on 2026-08-06.) Token: ~/.pi/.kb-token.
export KB_REMOTE="http://larry.home.arpa:8848"
EOF
source ~/.config/zsh/.zshenv
mkdir -p ~/projects/prototypes
```

**Token: run the script, don't paste it.**
```bash
setup/tower/handoff-scripts/kb-client-setup.sh
```
It fetches `KB_SERVE_TOKEN` from Larry once and writes it to **both** `~/.pi/.kb-token`
(chmod 600) and the gitignored `local.zsh`, plus `KB_REMOTE` to `.zshenv` — without printing
the token. Both destinations matter: the environment variable wins when set, but `kb_core.py`,
the pi `kb-search` extension and `al-rag` all fall back to the file, so a box with only one of
them updated gets a silent `401` from every non-interactive caller. Idempotent, so **re-run it
after any rotation** (last rotated 2026-08-16; a box that missed it gets `401` on every `kb`
call).

**`ssh larry` must resolve first** — the script fetches over ssh and exits at step 1 otherwise.
That needs a keypair on Larry *and* the host alias; without the alias, ssh sends this box's
local account name and Larry refuses it. In `~/.ssh/config`:
```
Host larry
    HostName larry.home.arpa
    User dav
    IdentityFile ~/.ssh/id_ed25519
```
Copy the public half over with `ssh-copy-id -i ~/.ssh/id_ed25519.pub dav@larry.home.arpa`.

`kb`'s local-index paths want numpy; a thin client doesn't (`kb_core.py` imports it lazily and
only the index/vector-rerank path needs it). Install `python3-numpy` only if this box ever
indexes locally.

Verify: `alw help`, `gow help`, `csw help` all print usage.

### Egress policy — keep work repos local (deny-by-default)

The pipeline **cannot** send content to Anthropic unless the egress policy allows it. Resolution is
per-repo: `<repo>/.anon/config.yml [policy:]` > env `EGRESS_POLICY` > **`local-only`** (default). For
a **work** repo, drop in a `local-only` config so pi→Larry is the only path and any Claude escalation
is hard-blocked:

```sh
mkdir -p <work-repo>/.anon && cp ~/larry-setup/tooling/anon-config.example.yml <work-repo>/.anon/config.yml
echo ".anon/" >> <work-repo>/.gitignore
ln -sf ~/larry-setup/tooling/anon ~/.local/bin/anon && chmod +x ~/.local/bin/anon
anon policy --repo <work-repo>    # -> local-only
anon check                        # show the ALLOW/BLOCK decision per profile
```

Profiles: `local-only` (no egress) · `enterprise-anon` (Anthropic only via the anon hook) ·
`personal` (raw Claude, own box). Flip a work repo to `enterprise-anon` when appropriate; personal
repos on the same box can be `personal` independently. See `tooling/anon-claude-hook.spec.md`.

---

## 6. Language toolchains — install only what you'll build

**Go** (`gow`):
```sh
sudo apt install -y golang-go && go version
# Debian stable's golang-go can lag. If a build needs newer, use the official tarball:
#   curl -fsSL https://go.dev/dl/go1.24.0.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
#   echo 'export PATH="/usr/local/go/bin:$PATH"' >> ~/.config/zsh/.zshenv && source ~/.config/zsh/.zshenv
```

**.NET / C# / Azure Functions** (`csw`):
```sh
curl -fsSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0
echo 'export PATH="$HOME/.dotnet:$PATH"' >> ~/.config/zsh/.zshenv && source ~/.config/zsh/.zshenv
dotnet --version      # 10.x. Referee = dotnet build + format + test (no func host needed)
```

**AL / Business Central** (`alw`) — heaviest; only if building AL. Needs the dotnet **AL compiler**
(`al`) + a symbol cache. See `pipeline/ALW.md` + `reference/AL-REFERENCE.md` for compiler/symbol
setup. Model `al-coder-qwen36` runs on Larry — no local sizing concern.

---

## 7. ALNvim — Neovim AL editor (only if editing AL in Neovim)

[ALNvim](https://github.com/drs76/ALNvim) = the Neovim AL plugin (BC language support + Claude/pi
in-editor). Reuses what earlier sections already installed: **Node 22** (§3), **pi + provider**
(§3), **claude** (§4), **dotnet** (§6, needed — install the AL toolchain there first). The plugin
itself + a few Neovim deps + the AL compiler/LSP are all that's left. Private values (Larry host,
`al-coder-*`, `qwen2.5-coder:32b`) live **only** in your nvim config below — never in the public repo.

### 7a. Neovim 0.11+ and ripgrep

ALNvim uses `vim.pack` (Neovim **0.11+**). Debian stable ships older, so use the official release:

```sh
sudo apt install -y ripgrep unzip                     # rg required; unzip for VSIX extract
curl -fsSLo /tmp/nvim.tar.gz https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo tar -C /opt -xzf /tmp/nvim.tar.gz
sudo ln -sf /opt/nvim-linux-x86_64/bin/nvim /usr/local/bin/nvim
nvim --version                                         # NVIM v0.11.x
```

### 7b. Clone the plugin

```sh
git clone git@github.com:drs76/ALNvim.git ~/Documents/ALNvim   # or https://
```

### 7c. Neovim config — [HUMAN edits the nvim config]

ALNvim needs four Neovim plugin deps (Telescope + plenary, nvim-dap, LuaSnip) and its own
`setup()`. Put this in `~/.config/nvim/init.lua` (merge if it exists). **This file carries the
private Larry values** — it is your config, not the ALNvim repo:

```lua
vim.pack.add({
  { src = "https://github.com/nvim-lua/plenary.nvim" },
  { src = "https://github.com/nvim-telescope/telescope.nvim" },
  { src = "https://github.com/mfussenegger/nvim-dap" },
  { src = "https://github.com/L3MON4D3/LuaSnip" },
  { src = vim.fn.expand("~/Documents/ALNvim") },       -- local clone
}, { load = true })

require("al").setup({
  -- ghost / FIM completions → Larry over the HTTPS proxy (CA trusted in §2b, so insecure=false)
  ghost = { endpoint = "larry.home.arpa:11443", model = "qwen2.5-coder:32b", insecure = false },
  -- in-editor agents: :ALClaude / <leader>ai (Pro) and :ALPi / <leader>ak (local via Larry)
  agent = {
    pi_provider = "~/.pi/ollama-provider.ts",
    pi_model    = "ollama/al-coder-qwen36",            -- AL-tuned model on Larry
    pi_env      = { NODE_OPTIONS = "--use-system-ca" },
  },
})
```

> Ghost needs `qwen2.5-coder:32b` present on Larry (`ollama ls` on Larry to confirm). The FIM
> endpoint is `https://larry.home.arpa:11443/api/generate` — same HTTPS proxy, same CA trust from
> §2b. `insecure = true` (curl `-sk`) is the fallback only if the CA isn't in the store yet.

### 7d. Install the AL toolchain — from inside Neovim

Open any `.al` file, then run these ALNvim commands once:

```
:ALInstallDotnetTool     " dotnet tool install microsoft.dynamics.businesscentral.development.tools -> ~/.dotnet/tools/al
:ALInstallExtension      " downloads the MS AL VSIX (EditorServices LSP + DAP) -> ~/.vscode/extensions (no VS Code needed)
:ALInfo                  " sanity: shows detected al tool + extension + versions
```

The `al` dotnet tool is the compiler + MCP/agentic-LSP server; the VSIX supplies EditorServices
(full LSP/DAP). Confirm `al` is on PATH: `~/.dotnet/tools` should be in PATH (§6 already exports
`$HOME/.dotnet`; add `$HOME/.dotnet/tools` too if `:ALInstallDotnetTool` reports `al` not found).

### 7e. Verify

```sh
nvim some.al        # :ALActions (<leader>aa) lists commands; gd/hover work once symbols download
```

`:ALDownloadSymbolsGlobal` to fetch base symbols, `<leader>ak` opens pi (Larry), `<leader>ai` opens
Claude Code with the per-project al-mcp auto-registered in `~/.claude/settings.json`. Full docs:
ALNvim wiki + `~/Documents/ALNvim/docs/pi-setup.md`.

---

## 8. Carry over Claude Code plugins / config (extends §4)

Claude plugins install from **git marketplaces** — reinstall them, don't copy the hashed cache
dirs (paths are absolute + versioned). Two plugins on the dev box:

| Plugin | Marketplace | Source repo | Note |
|---|---|---|---|
| `caveman@caveman` | caveman | `JuliusBrussee/caveman` | terse output mode + statusline |
| `gopls-lsp@claude-plugins-official` | claude-plugins-official | `anthropics/claude-plugins-official` | Go LSP — only if editing Go |

### 8a. Reinstall (recommended — portable, gets updates)

In `claude` on the ThinkPad:

```
/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
/plugin install gopls-lsp@claude-plugins-official
```

`claude-plugins-official` is built-in — no `marketplace add`. `/plugin install` sets `enabledPlugins`
in `~/.claude/settings.json` automatically.

**Caveman statusline** — the install writes a new hash path, so wire it after installing:

```sh
ls ~/.claude/plugins/cache/caveman/caveman/      # -> note the <hash>
```

Add to `~/.claude/settings.json` (path uses this box's user + the hash above):

```json
"statusLine": {
  "type": "command",
  "command": "bash \"$HOME/.claude/plugins/cache/caveman/caveman/<hash>/hooks/caveman-statusline.sh\""
}
```

### 8b. Copy (fast — ONLY if the ThinkPad user is also `dav`)

The cache + settings paths are absolute (`/home/<user>/...`). Same username → verbatim copy works;
different username → use 8a instead.

```sh
rsync -a ~/.claude/plugins/  <thinkpad>:~/.claude/plugins/
# then merge only these 3 keys into ~/.claude/settings.json:
#   statusLine, enabledPlugins, extraKnownMarketplaces
```

### 8c. Do NOT copy

- **`~/.claude/.credentials.json`** — re-auth on the new box (`claude`, follow prompt); §4 already
  does this.
- **`mcpServers` block** — the dev box's `al:*` servers point at `/mnt/rojaws` + `~/Documents/AL`
  paths that don't exist here, and `fff` needs the `fff-mcp` binary. Wire AL MCP **per-project**
  (ALNvim's `:ALMcpSetup` / §7 does this), never globally.
- **Hashed `plugins/cache/` dirs by hand** — let `/plugin install` create them.

Custom slash-commands (`~/.claude/commands/*.md`) are all symlinked by §5 — nothing to copy, and
a `git pull` updates them. Never copy one from the dev box's `~/.claude/commands/`: those are
themselves symlinks into `/mnt/rojaws/localDev/setup`, which is a *different checkout* of this
repo and drifts from `~/larry-setup`.

---

## 9. Smoke test

### After a `git pull` — check the pipeline still resolves

A pull is the whole update: the pipeline has no install step and every setting added since has a
working default. One check is worth the minute, because what it catches is a build that quietly
stops writing files rather than one that errors.

```sh
cd ~/larry-setup/pipeline && python3 test_al_intelligence.py 2>&1 | tail -3
```

Expect `258/258 PASS` — the count grows over time, so a **failure** is the signal, not the number.
This proves the pipeline's modules resolve on this box. `pipeline/coder.py` is imported by all
three build orchestrators (AL, Go, C#), so a partial clone or a stale symlink surfaces here first.

Then run the smoke below, because no unit test spawns the coder.


Prove the full loop — ThinkPad scaffolds, pi drives Larry over the proxy, referee grades:

```sh
gow new tp-smoke
# put a tiny spec in ~/projects/prototypes/tp-smoke/larry-handover.prompt.md
# (e.g. an http handler GET /ping -> "pong"), then:
gow build tp-smoke
```

Expect `RESULT: PASS` (Larry writes the code over HTTPS, `go build`+`vet`+`test` pass). Add
`--review` for the validator peer. Escalate to Claude after N stalled rounds: `gow build tp-smoke 2`.

Full lifecycle + `/spec` → `/handover` flow: `pipeline/PROJECT-LIFECYCLE.md`.

---

## 10. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `getent hosts larry.home.arpa` empty | not on home LAN / Pi-hole not the DNS server | join home LAN; `resolvectl status` should show Pi-hole IP as DNS |
| `curl` to `:11443` needs `-k`, pi errors `self-signed cert` / `unable to verify` | HomeLab CA not trusted | §2b: cp `ca.crt` → `/usr/local/share/ca-certificates/` + `update-ca-certificates` |
| pi lists models but every build stalls / times out | wrong/broken model | `PI_CODER_MODEL=ollama/qwen3-coder:30b`, not `ornith:35b`; check Larry has coder loaded (`ollama ps` on Larry) |
| pi TLS OK via curl but Node still rejects | `NODE_OPTIONS` unset | `export NODE_OPTIONS="--use-system-ca"` in `~/.config/zsh/.zshenv`, re-source |
| pi starts with `Warning: No models available` | provider extension not loaded | add `"extensions": ["~/.pi/ollama-provider.ts"]` to `~/.pi/agent/settings.json` (§3) |
| `pi update` says `Requires Newer Node` | Node < 22.19 (Debian repo max is 20) | NodeSource Node 22 (§3), then `pi update` |
| env exports don't persist / PATH empty in new shell | put in `~/.zshrc` (skeleton) not `.zshenv` | all exports go in `~/.config/zsh/.zshenv`; confirm `/etc/zsh/zshenv` sets `ZDOTDIR` |
| `alw`/`gow` uses `/mnt/rojaws/...` paths | env not overridden | confirm the §5 exports are in `~/.config/zsh/.zshenv` and sourced |
| everything worked at home, dead elsewhere | roaming off home LAN | expected — Larry is LAN-only; only Claude escalation works off-network |
| ALNvim: `require("al")` nil / commands missing | `vim.pack.add` didn't load, or Neovim < 0.11 | pass `{ load = true }`; `nvim --version` must be 0.11+ (§7a) |
| ALNvim: `:ALActions`/Explorer error `rg not found` / telescope missing | ripgrep or plugin deps absent | `sudo apt install ripgrep`; add plenary+telescope to `vim.pack.add` (§7c) |
| ALNvim: `al` not found / no compile | dotnet AL tool not installed / not on PATH | `:ALInstallDotnetTool`; add `$HOME/.dotnet/tools` to PATH in `~/.config/zsh/.zshenv` |
| ALNvim: no LSP (no hover/gd/diagnostics) | MS AL VSIX not installed | `:ALInstallExtension`; then `:ALInfo` to confirm ext detected |
| ALNvim ghost: empty/blank completions | model missing on Larry or FIM TLS | `ollama ls` on Larry for `qwen2.5-coder:32b`; CA trusted (§2b) or set `ghost.insecure=true` |

---

## What differs from the dev box / WSL (quick reference)

| | Dev box (localDev) | WSL client | **ThinkPad (this doc)** |
|---|---|---|---|
| ollama transport | `https://larry.home.arpa:11443/v1` | same | **same** |
| tooling source | `/mnt/rojaws/localDev/setup` (symlinks) | `~/larry-setup` clone | `~/larry-setup` clone |
| projects dir | `/mnt/rojaws/localDev/projects` | `~/projects` | `~/projects` |
| DNS | native LAN | mirrored networking (`.wslconfig`) | **native LAN (home only)** |
| CA trust | already installed | install `homelab-ca.crt` | **install `homelab-ca.crt`** |
| env file | `~/.config/zsh/.zshenv` | `~/.bashrc` | **`~/.config/zsh/.zshenv`** |
| Larry reachable | always (wired) | while WSL up | **home LAN only (roaming)** |
| coder model | qwen3-coder:30b | same | same (Larry does inference) |

Source-of-truth for all of the above: `setup/README.md`, `setup/tower/larry-context.md`,
`setup/tower/wsl-setup.md` (sibling client guide).

---

## 11. Desktop session (Sway) at the greeter — optional

The tiling-WM setup (sway/waybar/foot/mako/wofi) is separate from the Larry pipeline. Install it
from `tower/sway-setup/` — `./install.sh` handles packages + config symlinks. On this box run the
privileged steps with **`doas`**, not `sudo` (install.sh calls `sudo`, which needs a password here;
either run its apt line manually under `doas` or edit the script). Full guide + keybindings:
`tower/sway-setup/README.md`. `tmux` config is in `tower/tmux-setup/` (symlink `tmux.conf` →
`~/.tmux.conf`, and `cpu.sh`/`battery.sh` → `~/.config/tmux/`).

**Greeter gotcha (both this box and the dev box):** a fresh Debian `lightdm-gtk-greeter` ships
`/etc/lightdm/lightdm-gtk-greeter.conf` with `indicators=` commented out, so the login screen shows
**no session selector** — you can't choose Sway even though `/usr/share/wayland-sessions/sway.desktop`
exists. It is not a greeter-swap problem (`update-alternatives --query lightdm-greeter` stays
`lightdm-gtk-greeter`). Add under `[greeter]` (root, `doas`; back the file up first):

```ini
indicators=~host;~spacer;~clock;~spacer;~session;~language;~a11y;~power
default-session=sway
```

`~session` renders the picker; `default-session=sway` pre-selects Sway. Takes effect at the next
greeter show — **do not restart lightdm while logged in** (it kills your session).

**Powerline glyphs** (tmux/waybar): the Debian `fonts-jetbrains-mono` package is the plain family,
not the Nerd-patched one, so the status-bar icons render as tofu. Install the glyphs-only fallback —
`SymbolsNerdFont` from the nerd-fonts release `NerdFontsSymbolsOnly.zip` into `~/.local/share/fonts`,
then `fc-cache -f` — and fontconfig resolves the icons without touching any config file.

**Waybar module icons** (the cpu/mem/temp/net/vol/battery glyphs next to each %): two things must
both be true, and neither is automatic.

1. **Font chain must list the symbol font.** `waybar/style.css` sets
   `font-family: "JetBrains Mono", "Symbols Nerd Font", "Font Awesome 6 Free", monospace;`.
   Installing `SymbolsNerdFont` (above) is not enough — if it is missing from this chain, Pango has
   nothing to fall through to for the Private-Use-Area codepoints and every icon is an empty box.
   `Font Awesome 6 Free` is *not* installed on these boxes (only ancient FontAwesome v4), so it is a
   dead entry — `Symbols Nerd Font` is what actually renders.
2. **The glyphs must be in `waybar/config`.** Each module carries a literal Nerd Font codepoint in
   its `format` / `format-icons`. Current mapping (edit by codepoint, not by pasting — the MDI
   glyphs live in the astral plane and get mangled by many editors):

   | module | codepoint(s) | glyph |
   |--------|--------------|-------|
   | cpu | `U+F4BC` | oct-cpu |
   | memory | `U+F035B` | md-memory |
   | temperature | `U+F2C9` | fa-thermometer |
   | network wifi | `U+F1EB` | fa-wifi |
   | network ethernet | `U+F0E8` | fa-sitemap |
   | network off | `U+F05E` | fa-ban |
   | volume low/med/high | `U+F026 U+F027 U+F028` | fa-volume-* |
   | volume muted | `U+F0581` | md-volume-off (fa-mute `U+F6A9` is absent) |
   | battery empty->full | `U+F244 U+F243 U+F242 U+F241 U+F240` | fa-battery-* |
   | battery charging | `U+F0E7` | fa-bolt |
   | brightness | `U+F185` | fa-sun |

   A blank placeholder (`"  {usage}%"`, `["", ""]`) shows a bare percentage with no icon.

To pick or verify a codepoint against the installed font before editing the config:

```python
from fontTools.ttLib import TTFont
f = TTFont("~/.local/share/fonts/NerdSymbols/SymbolsNerdFont-Regular.ttf")
cmap = set().union(*(t.cmap for t in f["cmap"].tables))
print(0xF4BC in cmap)   # True = renders
```

Not every glyph exists in the symbols-only build (e.g. fa volume-mute `U+F6A9` is absent — use md
volume-off `U+F0581` instead). After editing, `swaymsg reload` respawns waybar with a new pid; a plain
`pkill -SIGUSR2 waybar` re-reads style but may not pick up config changes.

## 12. Roaming — reach Larry over WireGuard (out of the house)

Everything above assumes the ThinkPad is on the home LAN: `larry.home.arpa` is resolved by Pi-hole
(Nemesis, `192.168.0.175`) and nginx `:11443` is reachable at Larry's LAN IP `192.168.0.173`. Off the
LAN both break. A **WireGuard tunnel back home restores them unchanged** — the HomeLab CA is already
trusted, so nothing above the transport changes.

WireGuard is **already running at the home router** (`192.168.0.1`) for jellydav + navidrome — port
forward and DDNS exist. Roaming Larry is therefore just **one more peer** whose config (a) routes the
home `/24` and (b) uses Pi-hole for DNS. Larry/Nemesis/nomad do **not** run `wg` — don't look there.

**1. Client config** — `/etc/wireguard/larry.conf` (own keypair; `wg genkey | tee priv | wg pubkey`,
or via openssl: `openssl genpkey -algorithm X25519 -out k.pem; openssl pkey -in k.pem -outform der |
tail -c 32 | base64` for the private, add `-pubout` for the public):

```ini
[Interface]
PrivateKey = <client-priv>
Address    = 10.x.x.N/32          # next free tunnel IP — check an existing jellydav peer
DNS        = 192.168.0.175        # Pi-hole (Nemesis) -> resolves larry.home.arpa

[Peer]
PublicKey  = <router-wg-pubkey>   # same [Peer] PublicKey as the jellydav/phone config
Endpoint   = <ddns-host>:<wg-port># same public endpoint jellydav uses
AllowedIPs = 192.168.0.0/24       # split-tunnel: home LAN only. full-tunnel: 0.0.0.0/0
PersistentKeepalive = 25
```

The three placeholders that aren't LAN-derivable (`<router-wg-pubkey>`, `<ddns-host>:<wg-port>`, the
tunnel subnet for `Address`) are copied verbatim from an existing working peer (phone's jellydav
config or the router WG UI).

**2. Router** — add a peer: paste `<client-pub>`, set its AllowedIPs to `10.x.x.N/32`. The router
already routes to the LAN, so Larry is reachable once the client routes `192.168.0.0/24`.

**3. Use it:**

```bash
doas cp larry.conf /etc/wireguard/larry.conf && doas chmod 600 /etc/wireguard/larry.conf
doas wg-quick up larry                                   # bring tunnel up when out
getent hosts larry.home.arpa                             # -> 192.168.0.173 (via Pi-hole)
curl -sS https://larry.home.arpa:11443/api/version       # -> {"version":...} NO -k
doas wg-quick down larry                                  # back home: drop it (LAN is direct)
```

`pi/alw/gow/csw` then behave exactly as on the LAN. Split-tunnel (`AllowedIPs = 192.168.0.0/24`) keeps
all other traffic on the local link; use `0.0.0.0/0` only if you want everything through home.

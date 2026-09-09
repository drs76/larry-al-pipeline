# WSL setup — mirror the dev box as a Larry client (ollama → pi | claude)

**Goal:** stand up this machine's dev pipeline inside **WSL2 (Debian on Windows)** as a
**thin client of Larry** — pi and Claude Code drive builds, the LLM inference happens on
**Larry over the LAN**. No local GPU, no local ollama, no model pulls on WSL.

```
 WSL2 (Ubuntu)                         LAN                    Larry (Rocky 10, RX 7900 XTX)
 ┌─────────────────────────┐                                  ┌──────────────────────────┐
 │ alw / gow / csw          │                                  │ nginx :11443 (HTTPS)     │
 │   └ pi ──────────────────┼──► https://larry.home.arpa:11443 ┼─► ollama :11434          │
 │   └ claude (escalation) ─┼──► api.anthropic.com (public CA) │   qwen3-coder:30b, etc.  │
 └─────────────────────────┘                                  └──────────────────────────┘
```

**This is NOT COOP.** COOP (`coop-setup.md`) is a *standalone* box with its own GPU + ollama +
12 GB-sized models. This WSL box owns **no** inference — it reuses Larry's full-fat 30–35B models
over the HTTPS proxy, exactly like the primary dev machine. The whole job here is (1) let WSL
**reach + trust** Larry, then (2) drop in pi, Claude, and the workflow tooling.

> **Audience:** Claude Code executing on the WSL box. Steps marked **[HUMAN]** need the operator
> (Windows-side PowerShell, or copying the CA cert) — pause and ask; everything else is scriptable
> inside WSL. Run verify gates before moving on.

---

## 0. The two things that make or break this

Everything else is standard install. These two are the crux — get them first:

1. **DNS** — WSL must resolve `larry.home.arpa` (served by Pi-hole on Nemesis). Default WSL NAT
   networking uses its own resolver and **won't** see LAN DNS. Fix = **mirrored networking**
   (`.wslconfig`), which makes WSL share the Windows host's network + DNS.
2. **TLS** — pi talks to `https://larry.home.arpa:11443` which uses the **HomeLab CA** (self-signed
   root). WSL must trust that CA (`update-ca-certificates`) **and** Node must use the system trust
   store (`NODE_OPTIONS=--use-system-ca`).

If a later step fails, it's almost always one of these two. See **Troubleshooting**.

---

## 1. Windows prereqs — [HUMAN]

Run in **PowerShell as admin**:

```powershell
wsl --install -d Debian      # skip if Debian already installed
wsl --update
```

Enable **mirrored networking** so WSL resolves `*.home.arpa` and reaches the LAN. Create/edit
`C:\Users\<you>\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
```

Then apply:

```powershell
wsl --shutdown
```

Re-open Debian. Confirm the Windows host itself can resolve Larry (it should — same Pi-hole DNS):
`ping larry.home.arpa` in PowerShell should reply. If Windows can't resolve it either, fix Pi-hole
DNS on the Windows NIC first — WSL inherits it.

### 1b. Terminal — WezTerm on the Windows host [optional]

WezTerm config is tracked at `setup/tower/wezterm/wezterm.lua`. It defaults to **PowerShell**; WSL /
pwsh / cmd are on the launch menu (`Ctrl+Shift+L`). Install on the Windows host (from PowerShell):

```powershell
copy \\wsl$\Debian\home\<you>\larry-setup\tower\wezterm\wezterm.lua $env:USERPROFILE\.wezterm.lua
# or, if the NFS repo is mounted on Windows, copy from setup\tower\wezterm\wezterm.lua
```

Edits belong in the repo copy — re-copy after `git pull` (WezTerm hot-reloads `.wezterm.lua`).

---

## 2. Base tools (WSL)

```sh
sudo apt update && sudo apt install -y build-essential git curl unzip python3 python3-venv ca-certificates
```

---

## 3. Reach + trust Larry — the crux

### 3a. DNS resolves

```sh
getent hosts larry.home.arpa      # must print Larry's LAN IP
```

No output → mirrored networking (step 1) isn't active, or Pi-hole DNS isn't on the Windows NIC.
Do not proceed until this resolves.

### 3b. Install the HomeLab CA — [HUMAN to supply the cert]

pi/Node will reject Larry's cert until WSL trusts the HomeLab CA root (`ca.crt`). The operator must
copy the **public** `ca.crt` into WSL (the CA *key* stays on the Deb box — never copy that). Windows
filesystem is mounted at `/mnt/c`, so if the operator drops it in Downloads:

```sh
# adjust path to wherever the operator placed ca.crt
sudo cp /mnt/c/Users/*/Downloads/ca.crt /usr/local/share/ca-certificates/homelab-ca.crt
sudo update-ca-certificates          # should report "1 added"
```

Verify the full chain over the proxy — this is the real test that DNS **and** TLS both work:

```sh
curl -sS https://larry.home.arpa:11443/api/version      # -> {"version":"..."} with NO -k flag
```

`curl` succeeding **without `-k`** means the CA is trusted. If it needs `-k`, the cert isn't in the
trust store yet — fix before continuing.

---

## 4. Node + pi + provider

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

> **pi 0.81 migration (2026-07-22):** this file uses the 0.81 complete-provider form
> (`createProvider(openAICompletionsApi())`). The old legacy `registerProvider("ollama", {api:"openai-completions", …})`
> form **breaks native tool-calling on pi ≥ 0.81** — local qwen models emit tool calls as
> `<function=…>` text and `web_search`/`kb_search` never execute. Always deploy the repo copy.
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

Node must use the system CA store (so pi trusts Larry). Add to `~/.bashrc`:

```sh
echo 'export NODE_OPTIONS="--use-system-ca"' >> ~/.bashrc
echo 'export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Register the extension permanently in `~/.pi/agent/settings.json` so plain `pi` loads it —
no `-e` flag on every run (merge into the existing file if pi already created one):

```json
{
  "extensions": ["~/.pi/ollama-provider.ts"],
  "defaultModel": "qwen3-coder:30b"
}
```

Without this, `pi` starts with **"Warning: No models available"** — the provider file alone
does nothing until pi is told to load it.

Verify pi sees Larry's models over the proxy:

```sh
pi --list-models                     # must list qwen3-coder:30b etc.
pi -p "reply with exactly: OK"       # end-to-end: default model -> Larry over HTTPS
```

---

## 5. Claude Code

```sh
curl -fsSL https://claude.ai/install.sh | bash    # native installer -> ~/.local/bin/claude
claude --version
```

Sign in interactively once (`claude`, follow the auth prompt). Claude talks to `api.anthropic.com`
(public CA — no HomeLab cert needed). This is the escalation backend when local rounds stall.

---

## 6. Setup repo + workflow tooling

The dev box runs tooling straight out of `/mnt/rojaws/localDev/setup`. On WSL that path doesn't
exist — clone the source-of-truth repo and point the workflow env at it:

```sh
git clone git@github.com:drs76/larry-setup.git ~/larry-setup    # or https:// if no SSH key
```

Put the CLIs on PATH and the pi prompt-templates in place:

```sh
mkdir -p ~/.local/bin ~/.pi/agent/prompts ~/.claude/commands

# workflow CLIs (alw is a symlink on the dev box; copy is fine here)
cp ~/larry-setup/tooling/{alw,gow,csw} ~/.local/bin/ && chmod +x ~/.local/bin/{alw,gow,csw}

# pi triage/spec prompts
cp ~/larry-setup/tooling/{al-route.md,go-route.md,cs-route.md,spec.md,handover.md,warplan.md,bc-agent.md} ~/.pi/agent/prompts/

# Claude Code slash-commands. Two of them have a Claude-specific variant alongside the
# pi prompt of the same name (…-claude.md), so they install under the bare command name:
#   warplan-claude.md → /warplan (Claude is the planner; pi's warplan.md is the executor prompt)
#   spec-claude.md    → /spec    (Claude interview → SPEC/TASKS/handover; pi's spec.md is the free variant)
cp ~/larry-setup/tooling/warplan-claude.md ~/.claude/commands/warplan.md
cp ~/larry-setup/tooling/spec-claude.md    ~/.claude/commands/spec.md

# Single-source Claude commands (same file serves the slash-command):
#   /al    — BC AL expert session (compiler + cop + BCQuality grounded)
#   /fable — adopt the Fable 5 operating doctrine for the session
cp ~/larry-setup/tooling/{al.md,fable.md} ~/.claude/commands/

# Claude + pi shared: /bc-agent — BC agent discovery (prefill workbook / build plan).
# Needs the workbook template alongside it:
cp ~/larry-setup/tooling/bc-agent.md ~/.claude/commands/bc-agent.md
mkdir -p ~/larry-setup/templates   # bc-agent-requirements.template.md lives here
```

Installed Claude commands after this block: `/al`, `/fable`, `/spec`, `/warplan`, `/bc-agent`.
On the dev box these are symlinks into the setup repo (edits to the doctrine propagate); the
`cp` form above is the portable equivalent for a fresh WSL client.

Point the tooling env at `~/larry-setup` and set the working coder model. The `alw` script defaults
to `ornith:35b` (**broken** — ROCm cold-load hang) and to `/mnt/rojaws/...` paths, so override both.
Append to `~/.bashrc`:

```sh
cat >> ~/.bashrc <<'EOF'

# ---------- Larry workflow (WSL client) ----------
export RUN_BUILD="$HOME/larry-setup/pipeline/run-build.py"        # AL
export RUN_BUILD_GO="$HOME/larry-setup/pipeline/run-build-go.py"  # Go
export RUN_BUILD_CS="$HOME/larry-setup/pipeline/run-build-cs.py"  # C#
export TEMPLATE="$HOME/larry-setup/templates/larry-handover.template.md"
export PROJECTS_DIR="$HOME/projects"
export PROTOTYPES_DIR="$HOME/projects/prototypes"
export PI_CODER_MODEL="ollama/qwen3-coder:30b"                    # NOT ornith:35b (broken)
export COMS_VALIDATOR_MODEL="ollama/qwen3-coder:30b"
export COMS_RELAY_MODEL="ollama/qwen3-coder:30b"
EOF
source ~/.bashrc
mkdir -p ~/projects/prototypes
```

Verify: `alw help`, `gow help`, `csw help` all print usage.

### Egress policy — keep work repos local (deny-by-default)

The pipeline **cannot** send content to Anthropic unless the egress policy allows it. Resolution is
per-repo: `<repo>/.anon/config.yml [policy:]` > env `EGRESS_POLICY` > **`local-only`** (default). For a
**work** repo, drop in a `local-only` config so pi→Larry is the only path and any Claude escalation is
hard-blocked:

```sh
mkdir -p <work-repo>/.anon && cp ~/larry-setup/tooling/anon-config.example.yml <work-repo>/.anon/config.yml
echo ".anon/" >> <work-repo>/.gitignore
# symlink (not copy) so it finds pipeline/ — BUT if the share is mounted noexec
# (check `mount | grep <share>`), a symlink can't execute; use a wrapper instead:
ln -sf ~/larry-setup/tooling/anon ~/.local/bin/anon && chmod +x ~/.local/bin/anon
anon policy >/dev/null 2>&1 || printf '#!/bin/sh\nexec python3 %s "$@"\n' ~/larry-setup/tooling/anon > ~/.local/bin/anon && chmod +x ~/.local/bin/anon
anon policy --repo <work-repo>    # -> local-only
anon check                        # show the ALLOW/BLOCK decision per profile
```

Profiles: `local-only` (no egress) · `enterprise-anon` (Anthropic only via the anon hook — refuses
until that's built) · `personal` (raw Claude, own box). When the enterprise account lands, flip the
work repo's config to `enterprise-anon`. Personal repos on the same box can be `personal` independently.
See `tooling/anon-claude-hook.spec.md`.

### KB hybrid search — wire it, or `kb_search` fails at runtime

pi auto-discovers the `kb-search` extension, so this box advertises a `kb_search` tool whether
or not it can reach the index. Without this step the tool exists and returns `401` on every
call — worse than absent, because nothing says it is unwired.

**`ssh larry` must resolve first.** The script fetches the token over ssh and exits at step 1
otherwise. That needs a keypair on Larry **and** the host alias — without the alias ssh sends
this box's local account name and Larry refuses it. In `~/.ssh/config`:
```
Host larry
    HostName larry.home.arpa
    User dav
    IdentityFile ~/.ssh/id_ed25519
```
Copy the public half over with `ssh-copy-id -i ~/.ssh/id_ed25519.pub dav@larry.home.arpa`.

Then:
```sh
ln -sf ~/larry-setup/tooling/{kb,kb-lint} ~/.local/bin/
mkdir -p ~/.pi/agent/extensions
ln -sf ~/larry-setup/tooling/kb-search.pi-ext.ts ~/.pi/agent/extensions/kb-search.ts
bash ~/larry-setup/tower/handoff-scripts/kb-client-setup.sh
```

One fetch writes `KB_REMOTE` to `.zshenv`, and the token to **both** `~/.pi/.kb-token`
(chmod 600) and the gitignored `local.zsh`. Both matter: the environment variable wins when
set, but `kb_core.py`, the pi extension and `al-rag` all fall back to the file, so a box with
only one updated gets a silent `401` from every non-interactive caller. **Re-run after any
rotation** — it is the only supported refresh, and never paste the token into a shell file.

Verify: `kb stats` lists the corpora. There is no local index here; everything is served from
Larry.

### Doc tooling — `md2pdf` and the `/doc-convert` skill

`relink-tooling.sh` links `md2pdf` into `~/.local/bin`, but not the libraries it calls:

```sh
python3 -m pip install --user --break-system-packages \
  markdown weasyprint pymupdf pdfplumber python-docx openpyxl pypandoc-binary
ln -sf "$(python3 -c 'import pypandoc;print(pypandoc.get_pandoc_path())')" ~/.local/bin/pandoc
npm i -g @mermaid-js/mermaid-cli    # mmdc — without it, mermaid fences print as source text
```

**`--break-system-packages` is required on Debian 13**, which ships Python 3.13 as externally
managed. Without it pip refuses under PEP 668 and installs nothing.

WeasyPrint is the engine on Linux, and it needs the system pango/cairo libraries. Debian
desktop images already carry them; a minimal WSL rootfs may not, in which case
`md2pdf` reports "no PDF engine" rather than misbehaving. `pandoc` comes from the
`pypandoc-binary` wheel above so the whole toolchain stays in user space and needs no `sudo`.

Verify by conversion, not by import:
```sh
md2pdf ~/larry-setup/WORKFLOWS-OVERVIEW.md /tmp/wf.pdf   # expect: rendered 5 mermaid diagram(s)
```

---

## 7. Language toolchains — install only what you'll build

**Go** (`gow`):
```sh
sudo apt install -y golang-go && go version
# Debian stable's golang-go can lag. If a build needs newer, use the official tarball:
#   curl -fsSL https://go.dev/dl/go1.24.0.linux-amd64.tar.gz | sudo tar -C /usr/local -xz
#   echo 'export PATH="/usr/local/go/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
```

**C# / Azure Functions** (`csw`):
```sh
curl -fsSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0
echo 'export PATH="$HOME/.dotnet:$PATH"' >> ~/.bashrc && source ~/.bashrc
dotnet --version      # 10.x. Referee = dotnet build + format + test (no func host needed)
```

**AL / Business Central** (`alw`) — heaviest; only if building AL. Needs the dotnet **AL compiler**
(`al`) + a symbol cache. See `pipeline/ALW.md` + `reference/AL-REFERENCE.md` for the compiler/symbol
setup. Model `al-coder-qwen36` runs on Larry (fits its 24 GB) — no local sizing concern.

---

## 8. Smoke test

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


Prove the full loop — WSL scaffolds, pi drives Larry over the proxy, referee grades:

```sh
gow new wsl-smoke
# put a tiny spec in ~/projects/prototypes/wsl-smoke/larry-handover.prompt.md
# (e.g. an http handler GET /ping -> "pong"), then:
gow build wsl-smoke
```

Expect `RESULT: PASS` (Larry writes the code over the HTTPS proxy, `go build`+`vet`+`test` pass).
Add `--review` for the validator peer. Escalate to Claude after N stalled rounds: `gow build wsl-smoke 2`.

Full lifecycle + `/spec` → `/handover` flow: `pipeline/PROJECT-LIFECYCLE.md`.

---

## 9. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `getent hosts larry.home.arpa` empty | mirrored networking off / Pi-hole not on Windows DNS | step 1 `.wslconfig` + `wsl --shutdown`; confirm Windows resolves it |
| `curl` to `:11443` needs `-k`, pi errors `self-signed cert` / `unable to verify` | HomeLab CA not trusted | step 3b: cp `ca.crt` → `/usr/local/share/ca-certificates/` + `update-ca-certificates` |
| pi lists models but every build stalls / times out | wrong/broken model | `PI_CODER_MODEL=ollama/qwen3-coder:30b`, not `ornith:35b`; check Larry has the coder loaded (`ollama ps` on Larry) |
| pi TLS OK via curl but Node still rejects | `NODE_OPTIONS` unset | `export NODE_OPTIONS="--use-system-ca"` in `~/.bashrc`, re-source |
| pi starts with `Warning: No models available` | provider extension not loaded | add `"extensions": ["~/.pi/ollama-provider.ts"]` to `~/.pi/agent/settings.json` (step 4) |
| `pi update` says `Requires Newer Node` | Node < 22.19 (Debian repo max is 20) | NodeSource Node 22 (step 4), then `pi update` |
| DNS/LAN drops after Windows sleep/VPN | mirrored net + VPN interaction | `wsl --shutdown` and reopen; disable split-tunnel VPN or exclude LAN |
| `alw`/`gow` uses `/mnt/rojaws/...` paths | env not overridden | confirm the step 6 exports are in `~/.bashrc` and sourced |
| starship `Scanning current directory timed out` in `$HOME` | WSL/NFS home scan exceeds default 30ms | add `scan_timeout = 1000` + `command_timeout = 2000` to `~/.config/zsh/starship.toml` (top level) |

---

## 10. Roaming — reach Larry over WireGuard (out of the house)

Off the home LAN, `larry.home.arpa` (Pi-hole on Nemesis `192.168.0.175`) stops resolving and nginx
`:11443` at Larry's LAN IP `192.168.0.173` is unreachable. A **WireGuard tunnel back home restores
both** — the HomeLab CA is already trusted, so nothing above the transport changes. WireGuard already
runs at the home router (`192.168.0.1`) for jellydav + navidrome; roaming Larry is just one more peer.

**Run the tunnel on the Windows host, not inside WSL.** WSL already uses **mirrored networking** (step
1) for `*.home.arpa` DNS + LAN reach — so a tunnel on Windows is inherited by WSL automatically,
including the pushed Pi-hole DNS. Doing WireGuard inside WSL instead means TUN/kernel-module pain and a
second DNS to reconcile; skip it.

1. Install the **WireGuard for Windows** client on the host.
2. Import a tunnel config (same shape as the ThinkPad's — see `thinkpad-setup.md` §12; copy the
   router pubkey / DDNS endpoint / tunnel subnet from an existing jellydav peer):

   ```ini
   [Interface]
   PrivateKey = <client-priv>
   Address    = 10.x.x.N/32
   DNS        = 192.168.0.175        # Pi-hole -> larry.home.arpa
   [Peer]
   PublicKey  = <router-wg-pubkey>
   Endpoint   = <ddns-host>:<wg-port>
   AllowedIPs = 192.168.0.0/24       # home LAN only (split-tunnel)
   PersistentKeepalive = 25
   ```

3. Add the peer's `<client-pub>` on the router (AllowedIPs `10.x.x.N/32`), then **Activate** the
   tunnel in the Windows client. No `wsl --shutdown` needed — mirrored net picks it up live; if DNS
   looks stale, `wsl --shutdown` and reopen.

Verify inside WSL exactly as on the LAN:

```bash
getent hosts larry.home.arpa                       # -> 192.168.0.173
curl -sS https://larry.home.arpa:11443/api/version # -> {"version":...} NO -k
```

`pi/alw/gow/csw` then behave as on the LAN. Deactivate the Windows tunnel when back home (LAN is
direct). `AllowedIPs = 192.168.0.0/24` is split-tunnel; use `0.0.0.0/0` only to route everything home.

### `web_search` without the tunnel — the local SearXNG fallback

pi's `web_search` reads `SEARXNG_URL` **once at launch** and posts to `/search?format=json`. On the LAN
that is `https://searxng.home.arpa` (LXC 111 on Nemesis); off-LAN the name does not resolve, so
`.zshenv` falls back to `http://localhost:8888` — a `searxng/searxng` container on this box. `getent
hosts searxng.home.arpa` succeeding *is* the "am I home" test, so an active WireGuard tunnel puts you
back on the LAN instance and the container is not consulted.

```bash
searxng-local install    # write config, (re)create the container, verify engines answer
searxng-local status     # container state + a live query, per-engine result counts
```

Run `install` again after every `git pull` that touches `tooling/searxng-local-settings.yml` — the
container reads its config only at start, and `install` recreates it. The config is **copied**, not
symlinked: the container bind-mounts `~/.config/searxng-local`, and a symlink pointing outside that
directory does not resolve inside the container. `secret_key` is generated per machine into
`~/.config/searxng-local/.secret` and is not in the repo.

**If searches come back empty, the engines are blocked, not broken.** SearXNG scrapes; the big engines
answer a real browser and serve a CAPTCHA to a scraper. On 2026-08-29 every default general engine on
LXC 111 failed at once (duckduckgo + startpage CAPTCHA, brave HTTP 429, google empty with no error)
and searches returned zero results — which reads as "irrelevant results" rather than as an outage.
Diagnose per-engine, never from the result list alone:

```bash
curl -s "http://localhost:8888/search?q=test&format=json" | python3 -m json.tool | grep -A5 unresponsive
```

Then probe a candidate engine directly with its bang (`!bi` bing, `!yd` yandex, `!go` google) — bangs
work even for engines disabled in the config, so you can test one before enabling it. `bing` and
`yandex` are enabled here for exactly that reason; `bing` carries `weight: 0.3` because it broad-matches
and otherwise ranks a generic landing page above the pages that match all your terms.

---

## What differs from the dev box (quick reference)

| | Dev box (localDev) | **WSL client** |
|---|---|---|
| ollama transport | `https://larry.home.arpa:11443/v1` | **same** |
| tooling source | `/mnt/rojaws/localDev/setup` (symlinks) | `~/larry-setup` clone (copies) + env overrides |
| projects dir | `/mnt/rojaws/localDev/projects` | `~/projects` |
| DNS | native LAN | **mirrored networking** (`.wslconfig`) |
| CA trust | already installed | **install `homelab-ca.crt`** |
| coder model | qwen3-coder:30b | same (Larry does the inference) |

Source-of-truth for all of the above: `setup/README.md`, `setup/tower/larry-context.md`.

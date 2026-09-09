# Windows host setup — native Windows workstation as a Larry client (PowerShell, no WSL)

**Goal:** stand up a **native Windows workstation** as a Larry pipeline client — pi + Claude Code
drive builds, inference runs on **Larry** over the LAN HTTPS proxy. **PowerShell is the primary
shell**; **no WSL, no WezTerm**. **Git Bash** is installed for exactly one job: running the bash
workflow CLIs (`alw`/`gow`/`csw`). Everything else — installs, CA trust, provider config, pi,
Claude — is PowerShell-native.

Use this when you are moving off the **WSL2 thin client** ([`wsl-setup.md`](wsl-setup.md)) onto the
Windows host itself and want to live in PowerShell. This is the same Larry client as
[`windows-setup.md`](windows-setup.md) (the `docker-bc` **Server** box) but scoped to a personal
workstation terminal — PowerShell + Windows Terminal instead of WezTerm/tmux, and no docker-host
role. Almost all the porting knowledge is shared between the two docs; §7–§9 below are lifted from
`windows-setup.md`.

> **Audience:** the operator on the Windows box (or Claude Code running on it). `[HUMAN]` steps need
> the console (install media, sign-in). Reference implementation: `docker-bc` (192.168.0.191),
> built 2026-07-24 — this doc is its PowerShell-first cousin.

```
 Windows workstation                    LAN                    Larry (192.168.0.173)
 ┌─────────────────────────┐                                  ┌──────────────────────────┐
 │ PowerShell / Win Term    │                                  │ nginx :11443 (HTTPS)     │
 │   ├ pi  ─────────────────┼──► https://larry.home.arpa:11443 ┼─► ollama :11434          │
 │   └ claude (escalation) ─┼──► api.anthropic.com (public CA) │   qwen3-coder:30b, al-*  │
 │ Git Bash (alw/gow/csw) ──┘                                  └──────────────────────────┘
 └─────────────────────────┘
```

**Where you type what:** PowerShell (or Windows Terminal's default PowerShell tab) for everything —
installs, `pi`, `claude`. Open a **Git Bash** tab only to run `alw`/`gow`/`csw`, which are bash
scripts. `pi` and `claude` are npm binaries and run fine from PowerShell.

---

## 0. Base tools — [HUMAN or winget]

Windows 11 / 10 workstation. A workstation has **`winget`** (unlike the Server 2022 eval, which
does not — that box uses Chocolatey). Either works:

```powershell
winget install --id Git.Git Python.Python.3.12 OpenJS.NodeJS.LTS GoLang.Go
# Chocolatey equivalent: choco install -y git python nodejs-lts golang
```
Node **≥ 22** (pi ≥ 0.81 needs it — LTS gives 24). **Claude Desktop + Claude Code CLI are already
installed** here — just confirm: `claude --version`.

---

## 1. DNS — native, no mirrored networking

Native Windows resolves `larry.home.arpa` when the NIC uses the Pi-hole DNS (this is what WSL's
mirrored-networking hack was faking). Verify:
```powershell
Resolve-DnsName larry.home.arpa      # -> 192.168.0.173
```
Fallback: add `192.168.0.173 larry.home.arpa` to
`C:\Windows\System32\drivers\etc\hosts` (edit elevated).

---

## 2. Trust the HomeLab CA

pi/Node reject Larry's cert (`https://larry.home.arpa:11443`, HomeLab self-signed root) until the CA
is trusted. Copy the **public** `ca.crt` (deb: `~/certs/ca/ca.crt` — the CA *key* never leaves the
Deb box) to the Windows box, then in **PowerShell as admin**:
```powershell
Import-Certificate -FilePath ca.crt -CertStoreLocation Cert:\LocalMachine\Root
[Environment]::SetEnvironmentVariable('NODE_OPTIONS','--use-system-ca','Machine')   # Node trusts the Windows store
```
Open a fresh shell (so `NODE_OPTIONS` is live) and verify **without `-k`**:
```powershell
Invoke-RestMethod https://larry.home.arpa:11443/api/version    # -> {"version":"..."}
```
Success with no cert error means DNS **and** TLS both work. If it fails, it's one of those two —
fix here before continuing.

---

## 3. pi + provider

```powershell
npm i -g @earendil-works/pi-coding-agent
```
Copy `tower/ollama-provider.ts` → `%USERPROFILE%\.pi\ollama-provider.ts` (its `baseUrl` is already
the HTTPS proxy — leave it; there is **no** local ollama here). Write
`%USERPROFILE%\.pi\agent\settings.json`:
```json
{ "extensions": ["C:\\Users\\<user>\\.pi\\ollama-provider.ts"], "defaultModel": "qwen3-coder:30b" }
```
Without the `extensions` entry pi starts with **"Warning: No models available"** — the provider file
alone does nothing until pi is told to load it.

> **pi 0.81 provider form is mandatory.** The repo `ollama-provider.ts` uses the 0.81
> `createProvider(openAICompletionsApi())` form. The old `registerProvider("ollama", …)` form
> **breaks native tool-calling on pi ≥ 0.81** — local qwen models emit tool calls as `<function=…>`
> text and `web_search`/`kb_search` never run. Always deploy the repo copy, and ensure pi is ≥ 0.81
> (`npm i -g @earendil-works/pi-coding-agent@latest`) — the `createProvider` form errors with
> `undefined (reading 'streamSimple')` on pi 0.80.x.

Verify:
```powershell
pi --list-models                       # lists qwen3-coder:30b, al-coder-*, etc.
pi -p "reply with exactly: OK"         # end-to-end: default model -> Larry over HTTPS
```

---

## 4. Claude Code — already installed [HUMAN sign-in]

Claude Code CLI + Claude Desktop are already on the box. Run `claude` once and complete the auth
prompt if not signed in (talks to `api.anthropic.com`, public CA — no HomeLab cert needed). This is
the escalation backend when local rounds stall.

> **Claude Desktop shares the same `~/.claude` root** as the CLI — a terminal session resumes in the
> GUI and vice-versa, so **never run both at once** on the same session. (See the desktop install
> note; chat-side MCP wants absolute paths in `claude_desktop_config.json`.)

---

## 5. Setup repo + prompts + CLIs

**`git clone`** rather than copy, so `git pull` brings fixes:
```powershell
gh auth login                                              # account: drs76 (private repo)
git clone https://github.com/drs76/larry-setup.git C:\larry-setup
cd C:\larry-setup; git config core.autocrlf false          # in-clone: global default is true and
                                                           # .gitattributes only pins LF on the
                                                           # extensionless CLIs, so everything else
                                                           # would otherwise check out CRLF
```

Windows supports real symlinks when **run elevated**, so link rather than copy — one `git pull` then
updates every one at once. These `ln -s` commands run from a **Git Bash tab** with
`MSYS=winsymlinks:nativestrict`:
- `tooling/{al,al-route,go-route,cs-route,spec,handover,warplan,scout,bc-agent}.md` → `%USERPROFILE%\.pi\agent\prompts`
- `tooling/{al,fable,bc-agent}.md` + `warplan-claude.md`→`warplan.md` + `scout-claude.md`→`scout.md` + `spec-claude.md`→`spec.md` → `%USERPROFILE%\.claude\commands`
- `tooling/{alw,gow,csw,probe,bcw,anon,kb,kb-lint,al-rag}` → `%USERPROFILE%\.local\bin`
- `tooling/{kb-search,searxng-search}.pi-ext.ts` → `%USERPROFILE%\.pi\agent\extensions\{kb-search,searxng-search}.ts`
  (pi **auto-discovers** that directory — no `settings.json` entry needed; verify by asking pi to
  list its tools: expect `kb_search` and `web_search`).

### SSH to Larry — do this before the KB step

`kb-client-setup.sh` fetches the token over `ssh larry`, so the key and the host alias must
exist first. A fresh Windows box has neither: `~/.ssh/` holds only `known_hosts`, and with no
`config` the bare alias `larry` does not resolve — ssh falls back to the Windows account name
(`user@larry.home.arpa`) and Larry answers `Permission denied (publickey,…)`.

That failure surfaces as step 1 of the script saying **"cannot ssh to 'larry'. On WG, bring
the tunnel up first."** On a box that pings Larry in single-digit milliseconds the tunnel is
not the problem — read it as *no key* first, and check the route second.

From a **Git Bash** tab:
```sh
ssh-keygen -t ed25519 -C "dave-tsg-windows" -f ~/.ssh/id_ed25519
ssh-copy-id -i ~/.ssh/id_ed25519.pub dav@larry.home.arpa      # prompts for dav's password
```
`ssh-copy-id` ships **only with Git Bash**. From PowerShell it fails with "not recognized as a
name of a cmdlet" — Windows' own OpenSSH at `C:\Windows\System32\OpenSSH\` does not include
it. The PowerShell equivalent:
```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | ssh dav@larry.home.arpa 'mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
```

Then create `~/.ssh/config` — the alias is what the script calls, and no client doc previously
recorded it:
```
Host larry
    HostName larry.home.arpa
    User dav
    IdentityFile ~/.ssh/id_ed25519
```

Leave the key **without a passphrase**, or keep `ssh-agent` loaded: `kb-client-setup.sh` runs
ssh with `-o BatchMode=yes`, which cannot prompt. Verify before moving on:
```sh
ssh -o BatchMode=yes larry true && echo "ssh ok"
```

### Thin-client env

Run the script rather than pasting the token by hand — it fetches, installs and verifies
without the value ever reaching a terminal:
```sh
bash ~/larry-setup/tower/handoff-scripts/kb-client-setup.sh
```
It writes `KB_REMOTE` to `~/.bashrc` and the token to **`~/.pi/.kb-token` (chmod 600), and
nowhere else**. Expect `HTTP 200` for every source and `kb search via the file fallback: OK`.

**Never put `KB_REMOTE_TOKEN` in `~/.bashrc`.** That file gets read, grepped and pasted into
transcripts; a token there leaked on 2026-08-16 and forced a rotation, and the stale copy left
behind was still failing on this box on 2026-08-28. Re-run the script after any rotation.

The one variable still set by hand in the **Git Bash** `~/.bashrc` (its extension defaults to
the right LAN URL, so this is optional):
```sh
export SEARXNG_URL="https://searxng.home.arpa"
```
`kb` also needs `pip install numpy pyyaml`. Note: **curl in Git Bash uses its own CA bundle and
fails against `searxng.home.arpa`**; Node (and therefore pi) uses the Windows store and works —
don't chase that as a fault.

### Doc tooling — `md2pdf` and the `/doc-convert` skill

`relink-tooling.sh` installs `md2pdf` for you, but not the libraries it calls. Without them
`md2pdf` either refuses to start or silently prints diagrams as source.

```powershell
python -m pip install --user markdown pymupdf pdfplumber python-docx openpyxl pypandoc-binary
npm i -g @mermaid-js/mermaid-cli    # mmdc — without it, mermaid fences print as source text
```

**Do not install WeasyPrint here.** It needs a GTK3 runtime this box does not have, so
`md2pdf` falls back to headless Edge and renders diagrams as SVG. That path is the tested
one on Windows — Edge must exist at one of the two `Program Files` locations, which it does
by default.

`md2pdf` cannot be symlinked on Windows because it is a Python script with no launcher.
`relink-tooling.sh` writes two shims instead — `~/.local/bin/md2pdf.cmd` for PowerShell and
an sh `md2pdf` for Git Bash — both calling the repo copy through a `cygpath -m` native path.
Re-run that script rather than copying the file. Full detail:
[`tooling/md2pdf-handover.md`](../tooling/md2pdf-handover.md).

### Claude plugins
Mirror the dev box with the CLI:
```powershell
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
claude plugin install gopls-lsp@claude-plugins-official      # inert until: go install golang.org/x/tools/gopls@latest
```
Caveman's statusline (if you enable caveman mode — a per-operator choice; it changes how Claude
writes) must name **Git Bash explicitly**, because `bash` is not on the Windows system PATH and
Claude Code does not run `statusLine` through it:
```json
"statusLine": { "type": "command",
  "command": "\"C:/Program Files/Git/bin/bash.exe\" \"<...>/caveman/*/src/hooks/caveman-statusline.sh\"" }
```

---

## 6. Terminal — PowerShell + Windows Terminal + starship (no WezTerm, no tmux)

Use **Windows Terminal** with the default PowerShell profile as the host terminal — its tabs and
split-panes replace what tmux/WezTerm did on the Server box. **No WezTerm, no tmux, no psmux** —
those (and all their Windows font/psmux/glium gotchas in `windows-setup.md` §5) are deliberately not
part of this setup.

```powershell
winget install Microsoft.WindowsTerminal Starship.Starship
# choco fallback: choco install microsoft-windows-terminal starship -y
```

Wire starship into the PowerShell profile. `$PROFILE` is
`Documents\PowerShell\Microsoft.PowerShell_profile.ps1` for **pwsh 7** (or
`Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1` for Windows PowerShell 5.1). Add:
```powershell
$env:STARSHIP_CONFIG = "C:\larry-setup\tower\starship-setup\starship.toml"   # repo copy (adjust if path differs)
$env:PATH = "$env:ProgramFiles\starship\bin;$env:PATH"                       # winget/choco don't add it to existing sessions
Invoke-Expression (&starship init powershell)
```
(If starship reports `Scanning current directory timed out` in a big/NFS home, add
`scan_timeout = 1000` + `command_timeout = 2000` at the top level of that `starship.toml`.)

To open a Git Bash tab in Windows Terminal, add a profile pointing at
`C:\Program Files\Git\bin\bash.exe -l` — that is the tab you run `alw`/`gow`/`csw` in.

---

## 7. Git Bash env for the CLIs (`~/.bashrc`)

The workflow CLIs are bash; they run **only** in Git Bash. Everything else stays in PowerShell —
i.e. you type `alw build x` in a Git Bash tab, and `pi`/`claude`/installs in PowerShell. Set
`~/.bashrc` (Git Bash home = `%USERPROFILE%`):
```sh
export SETUP_DIR="/c/larry-setup"
export RUN_BUILD="/c/larry-setup/pipeline/run-build.py"
export RUN_BUILD_GO="/c/larry-setup/pipeline/run-build-go.py"
export RUN_BUILD_CS="/c/larry-setup/pipeline/run-build-cs.py"
export TEMPLATE="/c/larry-setup/templates/larry-handover.template.md"
export PROJECTS_DIR="$HOME/projects"; export PROTOTYPES_DIR="$HOME/projects/prototypes"
export PI_CODER_MODEL="ollama/qwen3-coder:30b"              # NOT ornith:35b (broken)
export COMS_VALIDATOR_MODEL="ollama/qwen3-coder:30b"; export COMS_RELAY_MODEL="ollama/qwen3-coder:30b"
export NODE_OPTIONS="--use-system-ca"
export PYTHONUTF8=1; export PYTHONIOENCODING=utf-8
export DOTNET_ROOT="$HOME/.dotnet"
export PATH="$HOME/.local/bin:$HOME/AppData/Roaming/npm:$HOME/.dotnet:$HOME/.dotnet/tools:$PATH"
alias python3=python
```
Verify: `alw help`, `gow help`, `csw help` all print usage.

---

## 8. Windows porting fixes — now upstream (2026-07-24)

The binary- and path-resolution fixes below **live in the repo** as of 2026-07-24 — `git pull` and
they are there (no-ops on Linux). No local patching of `C:\larry-setup` is needed.

Fixed upstream in `pipeline/run-build{,-go,-cs}.py`, `coms_review.py`, `run-analyse.py`, `tooling/{alw,gow,csw}`:
- **`PI_BIN` / `CLAUDE_BIN` / `AL_CLI`** hardcoded POSIX paths → `env → which() → old default`.
  Windows `shutil.which` finds the `.cmd` shim; Python subprocess runs it. In the bash CLIs the same
  applies as `$(command -v pi || …)` — the old hardcode hard-failed the `[ -x "$PI_BIN" ]` gate, so
  **`alw|gow|csw route` was broken on Windows** (`build` was unaffected).
- **Manifest paths** — `parse_manifest()` now accepts drive-letter absolutes (`C:/Users/...`) as
  well as POSIX, and `configure_project()` converts a Git-Bash `/c/...` project root to native form.
  Previously a catch-22 that made `alw build` **impossible** on Windows.
- **`cleanup.sh`** (generated by `alw new`) now normalises via `cygpath -u`, aborts on an empty
  manifest, and **defaults to dry-run** (`--apply` to delete; `run-build.py` passes it).
  ⚠️ **Projects scaffolded before 2026-07-24 still carry the old copy that deleted every source file
  in the project** — re-scaffold or patch by hand before running theirs.

Still per-box on Windows:
- **`python3`** doesn't exist on Windows — add a shim `~/.local/bin/python3` containing
  `#!/bin/sh` / `exec python "$@"` (the `alias python3=python` in §7 covers interactive Git Bash;
  the shim covers scripts that call `python3` directly).
- **`PYTHONUTF8=1`** — else Python reads pi's UTF-8 stdout as cp1252 and the reader thread crashes.
- **NuGet (csw):** a fresh .NET has no source → `NU1100`. Run once:
  `dotnet nuget add source https://api.nuget.org/v3/index.json -n nuget.org`.
- **Multi-line prompts must go via pi's `@file` syntax, never argv.** `pi` is an npm **`.CMD` shim**
  run through `cmd.exe`, which **truncates a multi-line argument at the first newline** (measured: a
  35-char/2-newline argv arrives as 8 chars). `run-build{,-go,-cs}.py` now write the prompt to a
  temp file and pass `@path` on Windows — keep it that way for any new pi call. (This also explains
  historic intermittent "Wrote 0/N expected files" on first attempt.)
- **`--review` works on Windows** via a headless one-shot path in `coms_review.py` (no pty/coms
  transport needed): the validator model is asked directly (`-p --no-session --no-tools`, prompt via
  `@file`). `~/.pi/coms.ts` is **not** required on Windows.

---

## 9. Language referees — install per language you build

- **Go** (`gow`): `winget install GoLang.Go` (or `choco install golang`). Referee = `go build`/`vet`/`test`.
- **C#** (`csw`): the .NET 10 SDK —
  `dotnet-install.ps1 -Channel 10.0 -InstallDir $HOME\.dotnet`; add to PATH; add the nuget.org
  source (§8). Referee = `dotnet build` → `format --verify-no-changes` → `test`.
- **AL** (`alw`): the AL compiler as a dotnet tool —
  `dotnet tool install -g Microsoft.Dynamics.BusinessCentral.Development.Tools` (cmd `al`, aka altool).
  It targets **net8.0**, so also install the **.NET 8 base + ASP.NET Core 8 runtimes**
  (`dotnet-install.ps1 -Channel 8.0 -Runtime dotnet` then `-Runtime aspnetcore`, same InstallDir) and
  set `DOTNET_ROOT` (§7).
  **Symbols are automatic** — `run-build.py` spawns a project-scoped AL MCP server
  (`al launchmcpserver`) and calls `al_downloadsymbols` with `globalSourcesOnly: true`, pulling the
  Microsoft NuGet/AppSource packages with **no BC server and no authentication** into
  `<project>/.alpackages`. A container/DVD is *not* required. There is **no** `al downloadsymbols`
  CLI verb — the capability exists only via MCP (and VS Code).
  `app.json` must match the target platform, e.g. for BC 27.5: `platform 27.0.0.0`,
  `application 27.5.0.0`, `runtime 16.1` — get the runtime from
  `al GetLatestSupportedRuntimeVersion 27.0` (it wants the **2-part** `27.0`, not `27.0.0.0`). Note
  `target` depends on the AL compiler version (al 17.x wants `OnPrem` at runtime 16.1; al 18.x wants
  `Extension`).

---

## 10. Verify (smoke)

### After a `git pull` — check the pipeline still resolves

A pull is the whole update: the pipeline has no install step and every setting added since has a
working default. One check is worth the minute, because what it catches is a build that quietly
stops writing files rather than one that errors.

```powershell
cd C:\larry-setup\pipeline; python test_al_intelligence.py 2>&1 | Select-Object -Last 3
```

Expect `258/258 PASS` — the count grows over time, so a **failure** is the signal, not the number.
This proves the pipeline's modules resolve on this box. `pipeline/coder.py` is imported by all
three build orchestrators (AL, Go, C#), so a partial clone or a stale symlink surfaces here first.

Then run the smoke below, because no unit test spawns the coder.

**Windows only.** The npm `.CMD` shim truncates a multi-line argument at the first newline, so long
prompts go to pi via its `@file` form. That code moved into `pipeline/coder.py` on 2026-08-31; if a
build reports `Wrote 0/N expected files` on the **first** attempt, that is the signature. Also
confirm the clone still suppresses CRLF translation, which a pull would otherwise apply to every
Python file:

```powershell
cd C:\larry-setup; git config core.autocrlf      # must print: false
```


PowerShell for the pi check; a **Git Bash** tab for the build wrappers:
```powershell
# PowerShell
pi -p "reply with exactly: OK"          # Larry over HTTPS
```
```sh
# Git Bash tab
ssh -o BatchMode=yes larry true && echo "ssh ok"   # key auth, before anything KB-shaped
kb stats                                 # -> 14 corpora. NOT /health: it needs no auth and
                                         #    answers {"ok": true} on a dead token
gow new win-smoke && gow build win-smoke # -> RESULT: PASS (Go referee)
csw new cs-smoke && csw build cs-smoke   # -> RESULT: PASS (.NET referee)
alw new al-smoke                         # then fill larry-handover.prompt.md — the machine-readable
                                         # manifest needs C:/Users/... paths
alw build al-smoke                       # -> RESULT: PASS (symbols auto-downloaded, al compile)
```
Reference result on `docker-bc` 2026-07-24 — `alw build` on a 2-file AL prototype:
```
Larry: writing files -> wrote 2/2 expected files (pi qwen3-coder:30b, 17s)
Manifest check      -> Passed
AL compile          -> al-mcp symbols: 5 package(s) [NuGet (Global Sources)]
                       Build PASSED, error score 0
RESULT: PASS
```

---

## 11. Roaming — reach Larry over WireGuard (out of the house)

Off the home LAN, `larry.home.arpa` (Pi-hole on Nemesis) stops resolving and nginx `:11443` at
Larry's LAN IP is unreachable. A **WireGuard tunnel back home restores both** — the HomeLab CA is
already trusted, so nothing above the transport changes. Run the **WireGuard for Windows** client on
the host (no WSL to reconcile here — it's just the host NIC):

1. Install the **WireGuard for Windows** client.
2. Import a split-tunnel config (copy the router pubkey / DDNS endpoint / tunnel subnet from an
   existing peer — see `thinkpad-setup.md` §12):
   ```ini
   [Interface]
   PrivateKey = <client-priv>
   Address    = 10.x.x.N/32
   DNS        = 192.168.0.175        # Pi-hole -> larry.home.arpa
   [Peer]
   PublicKey  = <router-wg-pubkey>
   Endpoint   = <ddns-host>:<wg-port>
   AllowedIPs = 192.168.0.0/24       # home LAN only (split-tunnel); 0.0.0.0/0 to route everything home
   PersistentKeepalive = 25
   ```
3. Add the peer's `<client-pub>` on the router (AllowedIPs `10.x.x.N/32`), then **Activate**.

Verify exactly as on the LAN, then deactivate when back home (LAN is direct):
```powershell
Resolve-DnsName larry.home.arpa                          # -> 192.168.0.173
Invoke-RestMethod https://larry.home.arpa:11443/api/version   # -> {"version":...}
```

---

## What differs across the three client docs

| | WSL client (retired) | **This PowerShell host** | `windows-setup.md` (Server / docker-host) |
|---|---|---|---|
| Primary terminal | WezTerm → WSL shell | **Windows Terminal + PowerShell** | WezTerm + psmux/tmux |
| Shell for `alw/gow/csw` | bash on PATH | **Git Bash tab only** | Git Bash |
| DNS | mirrored networking | **native (Pi-hole on NIC)** | native |
| CA trust | `update-ca-certificates` | **`Cert:\LocalMachine\Root`** | `Cert:\LocalMachine\Root` |
| tmux/WezTerm | WezTerm optional | **none** (Win Term panes) | WezTerm + psmux (full gotcha list) |
| docker host | no | **no** | yes (bccontainerhelper, §9 there) |
| pi prompts | argv | **`@file`** (argv truncates) | `@file` |
| `--review` | coms peer round-trip | **headless one-shot** | headless one-shot |

Source-of-truth: [`README.md`](../README.md), [`larry-context.md`](larry-context.md). Server /
docker-host variant of this same client: [`windows-setup.md`](windows-setup.md).

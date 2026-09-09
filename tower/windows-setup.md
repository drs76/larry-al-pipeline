# Windows setup — native Windows Server as a Larry client (no WSL)

**Goal:** stand up a **Windows** box (Server 2022 tested) as a Larry pipeline client — pi + Claude
Code drive builds, inference runs on **Larry** over the LAN HTTPS proxy. Pure PowerShell + **Git
Bash**, no WSL. Optionally the same box is a **bccontainerhelper docker host** (see §9).

Use this instead of [`wsl-setup.md`](wsl-setup.md) when you want a native Windows box (e.g. one that
already runs Windows containers) rather than a WSL2 guest. The Larry client is just Node + Claude +
a provider config + CA trust + DNS — all native-Windows capable.

> **Audience:** Claude Code / operator on the Windows box. `[HUMAN]` steps need the console
> (install media, sign-in). Everything else is scriptable over SSH. Reference implementation:
> `docker-bc` (192.168.0.191), built 2026-07-24.

```
 Windows Server                         LAN                    Larry (192.168.0.173)
 ┌─────────────────────────┐                                  ┌──────────────────────────┐
 │ pi / gow / csw / alw     │──► https://larry.home.arpa:11443 ┼─► ollama :11434           │
 │   (Git Bash)             │                                  │   qwen3-coder:30b, al-*   │
 │ claude (escalation) ─────┼──► api.anthropic.com             └──────────────────────────┘
 └─────────────────────────┘
```

## 0. Base tools — [HUMAN or choco]
Windows Server 2022 (eval fine). Install Chocolatey, then:
```powershell
choco install -y git python nodejs-lts golang
# optional docker host: choco install -y docker-engine ; and enable Containers + Hyper-V
```
Node ≥ 22 (pi ≥ 0.81 needs it — LTS gives 24). Claude Code: `npm i -g` or the native installer.

## 1. DNS — no mirrored networking needed
Native Windows already resolves `larry.home.arpa` if the NIC uses the Pi-hole DNS. Verify:
`Resolve-DnsName larry.home.arpa` → 192.168.0.173. Fallback: add `192.168.0.173 larry.home.arpa`
to `C:\Windows\System32\drivers\etc\hosts`.

## 2. Trust the HomeLab CA
Copy the public `ca.crt` (deb: `~/certs/ca/ca.crt`) to the box, then:
```powershell
Import-Certificate -FilePath ca.crt -CertStoreLocation Cert:\LocalMachine\Root
[Environment]::SetEnvironmentVariable('NODE_OPTIONS','--use-system-ca','Machine')   # Node trusts Windows store
```
Verify (no `-k`): `Invoke-RestMethod https://larry.home.arpa:11443/api/version`.

## 3. pi + provider
```powershell
npm i -g @earendil-works/pi-coding-agent
```
Copy `tower/ollama-provider.ts` → `%USERPROFILE%\.pi\ollama-provider.ts` (baseUrl already the HTTPS
proxy — unchanged). Write `%USERPROFILE%\.pi\agent\settings.json`:
```json
{ "extensions": ["C:\\Users\\<user>\\.pi\\ollama-provider.ts"], "defaultModel": "qwen3-coder:30b" }
```
Verify: `pi --list-models` (lists Larry models); `pi -p "reply with exactly: OK"`.

## 4. Claude Code — [HUMAN sign-in]
Install, then `claude` once and complete the auth prompt (api.anthropic.com, public CA).

## 5. Setup repo + prompts + CLIs
**`git clone` it** to `C:\larry-setup` (private repo — `gh auth login` first) rather than copying, so
`git pull` brings fixes. Set `git config core.autocrlf false` **in that clone**: the global default is
`true` and `.gitattributes` only pins LF on the extensionless CLIs, so everything else would check out
CRLF.

Windows supports real symlinks when run elevated, so link rather than copy — a `git pull` then updates
every one of these at once. Use `MSYS=winsymlinks:nativestrict ln -s <repo-file> <dest>`:
- `tooling/{al,al-route,go-route,cs-route,spec,handover,warplan,bc-agent}.md` → `%USERPROFILE%\.pi\agent\prompts`
- `tooling/{al,fable,bc-agent}.md` + `warplan-claude.md`→`warplan.md` + `spec-claude.md`→`spec.md` → `%USERPROFILE%\.claude\commands`
- `tooling/{alw,gow,csw,probe,bcw,anon,kb,kb-lint,al-rag}` → `%USERPROFILE%\.local\bin`
- `tooling/{kb-search,searxng-search}.pi-ext.ts` → `%USERPROFILE%\.pi\agent\extensions\{kb-search,searxng-search}.ts`
  (pi **auto-discovers** that directory — no settings.json entry needed; verify with a prompt asking
  pi to list its tools: expect `kb_search` and `web_search`).

Thin-client env (Git Bash `~/.bashrc`) — both extensions default to the right LAN URLs, so this is
optional:
```sh
export SEARXNG_URL="https://searxng.home.arpa"
```

**The KB token is not set by hand, and never goes in `~/.bashrc`.** Run the script; it writes
`KB_REMOTE` to `~/.bashrc` and the token to `~/.pi/.kb-token` (chmod 600) and nowhere else:
```sh
bash /c/larry-setup/tower/handoff-scripts/kb-client-setup.sh
```
A token pasted into `~/.bashrc` leaked on 2026-08-16 and forced a rotation, and the stale copy left
behind was still returning 401 on the workstation on 2026-08-28. Re-run the script after any
rotation — it is the only supported refresh.

**SSH to Larry must work first.** The script fetches the token over `ssh larry`, and a fresh Windows
box has no keypair and no `~/.ssh/config`, so the bare alias does not resolve and Larry refuses the
local account name. From a **Git Bash** tab:
```sh
ssh-keygen -t ed25519 -C "$(hostname)-windows" -f ~/.ssh/id_ed25519
ssh-copy-id -i ~/.ssh/id_ed25519.pub dav@larry.home.arpa   # Git Bash only; not a PowerShell cmdlet
```
Then `~/.ssh/config`:
```
Host larry
    HostName larry.home.arpa
    User dav
    IdentityFile ~/.ssh/id_ed25519
```
`kb` also needs `pip install numpy pyyaml`. Note curl in Git Bash uses its own CA bundle and will fail
against `searxng.home.arpa`; Node (and therefore pi) uses the Windows store and works — don't chase
that as a fault.

### Claude plugins
Mirror the dev box with the CLI: `claude plugin marketplace add JuliusBrussee/caveman`, then
`claude plugin install caveman@caveman` and `claude plugin install gopls-lsp@claude-plugins-official`.
`gopls-lsp` is inert until you `go install golang.org/x/tools/gopls@latest`. Caveman's statusline must
name Git Bash explicitly — `bash` is **not** on the Windows system PATH and Claude Code does not run
`statusLine` through it:
```json
"statusLine": { "type": "command",
  "command": "\"C:/Program Files/Git/bin/bash.exe\" \"<...>/caveman/*/src/hooks/caveman-statusline.sh\"" }
```
It prints nothing until caveman mode is switched on (`~/.claude/.caveman-active`), which is a
per-operator choice — it changes how Claude writes.

### Terminal: WezTerm + starship + tmux
**Server 2022 eval has no `winget`** — use Chocolatey:
`choco install wezterm starship nerd-fonts-jetbrainsmono cascadiacode -y`.
Font names differ by installer and the config depends on them: choco's Nerd Font package registers
`JetBrainsMono NF / NFM / NFP` (use **NFM**, the Mono variant) — the same gotcha as winget's DEVCOM
package. `cascadia-code-nerd-font` is **not** Cascadia Code; Nerd Fonts renames it *Caskaydia Cove*,
so the config's primary `Cascadia Code` still fails — install `cascadiacode` for the real family.
Check with `wezterm ls-fonts`, which reports exactly which file each fallback resolved to.

`tower/wezterm/wezterm.lua` is **host-aware** — it probes for pwsh7 / Git Bash / a WSL distro and
builds the launch menu from what exists, so it can be **symlinked** (`ln -s` to `%USERPROFILE%\.wezterm.lua`)
rather than copied-and-drifted. Note `wsl.exe` ships with Windows even when no distro is installed, so
the config asks `wsl -l -q` rather than testing for the binary.

⚠️ **On a headless VM WezTerm will not start at all**: it exits immediately with
`Failed to create window: The OpenGL implementation is too old to work with glium` — a Proxmox/basic
display adapter offers only OpenGL 1.1. Fix with `front_end = "WebGpu"`. **`front_end = "Software"`
does NOT work** (it still goes through glium), which is the obvious thing to try first. Because a GPU
box wants the default, this goes in the per-machine override the shared config loads at the end:
`%USERPROFILE%\.wezterm-local.lua` returning a table of config fields, e.g.
```lua
return { front_end = "WebGpu" }
```
Diagnose startup failures by launching `wezterm-gui.exe` with stderr redirected — the window vanishes
too fast to read otherwise.

Starship: `$PROFILE` (`Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`) sets
`STARSHIP_CONFIG` to the repo `starship.toml` and runs `starship init powershell`; it also prepends
`%ProgramFiles%\starship\bin` to PATH, which choco does not do for existing sessions.

**tmux is `psmux`** here (choco `tmux` → psmux 3.3.7, a Windows port). Two things bite:
- The shared conf's `default-shell /usr/bin/zsh` kills the server outright ("spawn shell error:
  CreateProcessW /usr/bin/zsh") — now guarded by `if-shell`, and the host wrapper points
  `default-shell` at Git Bash.
- **psmux runs `#()` through a non-POSIX shell that accepts only ONE unquoted argument.**
  `#(echo X)` works; `#(C:/PROGRA~1/Git/bin/bash.exe -c "echo X")` and any quoted path do not. Use the
  8.3 path plus a bare script path. The git-branch and battery segments therefore cannot run on
  Windows (both need quoting) and are dropped in the host wrapper; CPU works. Do **not** work around
  it with a helper that calls `tmux display-message` — a recursive tmux call during status render
  hangs psmux and the status bar goes permanently blank.
- psmux 3.3.7 warns `unknown option 'terminal-features'` on every load. Harmless — it is a tmux ≥3.2
  option psmux has not implemented; truecolor still comes from `terminal-overrides`.

Deploy `~/.tmux.conf` as a small **wrapper** that `source-file`s the repo conf and then applies the
Windows overrides — psmux does not reliably resolve the shared file's own `source-file -q ~/...`
include at startup, though the same command works once a server is running.

## 6. Git Bash env (`~/.bashrc`)
The CLIs are bash; run them in Git Bash (`C:\Program Files\Git\bin\bash.exe -lc '...'`).
```sh
export SETUP_DIR="/c/larry-setup"
export RUN_BUILD="/c/larry-setup/pipeline/run-build.py"
export RUN_BUILD_GO="/c/larry-setup/pipeline/run-build-go.py"
export RUN_BUILD_CS="/c/larry-setup/pipeline/run-build-cs.py"
export TEMPLATE="/c/larry-setup/templates/larry-handover.template.md"
export PROJECTS_DIR="$HOME/projects"; export PROTOTYPES_DIR="$HOME/projects/prototypes"
export PI_CODER_MODEL="ollama/qwen3-coder:30b"
export COMS_VALIDATOR_MODEL="ollama/qwen3-coder:30b"; export COMS_RELAY_MODEL="ollama/qwen3-coder:30b"
export NODE_OPTIONS="--use-system-ca"
export PYTHONUTF8=1; export PYTHONIOENCODING=utf-8
export DOTNET_ROOT="$HOME/.dotnet"
export PATH="$HOME/.local/bin:$HOME/AppData/Roaming/npm:$HOME/.dotnet:$HOME/.dotnet/tools:$PATH"
alias python3=python
```

### Doc tooling — `md2pdf` and `/doc-convert`

Optional, but `relink-tooling.sh` installs the `md2pdf` command whether or not its libraries
are there, so without this step the command exists and then fails at runtime:

```powershell
python -m pip install --user markdown pymupdf pdfplumber python-docx openpyxl pypandoc-binary
npm i -g @mermaid-js/mermaid-cli    # mmdc — without it, mermaid fences print as source text
```

**Do not install WeasyPrint on Windows.** It needs a GTK3 runtime this box does not have, so
`md2pdf` uses headless Edge instead and renders diagrams as SVG. Server 2022 ships Edge, but
confirm it — `md2pdf` reports "no PDF engine" if neither engine is found:

```sh
ls "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" 2>/dev/null || \
ls "/c/Program Files/Microsoft/Edge/Application/msedge.exe"
```

`md2pdf` is a Python script with no launcher, so it cannot be symlinked here.
`relink-tooling.sh` writes `~/.local/bin/md2pdf.cmd` (PowerShell) and an sh `md2pdf` (Git
Bash) instead, both calling the repo copy. Re-run that script rather than copying the file —
see [`tooling/md2pdf-handover.md`](../tooling/md2pdf-handover.md).

## 7. Windows porting fixes — now upstream (2026-07-24)
The binary- and path-resolution fixes below **live in this repo** as of 2026-07-24 — `git pull` and
they are there. They are no-ops on Linux (verified on `deb`: `al` isn't on PATH so `which()` returns
`None` and the old hardcoded default still wins). Historically these had to be patched into a local
`C:\larry-setup` copy; that is no longer needed.

Fixed upstream in `pipeline/run-build{,-go,-cs}.py`, `coms_review.py`, `run-analyse.py`, `tooling/{alw,gow,csw}`:
- **`PI_BIN` / `CLAUDE_BIN` / `AL_CLI`** hardcoded POSIX dev-box paths → `env → which() → old default`.
  Windows `shutil.which` finds the `.cmd` shim; Python subprocess runs it. In the bash CLIs the same
  applies as `$(command -v pi || …)` — the old hardcode hard-failed the `[ -x "$PI_BIN" ]` gate, so
  **`alw|gow|csw route` was broken on Windows** (`build` was unaffected).
- **Manifest paths** — `parse_manifest()` now accepts drive-letter absolutes (`C:/Users/...`) as well
  as POSIX (`/mnt/...`), and `configure_project()` converts a Git-Bash `/c/...` project root to native
  form. Previously this was a catch-22 that made `alw build` **impossible** on Windows: `C:/...` parsed
  to `[]` → hard abort *"could not read expected files from handover manifest"*, while `/c/...` parsed
  but failed every `os.path.exists()` in the write gate. Only the **AL** runner aborts on an empty
  manifest — Go/C# treat it as optional, which is why `gow`/`csw` never exposed it.
- **`cleanup.sh`** (generated by `alw new`) — matched only `/^\//` and compared manifest `C:/...`
  against `find`'s `/c/...`, so nothing matched and it **deleted every source file in the project**.
  Now accepts both forms, normalises via `cygpath -u`, aborts on an empty manifest, and **defaults to
  dry-run** (`--apply` to delete; `run-build.py` passes it). ⚠️ Projects scaffolded before 2026-07-24
  still carry the destructive copy — re-scaffold or patch by hand before running theirs.

Still per-box on Windows:
- **`python3`** doesn't exist on Windows — add a shim `~/.local/bin/python3` = `#!/bin/sh\nexec python "$@"`.
- **`PYTHONUTF8=1`** — else Python reads pi's UTF-8 stdout as cp1252 and the reader thread crashes.
- **NuGet (csw):** a fresh .NET has no source → `NU1100`. Run once:
  `dotnet nuget add source https://api.nuget.org/v3/index.json -n nuget.org`.
- **Multi-line prompts must go via pi's `@file` syntax, never argv.** `pi` is an npm **`.CMD` shim**
  run through `cmd.exe`, which **truncates a multi-line argument at the first newline** (measured: a
  35-char/2-newline argv arrives as 8 chars). The handover was therefore reaching pi as its *title
  line only*; builds still passed because pi went and read `larry-handover.prompt.md` out of the
  project dir itself — which is also why a first write attempt sometimes reported
  "Wrote 0/N expected files" and only the retry succeeded. `run-build{,-go,-cs}.py` now write the
  prompt to a temp file and pass `@path` on Windows. Keep it that way for any new pi call.
- **`--review` works on Windows** via a headless path in `coms_review.py`. The POSIX flow holds a
  *persistent interactive* validator agent open in a `pty` so a relay can `coms_send` to it; Windows
  has no `pty`, and a review is a single request/response, so there the validator model is asked
  directly in one shot (`-p --no-session --no-tools`, prompt via `@file`). What matters is preserved:
  a **different model** than the coder, the same request text, and the same `_classify_findings`
  contract. `--no-tools` is load-bearing — with read/bash the reviewer wanders the cwd and reviews
  whatever it finds instead of the inlined code. **`~/.pi/coms.ts` is NOT required on Windows.**
(The handover template no longer hardcodes `/mnt/rojaws` — `alw new` substitutes host-native paths,
so a stock-generated project builds here unedited.)

## 8. Language referees — install per language you build
- **Go** (`gow`): `choco install golang`. Referee = `go build`/`vet`/`test`.
- **C#** (`csw`): `.NET SDK` — `dotnet-install.ps1 -Channel 10.0 -InstallDir $HOME\.dotnet`; add to PATH;
  add the nuget.org source (§7). Referee = `dotnet build` → `format --verify-no-changes` → `test`.
- **AL** (`alw`): the AL compiler as a dotnet tool —
  `dotnet tool install -g Microsoft.Dynamics.BusinessCentral.Development.Tools` (cmd `al`, aka altool).
  It targets **net8.0**, so also install the **.NET 8 base + ASP.NET Core 8 runtimes**
  (`dotnet-install.ps1 -Channel 8.0 -Runtime dotnet` then `-Runtime aspnetcore`, same InstallDir) and set
  `DOTNET_ROOT`.
  **Symbols are automatic** — `run-build.py` spawns a project-scoped AL MCP server
  (`al launchmcpserver`) and calls `al_downloadsymbols` with `globalSourcesOnly: true`, pulling the
  Microsoft NuGet/AppSource packages with **no BC server and no authentication** (5 packages in ~8s
  into `<project>/.alpackages`). A container/DVD is *not* required. Note there is **no**
  `al downloadsymbols` CLI verb — the capability exists only via MCP (and VS Code).
  `app.json` must match the target platform, e.g. for a BC 27.5 container: `platform 27.0.0.0`,
  `application 27.5.0.0`, `runtime 16.1` — get the runtime from
  `al GetLatestSupportedRuntimeVersion 27.0` (it wants `27.0`, **not** the 4-part `27.0.0.0`).

## 9. Optional — bccontainerhelper docker host (BC containers reachable on the LAN)
`choco install docker-engine`; enable Hyper-V + Containers; `Install-Module bccontainerhelper`.
For containers with their own LAN IPs (publish apps + pull symbols from any LAN box), add a **2nd
NIC** and bind a **transparent** Docker network to it (keeps host SSH on NIC 1):
```
docker network create -d transparent -o com.docker.network.windowsshim.interface="Ethernet 2" \
  --subnet=<lan/24> --gateway=<gw> bclan
New-BcContainer -accept_eula -containerName bc1 -artifactUrl (Get-BCArtifactUrl -type OnPrem -country <cc> -version <v>) \
  -auth NavUserPassword -credential $cred -updateHosts \
  -additionalParameters @('--network=bclan','--ip=<free-lan-ip>')
```
Containers run their **own in-container SQL** by default — they do NOT use an external SQL box unless
you pass `-databaseServer/-databaseInstance/-databaseCredential`.

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

```sh
pi -p "reply with exactly: OK"          # Larry over HTTPS
gow new win-smoke && gow build win-smoke # -> RESULT: PASS (Go referee)
csw new cs-smoke && csw build cs-smoke   # -> RESULT: PASS (.NET referee)
alw new al-smoke                         # then fill larry-handover.prompt.md — the
                                         # machine-readable manifest needs C:/Users/... paths
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

## What differs from the WSL client
| | WSL client | **Native Windows** |
|---|---|---|
| DNS | mirrored networking | native (Pi-hole on NIC) |
| CA trust | `update-ca-certificates` | import to `Cert:\LocalMachine\Root` |
| CLIs | bash on PATH | Git Bash; `~/.bashrc` |
| orchestrators | run as-is | run as-is since 2026-07-24 (fixes upstream); still needs `python3` shim + `PYTHONUTF8` |
| .NET/AL | apt/dotnet-install | dotnet-install + altool + net8/aspnetcore8 runtimes + `DOTNET_ROOT` |
| `--review` | coms peer round-trip (pty-held validator) | same result, **headless one-shot** — no pty/coms transport |
| pi prompts | argv | **`@file`** — argv truncates at the first newline |

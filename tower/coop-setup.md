# COOP setup — mirror Larry for local C# / Azure Functions builds

> **Already set up? See [`coop-update.md`](coop-update.md)** to catch up on everything added since
> this guide. ⚠ One breaking change: a new **egress policy** is deny-by-default and will **disarm
> Claude escalation** unless COOP sets `EGRESS_POLICY=personal`. Do that before your next build.


Stand up **COOP** as a **standalone build box** (its own ollama + pi + `csw` workflow, no dependency
on Larry). COOP is **C#-first** — AL (`alw`) and Go (`gow`) are optional appendices at the end.

## COOP vs Larry — the three deltas

| | Larry | **COOP** |
|---|---|---|
| GPU | AMD RX 7900 XTX **24 GB** (ROCm) | **NVIDIA RTX 5070 12 GB** (CUDA) |
| OS | Rocky Linux 10 | **Windows 11** → run the tooling in **WSL2 (Ubuntu)** |
| CPU / RAM | — | i9-11900 / 64 GB |
| Models it can run on-GPU | 30–35B (qwen3-coder:30b, ornith:35b) | **≤ ~14B** (12 GB VRAM) |

**Why they matter**
1. **CUDA is *easier* than ROCm** — ollama auto-detects the NVIDIA GPU; no ROCm install, no `HSA_OVERRIDE`, no SELinux/firewalld.
2. **12 GB VRAM = half of Larry's** — the strong models Larry uses **don't fit**; COOP tops out around **14B**. Its drafts are weaker, so it **leans on Claude escalation more** for hard tasks.
3. **Windows** — the workflow tooling is bash + python + a TS pi extension, so it runs in **WSL2**.

You pick where **ollama** runs — **Path A (all in WSL2)** or **Path B (native Windows + WSL2 tooling)**. Everything after ollama is identical.

---

## 1. Prereqs (Windows)

- **NVIDIA driver** — install/upgrade the normal **Windows** GeForce driver (RTX 5070). WSL CUDA rides on the Windows driver — **do NOT install a driver inside WSL**.
- **WSL2 + Ubuntu** (PowerShell as admin):
  ```powershell
  wsl --install -d Ubuntu
  wsl --update
  ```
  Reboot, set up the Ubuntu user. Open "Ubuntu" from Start for a WSL shell.
- **Verify the GPU is visible in WSL:**
  ```sh
  nvidia-smi          # should list the RTX 5070
  ```
- **Base tools in WSL:** `sudo apt update && sudo apt install -y build-essential git curl python3 python3-venv unzip`

---

## 2. Ollama

### Path A — ollama inside WSL2 (closest to Larry)
```sh
curl -fsSL https://ollama.com/install.sh | sh      # auto-detects CUDA
# run it: either `ollama serve` in a terminal, or as a service if your WSL uses systemd
ollama --version
```
LAN-expose (optional — only if other machines call it): set `OLLAMA_HOST=0.0.0.0:11434` in the service/env + add a Windows firewall inbound rule for 11434. For a standalone box, the default `127.0.0.1:11434` is fine.

### Path B — ollama native on Windows (simplest GPU), tooling in WSL2
- Install **OllamaSetup.exe** from ollama.com on Windows. It uses the NVIDIA GPU directly.
- To let WSL reach it, set a Windows env var `OLLAMA_HOST=0.0.0.0:11434` (System → Environment Variables), restart ollama.
- From WSL, the Windows host is your default gateway — find it and point ollama clients at it:
  ```sh
  export OLLAMA_HOST="http://$(ip route | awk '/default/{print $3}'):11434"
  curl -s $OLLAMA_HOST/api/version      # should return a version
  ```
  (Put that `export` in `~/.bashrc`. If Windows firewall blocks it, allow inbound 11434 for the WSL vEthernet, or use mirrored networking: `wsl --set-version` / `.wslconfig` `networkingMode=mirrored` then `localhost:11434` works.)

Either way, verify a model runs **on the GPU** (see next section).

---

## 3. Models — sized for 12 GB (the key difference)

Larry's 30–35B coders (qwen3-coder:30b ~18 GB, ornith:35b ~21 GB, al-coder-qwen36 ~17 GB) **will not fit** 12 GB — they'd spill to CPU and crawl. COOP's roster:

| Model | ~Size (Q4) | Role on COOP |
|---|---|---|
| **`qwen2.5-coder:14b`** | ~9 GB | **default coder** (C#) — fits GPU, RTX 5070 ≈ 40–60 tok/s |
| `qwen2.5-coder:7b` | ~4.7 GB | fast coder / a *second* model for the review peer |
| `deepseek-coder-v2:16b` | ~9 GB | alternative coder/validator (diverse) — Q4 fits, test it |

```sh
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5-coder:7b
# verify GPU: run one, then check it's 100% GPU:
ollama run qwen2.5-coder:14b "say ok"
ollama ps          # PROCESSOR should read 100% GPU
```
> **Fit rule:** keep the loaded model + its KV cache under ~12 GB. A 14B at Q4 (~9 GB) leaves headroom for 32K context. Don't pull 30B+ as a default. If `ollama ps` shows CPU %, the model is too big — drop to a smaller one/quant.

---

## 4. pi + provider

```sh
npm install -g @earendil-works/pi-coding-agent      # (install Node 20+ first if needed)
```
Create **`~/.pi/ollama-provider.ts`** pointing at COOP's ollama and registering the 12 GB models:
```ts
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
const mk = (id: string, name: string) => ({
  id, name, reasoning: false, input: ["text"],
  cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
  contextWindow: 32768, maxTokens: 16384,
});
export default function (pi: ExtensionAPI) {
  pi.registerProvider("ollama", {
    baseUrl: "http://127.0.0.1:11434/v1",   // Path B: use the Windows-host URL from step 2
    apiKey: "ollama", api: "openai-completions",
    models: [
      mk("qwen2.5-coder:14b", "Qwen2.5 Coder 14B"),
      mk("qwen2.5-coder:7b",  "Qwen2.5 Coder 7B"),
    ],
  });
}
```
Verify: `pi --list-models` shows the ollama models.

---

## 5. .NET SDK (C# toolchain)

```sh
# .NET 10 SDK in Ubuntu (matches the csw Azure Functions scaffold: net10.0)
# via Microsoft's script (or apt — see learn.microsoft.com/dotnet/core/install/linux):
curl -fsSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0
echo 'export PATH="$HOME/.dotnet:$PATH"' >> ~/.bashrc && source ~/.bashrc
dotnet --version           # 10.x
dotnet tool install -g dotnet-format 2>/dev/null || true   # (format is built into the SDK on 10)
```
`func` (Azure Functions Core Tools) is **not required** — the referee is `dotnet build` + `dotnet format` + `dotnet test`, no local host run.

---

## 6. The C# workflow (csw)

```sh
git clone <the setup repo>  ~/larry-setup          # (drs76/larry-setup)
mkdir -p ~/.local/bin && echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc

# tooling on PATH:
cp ~/larry-setup/tooling/csw ~/.local/bin/ && chmod +x ~/.local/bin/csw
# pi prompt-templates:
mkdir -p ~/.pi/agent/prompts && cp ~/larry-setup/tooling/{cs-route.md,spec.md,handover.md} ~/.pi/agent/prompts/
# anonymiser (optional, for AL knowledge only): cp ~/larry-setup/tooling/anonymise.py ~/.local/bin/
```
Point `csw` at the setup repo + the smaller model (env in `~/.bashrc`):
```sh
export RUN_BUILD_CS="$HOME/larry-setup/pipeline/run-build-cs.py"
export TEMPLATE="$HOME/larry-setup/templates/cs-handover.template.md"
export PI_CODER_MODEL="ollama/qwen2.5-coder:14b"     # 12 GB default (overrides ornith:35b)
export COMS_VALIDATOR_MODEL="ollama/qwen2.5-coder:14b"
export COMS_RELAY_MODEL="ollama/qwen2.5-coder:14b"
```
Verify: `csw help`.

> The review peer (`csw build … --review`) loads a validator + relay model. On 12 GB keep them the **same** small model (as above) so nothing swaps. See `pipeline/COMS.md`.

### Doc tooling (optional) — `md2pdf` and `/doc-convert`

Only needed if COOP produces documents. COOP runs WSL2 Linux, so it uses the WeasyPrint
engine, the same as the dev box:

```sh
python3 -m pip install --user --break-system-packages \
  markdown weasyprint pymupdf pdfplumber python-docx openpyxl pypandoc-binary
ln -sf "$(python3 -c 'import pypandoc;print(pypandoc.get_pandoc_path())')" ~/.local/bin/pandoc
npm i -g @mermaid-js/mermaid-cli    # mmdc — without it, mermaid fences print as source text
ln -sf ~/larry-setup/tooling/md2pdf ~/.local/bin/md2pdf
```

`--break-system-packages` is needed on Ubuntu 24.04 and later, which mark the system Python
as externally managed. Drop it on older releases if pip objects to the flag instead.

Verify by conversion, not by import — `md2pdf ~/larry-setup/WORKFLOWS-OVERVIEW.md /tmp/wf.pdf`
should report `rendered 5 mermaid diagram(s)`.

---

## 7. Smoke test (C#)

```sh
csw new coop-smoke
# put a tiny spec in ~/cs/projects/prototypes/coop-smoke/larry-handover.prompt.md
# (e.g. an HTTP-trigger Ping function returning {"message":"pong"}), then:
csw build coop-smoke
```
Expect `RESULT: PASS` (Larry — here COOP — writes the function, `dotnet build` + format gate pass). Add `--review` for the validator pass. If a build stalls on the 14B model, escalate to Claude: `csw build coop-smoke 2` (runs 2 local rounds, then hands off to `claude`).

> **`csw build` lints the handover first.** `handover_lint` catches a defective spec before a build is spent on it; if the build stops before writing with a lint error, fix the handover (or bypass with `LINT=0 csw build …`).

Full lifecycle + `/spec`/`/handover` flow: see `pipeline/PROJECT-LIFECYCLE.md` and `pipeline/CSW.md`.

---

## Tier note — COOP is standalone but VRAM-limited

COOP runs its own ollama + `csw` end-to-end (free, and offline for the LLM part — only NuGet fetch needs internet). But at **14B** it drafts the lighter tier well and **relies on Claude escalation (`csw build <p> N`) more** for hard/large functions where Larry would throw a 30–35B model at it. Its `--review` validator is also a small model — weaker than Larry's ornith, so treat findings as hints.

---

## Optional — Larry parity extras

- **coms peer review:** `cp ~/larry-setup/tooling/{coms.ts,themeMap.ts} ~/.pi/` (adapt imports if the pi package name differs), seed a local `al-anon-map.txt` only if using the AL knowledge tools. `csw build … --review` then works. See `pipeline/COMS.md`.
- **Maintenance dashboard:** `setup/dashboard/` — deploy per its README, but set `LARRY_REPO=$HOME/larry-setup` and `BUILD_BOX=localhost` (COOP builds itself); front with a reverse proxy + basic-auth if exposing on the LAN.

---

## Appendix A — Go (`gow`), optional

Only if the colleague later wants Go. Install Go (`sudo apt install golang-go` or the official tarball), then:
```sh
cp ~/larry-setup/tooling/gow ~/.local/bin/ && chmod +x ~/.local/bin/gow
cp ~/larry-setup/tooling/go-route.md ~/.pi/agent/prompts/
export RUN_BUILD_GO="$HOME/larry-setup/pipeline/run-build-go.py"
```
Referee = `go build`+`vet`+`test`. Same 14B model + escalation notes. See `pipeline/GOW.md`.

## Appendix B — AL / Business Central (`alw`), optional

Only if needed. AL needs the **dotnet AL compiler** (`al`) + a symbol cache; heavier setup. Note **no AL-tuned model fits 12 GB** (`al-coder-qwen36` is ~17 GB) — use `qwen2.5-coder:14b` for AL too (lower AL quality) and lean on Claude. Copy `tooling/alw` + `al-route.md`, set `RUN_BUILD` at `pipeline/run-build.py`, read `reference/AL-REFERENCE.md` + `pipeline/ALW.md`.

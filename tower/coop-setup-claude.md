# Claude brief — set up COOP as a standalone C# build box (mirror of "Larry")

**You are Claude Code, running in a terminal on a Windows 11 machine called COOP (usually inside WSL2
Ubuntu). Your job: help the user stand up COOP as a self-contained local C# / Azure Functions build
box that mirrors an existing box called "Larry".** Work step-by-step, run read-only checks freely, and
**confirm with the user before any install, download, or system change**. Adapt to whatever is already
installed — do not assume a clean machine.

## The box
- Intel i9-11900, 64 GB RAM, **NVIDIA RTX 5070 — 12 GB VRAM**, ~8 TB disk, Windows 11.
- User works in **C# / Azure Functions** only (Go and AL are optional, skip unless asked).

## Three things that make COOP different from Larry (bake these in)
1. **NVIDIA/CUDA** (not AMD/ROCm) — ollama auto-detects the GPU; no ROCm, no `HSA_OVERRIDE`.
2. **12 GB VRAM** — the strong 30–35B models Larry uses **do not fit**. **Never pull a model bigger than
   ~14B as a default.** Use **`qwen2.5-coder:14b`** (~9 GB) as the coder; `qwen2.5-coder:7b` as a fast/second
   model. After pulling, run `ollama ps` and confirm `PROCESSOR` is **100% GPU** — if it shows any CPU%, the
   model is too big; drop to a smaller one.
3. **Windows** — the tooling is bash+python+a pi TS extension, so it runs in **WSL2 Ubuntu**.

## What "done" looks like
`csw new coop-smoke` → a tiny handover → **`csw build coop-smoke` prints `RESULT: PASS`** (COOP writes an
Azure Function locally, `dotnet build` + format gate pass), all on COOP's own ollama — no cloud for the LLM.

## Procedure (confirm before each install)
1. **Detect current state** (read-only): `uname -a`, `which wsl 2>/dev/null`, `nvidia-smi`, `which ollama`,
   `ollama ls 2>/dev/null`, `which node npm pi dotnet git python3`, `pi --list-models 2>/dev/null`.
   Summarise what's present/missing before doing anything.
2. **GPU in WSL:** confirm `nvidia-smi` lists the RTX 5070. If not, tell the user to install/upgrade the
   **Windows** NVIDIA driver (NOT a driver inside WSL) and `wsl --update`.
3. **Base tools:** ensure `build-essential git curl python3 python3-venv unzip` (apt).
4. **Ollama** — ask the user which they want (both are fine):
   - **A) inside WSL2:** `curl -fsSL https://ollama.com/install.sh | sh`; run `ollama serve`.
   - **B) native Windows ollama** already installed: point clients at the Windows host —
     `export OLLAMA_HOST="http://$(ip route | awk '/default/{print $3}'):11434"` (or mirrored networking →
     `localhost`). Verify `curl $OLLAMA_HOST/api/version`.
5. **Models:** `ollama pull qwen2.5-coder:14b` (+ `:7b`). Verify 100% GPU with `ollama ps`.
6. **pi:** `npm install -g @earendil-works/pi-coding-agent` (Node 20+). Write `~/.pi/ollama-provider.ts`
   registering `qwen2.5-coder:14b` + `:7b` (baseUrl = the ollama URL from step 4, `contextWindow:32768`,
   `maxTokens:16384`). Verify `pi --list-models`.
7. **.NET SDK 10:** `curl -fsSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0`, add
   `~/.dotnet` to PATH, verify `dotnet --version`. (`func`/Azure Functions Core Tools NOT needed.)
8. **The workflow:** `git clone` the setup repo (ask the user for the URL — it's the `larry-setup` repo).
   Put `tooling/csw` on `~/.local/bin` (chmod +x, PATH); copy `tooling/{cs-route.md,spec.md,handover.md}`
   into `~/.pi/agent/prompts/`. Export in `~/.bashrc`:
   `RUN_BUILD_CS=<repo>/pipeline/run-build-cs.py`, `TEMPLATE=<repo>/templates/cs-handover.template.md`,
   and the **12 GB model defaults** `PI_CODER_MODEL=ollama/qwen2.5-coder:14b`,
   `COMS_VALIDATOR_MODEL=ollama/qwen2.5-coder:14b`, `COMS_RELAY_MODEL=ollama/qwen2.5-coder:14b`. Verify `csw help`.
9. **Smoke test:** `csw new coop-smoke`; write a minimal `larry-handover.prompt.md` for an HTTP-trigger
   `Ping` function returning `{"message":"pong"}`; run `csw build coop-smoke`; expect `RESULT: PASS`.
   If it stalls on the 14B model, `csw build coop-smoke 2` escalates to Claude after 2 local rounds.

## Reference
Full human guide: `tower/coop-setup.md` in the repo. Deeper docs after cloning: `pipeline/CSW.md`,
`pipeline/PROJECT-LIFECYCLE.md`, `pipeline/COMS.md`. Optional Go/AL: appendices in `coop-setup.md`.

## Finish
Report exactly what you installed/configured, the ollama placement chosen (A or B), the model(s) pulled,
and the smoke-test result. Flag anything you skipped or that needs the user's action (driver, repo URL, firewall).

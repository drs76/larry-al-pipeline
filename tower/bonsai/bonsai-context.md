# Ternary-Bonsai-27B on Larry — pi chat brain (Mode B time-share)

Local **chat/vision/reasoning** model on Larry, separate from the `qwen3-coder:30b`
build coder. Runs on the GPU **one at a time** with the coder (Mode B time-share).

- **Model**: [prism-ml/Ternary-Bonsai-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf)
  — Qwen3.6-27B post-compressed to ternary weights {−1,0,+1}, GGUF `Q2_0` (~1.71 bpw). Not gated.
- **Runtime**: the [Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) fork of llama.cpp.
  Ubuntu-ROCm-7.2 prebuilt binary runs fine on Larry's Rocky 10 / ROCm 7.2.3 / gfx1100.
- **Measured**: 52 tok/s gen, ~140–270 tok/s prompt. VRAM 9.55 GB (27B + vision mmproj + KV4 @8K).

## Why Mode B (time-share), not co-resident
Coder ≈ 18 GB + Bonsai ≈ 9.55 GB = 27.5 GB > 24 GB card. Can't both be hot. So:
- `bonsai on` **evicts** the ollama coder (`ExecStartPre=bonsai-freevram`), then loads the 27B.
- Idle > 15 min → `bonsai-idle.timer` **stops** the server, handing VRAM back to the coder.
- The build pipelines (`run-build*.py`) call `bonsai off` before loading the coder, so a
  build never OOMs against a running chat server.

## Files in this dir
| File | Installs to | Purpose |
|---|---|---|
| `bonsai-env.sh` | `/mnt/models/bonsai/bonsai-env.sh` | systemd EnvironmentFile — **bare KEY=val, NO `export`** |
| `bonsai-llama.service` | `/etc/systemd/system/` | the llama-server (on-demand, not boot-enabled) |
| `bonsai-freevram.sh` | `/usr/local/bin/bonsai-freevram` | ExecStartPre — unload all ollama models |
| `bonsai` | `/usr/local/bin/bonsai` | control CLI: `on` / `off` / `status` / `log` |
| `bonsai-idle.sh` | `/usr/local/bin/bonsai-idle` | stop server after 15 min idle |
| `bonsai-idle.{service,timer}` | `/etc/systemd/system/` | 5-min idle poll |
| `bonsai.conf` | `/etc/nginx/conf.d/` | TLS proxy **:8444 → 127.0.0.1:8091** (mirrors larry.conf) |
| `bonsai-provider.ts` | client `~/.pi/` | pi provider `bonsai/ternary-bonsai-27b` |

> **Port note**: server binds `127.0.0.1:8091` (8090 is larry-dashboard). LAN reaches it only
> via nginx TLS `:8444` — raw port stays closed, same posture as ollama (11434 behind 11443).

## Install (on Larry)
```bash
# 1. clone + model on the NVMe (root fs is tight)
doas mkdir -p /mnt/models/bonsai && doas chown dav:dav /mnt/models/bonsai
cd /mnt/models/bonsai && git clone --depth 1 https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo
./scripts/download_binaries.sh                      # auto-picks ubuntu-rocm-7.2 build
python3 -m venv .venv && ./.venv/bin/pip install huggingface-hub
BONSAI_FAMILY=ternary BONSAI_MODEL=27B ./scripts/download_models.sh
rm -f models/ternary-gguf/27B/*dspark*.gguf         # CUDA-only drafter, dead weight on ROCm
sed -i 's/^PORT=8080/PORT=8091/' scripts/start_llama_server.sh

# 2. env + scripts + units (from this dir)
cp bonsai-env.sh /mnt/models/bonsai/bonsai-env.sh
doas install -m 755 bonsai             /usr/local/bin/bonsai
doas install -m 755 bonsai-freevram.sh /usr/local/bin/bonsai-freevram   # dst drops the .sh
doas install -m 755 bonsai-idle.sh     /usr/local/bin/bonsai-idle
doas install -m 644 bonsai-llama.service bonsai-idle.service bonsai-idle.timer /etc/systemd/system/
doas systemctl daemon-reload && doas systemctl enable --now bonsai-idle.timer

# 3. nginx TLS proxy + firewall
doas install -m 644 bonsai.conf /etc/nginx/conf.d/bonsai.conf
doas nginx -t && doas systemctl reload nginx
doas firewall-cmd --add-port=8444/tcp --permanent && doas firewall-cmd --reload
```

## Use
```bash
ssh larry 'bonsai on'      # ~18s: evict coder, load 27B, waits for real readiness
ssh larry 'bonsai status'  # active? ollama loaded? VRAM?
ssh larry 'bonsai off'     # free VRAM (or let the idle timer do it)
```

## Control from the chat client (no ssh)
The larry-dashboard maintenance API drives the service over TLS+basic-auth — no ssh key
needed on the client. Two dashboard actions run `doas systemctl {start,stop} bonsai-llama`:
`POST https://larry.home.arpa/dash/api/action/bonsai-{on,off}` (also buttons in the dash
Maintenance tab). The pi extension `bonsai-control.ts` uses them:

- **auto-wake** — `pi.on("session_start")` starts Bonsai when you launch pi pointed at it
  (`pi --provider bonsai`) and blocks until the model can answer (kills the chicken-egg).
  The public ExtensionAPI has no per-request hook, so a mid-session model switch to Bonsai
  isn't auto-woken — use `/bonsai on` for that.
- **`/bonsai on|off|status`** — explicit control from any pi session.

It shells `curl` (system CA already trusts the HomeLab cert, so no Node CA fuss).

**Client setup (per box that runs pi):**
```bash
cp <repo>/tower/bonsai/bonsai-control.ts ~/.pi/bonsai-control.ts
# add "../bonsai-control.ts" to packages[] in ~/.pi/agent/settings.json
# dashboard creds (NOT committed) — one of:
export LARRY_DASH_AUTH='user:pass'                 # env, or:
printf 'user:pass' > ~/.pi/.larry-dash-auth && chmod 600 ~/.pi/.larry-dash-auth
```
Without creds the `/bonsai` command and auto-wake print a clear "no dashboard creds" message.

## pi client wiring (each box that runs pi)
```bash
cp <this-repo>/tower/bonsai/bonsai-provider.ts ~/.pi/bonsai-provider.ts
# add "../bonsai-provider.ts" to the "packages" array in ~/.pi/agent/settings.json
pi --list-models bonsai            # verify: bonsai/ternary-bonsai-27b
```
Applied on the localDev workstation and on the **thinkpad** (`davlap`, 2026-08-10 — provider +
control in `~/.pi/`, both listed under `extensions` in `~/.pi/agent/settings.json`, dashboard
creds in `~/.pi/.larry-dash-auth`, so `/bonsai`, auto-wake and build-time VRAM eviction all work
from there; `defaultProvider`/`defaultModel` match the workstation, minus the openrouter package).
Round-trip verified from a stopped server: a bare `pi -p` woke `bonsai-llama` through the dashboard
and answered. TODO on the WSL client when next up (see wsl-setup.md).

> Creds go in **`~/.pi/.larry-dash-auth`**, not `~/.larry-dash-auth` — `_creds()` in
> `bonsai-control.ts` and `pipeline/bonsai_vram.py` only look under `~/.pi/`. A file in the home
> root is silently ignored and every eviction reports "no dashboard creds".

### Bonsai is the interactive-chat default (2026-08-07)
`~/.pi/agent/settings.json` on the localDev workstation:
```json
"packages": ["../ollama-provider.ts", "../bonsai-provider.ts",
             "../bonsai-control.ts", "../openrouter-provider.ts"],
"defaultProvider": "bonsai",
"defaultModel": "ternary-bonsai-27b"
```
So a bare `pi` chats on Bonsai (auto-woken by `bonsai-control.ts`), and
`pi --provider openrouter --model deepseek/deepseek-chat` reaches the cheap cloud
tier (needs `OPENROUTER_API_KEY`; **egress — never for customer code**).

**Builds are unaffected by these defaults.** Every pipeline runner passes an
explicit `-e <provider-ext> --model <model>` *and* `-ne` (no extension discovery),
so `run-build{,-go,-cs}.py` never reads `packages[]`, `defaultProvider`, or
`defaultModel`. Verified 2026-08-07.

**Contention, and how builds handle it.** With Bonsai as the chat default it is up
far more often, and Bonsai + the ollama coder co-resident spills the coder to CPU
(measured: 33%/67% CPU/GPU on a 30b coder), which makes the write phase thrash
toward its 1200s timeout.

Eviction lives in **`pipeline/bonsai_vram.py`** and is used by all four runners
(`run-build{,-go,-cs}.py`, `run-edit.py`). It tries, in order:

1. `bonsai off` — the CLI, **Larry-local only** (`/usr/local/bin/bonsai`, shells
   `doas systemctl`).
2. `POST {dash}/api/action/bonsai-off` — the larry-dashboard API over TLS+basic-auth,
   which runs the same systemctl stop on Larry. **This is what makes eviction work
   from deb / WSL / thinkpad**, where step 1 raises FileNotFoundError.

Creds follow the same contract as `bonsai-control.ts`: `LARRY_DASH_AUTH="user:pass"`
or `~/.pi/.larry-dash-auth` (chmod 600). Without them the build prints a loud,
actionable warning instead of silently contending.

It is called from each runner's `main()` and from the `run_pi()` funnel
(`free_bonsai_vram_once()`, at most one probe per process), so paths that skip
prewarm — e.g. `run-edit.py --build-only`, whose fix rounds call `run_pi` directly —
are covered too. Mid-tier (OpenRouter) calls are excluded by an `ext == PI_EXT`
guard: a cloud call needs no local VRAM and must not stop someone's chat server.

Knobs: `BONSAI_EVICT=0` to skip eviction entirely, `LARRY_DASH_URL` /
`BONSAI_HEALTH_URL` to point at a different host.

Before 2026-08-07 this was broken in three ways: `run-build.py` shelled the CLI with
no fallback, `run-build-{go,cs}.py` did the same inside a blanket `except: pass`
(fully silent), and `run-edit.py` only got eviction transitively via
`rb.prewarm_coder()`, so `--build-only` never evicted at all.

## Gotchas (learned the hard way)
- `llama-cli` headless (no TTY) drops to conversation mode and spins on `>` EOF — looks like
  a hang, isn't. **Use the server only.**
- Run thinking-OFF for clean output: `chat_template_kwargs:{enable_thinking:false}` — otherwise
  all tokens go to the reasoning channel and `content` is empty.
- systemd `EnvironmentFile` silently ignores `export KEY=val`. Bare `KEY=val` only.
- `/health` goes green ~3s before weights finish loading (~18s); the `bonsai on` probe waits
  on a real 1-token completion instead.

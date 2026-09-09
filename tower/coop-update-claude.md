# Claude brief — update an existing COOP box to the latest larry-setup

**You are Claude Code, running in a terminal on COOP (Windows 11, usually inside WSL2). COOP is an
already-working standalone C# build box that mirrors "Larry" (own ollama + `csw`). Your job: pull the
latest `larry-setup` and reconcile the weekend's changes — the important one is a new egress policy
that will otherwise break Claude escalation.** Run read-only checks freely; **confirm before any
change to `~/.bashrc` or installs**. Do not re-run the first-time setup — COOP is already configured.

## The box (unchanged)
- NVIDIA RTX 5070 **12 GB VRAM** (CUDA), i9-11900 / 64 GB, Win11 + WSL2. **C#/Azure Functions only.**
- Hard rule still: **never load a model bigger than ~14B** — the coder is `qwen2.5-coder:14b`.

## The one thing that will bite (bake this in)
A new **egress policy** gate (`pipeline/egress_policy.py`, now imported by `run-build-cs.py`) is
**deny-by-default**: the default profile `local-only` **blocks all Claude calls and disarms
escalation**. COOP's 12 GB tier **relies on Claude escalation** (`csw build <p> N`). COOP is the
user's own box on non-work code, so the correct profile is **`personal`**. If you skip this, builds
silently stop escalating.

## Procedure (confirm before each change)

1. **Detect current state** (read-only): `ls ~/larry-setup/pipeline/egress_policy.py 2>/dev/null`
   (absent = not yet updated); `grep -E 'PI_CODER_MODEL|COMS_.*_MODEL|EGRESS_POLICY' ~/.bashrc`;
   `which csw anon`; `nvidia-smi -L`. Summarise what's present before changing anything.
   (COOP has **no repo access** — `~/larry-setup` is a plain file tree, not a git clone, so there is
   no `git pull`; updates arrive as a zip.)

2. **Apply the update zip** (confirm the path with the user, default `~/coop-update.zip`):
   `unzip -o ~/coop-update.zip -d ~/larry-setup` — overwrites changed files, adds new ones, leaves
   the user's `.anon/` and handovers alone. Refresh the CLI:
   `cp ~/larry-setup/tooling/csw ~/.local/bin/ && chmod +x ~/.local/bin/csw`.

3. **Set the egress policy** (the critical fix). Confirm, then append to `~/.bashrc`:
   `export EGRESS_POLICY=personal` → `source ~/.bashrc`.
   Install the helper + verify: `ln -sf ~/larry-setup/tooling/anon ~/.local/bin/anon && chmod +x ~/.local/bin/anon` (symlink, **not** a copy — it imports `pipeline/` by real path);
   `anon check` → `personal` must show **ALLOW**, `local-only` **BLOCK**.
   (If the user ever hosts **work/client** code here, tell them to add a per-repo
   `<repo>/.anon/config.yml` with `policy: local-only` — it overrides the env for that repo.)

4. **Re-confirm the 12 GB model override** (the pipeline default is now a 30B that won't fit):
   ensure `~/.bashrc` still has `PI_CODER_MODEL=ollama/qwen2.5-coder:14b` (and the two
   `COMS_*_MODEL` = same). After the next build, `ollama ps` → `PROCESSOR` must read **100% GPU**.

5. **Opt-in extras** (mention; enable only if the user wants):
   - **anon hook** — `anon scrub`/`anon run`: scrub sensitive tokens + fail-closed secret gate before
     sending a repo to Claude (only relevant if work/client code lands on COOP).
   - **`FIX_STRATEGY=snippet`** — local Fast-Apply edits; good if the 14B mangles files on rewrites.
   - **BCQuality** knowledge injection (AL-oriented, neutral for C#; needs a clone — `pipeline/bcquality-integration.md`).
   - **`REVIEW_BACKEND=claude`** — stronger reviewer on `csw build … --review` (egress-gated → needs step 3).
   - Metrics/leaderboard, pre-warm, forward-fix — automatic, no action.

6. **Verify end-to-end:** `csw help`, then `csw build coop-smoke 2` (or the user's project). The banner
   must print **`Egress policy: personal`** and **`Escalation: ARMED …`** — NOT `DISARMED by egress
   policy`. If DISARMED, step 3 didn't take.

## Reference
Human runbook: `tower/coop-update.md`. Original setup: `tower/coop-setup.md`. Deeper: `pipeline/RUN-BUILD.md`
(egress policy in the config table + escalation section), `tooling/anon-claude-hook.spec.md`.

## Finish
Report: whether the zip extracted cleanly, whether `EGRESS_POLICY=personal` is now set, the model override state,
the `anon check` result, and the smoke-build banner (policy + escalation lines). Flag anything skipped or
needing the user (dirty tree, work-code repos that should stay `local-only`).

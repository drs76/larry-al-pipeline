# Larry Model Benchmark & Tuning Plan

**Goal:** find whether a different coder model + tuned runtime squeezes more out of Larry
(RX 7900 XTX, 24GB) for the AL build pipeline than the current default `qwen3-coder:30b`.
Measure objectively via the existing build leaderboard, then tune the winner.

Created 2026-07-25. Harness: `setup/pipeline/run-build.py` (`alw`) + `build_leaderboard.py`.

---

## 1. Roster (all fit 24GB, all pull from ollama)

| Role | Model | Size (Q4) | Notes |
|---|---|---|---|
| Incumbent (default) | `ollama/qwen3-coder:30b` | 18GB | current `alw` default; MoE ~3B active, tool-call native |
| Incumbent (surprise) | `ollama/al-coder-qwen36` | 17GB | beat default on 2 leaderboard runs — validate w/ N≥3 |
| **Challenger** | `ollama/qwen3:32b` | ~20GB | **dense 32.8B**, hybrid thinking. Run `/no_think` (see risks) |
| **Challenger** | `ollama/deepseek-coder-v2:16b` | ~9GB | MoE 16B; DeepSeek slot (V3=671B can't fit) |

**Named-but-unavailable (resolved):** "Qwen3-Coder 32B" doesn't exist (Qwen3-Coder = 30B-A3B / 480B
only) → using dense **Qwen3-32B**. "DeepSeek Coder V3" not on ollama + V3 is 671B → using
**deepseek-coder-v2:16b**.

Optional wider sweep (already local): `devstral`, `gemma4:26b`, `north-mini-code`, `al-coder-qwen3`.

---

## 2. Test project suite (fixed, like-for-like)

Same handover files for every model. Graded difficulty; covers the object types the leaderboard
tracks (Table/Page/Codeunit/TableExt/ControlAddin). Stored under `pipeline/bench/projects/`.

| # | Project | Difficulty | Exercises | Source |
|---|---|---|---|---|
| P1 | CRUD extension (table + card + list page) | Easy | Table, Page basics | new, minimal |
| P2 | Map Integration factbox | Medium | ControlAddin, TableExt, layout gotchas | existing proven ([[project_tsg_map_integration]]) |
| P3 | Doc-Link → AZ Storage | Hard | events, interception, ABS ext ([[project_doc_link_az_storage]]) | existing |
| P4 | Fresh unseen mini-project | Medium | generalization (not in RAG/training) | author new, hold back |

P4 matters: P2/P3 may be in `al-rag` corpus → inflates familiar models. A held-back project
measures true generalization.

---

## 3. Method & fairness controls

Past lesson: **2-run samples misled us** (al-coder-qwen36 looked great on n=2). Enforce:

- **N ≥ 3 repeats** per (model × project). 4 models × 4 projects × 3 = 48 runs baseline.
- **Autonomous only** — disable Claude escalation to measure *raw* model (verify the no-escalate
  knob in Phase 0; `CODER_BACKEND=pi` + cap fix rounds).
- **Fixed fix-round cap** (e.g. 5) across all runs.
- **Warm the model** before the timed run (exclude ROCm cold-load; `ornith` taught us cold-load
  can hang — [[reference_larry_models]]).
- **One model resident at a time**, `bonsai off` (free the GPU), fixed `keep_alive`.
- **Fixed sampling:** low temp (0.1–0.2), fixed seed where supported, same `top_p`.
- **Same `num_ctx`** across models (cap to what 32B allows in VRAM — likely 16K, see §5).
- **qwen3:32b in `/no_think`** for the agentic loop.

**Select model per run:** `PI_CODER_MODEL=ollama/<model> CODER_BACKEND=pi alw build <project>`.
Metrics auto-append to the build log → `build_leaderboard.py` aggregates.

**Pre-req fix:** leaderboard groups by raw `coder_model` string (`build_leaderboard.py:63`), so
`x` and `x:latest` split into two rows. Normalize (strip `:latest`) before running, else results
fragment. See §7.

---

## 4. Metrics (leaderboard columns + additions)

Existing: first-pass %, final %, autonomous %, avg fix rounds, regression rate, fix efficiency,
avg time, manifest %, Claude-escalation %, first-pass-by-object-type, error-category profile.

Add per model: **tokens/sec** (throughput), **VRAM peak** (`rocm-smi`), **cold-load time**,
a **diff-size per fix round** (lines touched / errors cleared — exposes rewrite-happy repair, §5b-c),
and for qwen3:32b a **think vs no-think** A/B.

Primary ranking key: **final % → autonomous % → avg time** (quality first, then self-sufficiency,
then speed).

---

## 5. Tuning phase (squeeze knobs — on top 1–2 only)

After baseline ranks the field, tune the leader:

- **`num_ctx` vs VRAM** — biggest lever for a 32B on 24GB. Find max context that fits with headroom.
- **KV-cache quant / flash-attention** (`OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`) —
  fits larger context in less VRAM; measure quality impact.
- **Quant level** — Q4_K_M vs Q5/Q6 (if it fits) vs Q8; quality/VRAM/speed trade.
- **Sampling sweep** — temperature / top_p grid on the suite.
- **RAG injection on/off** — `al-rag` pre-inject vs bare; does grounding help *this* model
  ([[project_ms_al_source_rag]])?
- **Modelfile SYSTEM wrap** — an AL-primed system prompt (like `al-coder-*` wraps) on the raw model.
- **GPU power/clock** — `rocm-smi` perf level; confirm not power/thermal capped under sustained load.
- **`keep_alive` / warm strategy** — eliminate reload stalls between fix rounds.

---

## 5b. Workflow changes under test

Model swap is one axis; the *workflow* is another and may matter more. Three changes, each measured
against the current flow on the same suite.

### (a) Verified symbol pre-flight — ship candidate
Targets the #1 first-pass error class (missing-symbols: 39% for qwen3-coder, 100% of al-coder-qwen36's
fails). New step **before Generate AL**:

1. Model *declares* the external objects/deps it will reference (from the handover + analysis).
2. **Resolve deterministically** — verify each against real packages via `al_downloadsymbols`
   (`globalSourcesOnly:true`, MS NuGet/AppSource, no auth — [[reference_al_symbols]]) and pre-stage
   `.alpackages`.
3. **Do NOT trust the model's list** — these models hallucinate APIs (see `al-coder-tuned`). The
   declared names are a *fetch hint*, verified against what actually resolves; unresolved names are
   flagged back before a line of AL is written.

Measure: does first-pass% rise and missing-symbols% fall vs current? If yes, ship it into `run-build.py`
regardless of model outcome.

### (b) `WORKFLOW=decomposed` variant — A/B only
Full chain: `analyse → list objects → list symbols → (verified) → generate AL → compile → repair`,
vs current single-pass generate. Gated behind an env flag so Phase 1 runs both.

- **Keep the manifest human/Claude-authored** — it is the spec contract that gates the write and
  defines "done". The model must NOT generate its own manifest (it would grade its own homework:
  under-scope then "pass"). The decomposed "list objects" step is *checked against* the manifest, not
  a replacement for it.
- Watch cost: extra round-trips add latency, tokens, and **pi stream-wedge risk** on long/32K-ctx
  agentic runs ([[reference_pi_stream_wedge]] — keep missions small). Decomposition fights that; the
  A/B must show it pays for itself.
- Hypothesis: helps weak local models (plan-then-write), marginal for strong ones. The suite decides.

### (c) Minimal-edit repair discipline — ship candidate
Directly attacks the **40% regression rate** on qwen3-coder (big rewrites = the regressions the
leaderboard flags; a "fix" that rewrites working code re-breaks it). Inject these rules into the repair
prompt, and prefer the deterministic **FIND/REPLACE** edit path ([[project_edit_flow]]) over full-file
regen so the constraint is *structural*, not just asked-for:

> **Repair rules — surgical only:**
> - Only modify lines involved in the reported errors.
> - Never rename working procedures.
> - Never change object IDs.
> - Preserve all working code.
> - Minimise edits.

Measure: regression rate + avg fix rounds down, fix efficiency up, final% not worse. Add a **diff-size
per fix round** metric (lines touched / errors cleared) — a rewrite shows up as a huge ratio. If it
holds, ship into the repair loop for all models.

---

## 6. Phases

- **Phase 0 — Setup (½ day):** pull `qwen3:32b`, `deepseek-coder-v2:16b`; smoke-test each drives
  tools in the pi loop (watch for reasoner "describe-not-do" — [[reference_pi_coms]]); verify VRAM
  fit + no-escalate knob; fix the `:latest` grouping; author P1 + P4 handovers. **Implement the two
  ship-candidate workflow changes behind flags** — verified symbol pre-flight (§5b-a) and minimal-edit
  repair rules + diff-size metric (§5b-c) — plus the `WORKFLOW=decomposed` variant (§5b-b).
- **Phase 1 — Baseline (compute-bound):** 4 models × 4 projects × N≥3, autonomous, fixed controls →
  aggregate leaderboard. Run each **workflow variant** as its own arm: `current` vs `+symbol-preflight`
  vs `+minimal-repair` vs `decomposed` (add arms incrementally so each change's delta is isolated, not
  confounded). Compare first-pass% + missing-symbols% (pre-flight), regression rate + diff-size
  (repair), and net final%/time (decomposed).
- **Phase 2 — Analyze:** rank; pick top 1–2; note per-object-type + error-category weak spots.
- **Phase 3 — Tune:** §5 sweep on the leader; re-run the suite per config.
- **Phase 4 — Decide:** promote a new `alw` default only if it beats `qwen3-coder:30b` on
  **final % AND autonomous %** over N≥3, without materially worse time. Update `PI_CODER_MODEL`
  default + memory.

---

## 7. Risks / gotchas

- **qwen3:32b thinking mode** → may narrate instead of executing tools in the agentic loop (like
  deepseek reasoners). Mitigate: `/no_think`. If still flaky, it's a chat model not a pipeline coder.
- **32B VRAM tight** — Q4 ~20GB leaves ~4GB for KV; large context may OOM. KV-quant (§5) is the fix.
- **deepseek-coder-v2 AL quality** unknown — may be weak on AL specifically.
- **RAG corpus bias** — P2/P3 may be in `al-rag`; P4 controls for it.
- **Small-sample variance** — the whole reason for N≥3; don't promote on n=2.
- **Leaderboard `:latest` split** — fix before running or data fragments (§3).

---

## 8. Quick-start commands (Phase 0)

```bash
# pull challengers
ssh larry 'ollama pull qwen3:32b && ollama pull deepseek-coder-v2:16b'

# free GPU, warm a model, check VRAM fit
ssh larry 'bonsai off; ollama run qwen3:32b "/no_think ok" >/dev/null; rocm-smi --showmeminfo vram'

# one benchmark run
PI_CODER_MODEL=ollama/qwen3:32b CODER_BACKEND=pi alw build pipeline/bench/projects/P1

# aggregate
ssh larry 'python3 /mnt/rojaws/localDev/setup/pipeline/build_leaderboard.py'
```

Related: [[reference_larry_models]], [[project_pi_harness_plan]], [[reference_pi_coms]],
[[project_ms_al_source_rag]], build-leaderboard.md.

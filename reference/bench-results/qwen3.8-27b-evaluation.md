# Qwen3.8-27B evaluated as the default AL coder — 2026-08-16

**Verdict: NOT the default.** Quality is competitive with the incumbent; wall clock is ~4× worse
and structural. Keeping the model pulled and registered, since it is usable interactively.

| | Qwen3.8-27B (`qwen3.8:27b`) | `qwen3-coder:30b` (incumbent) |
|---|---|---|
| architecture | **dense** — 27B active/token | **MoE** — ~3B active/token |
| generation | **29.3 tok/s** | **88.2 tok/s** |
| cold load | **210s** | 24s |
| VRAM | 19GB, 100% GPU | 21GB, 100% GPU |
| suite pass | **6/9** | **7/9** |
| median run | **373s** | 96s |

Source: `hf.co/unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_XL` (18GB), wrapped as `qwen3.8:27b`
(temp 0.15 / top_p 0.8 / num_ctx 32768).

## Results — SUITE40, thinking OFF (the valid run)

| Project | Control | Challenger |
|---|---|---|
| p1 (5 files) | 2/3 — 64–182s | **3/3** — 188–373s |
| p4 (8 files) | 2/3 — 83–127s | 2/3 — 315–1877s |
| map (8 files) | **3/3** — 74–123s | 1/3 + 1 TIMEOUT — 931–2400s |
| **total** | **7/9**, 152 min for both arms | **6/9** |

6/9 vs 7/9 on n=3 is one run apart — **not a distinguishable quality difference**. The gap that
decides it is time: ~4× median, widening with task size (map: control averaged 94s, challenger
931/984/2400s).

## The thinking-mode trap — why the first run was void

`SUITE38` scored the challenger **3/9**, with **0/8 files written** on every 8-file task. That
measured a misconfiguration, not the model: thinking was ON, so it reasoned for ~540s, exited 0
and emitted no tool calls at all. It is fine on 5-file tasks and collapses past that.

Getting thinking off is not obvious:

- `PARAMETER think false` in a Modelfile → `Error: unknown parameter 'think'`
- ollama's **`/v1`** endpoint ignores both `think` and `chat_template_kwargs`
- the only knob `/v1` honours is **`reasoning_effort`**

pi sends `reasoning_effort` under the default `thinkingFormat: "openai"`, so the fix lives in the
provider entry in `~/.pi/ollama-provider.ts` (per-machine, untracked):

```ts
{ ...mk("qwen3.8:27b", "Qwen3.8 27B"),
  reasoning: "minimal" as const,          // makes pi send the field at all
  compat: { thinkingFormat: "openai" as const,
            thinkingLevelMap: { off:"none", minimal:"none", low:"none", medium:"none",
                                high:"none", xhigh:"none", max:"none" } } }
```

Mapping **every** level to `"none"` pins it off regardless of what pi or the caller asks for.
Model-scoped, so no other entry is affected.

## Two traps that nearly produced a false result

**1. An injection-budget regression, caught only by re-running control.** Between SUITE38 and
SUITE40 the Learn ingest took `01-syntax-style.md` from 1.8k → 7.4k tokens, which evicted
`02-objects.md` from the handover's ~12.5k injection set. Control collapsed 2/3 → **0/3** on p1
with `AL0104` brace errors. Had the challenger been compared against *that* control it would have
looked strong for entirely spurious reasons. Fixed by splitting out `24-language-basics.md`
(commit `912832e`); always confirm the `inject:` line matches the baseline run before trusting a
comparison.

**2. A stalled run needs a hard cap.** `map__challenger__r1` hit the 2400s `RUN_TIMEOUT` — the
first live firing of that cap. Unbounded it would have hung the suite indefinitely. It is recorded
as its own `TIMEOUT` verdict, never folded into `FAIL`, because a stall is an infrastructure event
and counting it as a model failure biases the benchmark.

## Also observed

Control improved **5/9 (SUITE38) → 7/9 (SUITE40)**, most plausibly from the `DataClassification`
and tooltip rules added to the injected gotcha table that day. Not isolated by a controlled test —
treat as suggestive, not measured.

## Reproduce

```bash
cd projects/bench
MAX_FIX_ROUNDS=3 RUN_TIMEOUT=2400 \
  ./run-suite.sh <tag> ollama/qwen3-coder:30b ollama/qwen3.8:27b p1 p4 map
```
Runner: `pipeline/bench-run-suite.sh`. Arms run grouped (not interleaved) so each model loads once
— interleaving would pay the challenger's 210s cold load on every run.

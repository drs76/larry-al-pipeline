# Upgrade validation — Ollama 0.31.1 → 0.33.2 on Larry

Run 2026-08-31. An **experiment**, not maintenance: the pin was working, and the regression
behind it was independently diagnosed. Criteria were fixed before the long build.

## Hypothesis, and why 0.33.2

Larry was pinned at 0.31.1 because 0.32.5 caused long agentic pi runs to wedge. The recorded
client-visible symptom was `Stream ended without finish_reason`; the recorded server-side
signature was `KV cache shifting is not supported for this context, disabling KV cache shifting`
on model load.

No release note after 0.31.1 mentions KV cache shifting. Searching on the **symptom** rather
than the diagnosis found two candidates, both after the pin:

- **0.32.6** (one week after the version that broke us) — "`/v1/chat/completions` streaming now
  matches OpenAI's wire format: `role` only on the first chunk, `finish_reason` on its own
  chunk, and usage in a separate chunk"
- **0.33.0** — "Fixed a hang where agent clients that cancel long prefills" and "Prefill restore
  points are now trustworthy by construction"

0.32.5 itself contained only an MLX Metal fix, so whatever broke arrived with its llama.cpp
bump. 0.33.2 carries both candidate fixes; testing once at the newest release rather than
bisecting.

**This is weak positive evidence, not a fix announcement.** Nobody upstream wrote "fixed the
thing that broke you."

## Two faults, kept apart

This upgrade tests **fault B only**. Fault A — pi never issuing the request, an inherited-stdin
bug entirely client-side — was closed the same week in `8eb6f67` and says nothing about the
server. Conflating them is what let fault A survive for weeks as a "context overflow".

## The signature that is NOT the fault

`mxbai-embed-large` emits `KV cache shifting is not supported` on every load: it is a
bidirectional encoder at `n_ctx 512` with `causal_attn = 0`, and cannot KV-shift by
construction. It did so **16 times in 7 days on the pinned 0.31.1**, where the coder was clean.

A naive `grep -c "KV cache shifting"` therefore reads as "already broken" on a perfectly healthy
server and would abort a good upgrade. **Scope every check to `n_ctx_seq = 32768`.**

## Baseline (pre-upgrade, 0.31.1)

```
ollama 0.31.1   /usr/local/bin/ollama   38,270,704 bytes   dated 2026-06-30
service active, pid 623069, running since 2026-08-01
resident: mxbai-embed-large only
journal mark: 2026-08-31 22:40:31
```

Rollback prepared **before** touching anything — `reference/bench-results/ollama-0332-upgrade/ROLLBACK.sh`. It uses
`doas env OLLAMA_VERSION=0.31.1`: plain `VAR=x doas` strips the environment and reinstalls
latest, which is how this pin was lost once before.

## Acceptance criteria — fixed before the long build

1. Zero `KV cache shifting` within any **32,768-context** load block.
2. A real long agentic doclink build completes with no coder timeout or wedge.
3. Terminal streaming semantics intact — `finish_reason`, usage chunk, `[DONE]` — observed on
   the wire, not inferred from process exit.
4. No server-side errors or non-200 responses across the build.

Rejection on any of these → immediate rollback.

## Results

**1. KV-shift — PASS.** 3 coder loads at `n_ctx 32768`, **0** occurrences in any load block.

**2. Wire format — changed as advertised, terminal semantics identical.**

| | chunks | `finish_reason:"stop"` | `[DONE]` | usage | role chunks |
|---|---|---|---|---|---|
| 0.31.1 | 34 | 1 | 1 | 1 | **32** |
| 0.33.2 | 34 | 1 | 1 | 1 | **1** |

0.32.6's change is real and visible. **pi tolerated it** across 10 agentic calls, so the
provider parses the new shape — now a dependency worth knowing if that extension is rewritten.

**3. Long agentic build — PASS.** doclink, `MAX_FIX_ROUNDS=8`, 1 write + 8 fix rounds:

```
coder calls (s): 85 (write), 9, 30, 35, 24, 29, 131, 10, 7, 22
10 calls, 0 timeouts, 0 wedges
RESULT: FAIL (best achieved: error score 1)
```

`FAIL` is **not** a rejection. doclink's measured local pass rate is 3/19 and error score 1 is
its normal outcome; the criteria were a wedge or a stream failure, and neither occurred. The
131s call matters most — that is the long-generation case that used to hang.

**4. Server side — PASS.** 95 requests, **95 × HTTP 200**, **95 × "all slots are idle"**,
0 KV-shift lines, 0 errors.

One `qwen tool call parsing failed` (WARN, XML syntax) appeared. **Pre-existing and less
frequent**: 225 in 14 days and 88 in the last 2 on 0.31.1, versus 1 since the upgrade. Not a
regression.

## Verdict — PASS, provisionally accepted

0.33.2 is accepted **for this workload**: qwen3-coder:30b at 32k via the nginx HTTPS proxy,
driven by pi's agentic loop.

**Residual limitation: n=1, on one fixture.** This clears the bar the pin was set at. It is not
proof the 0.32.5 regression is gone in general — only that it does not reproduce on our workload.
If a wedge reappears, ollama version returns to the suspect list, and `ROLLBACK.sh` is ready.

## Diagnosing the next wedge, before anyone reaches for a version pin

```bash
ssh larry "doas journalctl -u ollama --since '30 min ago' --no-pager | grep POST"
```

- **No POST after the ~200ms prewarm** → client-side. Suspect the stdin/event-loop wedge
  (fault A). Check `/proc/<pid>/fdinfo/<epfd>` for what the loop is waiting on.
- **POST arrives, then the stream fails or hangs** → server/model/streaming path, including an
  ollama regression (fault B). Then, and only then, is the version relevant.

## Evidence

`reference/bench-results/ollama-0332-upgrade/` — baseline, both stream captures, both journal slices, the build
log, and the rollback script.

# AL capability by failure class

Measured locally from build metrics. Rates below 8 runs are shown but never routed on.

| model | runs | observed | 1st-pass | final | fix rounds | tests | perf/run |
|---|---:|---:|---:|---:|---:|---:|---:|
| `ollama/qwen3-coder:30b` | 210 | 123 | 37% | 72% | 2.9 | not measured | 0.0 |
| `ollama/al-coder-qwen36` | 31 | 30 | 19% | 65% | 3.6 | not measured | 0.0 |
| `ollama/qwen3.8:27b` | 21 | 14 | 29% | 52% | 1.9 | not measured | — |
| `ollama/al-coder-qwen3` | 12 | 12 | 0% | 25% | 6.9 | not measured | — |
| `ollama/al-coder-qwen36:latest` | 1 | 1 | 0% | 0% | 8.0 | not measured | — |
| `ollama/hf.co/ProCreations/grug-27b-qat-q4-gguf:Q4_K_M` | 1 | 1 | 0% | 0% | 8.0 | not measured | — |

## Failure classes — % of OBSERVED runs affected

Denominator is runs that produced first-pass diagnostics, not all runs. Read with one caveat: a model that dies at syntax never reaches the point where an API can be hallucinated, so a low rate in a later class may mean it failed earlier rather than that it is good at that class. Check the first-pass and syntax columns before concluding anything.

| model | api hallucination | duplicate declaration | event hallucination | permission failure | syntax break | type misuse | ui failure |
|---|---|---|---|---|---|---|---|
| `ollama/qwen3-coder:30b` | 20% | 0% | 7% | 0% | 20% | 0% | 9% |
| `ollama/al-coder-qwen36` | 7% | 0% | 13% | 0% | 27% | 3% | 3% |
| `ollama/qwen3.8:27b` | 7% | 0% | 7% | 0% | 43% | 0% | 0% |
| `ollama/al-coder-qwen3` | 8% | 0% | 0% | 0% | 75% | 0% | 0% |
| `ollama/al-coder-qwen36:latest` | 100% | 0% | 0% | 0% | 0% | 0% | 0% |
| `ollama/hf.co/ProCreations/grug-27b-qat-q4-gguf:Q4_K_M` | 0% | 0% | 0% | 0% | 100% | 0% | 0% |

## Routing

**No routing is justified by the current evidence.** Every task kind below is either short of runs or too close to call. Route by cost and availability until the gaps are measured — a table built on this data would look like knowledge and be noise.

- **api** → no recommendation — NO CLEAR WINNER — ollama/qwen3.8:27b (4%) and ollama/al-coder-qwen3 (4%) are within 5 points on api_hallucination, type_misuse. Not a difference worth routing on.
- **events** → no recommendation — NO CLEAR WINNER — ollama/al-coder-qwen3 (4%) and ollama/qwen3.8:27b (7%) are within 5 points on event_hallucination, api_hallucination. Not a difference worth routing on.
- **greenfield** → no recommendation — NO CLEAR WINNER — ollama/qwen3-coder:30b (10%) and ollama/al-coder-qwen36 (14%) are within 5 points on syntax_break, duplicate_declaration. Not a difference worth routing on.
- **permissions** → no recommendation — NO CLEAR WINNER — ollama/al-coder-qwen3 (0%) and ollama/al-coder-qwen36 (0%) are within 5 points on permission_failure. Not a difference worth routing on.
- **ui** → no recommendation — NO CLEAR WINNER — ollama/qwen3-coder:30b (14%) and ollama/al-coder-qwen36 (15%) are within 5 points on ui_failure, syntax_break. Not a difference worth routing on.
- **upgrade** → no recommendation — NO CLEAR WINNER — ollama/al-coder-qwen3 (3%) and ollama/qwen3.8:27b (5%) are within 5 points on api_hallucination, event_hallucination, type_misuse. Not a difference worth routing on.

_Excluded from routing (8-run minimum): `ollama/al-coder-qwen36:latest`, `ollama/hf.co/ProCreations/grug-27b-qat-q4-gguf:Q4_K_M`._

_Exact per-diagnostic evidence on 27/276 runs; the remainder use the coarse first-pass classes recorded before diagnostic codes were kept._

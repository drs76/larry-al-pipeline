# Warplan — mid-tier-routing (cheap-cloud rung between Larry and Claude)

> A warplan is NOT a plan. It pre-simulates reality pushing back — action → reaction →
> counteraction — so the executor runs the risky 20% confidently. This mission is a **pipeline
> (Python) change** to `setup/pipeline/run-build*.py` + `egress_policy.py`, not an AL/Go/C# build,
> so the executor is a **Claude Code / operator editing session**, not a Larry AL build. The referee
> is `python3 -c "import ast"` + a **live routing/egress test harness** (Move 7), not a compiler.

## Mission brief

Today escalation is **binary**: pi/Larry (local, free) → Claude (Opus/subscription), a one-way latch
at `run-build.py:1845` when `fix_round >= ESCALATE_AFTER`. There is no cheap rung between. Goal: add a
**mid tier** — a cheap-but-capable cloud model reached **via OpenRouter** (one key, swap models) — that
closes *medium* stalls, reserving Opus for the hardcore. **Hard constraint:** the deny-by-default
egress gate must not weaken. Customer/work AL stays `local-only` (Larry only); the mid tier is available
**only** on the egress-allowed lane (Go/C#, personal AL, non-NDA). Two phases, decided at a fork:
**Phase 1** = self-controlled `CODER_BACKEND=mid` rung we own; **Phase 2 (gated)** = evaluate OmniRoute
as the mechanism only if Phase 1 proves the tier pays off.

**Load-bearing recon finding (the whole risk):** `egress_policy.allowed(target)` gates **only**
`"anthropic"` — for any other target it returns `(True, "")` unconditionally (`egress_policy.py`
`allowed()`, the `if target != "anthropic": return True` line). So a cloud mid-model call added naively
is **completely ungated** — it would send code to OpenRouter from a `local-only` customer repo with no
block. Closing this hole is Move 1 and is non-negotiable; nothing else ships until it holds.

## Executor + referee
- **Executor:** Claude Code (or the operator) editing `setup/pipeline/*.py`. Not Larry — this is Python
  plumbing, and the egress logic is exactly the "load-bearing 10%" a local model must not author.
- **Referee (ground truth):** `python3 -c "import ast; ast.parse(open(f).read())"` per file, **plus** the
  egress test harness in Move 7 (asserts a `local-only` repo BLOCKS the mid target). Green ast ≠ safe;
  the egress assertions are the real gate.
- **Tailored for:** a naive edit that adds the mid call but forgets to gate it (the default `allowed()`
  returns True for non-anthropic → silent customer-code egress). Every move re-checks the block.

## Moves (action → reaction → counteraction)

### Move 1 — Close the egress hole FIRST: gate a `cloud-mid` target + profile
- **Action:** in `egress_policy.py`: (a) add `"cloud-mid"` to `PROFILES`; (b) change `allowed()` so a new
  target `"openrouter"` (the mid tier) is **denied by default** and permitted **only** under profiles
  `personal` or `cloud-mid` — i.e. remove the blanket `target != "anthropic" → True` for this target.
  Keep `anthropic` semantics exactly as-is. Add `mid_available()` mirroring `escalation_available()`
  (a `cloud-mid`/`personal` repo can reach the mid tier; `local-only`/`enterprise-anon` cannot).
- **Expected (success):** `resolve()` accepts `cloud-mid`; `allowed("openrouter")` returns `(False, …)`
  under `local-only`/`enterprise-anon`, `(True,"")` under `personal`/`cloud-mid`. `allowed("anthropic")`
  unchanged (regression-tested in Move 7).
- **Expected (failure):** `allowed("openrouter")` returns True under `local-only` → the hole is still open.
- **Most-likely failure + cause:** the executor keeps the early `if target != "anthropic": return True`
  fast-path, so `"openrouter"` slips through it before the new profile check.
- **Counter-move:** invert the structure — resolve the *per-target* allow-set from the profile, not a
  target-specific early return. `local-only → {}`; `enterprise-anon → {anthropic-via-anon}`;
  `personal → {anthropic, openrouter}`; `cloud-mid → {openrouter}` (NOT anthropic — a cloud-mid repo gets
  the cheap tier but NOT raw Opus unless it also opts into personal/enterprise-anon).
- **Fork:** if downstream code calls `allowed()` with no arg (defaults `"anthropic"`) anywhere → audit
  every call site (`grep -n "allowed(" run-build*.py coms_review.py`) so the default path is untouched;
  else → proceed.

### Move 2 — Add `run_mid()` + a mid entry in the coder dispatch
- **Action:** in each `run-build*.py`: add `run_mid(prompt, label="Mid", …)` that funnels through
  `egress_policy.allowed("openrouter")` (hard-error/skip if denied, exactly like `run_claude_code`
  funnels `allowed("anthropic")`), then calls the mid model. Extend `run_coder()` (`run-build.py:482`)
  so `_coder_state["backend"] == "mid"` dispatches to `run_mid`.
- **Expected (success):** with a `cloud-mid` repo + key set, `run_coder` can route a round to the mid model
  and get source back; with `local-only`, `run_mid` refuses before any network call.
- **Expected (failure):** mid call fires the network before the gate (egress leak), or `run_coder` has no
  branch for `"mid"` and silently falls through to pi.
- **Most-likely failure + cause:** the gate is checked in `main()` arming but NOT inside `run_mid` itself,
  so a direct/review-fix path reaches the model ungated (the same reason `run_claude_code` gates *per call*,
  not just at startup).
- **Counter-move:** gate **inside** `run_mid` on every invocation, return `""` (treated as a no-op round)
  on denial — mirror `run_claude_code`'s per-call `allowed()` check exactly.
- **Fork:** mid transport = OpenRouter via a **pi provider extension** (reuse pi's tool loop with
  `model=openrouter/…`, base_url + key) → Move 5 route A; else a **direct OpenAI-compatible HTTP call** in
  `run_mid` (no pi) → route B. Prefer A (reuses the write/edit tool loop the pipeline already trusts).

### Move 3 — Two-stage escalation ladder: pi → mid → claude
- **Action:** add `ESCALATE_MID_AFTER=M` alongside `ESCALATE_AFTER=N` (`run-build.py:227`). Latch order in
  the fix loop (near `:1845`): pi does rounds `0..M-1`; at `M` latch `_coder_state["backend"]="mid"`; at
  `N` (N>M) latch to `"claude"`. Both latches one-way. Unset `ESCALATE_MID_AFTER` → no mid rung (today's
  binary behaviour, unchanged).
- **Expected (success):** banner prints a 3-rung ladder when armed; each round labels the fixer
  (`Larry (Pi)` / `Mid (OpenRouter)` / `Claude`); mid rounds only fire when `mid_available()` is true.
- **Expected (failure):** the mid latch fires under `local-only` (should be disarmed like the Claude latch
  at `:1654`), or `N<=M` inverts the ladder.
- **Most-likely failure + cause:** arming logic copies the Claude arming (`escalation_available()`) but
  forgets a parallel `mid_available()` disarm, so a `local-only` repo latches to mid and leaks.
- **Counter-move:** at startup (near `:1649`) resolve BOTH gates: disarm `ESCALATE_MID_AFTER` if
  `mid_available()` is false, disarm `ESCALATE_AFTER` if `escalation_available()` is false. Assert `M<N`
  or drop the mid rung with a warning.
- **Fork:** if `mid_available()` but NOT `escalation_available()` (a `cloud-mid` repo with no Claude) →
  ladder is pi → mid → **STOP/FAIL** (never Claude); else full pi → mid → claude.

### Move 4 — Restrict the lane: AL customer path stays local
- **Action:** confirm the mid rung is wired identically in `run-build-go.py` and `run-build-cs.py` (the
  intended lane) and that `run-build.py` (AL) inherits it but is **governed by the repo policy** — a
  customer AL repo has no `.anon/config.yml` → resolves `local-only` → mid disarmed. No AL-specific code
  needed; the policy does the gating.
- **Expected (success):** a Go/C# prototype under a `cloud-mid` repo uses the mid rung; a customer AL
  folder (`local-only`) never does, even with `ESCALATE_MID_AFTER` set in the env.
- **Expected (failure):** an env-level `ESCALATE_MID_AFTER` overrides a `local-only` repo (env beats repo).
- **Most-likely failure + cause:** resolution precedence — `resolve()` already puts repo `.anon/config.yml`
  **above** env `EGRESS_POLICY`, but the *arming* reads `ESCALATE_MID_AFTER` from env directly; the gate
  must still be `mid_available()` (policy-resolved), not the env var.
- **Counter-move:** the env var only sets the *round number*; whether the latch is allowed is always
  `mid_available()`. Test: `EGRESS_POLICY=` unset + customer repo + `ESCALATE_MID_AFTER=2` → mid disarmed.

### Move 5 — OpenRouter pi provider + credentials
- **Action:** add an OpenRouter provider entry to `~/.pi/ollama-provider.ts` (or a sibling
  `openrouter-provider.ts`): OpenAI-compatible `baseURL=https://openrouter.ai/api/v1`, key from
  `OPENROUTER_API_KEY`, model id `openrouter/<vendor>/<model>` selectable via `MID_MODEL`. `run_mid`
  passes `-e <provider>` + `--model $MID_MODEL`.
- **Expected (success):** `pi -e openrouter-provider.ts --model openrouter/… -p "ping"` returns a reply.
- **Expected (failure):** 401 (no/invalid key), or the provider isn't `reasoning`-aware for a CoT model.
- **Most-likely failure + cause:** key not present (see ledger) or pi 0.81 provider migration
  (`createProvider(openAICompletionsApi())`) not applied to the new provider → tool calls leak as text
  (the known pi-0.81 regression).
- **Counter-move:** build the provider with the migrated `createProvider(openAICompletionsApi())` shape
  from day one; smoke-test tool-calling (not just chat) before wiring into the loop.
- **Fork:** provider tool-calling broken → fall back to Move 2 route B (direct HTTP, no pi tool loop, mid
  does whole-file rewrites only); else use the pi tool loop.

### Move 6 — Metrics: prove the tier pays off (the Phase-1/Phase-2 fork gate)
- **Action:** extend the existing per-build metrics (the leaderboard feed) to record, per run: which rungs
  fired (pi/mid/claude round counts), pass/fail, and a cost proxy (Claude rounds avoided). Run the standard
  suite (P1/P4/map for AL is out-of-lane; use the Go/C# fixtures) with and without the mid rung.
- **Expected (success):** mid closes a measurable share of builds that previously needed Claude, at equal
  or near-equal pass rate → the tier pays off.
- **Expected (failure):** mid rounds don't converge (add rounds, then Claude still closes) → net *slower*
  and no spend saved.
- **Most-likely failure + cause:** the mid model is capable but the *handover/referee loop* doesn't suit it
  (chatty drift, partial writes) — same class as [GOW SE-1/SE-2](../../GOW.md).
- **Counter-move:** tune `MID_MODEL` (OpenRouter lets you swap with no code change) before concluding the
  tier is worthless; only after 2–3 models fail declare Phase-1 a no-go.
- **Fork (THE decision):** Phase-1 self-rung saves ≥ a set threshold of Claude rounds at ≥ baseline pass
  rate → **Phase 2:** evaluate OmniRoute as the mechanism (breadth + quota-fallback + compression) against
  the same metrics; else → **stop**, keep the binary ladder, delete the mid rung behind its env flag.

### Move 7 — Egress regression harness (the referee for this warplan)
- **Action:** a `test_egress_midtier.py` asserting: `local-only` → `allowed("openrouter")` False AND
  `allowed("anthropic")` False; `enterprise-anon` → openrouter False, anthropic only via `CLAUDE_ANON`;
  `personal` → both True; `cloud-mid` → openrouter True, anthropic False. Run it in CI/pre-commit and as
  the definition-of-done gate.
- **Expected (success):** all assertions green; the customer-code path (`local-only`) blocks the mid target.
- **Most-likely failure + cause:** a profile added to `PROFILES` but not handled in `allowed()` → falls to
  the deny default, or worse, a permissive default.
- **Counter-move:** table-drive `allowed()` from an explicit `{profile: {allowed targets}}` map so an
  unlisted profile is empty-set (deny-all), never permissive.

## Second/third-order consequences
- **The `allowed()` default flips meaning.** Today non-anthropic targets are implicitly allowed; after
  Move 1 they're implicitly denied. **Audit every existing `allowed()` call** — if anything else relies on
  the permissive default (e.g. a symbol download check), it will start blocking. (grep shows only anthropic
  today, but confirm.)
- **`cloud-mid` is a NEW trust boundary.** A repo marked `cloud-mid` sends source to OpenRouter's chosen
  upstream vendor — that vendor's data policy now matters. Document that `cloud-mid` ≠ private; it's for
  non-NDA code only, same spirit as `personal`.
- **Mid rung changes the leaderboard shape.** "autonomous_pass" (no Claude) currently means free; a mid
  round is cloud-billed but not Claude. Metrics need a third state (`mid_closed`) or the "free" stat lies.
- **Two API-cost surfaces now.** Claude quota AND OpenRouter spend. A runaway mid loop (many rounds ×
  cheap) can still add up — cap mid rounds (`N-M`) tightly.

## Assumptions the recon could NOT resolve → ledger
See `ledger.md`. Headlines: **no OpenRouter key/budget yet** (blocker), the exact `MID_MODEL`, the
round-split `M<N` defaults, and the profile name (`cloud-mid` proposed).

## Abort conditions
- **Hard blocker:** no OpenRouter key/credit at build time → Phase 1 cannot run; STOP, ledger it, do not
  fake a mid call.
- **Egress assertion red (Move 7):** if `allowed("openrouter")` is ever True under `local-only`, STOP the
  whole mission — the constraint is violated; nothing ships until it's green.
- **Ladder inversion / disarm miss:** mid latch fires under `local-only` in any test → STOP, fix arming.
- **No convergence after 2–3 `MID_MODEL`s:** declare Phase-1 a no-go at the Move 6 fork; do not proceed to
  OmniRoute.

## Success criteria (→ success.md)
See `success.md` — egress-first, then the spend/pass-rate payoff gate.

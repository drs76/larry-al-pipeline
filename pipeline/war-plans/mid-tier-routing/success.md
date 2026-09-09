# success.md — mid-tier-routing

Definition of done. **Egress gates are hard gates** — any red here fails the whole mission, regardless
of feature completeness.

## Must pass (blocking — the hard constraint)
1. **`test_egress_midtier.py` green** (Move 7), asserting the full profile × target matrix:
   | profile | `allowed("anthropic")` | `allowed("openrouter")` |
   |---|---|---|
   | local-only | ❌ | ❌ |
   | enterprise-anon | only if `CLAUDE_ANON=1` | ❌ |
   | personal | ✅ | ✅ |
   | cloud-mid | ❌ | ✅ |
2. **Customer-code path proven blocked:** a folder with no `.anon/config.yml` (resolves `local-only`),
   with `ESCALATE_MID_AFTER=2` set in the env, **never** latches to mid — `mid_available()` is false and
   the arming disarms it (Move 3/4).
3. **`allowed("anthropic")` behaviour byte-for-byte unchanged** vs pre-change (existing escalation/review
   still gated identically) — regression asserted.
4. **`run_mid` gates per call**, not just at startup: a direct call under `local-only` returns no-op with
   no network I/O.
5. All three orchestrators (`run-build.py`, `run-build-go.py`, `run-build-cs.py`) and `coms_review.py`
   parse (`ast`) and their `allowed()` call sites audited.

## Must pass (functional)
6. With a `cloud-mid` repo + valid `OPENROUTER_API_KEY` + `MID_MODEL`, a Go or C# build routes a fix round
   through the mid model and receives usable source (pi tool loop or HTTP fallback).
7. Ladder ordering enforced: `ESCALATE_MID_AFTER=M`, `ESCALATE_AFTER=N`, `M<N` → pi rounds `0..M-1`, mid
   `M..N-1`, Claude `N+`. `M>=N` or unset mid → clean fallback (warn / binary behaviour), no crash.
8. Banner + per-round labels show which rung ran; metrics record `mid_closed` as a distinct state from
   `autonomous_pass` (free) and `claude_escalated`.

## Payoff gate (the Phase-1 → Phase-2 fork)
9. On the Go/C# fixture suite, the mid rung **closes ≥ 30% of builds that previously required Claude**
   (PAYOFF_THRESHOLD), at **≥ baseline pass rate** (no regression). Met → Phase-2 OmniRoute
   evaluation is warranted. Not met after 2–3 `MID_MODEL`s → Phase-1 no-go, remove the rung behind its flag.

## Explicitly out of scope (this warplan)
- OmniRoute stand-up/config (Phase 2 only, gated by criterion 9).
- Any change to the AL customer path beyond confirming it stays `local-only`.
- Token-compression (RTK/Caveman) — an OmniRoute feature, evaluated in Phase 2 if reached.

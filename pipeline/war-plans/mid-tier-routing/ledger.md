# ledger.md — mid-tier-routing (RESOLVED)

Recon assumptions, now resolved to build-ready values. One credential blocker remains (a secret, kept
out of this tracked file). Design decisions from the recon interview are recorded at the bottom.

## Blocker (credential — resolve before Phase 1 makes a real mid call)
- **OPENROUTER_API_KEY** — NOT set yet. Get it at <https://openrouter.ai/keys>, add credit +
  a per-key spend cap at <https://openrouter.ai/credits>. Store in `~/.config/zsh/local.zsh`
  (gitignored) — never in this file or any tracked dotfile. Until it exists, keep the rung code but
  leave `ESCALATE_MID_AFTER` unset so the ladder stays binary (pi → claude).
- **Spend cap** — set the per-key limit on OpenRouter = the mid-tier budget. Mid round budget is
  `N-M` = 2 rounds (see ROUND_SPLIT), so exposure is bounded per build.

## Resolved design values
- **MID_MODEL** = `deepseek/deepseek-chat` (DeepSeek-V3) primary. A/B alternates (swap via env, no code
  change): `moonshotai/kimi-k2`, `z-ai/glm-4.6`.
- **PROFILE_NAME** = `cloud-mid` — new profile added to `PROFILES` and the `allowed()` target map.
- **MID_TARGET_NAME** = `openrouter` — the `allowed()` target string the mid tier funnels through.
- **ROUND_SPLIT** = `ESCALATE_MID_AFTER=2`, `ESCALATE_AFTER=4` → pi rounds 0–1, mid rounds 2–3,
  Claude rounds 4+. Constraint M<N holds (2<4). Mid budget = 2 rounds (spend guard).
- **PAYOFF_THRESHOLD** = 30% of previously-Claude builds closed by the mid rung, at >= baseline pass
  rate → warrants the Phase-2 OmniRoute evaluation (success.md #9).
- **MID_TRANSPORT** = pi provider extension (route A — reuses pi's write/edit tool loop). Fall back to
  direct OpenAI-compatible HTTP (route B) only if pi-0.81 tool-calling breaks on the new provider.

## Scope note
- **AL customer lane unchanged.** A customer AL repo resolves `local-only`; the mid rung is gated off by
  policy, no AL-specific code. Mid tier targets the Go/C# (+ personal AL) lane only.

## Confirmed in recon interview (2026-07-31)
- Mechanism: **warplan both** — Phase-1 self-controlled `CODER_BACKEND=mid` rung, Phase-2 OmniRoute at a
  gated fork (Move 6).
- Mid model access: **via OpenRouter** (one key, swap models).
- Egress enforcement: **new policy tier in `egress_policy.py`** (`cloud-mid`), NOT reuse of `personal`,
  NOT a bare env flag.
- Credentials: **not ready** → the one blocker above.

## Go / no-go
All design values resolved. **Go for implementation** (Moves 1→7) with `ESCALATE_MID_AFTER` unset until
the key lands; Move 1 (egress gate) + Move 7 (regression harness) need no key and should ship first.

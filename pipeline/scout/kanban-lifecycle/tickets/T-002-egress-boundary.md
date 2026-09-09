# T-002 — Egress boundary policy
type:   grilling
status: closed
claim:  operator + Claude (grilling, 2026-08-02)
blocked-by: []

## Question
The exact rule for what may reach GitHub. Which prototypes NEVER touch github (all `local-only`? a
per-project opt-in?); does `promote` consult `egress_policy.allowed("github")` (a new gated target) so
customer work stays on the local board only; what happens to a `local-only` project at promote time
(local board only, no repo/mirror). Settles the whole cloud/local seam. Independent root — a policy call,
not engine-dependent.

## Resolution
**Deny-by-default, policy-gated, best-effort.** Four calls:

1. **Opt-in (deny-by-default).** A prototype is **local-board-only** unless it explicitly permits github —
   no accidental customer egress. The opt-in *is* the egress policy (below), not a second flag.
2. **New `github` egress target.** Add `allowed("github")` to `setup/pipeline/egress_policy.py` alongside
   `anthropic`/`openrouter`, deny-by-default, table-driven. Profile map: `local-only`→❌, `enterprise-anon`→❌
   (Anthropic-only via the anon hook; github is a different vendor), `personal`→✅. (`cloud-mid` = mid-model
   only, no github unless a repo also opts into a github-allowing profile.) Extend `test_egress_midtier.py`
   (or a sibling) with the github column. `promote` consults `allowed("github")` before any `gh` call.
3. **Local promote = log-skip, never fail.** Promoting a `local-only` prototype **succeeds**, stays on the
   nomad board, creates **NO** repo/mirror, and prints why (github egress blocked). Reconcilable later if
   the repo is ever wanted. A blocked gate NEVER fails the promote (ties into T-009's best-effort rule).
4. **Board reach = LAN + WireGuard only.** The nomad Kanboard binds LAN, reachable off-site only via the
   existing WG tunnel (navidrome/searxng pattern) — never publicly exposed.

**Unblocks:** T-004 (mirror — now has both T-001+T-002). Feeds T-009 (hook failure model) + T-010
(automation gates on `allowed("github")`). Sets the T-004/T-006 rule: github artefacts (repo, Project,
commit links) exist ONLY for github-permitted prototypes; everything else lives only on the local board.

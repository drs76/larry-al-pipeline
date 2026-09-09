# T-009 — new/promote hook UX + failure model
type:   grilling
status: closed
claim:  operator + Claude (grilling, 2026-08-02)
blocked-by: [T-003, T-002]

## Question
How do the hooks behave? Does `alw/gow/csw new` auto-create the board project (default-on, or an opt-in
flag / env like the mid-tier `ESCALATE_*`)? Idempotency (re-running `new`, or `promote` twice). **Hard
rule: a board/API/github outage must NOT fail a build or a promote** — best-effort, log-and-continue,
reconcilable later. What's the reconcile path if the board was down at `new`? Depends on topology (T-003)
+ egress policy (T-002).

## Resolution
**Default-on with an escape hatch, best-effort, reconcilable, idempotent.**

1. **Default-on; `BOARD=0` to disable.** `new`/`promote` wire the board automatically (it's the PM spine);
   `BOARD=0 alw new x` skips for a throwaway — mirrors the `LINT=0` / `ESCALATE_*` env pattern.
2. **Best-effort — a board/gh outage NEVER fails the build or promote.** On any board/github/API error: log
   a warning, carry on, mark the prototype as needing reconcile. The pipeline's contract is code, not the
   board. (The hard rule already implied by T-002 log-skip + T-006 hook best-effort.)
3. **Reconcile via `board sync <proto>`** — idempotent: create any missing project/columns/cards, attach
   unlinked commits (scan `Ticket:` trailers since the last link), move the overview card to the current
   stage, refresh doc/commit external links. Safe to re-run anytime; the backfill path when the board was down.
4. **Idempotent hooks.** `new` on an existing board project **adopts** it (no duplicate); `promote` **skips**
   repo/project creation if they already exist and just updates links + moves the overview card. Re-runs and
   `board sync` are always safe.

**State model:** the overview card's column IS the prototype's lifecycle state; `new`→Planning,
`build`→Building/Review, `promote`→Promoted. A local marker (e.g. `<proto>/.board`) records the Kanboard
project id + last-linked sha so `sync` knows what's already wired without querying blindly.

**Unblocks:** T-010 (automation home — now knows the surface: create/adopt project+columns+cards, a `board`
CLI with `rfc`/`sync` verbs, a post-commit hook installer, all best-effort + `BOARD=0`-gated).

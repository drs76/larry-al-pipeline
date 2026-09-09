# T-010 — Where the automation lives
type:   grilling
status: closed
claim:  Claude (converged from the resolved map, 2026-08-02)
blocked-by: [T-001, T-009]

## Question
Where does the board-wiring code live? A new **`board` CLI + shared lib** the three `*w` scripts call
(one implementation, testable) vs **inline** in each script (simpler, triplicated) vs a **Larry-dashboard
tab/endpoint** (central, but couples to the dashboard). Given `alw/gow/csw` are bash and the mid-tier/egress
logic is Python, likely a small Python `board.py` beside `egress_policy.py`, shelled from the `*w` scripts.
Depends on engine API (T-001) + hook UX (T-009).

## Resolution
**A Python `board.py` + `board` CLI beside `egress_policy.py`, shelled from the bash `*w` scripts.**

The rest of the map converged on this: the logic (Kanboard JSON-RPC + `gh` orchestration + link rewriting +
egress gating) is far cleaner in Python than bash, the egress/mid-tier code is already Python, and the three
`*w` scripts must share ONE implementation.

- **`setup/pipeline/board.py`** — library + CLI, next to `egress_policy.py` (imports it for `allowed("github")`).
  Verbs:
  - `board project <proto>` — create/adopt the Kanboard board + columns + doc cards + overview card (called by `new`).
  - `board rfc <proto> "<desc>"` — mint an RFC card, print its `T-NNN` id (T-006).
  - `board link <proto> <sha>` — attach a commit external link (called by the post-commit hook, T-006).
  - `board promote <proto>` — `gh repo create`/`project create`/`link`, rewrite doc+commit links to github URLs, move overview card to Promoted (called by `promote`, egress-gated).
  - `board sync <proto>` — idempotent reconcile (T-009).
  - `board install-hook <proto>` — drop the post-commit hook into `.git/hooks`.
- **Bash `*w` scripts:** `cmd_new` → `BOARD=0 || board project … && board install-hook …`; `cmd_promote`
  → `board promote …`. All **best-effort** (a non-zero board exit logs a warning, never fails the build).
- **NOT a Larry-dashboard tab** now — keep the board decoupled; a read-only board embed in the dashboard is
  possible later (parked in the map's Fog, not scoped here).

**Closes the map.** Every decision settled; the implementation surface is a single `board.py` + a git hook +
thin hook-ins to `tooling/{alw,gow,csw}` + a Kanboard container on nomad + `egress_policy` github target.

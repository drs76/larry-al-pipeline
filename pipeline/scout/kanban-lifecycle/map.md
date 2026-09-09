# Wayfinder/Scout map — Kanban lifecycle board

## Destination
Creating a new prototype spins up a **Project on a Kanban board** with its warplan/handover/spec docs
linked; each **request-for-change** becomes a **ticket linked to a github commit**; the **github repo is
linked to the project** — wired **on promote**. Board is the project-management spine of the
prototype→build→promote lifecycle.

## Notes
- **Pinned (operator):** engine = **hybrid** — local self-hosted board on **nomad** = source of truth for
  ALL prototypes (customer-safe); on **promote** of non-customer work also create the github repo + mirror
  to a GitHub Project for native issue↔commit links. Egress = **gated** (customer/`local-only` stays local;
  github fires on promote only when `egress_policy` permits). Approach = **scout first**.
- **Hooks:** `cmd_new` + `cmd_promote` in `setup/tooling/{alw,gow,csw}` (alw promote is bare `mv`, `tooling/alw:200`).
- **`gh`** 2.46.0, authed `drs76`, scopes `repo/workflow/read:org/gist` — **missing `project`**; needs
  `gh auth refresh -s project` before any GitHub Projects v2 work.
- **nomad** = docker-compose (`/opt/nomad/docker-compose.yml`, ssh root@nomad) — add a kanban container here.
- **`egress_policy.py`** already gates targets (`anthropic`, `openrouter`); a `github` target slots in.
- Secrets pattern: local `/opt` on the run-host, chmod 600, never NFS (bclinux/openrouter precedent).

## Decisions so far
- **[T-001] Engine = Kanboard** (php+sqlite, one container on nomad). JSON-RPC API maps 1:1 to
  project→columns→tasks; picked for first-class **external task links** (doc + commit URLs) + **task
  links** (RFC↔ticket) — exactly T-005/06/07. Vikunja = fallback. → `tickets/T-001-engine-choice.md`
- **[T-002] Egress = deny-by-default, policy-gated.** New `github` target in `egress_policy` (personal→ok,
  local-only/enterprise-anon→blocked); prototypes are local-board-only unless the policy permits github;
  local-only promote = **log-skip, never fail** (no repo/mirror); board = LAN+WireGuard only.
  → `tickets/T-002-egress-boundary.md`
- **[T-004] Mirror = one-way, promote-time, no sync.** On promote (github-permitted): `gh repo create
  --source --push` + `gh project create` + `gh project link` (repo↔project); write repo/project URLs back
  onto the Kanboard card. RFC=github issue, commit `#N`=native link. Kanboard = local truth, github =
  mirror for commit links. Prereq `gh auth refresh -s project`. → `tickets/T-004-github-mirror-model.md`
- **[T-003] Topology = board-per-prototype + overview board.** Each prototype = its own Kanboard Project;
  columns `Backlog·Planning·Building·Review·Promoted·Done`; `new` seeds a doc card per planning artefact
  (in Planning); a top-level "Prototypes" board holds one card per prototype (column=lifecycle stage,
  links to its board). → `tickets/T-003-board-topology.md`
- **[T-005] Schema = Doc + RFC cards, native external links, colour+egress tag.** Build results = comments
  on the RFC (not cards). Links via Kanboard external-links (doc/commit/issue URLs, queryable). Colour by
  type + `🔒 local-only`/`☁ github` tag. RFC identity = Kanboard task id; commit URL = external link
  (local sha pre-promote → github URL post). → `tickets/T-005-ticket-schema.md`
- **[T-006] RFC↔commit = `Ticket: T-NNN` trailer + post-commit hook + sha-now/rewrite-on-promote.**
  `board rfc` mints the card+id; a repo-local post-commit hook (installed by `new`) parses the trailer →
  `board` CLI attaches the commit as an external link (local sha → github commit URL on promote); github
  `#N` is the post-promote projection. Best-effort, reconcilable. → `tickets/T-006-rfc-ticket-commit.md`
- **[T-009] Hooks = default-on (`BOARD=0` off), best-effort, reconcilable, idempotent.** Board/gh outage
  NEVER fails build/promote (log+continue). `board sync <proto>` backfills (idempotent). `new` adopts an
  existing project; `promote` skips existing repo/project. Overview-card column = lifecycle state; a
  `<proto>/.board` marker tracks project id + last sha. → `tickets/T-009-hook-ux-failure.md`
- **[T-007] Doc-linking = repo-relative path → github blob URL on promote.** Doc cards carry an external
  link = repo-relative path (local fs pre-promote); promote/`sync` rewrites to
  `github.com/drs76/<repo>/blob/<branch>/<path>`. Local-only keeps the path. Same rewrite step as commit
  shas. → `tickets/T-007-doc-linking.md`
- **[T-008] Auth/secrets = `~/.config/board/env` (KANBOARD_URL+TOKEN), chmod 600, never NFS.** `board.py`
  runs on the dev box → nomad Kanboard over LAN/WG; JSON-RPC Basic `jsonrpc:<token>`. gh already authed
  (drs76) + one-time `gh auth refresh -s project`. Provisioning = build-time task. → `tickets/T-008-auth-secrets.md`
- **[T-010] Automation home = `setup/pipeline/board.py` + `board` CLI beside egress_policy.py**, shelled
  from the bash `*w` scripts (verbs: project/rfc/link/promote/sync/install-hook); best-effort, BOARD=0-gated.
  NOT a dashboard tab. → `tickets/T-010-automation-home.md`

## Not yet specified  (fog)
- Historical/audit view (who moved what, when) — depends on engine (T-001).
- Multi-machine access to the board (WG roaming) — after T-001/T-009.
- Whether the Larry dashboard gets a read-only board embed vs the board's own UI — after T-010.
- Backfill: do existing promoted projects get retro-boards, or new-only? — after T-003.

## Out of scope  (never graduates unless the destination is redrawn)
- A cloud-only board (breaks no-egress for customer prototypes).
- Any customer/NDA prototype intent or docs reaching GitHub.
- Replacing the Larry maintenance dashboard.
- General issue-tracking beyond the prototype lifecycle.

## Frontier (open · unblocked · unclaimed)
**EMPTY — MAP CLEARED 2026-08-02.** All 10 decisions closed. Fog gone. Destination is buildable.

**→ Graduate to `/warplan`.** The settled design: a Kanboard container on nomad; `setup/pipeline/board.py`
+ `board` CLI (project/rfc/link/promote/sync/install-hook) beside `egress_policy.py`; a new `github` egress
target + test-harness column; a git post-commit hook; best-effort `BOARD=0`-gated hook-ins to
`cmd_new`/`cmd_promote` in `tooling/{alw,gow,csw}`; board-per-prototype (columns Backlog·Planning·Building·
Review·Promoted·Done) + a "Prototypes" overview board; local-first, github mirror on promote when permitted.
**Risky 20% (for the warplan):** the promote-time github+egress+link-rewrite dance, and idempotent reconcile.
Build-time prereqs: stand up Kanboard on nomad, create its API token, write `~/.config/board/env`,
`gh auth refresh -s project`.

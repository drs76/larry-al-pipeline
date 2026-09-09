# Warplan — Kanban lifecycle board

> Fight the build move-by-move (action → reaction → counteraction) so the executor runs the risky 20%
> confidently. Design is already settled by the cleared scout map
> (`setup/pipeline/scout/kanban-lifecycle/`, 10/10 closed) — this warplan is about **execution risk**, not
> design unknowns. The risky 20% = the **promote-time github + egress + link-rewrite dance** and
> **idempotent reconcile**.

## Mission brief
Build: a **Kanboard** container on **nomad**; **`setup/pipeline/board.py`** + a `board` CLI
(`project`/`rfc`/`link`/`promote`/`sync`/`install-hook`) beside `egress_policy.py`; a new **`github` egress
target** (deny-by-default) with the test harness extended; a **git post-commit hook** + best-effort,
`BOARD=0`-gated hook-ins to `cmd_new`/`cmd_promote` in `tooling/{alw,gow,csw}`; **board-per-prototype**
(columns Backlog·Planning·Building·Review·Promoted·Done) + a **"Prototypes" overview** board; **local-first**
with a **one-way github mirror on promote** (`gh repo create` + `project create` + `link`) **only when
egress permits**; commit/doc **external links** that rewrite local→github URL on promote.

## Executor + referee
- **Executor:** Claude Code / operator editing `setup/pipeline/*.py` + `tooling/{alw,gow,csw}` (bash) + a
  nomad `docker-compose.yml` addition. NOT Larry — the egress gate + partial-failure orchestration is the
  load-bearing 10%.
- **Referee (ground truth):** `python3 -m py_compile` + **the egress harness (extended with a `github`
  column)** + `board.py` **dry-run/mock mode** (no live Kanboard) + **live smoke** (a real `board project`
  against nomad Kanboard, a throwaway personal repo for `board promote`). Green Python ≠ safe; the egress
  assertions + the local-only-never-touches-github assertion are the real gate.
- **Tailored for:** the failure class here is **many-step promote with partial-failure states** and
  **accidental customer egress**. Every move's counter is **idempotency + reconcile + gate-before-call**.

## Moves (action → reaction → counteraction)

### Move 1 — Egress `github` target FIRST (before any `gh` code exists)
- **Action:** extend `setup/pipeline/egress_policy.py`: add `"github"` to the `_ALLOW` map (`personal` →
  yes; `local-only`/`enterprise-anon`/`cloud-mid` → no), deny-by-default. Extend `test_egress_midtier.py`
  (or a sibling) with a `github` column across all profiles + a `github_available()` mirror of `mid_available()`.
- **Expected (success):** harness green; `allowed("github")` False under `local-only`/`enterprise-anon`,
  True under `personal`. `anthropic`/`openrouter` unchanged.
- **Expected (failure):** `allowed("github")` True under `local-only`.
- **Most-likely failure + cause:** the table-driven `allowed()` already denies unlisted targets by default
  (post-mid-tier), so the risk is only *adding github to too many profiles*. Double-check `cloud-mid` does
  NOT get github.
- **Counter-move:** github ∈ `personal` only (for now); a github-permitting work profile is a later, separate
  decision. Harness asserts the whole matrix.
- **Fork:** if a future repo needs github under a non-personal policy → add a dedicated profile, never widen
  `local-only`.
- **Why first:** nothing else ships until `local-only` provably blocks github. This is the mission's hard constraint.

### Move 2 — Kanboard on nomad
- **Action:** add a `kanboard` service to `/opt/nomad/docker-compose.yml` (`kanboard/kanboard`, a named
  volume for `/var/www/app/data` (SQLite) + `/var/www/app/plugins`, publish a chosen LAN port). `docker
  compose up -d kanboard`. Then in the UI: enable the **JSON-RPC API** + capture the API token.
- **Expected (success):** `curl -u jsonrpc:<token> http://nomad:<port>/jsonrpc.php -d '{"jsonrpc":"2.0",
  "method":"getVersion","id":1}'` returns a version.
- **Expected (failure):** 404/`/jsonrpc.php` missing, or 401.
- **Most-likely failure + cause:** Kanboard's API is **off by default** and/or the token is the *personal*
  vs *application* token — auth is HTTP Basic `jsonrpc:<APPLICATION-token>` (user `jsonrpc` literally) for
  app-scope, or `<username>:<personal-token>` for user-scope. Getting the pair wrong → 401.
- **Counter-move:** enable API in Settings → API; use the **application** token with basic user `jsonrpc`;
  verify with `getVersion` before writing any board code.
- **Fork:** app-token works → use it (full API); if only user-token available → user procedures only, adjust
  `board.py` auth accordingly.

### Move 3 — `board.py` skeleton + JSON-RPC client + `board project` (create/adopt)
- **Action:** `board.py` beside `egress_policy.py`: a thin JSON-RPC client (endpoint+token from
  `~/.config/board/env`), plus `board project <proto>` = create-or-**adopt** the prototype's board, set the
  6 columns, seed a doc card per existing artefact, add/update its card on the "Prototypes" overview board.
  Persist `{project_id, last_sha}` to `<proto>/.board`.
- **Expected (success):** first run creates board+columns+doc cards + overview card; re-run **adopts**
  (no dupes), reads `.board`.
- **Expected (failure):** duplicate boards/columns on re-run; `createProject` id not captured.
- **Most-likely failure + cause:** Kanboard seeds **default columns** on `createProject`; blindly
  `createColumn`-ing the 6 yields 4 defaults + 6 = 10 columns.
- **Counter-move:** after create, `getColumns` → reconcile: rename/remove defaults to the target 6
  (or `changeColumns`/`removeColumn`), idempotently. Guard all creates behind an existence check + `.board`.
- **Fork:** `.board` exists + project resolves → adopt; `.board` missing but a same-named board exists →
  adopt it and write `.board` (recovery); neither → create.

### Move 4 — `board rfc`, `board link`, post-commit hook
- **Action:** `board rfc <proto> "<desc>"` → create an RFC card, print `T-<id>`. `board link <proto> <sha>`
  → attach the commit as an external link on the card named by the commit's `Ticket:` trailer.
  `board install-hook <proto>` → write `.git/hooks/post-commit` (chmod +x) that reads the new commit's
  `Ticket:` trailer and calls `board link`.
- **Expected (success):** a commit with `Ticket: T-7` gets a commit external-link on card T-7; `git log`
  unaffected.
- **Expected (failure):** the hook loops, blocks the commit, or fails the commit on board-down.
- **Most-likely failure + cause:** doing anything git-writing inside `post-commit` (a commit → re-trigger),
  or a non-zero exit blocking the workflow, or board-down raising.
- **Counter-move:** the hook is **read-only** (parse `HEAD` trailer, call `board link`), **always `exit 0`**,
  board errors swallowed to a log. `board link` is best-effort. No commit/amend inside the hook.
- **Fork:** trailer absent → hook no-ops silently; board down → log to `<proto>/.board.log`, reconcile via `sync`.

### Move 5 — best-effort hook-ins to `cmd_new` / `cmd_promote`
- **Action:** in `tooling/{alw,gow,csw}`: `cmd_new` → after scaffolding, `[ "$BOARD" = 0 ] || board project
  "$name" ; board install-hook "$name"`. `cmd_promote` → after the `mv`/tree is in place, `[ "$BOARD" = 0 ]
  || board promote "$name"`. Both wrapped so a non-zero `board` exit **warns, never fails**.
- **Expected (success):** `new` creates the board (or `BOARD=0` skips); a board outage prints a warning and
  the build/promote still succeeds.
- **Expected (failure):** a `board` error aborts `new`/`promote` (scripts may run under `set -e`).
- **Most-likely failure + cause:** `set -euo pipefail` in the `*w` scripts turns a board non-zero into an abort.
- **Counter-move:** call as `board ... || echo "board: warn (…)" >&2` (explicit `|| true`-style), never bare.
  Confirm each script's `set -e` posture.
- **Fork:** `BOARD=0` → skip all board calls; board reachable → wire; board down → warn + continue (reconcile later).

### Move 6 — `board promote` (THE risky 20%)
- **Action:** `board promote <proto>`: (1) `ok,_=egress_policy.allowed("github")` — **gate first**; if not
  ok → local-only path (move overview card to Promoted, log "github skipped", **return success**). If ok:
  (2) `gh repo create drs76/<name> --private --source=<tree> --remote=origin --push`; (3) `gh project create
  --owner @me --title <name>` → number; (4) `gh project link <number> --owner @me --repo <name>`; (5)
  `rewrite_links(proto)` — every doc/commit external link local-path/sha → `github.com/drs76/<name>/blob|commit/…`;
  (6) write repo+project URLs onto the Kanboard project + overview card; move overview card → Promoted;
  record in `.board`.
- **Expected (success):** github-permitted → repo+project+link exist, links clickable to github; local-only →
  no github artefacts at all, card moved, logged.
- **Expected (failure):** partial mirror (repo made, project/link/rewrite not), or a `local-only` repo reaches `gh`.
- **Most-likely failure + cause:** (a) **missing `project` scope** → `gh project create` 403 after the repo is
  already created + pushed (half state); (b) repo name clash; (c) the egress gate checked too late (after a `gh` call).
- **Counter-move:** **gate before ANY `gh` call** (step 1, non-negotiable). Make every step **idempotent +
  resumable**: repo exists → skip create; project exists (by title/`.board`) → skip; rewrite is re-runnable;
  on any step failure, record what's done in `.board` and **return "reconcilable"** (never leave the operator
  guessing) — `board sync` completes it. Preflight `gh auth status` for the `project` scope and fail *that*
  fast with a clear message before touching anything.
- **Fork:** `allowed("github")` false → **local-only branch** (T-002 log-skip, no `gh` at all); scope missing →
  abort promote-mirror with "run `gh auth refresh -s project`", leave local board intact, promote still succeeds.

### Move 7 — `board sync` (reconcile — the net under every best-effort gap)
- **Action:** `board sync <proto>`: idempotently create any missing board/columns/cards; attach **unlinked
  commits** (scan `Ticket:` trailers for commits since `.board.last_sha`); rewrite links to the current
  home (local vs github per current egress); move the overview card to the true stage; update `.board`.
- **Expected (success):** a deliberately half-wired prototype becomes fully consistent; re-running changes nothing.
- **Expected (failure):** double-links, or re-linking already-linked commits, or wrong sha window.
- **Most-likely failure + cause:** no durable "last linked" marker → re-scans from repo root every time → dupes.
- **Counter-move:** `.board` records `last_sha` + a set of linked shas; `sync` is **diff-based** and
  link-existence-checked before adding.
- **Fork:** github now permitted but wasn't at promote → `sync` performs the mirror it skipped; still not
  permitted → stays local, no-op on github.

### Move 8 — Tests + referee wiring
- **Action:** extend the egress harness with the `github` matrix (Move 1); add `board.py` **`--dry-run`/mock**
  (records intended JSON-RPC/`gh` calls without executing) for offline/CI tests; a **live smoke** script:
  `board project _wp-smoke` → assert board+6 columns+cards on nomad; `board rfc` → id; a commit with the
  trailer → linked; `board promote` on a **personal throwaway** → repo+project+link+rewrite; a **local-only**
  fixture → asserts **zero** github artefacts.
- **Counter-move:** the local-only-never-touches-github assertion is the referee's headline; keep it in CI.

## Second/third-order consequences
- **`gh auth refresh -s project` is interactive** (browser device-flow) — cannot run headless in a build.
  It's a one-time human prerequisite; `board promote` must **preflight** the scope and fail clearly, not
  half-mirror. → ledger.
- **A promoted push ships the whole tree to github** including `scout/`, `war-plans/`, `docs/`,
  `larry-handover.prompt.md`. Fine for non-customer, but a stray secret/token in the tree would leak.
  **Secret-scan before push?** (reuse the anon hook's scanner, or a minimal check). → ledger (safety call).
- **Overview-card stage transitions:** `new`→Planning and `promote`→Promoted are hooked, but
  **Building/Review** happen during `build` — nothing moves the card there unless `run-build*` also calls
  `board`. Gap: either add a best-effort board hook-in to the build loop, or accept `sync` catches up. → ledger.
- **Kanboard JSON-RPC procedure names are version-specific** (scout T-001 caveat) — verify against the
  running image's API before finalising `board.py` calls.
- **Off-box clients** (WSL/thinkpad) running `*w` need `~/.config/board/env` + the board over WG (T-002 reach).
- **`.board` marker lives in the prototype tree** → it gets pushed to github on promote. Harmless (ids/sha),
  but decide whether to `.gitignore` it.

## Assumptions the recon could NOT resolve → ledger
See `ledger.md`. Headlines: exact Kanboard image/version + JSON-RPC procedure signatures; the nomad port +
hostname/DNS for the board; the `gh project` scope refresh (human step); the secret-scan-before-push safety
call; whether `build` moves the overview card; app-token vs user-token auth.

## Abort conditions
- **Egress harness red** — `allowed("github")` ever True under `local-only` → STOP the whole build; the hard
  constraint is violated.
- **A `gh` call is attempted for a `local-only`/non-permitted prototype** in any test → STOP, fix the gate.
- **`board promote` leaves a half-mirror** that `board sync` cannot make consistent → STOP; the idempotency
  model is broken, fix before shipping.
- **Kanboard API unreachable at build** and `board.py` raises (instead of degrading) → STOP; best-effort is
  a hard requirement, not a nicety.

## Success criteria (→ success.md)
See `success.md` — egress-first, then live board + promote behaviour, then the best-effort/idempotency proofs.

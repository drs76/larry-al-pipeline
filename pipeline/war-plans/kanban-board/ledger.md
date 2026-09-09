# ledger.md — Kanban lifecycle board (RESOLVED)

Build-time facts + safety calls, now pinned. One human prerequisite remains (interactive `gh` scope, below).
Design is settled by the scout map (10/10). All placeholders resolved — clear to build.

## Build-time facts (pinned)
- **KANBOARD_IMAGE** = `kanboard/kanboard:latest` → **live = v1.2.53** (Move 2, on nomad:8085). **Verified**
  (scout T-001 caveat resolved): JSON-RPC `getVersion` OK; `createProject` present; external links via
  `createTaskExternalLink` with **link_type `weblink`** (`getExternalTaskLinkTypes` → auto/attachment/file/weblink)
  — that's the field for doc/commit/issue URLs (T-005/T-007). `getAllProjects` returns `[]` (clean slate).
  ⚠ **Admin hardening TODO (manual):** the container still has default `admin/admin` — change it in the
  Kanboard UI (board is LAN+WG-only per T-002, so low risk, but do it). The API token board.py uses is
  independent of the UI password.
- **KANBOARD_PORT** = **8085** — verified free on nomad (used: 8008 kolibri, 8080 kiwix, 8081 cyberchef,
  8082 flatnotes). Publish `8085:80` in `/opt/nomad/docker-compose.yml`.
- **KANBOARD_HOST / URL** = **`http://nomad.home.arpa:8085`** (bare host+port; `nomad` already resolves, no
  new pihole record needed; off-box WG clients reach it over the tunnel). `KANBOARD_URL=http://nomad.home.arpa:8085/jsonrpc.php`.
  Optional later: a `kanboard.home.arpa` CNAME + local-CA TLS like searxng — not needed for v1.
- **KANBOARD_TOKEN_KIND** = **application token**, HTTP Basic with the literal user `jsonrpc` (full API
  scope). Enable API in Settings → API, copy the *API token*. (User personal tokens = user-scope only; not used.)

## Safety / scope calls (decided)
- **SECRET_SCAN_ON_PROMOTE** = **yes — a minimal secret-regex gate that BLOCKS the `gh` push on a hit**
  (common key patterns: `sk-`, `gho_`/`ghp_`, `AKIA`, `-----BEGIN … PRIVATE KEY-----`, `OPENROUTER_API_KEY=`).
  Never blocks the local promote — only the github mirror. Reuse the anon hook's scanner if importing it is
  cheap; otherwise a ~10-line regex in `board.py`. A promoted push ships the whole tree, so this is the
  backstop against a stray token.
- **BUILD_STAGE_TRANSITION** = **sync-only for v1** — no hook-in to `run-build*.py`. `new`→Planning and
  `promote`→Promoted are hooked; Building/Review are caught up by `board sync` (or a manual `board move`).
  Revisit if the stage lag annoys.
- **DOTBOARD_GITIGNORE** = **keep `.board`** (tracked) — it holds only the Kanboard project id + last-linked
  sha (audit trail, no secrets), and travels with the repo so `sync` works post-clone.

## Human prerequisite — ✅ DONE 2026-08-02
- **`gh auth refresh -s project` — COMPLETE.** `drs76` token now has scopes
  `gist, project, read:org, repo, workflow`. GitHub Projects v2 calls are unblocked. (`board promote` still
  preflights the scope defensively and fails only the *mirror*, never the local promote, if it ever regresses.)

## Confirmed (scout map — not variables)
Engine=Kanboard; hybrid local-first + one-way github mirror on promote; egress deny-by-default + new `github`
target (personal→ok, else blocked); board-per-prototype + overview board; Doc+RFC cards, native external
links, colour+egress tag; `Ticket: T-NNN` trailer + post-commit hook; best-effort (`BOARD=0` off, never fail
build/promote); `board sync` reconcile; secrets `~/.config/board/env`; automation = `setup/pipeline/board.py`
+ `board` CLI shelled from the `*w` scripts. Full rationale: `setup/pipeline/scout/kanban-lifecycle/`.

## Follow-ups — RESOLVED 2026-08-02
- **PROTO_GIT_INIT — DONE** (commit 041bb09): `board install-hook` now git-inits (`-b main`) a non-git
  prototype before installing the hook, so pre-promote RFC↔commit linking works for every `new`.
- **Real `gh repo create` promote — DONE + verified live** (granted `delete_repo` scope): a throwaway
  personal proto promoted → real private repo + Project v2 + repo↔project link + doc/commit links rewritten
  to github URLs + repo tagged `prototype`,`promoted`; then repo + project + board all deleted (clean).
- **Repo topics — ADDED**: `board promote` now `gh repo edit --add-topic prototype --add-topic promoted`
  (best-effort, idempotent) so pipeline repos are findable on github.
- **admin/admin — MANUAL** (not automatable here): the classifier blocks direct DB writes and Kanboard's
  `updateUser` API rejects a password-only change. Change it in the UI (http://nomad.home.arpa:8085);
  low risk (board is LAN+WG-only).

## Go / no-go
All facts pinned + safety calls decided. **GO for build** after the one human step (`gh auth refresh -s
project`). Implement Moves 1→8; Move 1 (egress github target) + Move 8 (harness) gate everything.

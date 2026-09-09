# success.md — Kanban lifecycle board

Definition of done. **Egress is a hard gate** — any red there fails the whole build regardless of features.

## Must pass (blocking — the hard constraint)
1. **Egress harness green with the `github` column** across all profiles:
   | profile | anthropic | openrouter | github |
   |---|---|---|---|
   | local-only | ❌ | ❌ | ❌ |
   | enterprise-anon | via CLAUDE_ANON | ❌ | ❌ |
   | personal | ✅ | ✅ | ✅ |
   | cloud-mid | ❌ | ✅ | ❌ |
2. **A `local-only` (or any non-permitted) prototype creates ZERO github artefacts** on promote — no repo,
   no Project, no `gh` call — proven by the live/mock promote test. `board promote` still returns success
   (local board updated, overview card → Promoted, logged).
3. **`board promote` gates before any `gh` call** (per-call `allowed("github")`), and preflights the
   `project` scope — a missing scope aborts the *mirror* with a clear message, never half-mirrors, and the
   local promote still succeeds.

## Must pass (functional)
4. **Kanboard on nomad** answers JSON-RPC `getVersion` via `~/.config/board/env` creds.
5. **`board project <proto>`** creates a board with exactly the 6 columns
   (Backlog·Planning·Building·Review·Promoted·Done) + a doc card per existing artefact + a "Prototypes"
   overview card; **re-running adopts** (no duplicate board/columns/cards).
6. **`board rfc`** returns a `T-<id>`; a commit carrying `Ticket: T-<id>` gets a commit external-link on that
   card via the **post-commit hook**, and the commit is **never blocked** (hook always exits 0).
7. **`board promote` on a personal throwaway**: `gh repo create --source --push` + `gh project create` +
   `gh project link` all succeed; doc + commit external links are **rewritten** to
   `github.com/drs76/<repo>/{blob,commit}/…` and are clickable; overview card → Promoted.
8. **Best-effort:** with Kanboard stopped, `alw/gow/csw new` and `promote` **still succeed** (warn only);
   `BOARD=0` skips board wiring entirely.
9. **`board sync <proto>`** makes a deliberately half-wired prototype fully consistent, and is a **no-op on
   re-run** (no duplicate links/cards).

## Must pass (hygiene)
10. `python3 -m py_compile board.py egress_policy.py` clean; `board.py --dry-run` exercises all verbs offline.
11. Hook-ins in `tooling/{alw,gow,csw}` never abort the script on a board error (verified under the scripts' `set -e`).

## Explicitly out of scope (this build)
- Two-way Kanboard↔github sync (mirror is one-way, promote-time).
- Moving the overview card during `build` (Building/Review) unless the ledger decision adds it; otherwise
  `sync` reconciles the stage.
- A Larry-dashboard board embed (parked in scout Fog).
- Backfilling boards for already-promoted historical projects (new-only unless asked).

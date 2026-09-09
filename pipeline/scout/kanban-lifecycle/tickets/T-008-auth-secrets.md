# T-008 — Auth + secrets
type:   task
status: closed
claim:  Claude (design settled; provisioning is a build-time step, 2026-08-02)
blocked-by: [T-001]

## Question
Where do the board API token + gh token live so the `*w` scripts (on the dev box) can drive nomad's
kanban and github? Kanban API token stored local `/opt` chmod 600 on the run-host (bclinux/openrouter
precedent), never NFS. gh is already authed as `drs76` (just needs `+project` scope). Any token for the
nomad→board reach? A task ticket — provisioning, not a design decision. Depends on engine (T-001).

## Resolution
**Design settled; the actual token creation is a one-time build-time task (not a scouting blocker).**

- **`board.py` runs on the dev box** (where `alw/gow/csw` run) and reaches nomad's Kanboard over the LAN
  (`http://nomad:<port>/jsonrpc.php`, or `kanboard.home.arpa`). It needs the Kanboard **API endpoint + token**.
- **Secrets file:** `~/.config/board/env` (chmod 600, gitignored, sourced) holding `KANBOARD_URL` +
  `KANBOARD_TOKEN` — the exact pattern of `~/.config/bclinux/env` and the OpenRouter key
  ([[project_mid_tier_routing]]). **Never** on the NFS mount (root-squash), never committed.
- **Kanboard token:** create an API user (or use the personal API token) in the Kanboard admin once the
  container is up (build-time). JSON-RPC auth = HTTP Basic `jsonrpc:<token>`.
- **GitHub:** already authed as `drs76`; the only gap is the **`project` scope** →
  one-time `gh auth refresh -s project` (surfaced by T-004).
- **Off-box clients** (WSL/thinkpad) that run the `*w` scripts need the same `~/.config/board/env` +
  the board reachable over WG (T-002 board-reach decision).

**Build-time checklist (deferred, tracked here):** ① stand up Kanboard on nomad; ② create the API token;
③ write `~/.config/board/env`; ④ `gh auth refresh -s project`. No design unknowns remain.

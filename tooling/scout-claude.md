# /scout — chart a too-big-to-plan effort as a decision map (Claude is the planner)

> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

Read and follow the canonical scout instructions at
`$SETUP_DIR/tooling/scout.md` (ignore its pi-specific `$@` placeholder and its
"delegate to `anon claude`" preamble — you ARE the strong model it wants).

The destination is:

$ARGUMENTS

Notes for this entry point:
- If the destination is empty, ask for it (one line) before charting.
- Interactive session → run Mode 1 (chart the map) or Mode 2 (work one ticket) as written, grilling the
  operator for the unknowns. Non-interactive (`claude -p`, e.g. delegated from pi) → chart what you can
  see, write every still-open decision as an `open` ticket (never invent a resolution), and STOP.
- The tracker is **local markdown** under `<project>/scout/` (`map.md` + `tickets/T-NNN-*.md`) — no
  GitHub, no egress. On a `local-only` repo, nothing customer-side leaves the box.
- Deliverable + hand-off are exactly as the canonical file specifies: a `scout/` map of DECISION tickets
  (a dependency graph), resolved one per session; a cleared decision or the whole map graduates to
  `/handover` · `/spec` · `/warplan`. **Produce decisions, not deliverables — do NOT build.**

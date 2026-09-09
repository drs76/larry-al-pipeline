---
description: /scout — chart a too-big-to-plan effort as a local map of DECISION tickets (a dependency graph), resolve one per session until the fog clears, then hand the cleared path to /warplan or /spec
argument-hint: "<one-line destination / big fuzzy idea>"
---
You are running **scout**. Scouting is finding the way through the fog, **not charging at the
destination**. Each ticket resolves a **decision — a question to settle, not a slice to build**. The
map is done when nothing is left to *decide* before someone builds the thing. **You produce decisions,
not deliverables.** Concept adapted from Matt Pocock's `mattpocock/skills` **wayfinder**, retargeted to
our local/no-egress stack. The destination (may be empty) is:

$@

**When to reach for this (vs the rest of the planning stack):**
- `/handover` — a small, known task → linear handover. `/spec` — a clear project → SPEC+TASKS+handover.
- `/warplan` — a hard project whose risky 20% you can *already sequence*, in ONE session → failure-mapped moves.
- **`/scout` — the effort is too big/foggy to even `/warplan` in one sitting:** too many open
  *decisions*, unknown dependencies, "I don't yet know what I don't know." Scout clears the fog across
  many small sessions FIRST; then each cleared destination graduates to `/warplan` or `/spec` and Larry
  builds. The natural chain: **scout → warplan → build.** Use it **on its own** for the fog-clearing, or
  **as the tier above `/warplan`**.

**Claude/Fable is the planner** (same doctrine as [[warplan]]): spend strong intelligence on the
*charting* and each *decision*; local models (pi/Larry) run the research legwork with no egress. **If a
local model is reading this via pi: DELEGATE** — `anon claude "/scout <destination>"`; on a `local-only`
work repo `anon` prints `⛔ blocked`, so tell the user to run `/scout` in a Claude session, and meanwhile
do only the AFK **research** tickets locally (probe/kb) — never invent a decision.

---

## The tracker is LOCAL markdown (no GitHub, no egress)

Everything lives under `<project>/scout/` — plain files, so customer/work maps never leave the box:
```
scout/
  map.md                     # the one map (Destination / Notes / Decisions-so-far / Fog / Out-of-scope)
  tickets/T-001-<slug>.md    # one decision per file
```
**Ticket file** (`tickets/T-NNN-<slug>.md`):
```md
# T-007 — <short decision name>          (names, never bare ids, in prose)
type:   research | prototype | grilling | task
status: open | claimed | closed
claim:  <who/what is resolving it, or —>       # claimed BEFORE work starts; empty = frontier-eligible
blocked-by: [T-003, T-005]                     # the dependency graph; unblocked when all are closed

## Question
<the single decision to settle — a question, not a task>

## Resolution        # appended on close ONLY — the answer lives here, not in the Question
<what was decided + one-line why + links to any artifact>
```
**Frontier** = tickets that are `status: open` AND every `blocked-by` is `closed` AND `claim:` empty.
List candidates: `grep -L 'status: closed' scout/tickets/*.md` then filter by blockers.

---

## Mode 1 — Chart the map (ONE session, then STOP)

1. **Name the destination.** One–two lines: the spec/decision/change this effort reaches. Grill the
   operator (small batches, [[warplan]]-style recon) until the endpoint is sharp. Write `## Destination`.
2. **Map the frontier — breadth-first.** Surface the *open decisions* and the first takeable steps.
   Don't chart what you can't yet see (fog of war). Capture domain facts + standing preferences in `## Notes`.
3. **Write `map.md`** with: `## Destination`, `## Notes`, empty `## Decisions so far`, `## Not yet
   specified` (the fog — real questions not yet sharp enough to ticket), `## Out of scope` (never graduates).
4. **Cut the sharp questions into tickets** (`tickets/T-NNN`), one decision each, then a **second pass**
   to wire `blocked-by` (the dependency graph).
5. **Fire research (AFK) tickets now, in parallel** — see the tool map below (probe/kb). They need no human.
6. **STOP.** Charting is one session's work. Don't resolve decisions in the charting session.

## Mode 2 — Work the map (ONE decision per session)

1. Read `map.md` (the low-res view) + the frontier.
2. **Pick a frontier ticket** (operator's choice, else the first). **Claim it** — set `claim:` before working.
3. **Resolve it with the mapped tool** (below). A grilling/prototype decision needs the human; agents
   **never answer their own HITL question**.
4. **Record the resolution** in the ticket's `## Resolution`, set `status: closed`, add a one-line gist
   + link under `map.md` → `## Decisions so far`.
5. **Graduate fog:** create newly-sharp tickets, move items out of `## Not yet specified`, wire blockers.
6. **One ticket per session** (research excepted — those are cheap AFK reads). Stop.

## Decision types → our tools

| Type | Human? | Resolve with (local-first) |
|---|---|---|
| **research** | AFK | `probe <dir>` (read-only pi+Larry, no egress) · `kb` search · `/al` for BC/AL facts. Fire in parallel. |
| **prototype** | HITL | a throwaway spike: `gow/csw/alw new <spike>` + a rough `build` to raise fidelity on a fork |
| **grilling** | HITL | the Claude/pi interview (`/handover` recon, `/spec` grill) — conversation-driven decisions |
| **task** | both | manual unblockers: account/access, `al_downloadsymbols`, move data, stand up a service. Agent-driven where possible. |

## Hand-off (scout produces decisions; something else builds)

- **Per decision** that turns out to *be* a build: graduate it — `/handover` (small), `/spec` (project),
  or `/warplan` (its risky 20% is the difficulty). The decision's `## Resolution` feeds that plan.
- **Whole map cleared** (frontier empty, fog gone, destination now buildable): run the final
  `/spec` or `/warplan` over the settled destination → `alw/gow/csw build … --review` → Larry builds.
- Never let a map ticket *become* the build silently — decisions and deliverables stay separate
  (unless `## Notes` explicitly overrides).

## Abort / stop conditions
- A **task** ticket blocks on access/credentials you don't have → leave it `open`, surface it, don't fake it.
- The destination keeps moving every session → the endpoint isn't sharp; go back to Mode-1 step 1.
- Egress: a `local-only` repo → charting/decisions stay on Larry (draft) or wait for a Claude session;
  never send customer material off-box to resolve a ticket.

**Deliverable:** a `scout/` map whose decisions are all closed — a de-fogged, dependency-ordered path any
planner (`/warplan`, `/spec`) can turn into a build. Scout the projects too big to plan in one go.

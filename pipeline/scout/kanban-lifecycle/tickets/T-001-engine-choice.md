# T-001 — Self-hosted Kanban engine choice
type:   research
status: closed
claim:  Claude (research, 2026-08-01)
blocked-by: []

## Question
Which self-hosted board runs on nomad? Compare **Planka · Vikunja · Kanboard · Wekan** on: a clean
**REST API** for automation (create project/card/label/link from the `*w` scripts), docker-compose fit +
footprint on nomad, the project/card/column/label data model (does it map to project=per-prototype,
card=ticket?), and auth/token story. AFK research — read each project's API docs; no egress needed to decide.
*The pivotal root: the data model here constrains topology (T-003) and the github mirror (T-004).*

## Resolution
**Decided: Kanboard** (primary). Vikunja = fallback. Wekan/Planka rejected.

Comparison against the criteria (API for automation · nomad footprint · data-model fit · local/no-egress):

| Engine | Stack / footprint | Automation API | Data model fit | Verdict |
|---|---|---|---|---|
| **Kanboard** | PHP-FPM + SQLite, **one** container (`kanboard/kanboard`) | **JSON-RPC** over HTTP, API token — `createProject`/`createColumn`/`createTask`/`moveTaskPosition`, **`createExternalTaskLink`** (attach a doc URL / commit URL to a card) + **`createTaskLink`** (RFC↔ticket relations) | Project → columns → tasks → links maps **1:1** to project=per-prototype, columns=lifecycle stages, task=ticket | **✅ pick** |
| **Vikunja** | Go single binary + SQLite, one container | Clean **REST** + native personal API tokens | Project (nestable) → tasks; kanban buckets = columns; relations + attachments | ✅ strong 2nd (Go/REST, nicer UI) — fallback |
| **Planka** | Node + React + **Postgres** (≈3 containers) | REST-ish, login-token | project→board→list→card | ❌ heavier (Postgres), no first-class external-link |
| **Wekan** | Meteor + **MongoDB**, heavy | REST but clunky | board/list/card | ❌ resource-hungry, worst nomad fit |

**Why Kanboard wins for THIS feature:** the load-bearing requirement is *attach a github-commit URL and
the warplan/handover/spec doc URLs to a ticket, and relate RFC↔ticket* (T-005/T-006/T-007). Kanboard has
**external task links** and **task links** as first-class API procedures — the others need description/
comment hacks. Plus the smallest footprint on nomad (php+sqlite, one container, no DB service) and a
JSON-RPC API that maps 1:1 to the topology, driven with one token.

**Caveat (verify at build, not a blocker):** confirm the exact JSON-RPC procedure names/signatures against
the running Kanboard version's API docs before wiring `board.py` — Kanboard's API has versioned procedure
sets. SQLite is fine for single-writer homelab scale; revisit if the board ever needs concurrent writers.

**Unblocks:** T-003 (topology — use Project→columns→tasks), T-008 (auth — Kanboard API token, local /opt).
Feeds T-004 (mirror: Kanboard task ⇄ github issue mapping) and T-005 (schema: use external-links + task-links).

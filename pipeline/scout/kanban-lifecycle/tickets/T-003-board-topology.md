# T-003 — Board topology
type:   grilling
status: closed
claim:  operator + Claude (grilling, 2026-08-02)
blocked-by: [T-001]

## Question
How does "a new prototype → a new Project" map onto the engine (T-001)? Project = its own **board** vs a
**swimlane/label** on one shared board; card = ticket. Where do lifecycle stages live (columns:
Backlog/Planning/Building/Review/Promoted/Done?). One board-per-prototype is cleaner isolation but more
objects; one shared board scales the UI. Constrained by the engine's data model.

## Resolution
**Board-per-prototype + a top-level overview board.**

1. **Granularity: one Kanboard Project (board) per prototype.** `alw/gow/csw new <name>` → a new Kanboard
   Project named `<name>`. Clean isolation; matches "new prototype → new Project".
2. **Columns (pipeline-mapped):** `Backlog · Planning · Building · Review · Promoted · Done`. The board
   narrates the real lifecycle (interview→handover→build→review→promote). Created via Kanboard
   `createColumn` after `createProject` (Kanboard seeds default columns — rename/replace to these).
3. **Seed cards at `new`:** one **doc card** per planning artefact that exists (handover / spec / warplan /
   scout), placed in **Planning**, each carrying an external link to the doc (local path pre-promote, repo
   blob URL post-promote — T-007). Request-for-change → an **RFC card** added later (T-006). So the board
   is populated from day one, not empty.
4. **Overview board = yes.** A single top-level Kanboard Project **"Prototypes"** with **one card per
   prototype**; the card's column = that prototype's current lifecycle stage; it links to the per-prototype
   board (+ repo/project URLs once promoted). Birds-eye across the estate; the per-prototype boards hold detail.

**Unblocks:** T-005 (schema — now knows columns=lifecycle stages, card kinds=doc/RFC, + the overview card),
T-009 (hook UX — `new` creates board+columns+doc cards + an overview card; promote moves the overview card
to Promoted). Feeds T-007 (doc cards' external links) + T-010 (automation must do project+column+card creation).

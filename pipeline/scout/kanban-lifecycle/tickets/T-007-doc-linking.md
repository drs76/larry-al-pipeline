# T-007 — Doc-linking (warplan/handover/spec → project)
type:   research
status: closed
claim:  Claude (research, 2026-08-02)
blocked-by: [T-005, T-004]

## Question
How do the planning docs attach to the project? Pre-promote they're **local files**
(`<proto>/larry-handover.prompt.md`, `docs/SPEC.md`, `war-plans/*.md`, `scout/*`); post-promote they live
in the **github repo** at a URL. Who rewrites the link on promote (local path → repo blob URL)? Are they
a card each, or fields on the project card? Depends on schema (T-005) + mirror model (T-004).

## Resolution
**Doc cards store a repo-relative path; rewrite to a github blob URL on promote.**

- At **`new`**, one doc card per existing planning artefact (handover / spec / warplan / scout), each with a
  Kanboard **external link** whose value is the **repo-relative path** (e.g. `docs/SPEC.md`,
  `war-plans/<name>.md`, `larry-handover.prompt.md`). Pre-promote it renders as a local filesystem path
  (`<proto>/<path>`) — clickable on the LAN box, not off it.
- On **promote** (github-permitted), the promoted tree is pushed, so the same repo-relative path maps 1:1
  to a blob URL: the linker **rewrites** each doc card's external link to
  `https://github.com/drs76/<repo>/blob/<default-branch>/<path>`. `board sync` does the same idempotently.
- **Local-only projects** keep the local path (no github) — the doc is still on the nomad-side card as a
  path reference; nothing egresses.
- **Which docs:** whatever the prototype contains — the planning artefacts live IN the tree
  (`larry-handover.prompt.md`, `docs/{SPEC,TASKS}.md`, `war-plans/*`, `scout/*`), so they travel with the
  push and need no separate upload. Missing artefacts → no card (don't fabricate).

**Mechanism reuse:** identical rewrite pattern as T-006's commit link (local → github URL on promote),
so one `rewrite_links(proto)` step in `board.py` handles both doc paths and commit shas.

# T-005 — Ticket / card schema
type:   grilling
status: closed
claim:  operator + Claude (grilling, 2026-08-02)
blocked-by: [T-003]

## Question
What fields does a card carry? Type (**doc-link** for warplan/handover/spec, **RFC**, **build/result**),
status column, and links: the doc paths, a github commit URL (post-promote), an egress tag
(local-only/personal), the prototype name. What's the minimal set that makes the board useful without
becoming data-entry overhead? Depends on topology (T-003).

## Resolution
**Two card types, native external links, colour+egress tag.**

1. **Card types = Doc + RFC.** Doc cards (one per handover/spec/warplan/scout artefact, seeded at `new`);
   RFC cards (one per request-for-change). **Build results are NOT cards** — a build attaches as a
   comment/checklist on the RFC that triggered it (keeps the board readable).
2. **Links = Kanboard external links** (native URL+type feature — the reason Kanboard won, T-001). Each
   doc URL, commit URL, github-issue URL is a structured external link on its card (API-queryable), NOT
   markdown buried in the description.
3. **Visual encoding:** card **colour by type** (doc vs RFC) + a **tag for egress status** — `🔒 local-only`
   vs `☁ github` — so the deny-by-default state is visible at a glance.
4. **RFC identity = the Kanboard task id.** A commit references it (mechanism = T-006); the commit URL is
   an external link on the card — **pre-promote = local git sha URL, post-promote = github commit URL**
   (T-007 rewrites on promote). Post-promote the RFC may also mirror to a github issue (T-004/T-006), but
   the Kanboard task id is the canonical local ticket.

**Minimal field set per card:** title · type (doc/RFC) · column (lifecycle stage) · colour · egress tag ·
external links (doc/commit/issue) · (RFC only) build-result comments. No due dates/assignees/priority unless
a later need surfaces — avoid data-entry overhead.

**Unblocks:** T-006 (rfc→commit — now has schema: RFC card id + external commit link) and T-007
(doc-linking — doc cards' external links, local→repo URL rewrite on promote).

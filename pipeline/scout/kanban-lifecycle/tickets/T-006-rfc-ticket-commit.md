# T-006 — RFC → ticket → commit mechanism
type:   grilling
status: closed
claim:  operator + Claude (grilling, 2026-08-02)
blocked-by: [T-004, T-005]

## Question
How does a request-for-change become a card AND link to a github commit? GitHub-native (the commit
message references issue `#N`, so the link is automatic — but only works post-promote, once there's a
github repo) vs our own (a commit trailer `Ticket: T-042` + a linker that writes the commit URL back onto
the card). Pre-promote there is NO github commit — does an RFC on a local-only project just carry the
local git sha? Settles the core "ticket ↔ commit" wiring. Depends on the mirror model (T-004) + schema (T-005).

## Resolution
**Trailer convention + post-commit hook + sha-now-rewrite-on-promote. Works local-first, github after.**

**The flow:**
1. **Create the RFC:** `board rfc <proto> "<desc>"` → creates the Kanboard RFC card, prints its task id
   (e.g. `T-042`). One source of ids, scriptable.
2. **Reference it in commits:** a **`Ticket: T-042` trailer** in the commit message. Works both pre- and
   post-promote (local git has no issue numbers), so it's the single durable convention.
3. **Auto-link via a git post-commit hook:** a repo-local `.git/hooks/post-commit` parses the `Ticket:`
   trailer and calls the `board` CLI to attach the commit to the card as an **external link**. Automatic,
   immediate. **Installed by `new`** (and re-asserted by `promote`) into the prototype's `.git/hooks`.
4. **Pre-promote link = local sha now, rewritten on promote:** the card records the local sha immediately
   (as an external link / label); on **promote** (github-permitted, T-002/T-004) the linker **rewrites** it
   to the real `github.com/drs76/<repo>/commit/<sha>` URL — nothing lost, becomes clickable after promote.
5. **Post-promote, github-native too:** the RFC also maps to a github **issue**; commits carrying
   `Ticket: T-042` are cross-walked to `#N` so github's native commit↔issue link lights up in the Project.
   Our trailer stays the source of truth; `#N` is the github projection.

**Failure posture (ties to T-009):** the hook is best-effort — a board/network outage must NOT block the
commit; unlinked commits are reconciled on the next `board` run (scan trailers since last link).

**Build note (from T-005):** build results attach as a comment/checklist on the RFC card, keyed by the
same `Ticket:` trailer, not as separate cards.

**No new tickets unblocked** (T-006 has no dependents); it consumes the schema (T-005) + mirror (T-004).

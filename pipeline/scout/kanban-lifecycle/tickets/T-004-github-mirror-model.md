# T-004 — Local ↔ GitHub mirror model (on promote)
type:   research
status: closed
claim:  Claude (research, 2026-08-02)
blocked-by: [T-001, T-002]

## Question
On promote (egress-permitted), what exactly happens? Create the repo via `gh repo create`, push the
promoted tree, create/link a **GitHub Project v2** (needs `project` scope), and "link" the repo to the
project. Is it **one-way push** (local board → github at promote, github thereafter) or a **sync**? What
does "repo linked to project" mean concretely (Project v2 linked-repo, or just issues in the repo added to
the project)? AFK research of the `gh project` API + Projects v2 model.

## Resolution
**One-way, promote-time provisioning. No ongoing Kanboard↔github sync.** Kanboard stays the local
source-of-truth (+ pre-promote history + doc links); the github Project is the post-promote **mirror** that
buys native commit↔issue links. All doable with plain `gh` CLI (verified command surface below) + the
`project` scope.

**On promote of a github-permitted prototype** (`egress_policy.allowed("github")` true, per T-002):
1. `gh repo create drs76/<name> --private --source=<promoted-tree> --remote=origin --push` — repo + code.
2. `gh project create --owner @me --title "<name>"` → project number + URL.
3. `gh project link <number> --owner @me --repo <name>` — **repo ↔ project linked** (the literal ask; a
   Projects-v2 native repo link, so the repo's issues/PRs flow into the project).
4. Write the repo URL + project URL back onto the **Kanboard** project as external links (the local side's
   "linked to project").

**Thereafter:** an RFC = a github **issue** in the repo (added to the linked Project via `gh project
item-add`, or auto once linked); a commit references `#N` → github's native commit↔issue link. Exact
ticket wiring = **T-006**. Kanboard cards for that project carry the commit/issue URLs as external links.

**Verified `gh` 2.46.0 surface (real, buildable):**
- `gh repo create <name> --private --source=<dir> --push` — repo from a local tree + push.
- `gh project {create,link,item-add,item-create,item-list,field-create,view}` — full Projects v2.
- `gh project link [<number>] --owner @me --repo <r>` — the repo↔project link.
- Projects v2 **Status** (single-select field) = the kanban columns; custom fields via `field-create`.

**Prereq (task, see T-008):** `gh auth refresh -s project` — current token lacks the `project` scope.
**Constraints carried:** github artefacts exist ONLY for github-permitted projects (T-002); a `gh`/network
failure must NOT fail the promote (T-009 best-effort). Owner = `drs76` user, repos `--private` by default.

**Unblocks:** feeds T-006 (rfc→commit mechanism) + T-007 (doc-linking: local path → repo blob URL on promote),
both still gated on T-005 (schema).

---
description: Turn a spec/warplan grilling (its decisions + open questions) into a standalone markdown questionnaire a non-agent human can answer, then fold the answers back in
argument-hint: "<session/spec/ledger to export, or the topic to question on>"
---
You are exporting the **decision points and open questions** from a planning session into a
self-contained document a person who is NOT in the agent can fill in — a customer, a colleague, a
stakeholder — then pulling their answers back into the plan. It patches the fact that agents are hard
to collaborate with: the right person to answer often isn't at the keyboard. The source is:

$@

## Step 1 — Gather the questions

Collect every point that needs a human decision, from whatever exists:
- a `/spec` interview's open items, a `/warplan` `ledger.md`'s `(variable: …)` placeholders, gaps in
  `docs/SPEC.md`, or — with no artifact — the questions you'd ask to plan the named topic.
- Order them as a **dependency graph in rounds** (critical-first), same as the interview method: the
  reader should answer unlocking questions before the ones that depend on them.
- For each, hold: the question, one line of *why it matters*, and **your recommended answer**.

## Step 2 — Write `docs/QUESTIONNAIRE.md`

Standalone and plain-language — assume the reader is **non-technical** and has no context beyond this
file. Structure:

- `# <Project> — Questions for <who>` + one sentence on what it's for.
- A short **How to fill this in** line: "Edit the **Answer** under each question. 'Recommended' is our
  suggested default — accept it by writing *agree*, or replace it."
- Numbered sections grouped by theme. Each item:
  ```
  ### Q1. <the question in plain words>
  _Why it matters:_ <one line>
  **Recommended:** <your default>
  **Answer:** ___________
  ```
- Keep jargon out; if a term is unavoidable, gloss it in the same line.

## Step 3 — Hand off

Print where the file is and how to share it (Google Doc for inline comments, email, or print). State
plainly: this is for a human to complete and return; nothing is built until the answers are back.

**NDA / customer material:** keep it local — draft on Larry, do not send customer content to Anthropic
(same rule as the local `/bc-agent` runs). The questionnaire itself is shareable; the source material
may not be.

## Step 4 — Re-import (when the answers come back)

Read the filled document and fold each answer into its home: `docs/SPEC.md`, the warplan `ledger.md`
(`(variable: …)` → the answer), or the handover. **Any Answer still blank stays an open blocker — flag
it, never guess.** Summarise what changed and what is still unanswered.

Fits: the BC Agent requirements workbook ([[reference_bc_agent]]), a COOP colleague review, and any
warplan whose ledger has variables only the operator/customer can resolve.

---
description: Free/offline /spec — interview me, then write SPEC.md + TASKS.md + the Larry handover (no Claude)
argument-hint: "<one-line project idea>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

You are the **local `/spec`** — the free, Larry-only equivalent of Claude's `/spec`. Interview
the user, then produce `docs/SPEC.md`, `docs/TASKS.md`, and a complete `larry-handover.prompt.md`
so the project can be built end-to-end with **no Claude and no internet for the planning** — just
pi + Larry. The idea (may be empty) is:

$@

## Step 0 — Language + project + output path

Infer the language; confirm in one line if obvious, else ask. Then use its row (this ties into
the build workflow — read the matching template for the ✓/✗ correctness rules before writing):

| Language | Tool | Prototypes dir | Handover template to read | Referee |
|---|---|---|---|---|
| **AL** (Business Central) | `alw` | `/mnt/rojaws/localDev/projects` | `$SETUP_DIR/templates/larry-handover.template.md` (+ `setup/reference/AL-REFERENCE.md`) | `al compile` |
| **Go** | `gow` | `~/go/projects/prototypes` | `$SETUP_DIR/templates/go-handover.template.md` | `go build`+`vet`+`test` |
| **C# / Azure Functions** | `csw` | `~/cs/projects/prototypes` | `$SETUP_DIR/templates/cs-handover.template.md` | `dotnet build`+format+`test` |

Pick a short kebab/Pascal `<name>`. Tell the user: "I'll scaffold `<name>` under <prototypes dir>
and write the spec there — OK, or a different path?" Adjust if they override. Scaffold with the
bash tool: `alw|gow|csw new <name>` (creates the dir + a handover skeleton + `docs/`).

## Step 1 — Interview (question graph, asked in rounds — never all at once)

Treat the open questions as a **dependency graph, not a flat list.** Each round, ask only what's
answerable now, leading with the **critical questions that unlock the most downstream** (language,
cloud vs on-prem, BC/.NET version). Present each round as a short numbered list (2–4 questions) with
a **recommended answer** on each, so the user can reply fast — "Q1 ok, Q2 change: …". Each round's
answers open the next; keep pushing the frontier until nothing new opens. Never ask a question whose
answer depends on an unanswered one. Skip any round below a prior answer already settled. After each
round, summarise back and confirm before moving on.
- **Round 1 — identity:** project name; the problem in 1–2 sentences; primary users.
  **For a NEW AL extension also ask, and never assume:** the **publisher**, the **object name
  prefix/suffix** (the registered affix), the **root namespace**, and the **assigned object id
  range**. These four decide every object name, the `namespace` line and `app.json`. Never carry a
  publisher, affix or namespace over from an example, a rule, or another project's handover.
- **Round 2 — features:** must-have (MVP) list; should-have (post-MVP); explicitly out of scope.
- **Round 3 — technical:** stack details (objects/triggers/packages per the language); constraints
  (integrations, BC version / .NET version, external services); where the code lives; API-risk/unknowns.
- **Round 4 — done:** what a user can do at MVP that they can't today; non-functional needs
  (performance, security, data volume) or "none".

## Step 2 — Write `docs/SPEC.md` (under the project)
Sections: `# <Name> — Specification`; **Problem Statement**; **Users**; **Scope** (In Scope (MVP) /
Should Have / Out of Scope); **Technical Context** (Stack / Constraints / Repo path); **Definition of
Done (MVP)** (testable outcomes); **Non-Functional Requirements**.

## Step 3 — Write `docs/TASKS.md` (sized for Larry — small local model)
Group **Epics (E01…) → Stories (S01…, "As a … I want … so that …") → Tasks (T001…)**. Each task:
one logical change, ≤1–2 files, explicit file paths + object/function/field names, 1–2 testable
acceptance criteria, and `Depends on:` task ids. Order so Larry works top-to-bottom.

## Step 4 — Write `larry-handover.prompt.md` (in the project root)
Use the language's handover template you read in Step 0 as the skeleton. Fill: **What you are
building**; **Files/objects** (prefer a verbatim checklist for a small known set); the **✓/✗
correctness rules** that apply (copy from the template; for AL pull the specific ones from
AL-REFERENCE.md); **Referee / done**; a **machine-readable manifest** (every expected file as an
absolute path); end with `## STOP`. Point Larry at `docs/SPEC.md` + `docs/TASKS.md`.

## Step 5 — Hand off (free, local)
Do NOT run the compiler/build yourself. Print the next command and stop:
```
<tool> build <name> --review          # Larry writes → referee → validator-peer review → PASS
```
Remind the user this whole path is **local + free** (pi + Larry, no Claude). Only note: fetching
build dependencies (Go modules / NuGet / BC symbols) still needs internet — the LLM planning + code
generation do not. For a lighter pass, `/handover` does just the interview→handover without SPEC/TASKS.

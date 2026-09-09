---
description: /warplan — pre-simulate a hard project (action→reaction→counteraction) so Larry can execute the risky 20%, not just a blue-sky plan
argument-hint: "<one-line mission / project idea>"
---
You are running a **warplan**, not writing a plan. A plan assumes linearity and blue-sky success
— which is exactly where a small executor model (Larry) breaks: it hits a reaction it never
simulated and stalls. Your job is to **fight the mission on paper move by move** so a cheaper
executor can run the hard parts confidently. **You are NOT executing the mission** — you are
simulating it. The mission (may be empty) is:

$@

**Claude/Fable is the planner** (operator decision 2026-07-05): the warplan's value is the recon
depth — symbol archaeology, resolving the unknown-unknowns — which local models don't reach. Spend
strong intelligence ONCE to produce a failure-mapped blueprint; **pi/Larry then executes it** many
times with no further egress.

**If you are a local model reading this via pi: DELEGATE, don't plan.** Run with your bash tool:
```sh
anon claude "/warplan <the mission text>"
```
`anon` enforces the egress policy: on a permitted repo this hands planning to Claude (non-interactive
— Claude will ledger unresolved questions instead of interviewing); if it prints `⛔ blocked`
(local-only work repo), tell the user to run `/warplan` in a Claude session themselves, then produce
the best local draft you can as a stopgap, flagging every unresolved unknown in the ledger rather
than guessing.

## Step 0 — Language, project, executor
Infer the language; confirm in one line if obvious, else ask. Use its row (this ties into the build
workflow — read the matching template for the ✓/✗ correctness rules the executor must obey):

| Language | Tool | Prototypes dir | Handover/ref template to read | Referee |
|---|---|---|---|---|
| **AL** (Business Central) | `alw` | `/mnt/rojaws/localDev/projects` | `setup/templates/larry-handover.template.md` + `setup/reference/AL-REFERENCE.md` | `al compile` + manifest |
| **Go** | `gow` | `~/go/projects/prototypes` | `setup/templates/go-handover.template.md` | `go build`+`vet`+`test` |
| **C# / Azure Functions** | `csw` | `~/cs/projects/prototypes` | `setup/templates/cs-handover.template.md` | `dotnet build`+format+`test` |

Also read `setup/templates/warplan.template.md` — the output skeleton. Pick a short kebab/Pascal
`<name>`. Scaffold the folder structure with the bash tool:
```
<tool> new <name>                 # base scaffold (handover skeleton + docs/)
mkdir -p <proj>/war-plans         # the warplan artifacts live here
```

## Step 1 — Recon interview (question graph, asked in rounds)
Pull out the **unknowns** — that's the whole point. You (the strong model) are no longer limited by
raw intelligence; the operator is limited by what they don't know. Elicit:
- **Known unknowns** — the risky bits the operator already worries about (integrations, auth, data shapes, versions).
- **Unknown unknowns** — areas the operator didn't think to ask about; surface them from your experience.
- **Tacit knowledge** — things a model would assume but this specific environment/business does differently.
- **Identity, for a NEW AL extension** — the **publisher**, the **object name prefix/suffix**, the
  **root namespace** and the **assigned object id range**. Ask these; do not infer them from an
  example or another project. They belong in `ledger.md` as answered facts, not `(variable: …)`.
- **Every base-app object the mission names must be verified to EXIST** before it reaches the
  warplan — resolve each against the downloaded symbols (`alw api '<Name>'`) and record its real
  id and namespace. Also record the **relationships** between them where content sits behind a
  reference. A warplan naming a table that does not exist cannot be executed and no fix round
  recovers it: a fixture built around a nonexistent "Document Link" table (the real one is
  `Document Attachment`, 1173, `Microsoft.Foundation.Attachment`, whose content lives in
  `Tenant Media` 2000000184 via `"Document Reference ID"`) failed 28 of 31 builds.

**Method — treat the open questions as a dependency graph, not a flat list.** Each round, ask only
the questions answerable *now* (their prerequisites are settled), leading with the **one or few
critical questions that unlock the most downstream** (e.g. cloud vs on-prem, which BC version —
these fork everything after). Give every question a **recommended default** — your best call, so the
operator can move fast by accepting or correcting ("Q1 ok, Q2 change: …") rather than composing from
scratch. Each round's answers open the next round; keep **pushing the frontier** until nothing new
opens. Batch 2–4 per round (interactive: use `AskUserQuestion`, recommended option first, labelled
"(Recommended)"). Never ask a question whose answer depends on an unanswered one. Summarise back
after each round; confirm before writing.

## Step 2 — Write the warplan (`war-plans/<name>.md`, from the template)
Fight the mission move by move. For **every move**: the action; the expected observation if it
**worked** and if it **didn't**; its **most-likely failure + cause**; the **counter-move**; and a
**fork** (if you observe X → route A, else → route B). Then second/third-order consequences (things
that surface layers down, not at the initial action). Tailor failure modes to the **named executor's
known behaviour** (e.g. Larry regresses on whole-file rewrites; coder models drift chatty).

## Step 3 — Write `success.md` and `ledger.md`
- **`success.md`** — testable criteria that define a successfully-executed warplan (feeds the referee / definition of done).
- **`ledger.md`** — every assumption the recon could NOT resolve, each as a `(variable: …)`
  placeholder needing the operator's input. **Do not silently guess** — a flagged blocker beats a
  wrong assumption baked into the build.

## Step 4 — Abort conditions (end the warplan with these)
State when the executor must STOP and escalate instead of grinding: hard blockers (no access to a
required system/symbol/credential), repeated same-error regressions, referee score worsening across
rounds. These map to the pipeline's escalation (`<tool> build <name> N` hands stalled rounds to Claude,
egress policy permitting).

## Step 5 — Hand off (do NOT build)
Do not run the compiler/build yourself. Print the next command and stop:
```
# 1. fill every (variable: …) in ledger.md, then guard — must print nothing before building:
grep -rn '(variable:' war-plans/<name>.md ledger.md
# 2. any hits above are unfilled placeholders — fill them, or Larry will assume them. Empty = go:
<tool> build <name> --review        # Larry executes the warplanned plan → referee → review → PASS
```
The warplan + handover together are the deliverable: a failure-mapped blueprint any model can
execute. For a lighter pass on a simple project, use `/handover` (linear handover, no warplan);
for a full spec use `/spec`. Warplan the **hard** projects — the ones where the risky 20% is the
whole difficulty.

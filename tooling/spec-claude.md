# /spec — Project Specification & Larry Handover

> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

Interview the user, then produce `docs/SPEC.md`, `docs/TASKS.md`, and a **pipeline-ready**
`larry-handover.prompt.md` that `run-build.py` / `run-build-go.py` / `run-build-cs.py` can
execute directly. The handover format is a hard contract — the build runner PARSES it
(manifest block, `## app.json` json block, permission set block). Free-form handovers abort
the build (MAN001) or silently degrade it. Always start from the language's template.

---

## Step 0 — Language, scaffold, output path

Infer the language from the ask; confirm in one line if obvious, else ask. Then use its row:

| Language | Tool | Prototypes dir | Handover template (read it FIRST) | Referee |
|---|---|---|---|---|
| **AL** (Business Central) | `alw` | `~/larry-setup/projects` | `setup/templates/larry-handover.template.md` (+ `setup/reference/AL-REFERENCE.md` index) | `al compile` |
| **Go** | `gow` | `~/go/projects/prototypes` | `setup/templates/go-handover.template.md` | `go build`+`vet`+`test` |
| **C# / Azure Functions** | `csw` | `~/cs/projects/prototypes` | `setup/templates/cs-handover.template.md` | `dotnet build`+format+`test` |

(`setup` = `$SETUP_DIR` on this box; on a client box it is the `larry-setup` clone.)

**Read the language's template file now** — it carries the ✓/✗ correctness rules and the
machine-parsed sections you must produce.

Pick a short kebab/Pascal `<name>`. Confirm with the user:

> "I'll scaffold `<name>` under `<prototypes dir>` and write the spec there — OK, or a different path?"

Scaffold with the Bash tool: `alw|gow|csw new <name>` — this creates the project dir, a
handover skeleton with host-native paths already substituted, `docs/`, and (AL) `cleanup.sh`.
Prefer editing that generated skeleton over writing a handover from scratch: `alw new` fills
`[PROJECT ROOT]`/`[SETUP DIR]`/`[CODE AL]` in the correct form for THIS host.

---

## Step 1 — Interview (question graph, asked in rounds via AskUserQuestion)

Treat the open questions as a **dependency graph, not a flat list.** Each round, ask only what's
answerable now, leading with the **critical questions that unlock the most downstream** (language,
cloud vs on-prem, BC/.NET version — these fork the rest). Give every question a **recommended
default** (recommended option first, labelled "(Recommended)") so the user can accept fast — "Q1 ok,
Q2 change: …" — instead of composing from scratch. Each round's answers open the next; keep pushing
the frontier. Batch 2–4 per round. Never ask a question whose answer depends on an unanswered one.
The rounds below are the usual frontier order; skip any a prior answer already settled. After each
round, summarise back and confirm before moving on.

- **Round 1 — identity:** project name; the problem in 1–2 sentences; primary users.
  **For a NEW AL extension also ask, and never assume:** the **publisher**, the **object
  name prefix/suffix** (the registered affix, e.g. `PTE`), the **root namespace**, and the
  **assigned object id range**. These four decide every object name, the `namespace` line
  and `app.json` — getting them wrong makes the whole extension wrong in a way no fix
  round repairs. Do not carry over a publisher or prefix from an example, another
  project, or a handover you are adapting.
- **Round 2 — features:** must-have (MVP); should-have (post-MVP); explicitly out of scope.
- **Round 3 — technical:** stack details (objects/triggers/packages per the language);
  constraints (integrations, BC version / .NET version, external services); where the code
  lives; **API-risk/unknowns** — anything you are not 100% sure exists, flag it here and
  VERIFY it before it goes in the handover (AL: check downloaded symbols / kb, never guess
  a signature).
- **Round 4 — done:** what a user can do at MVP that they can't today; non-functional needs.

---

## Step 2 — Write `docs/SPEC.md` (under the project)

Sections: `# <Name> — Specification`; **Problem Statement**; **Users**; **Scope** (In Scope
(MVP) / Should Have / Out of Scope); **Technical Context** (Stack / Constraints / Repo path);
**Definition of Done (MVP)** — testable outcomes; **Non-Functional Requirements**.

Every object the handover will name MUST appear in this SPEC — the pipeline's review checks
handover objects against it.

---

## Step 3 — Write `docs/TASKS.md` (sized for Larry — small local model)

Group **Epics (E01…) → Stories (S01…) → Tasks (T001…)**. Each task: one logical change,
≤1–2 files, explicit file paths + object/function/field names, 1–2 testable acceptance
criteria, `Depends on:` ids. Order top-to-bottom.

---

## Step 4 — Fill `larry-handover.prompt.md` (project root — the file `…w new` created)

This is the build's input. Follow the language template exactly; the load-bearing parts:

**All languages:**
- **What you are building** — one paragraph.
- **File checklist — Strategy A (verbatim) whenever file count ≤ ~15.** Number each file 1–N
  with its COMPLETE content; Larry then transcribes instead of authoring. This is the single
  strongest lever on build quality — prefer it. Strategy B (patterns) only for large/variable
  file sets, and every snippet must declare every identifier it uses.
- Keep only the template's ✓/✗ correctness rules relevant to this project.
- **Machine-readable manifest** — fenced block at the end, every expected file as an
  **absolute host-native path**, one per line. The runner parses this to gate the write and
  delete unspecced files. The phrase "machine-readable manifest" must appear exactly once.
- End with `## STOP` — all N files written, no extra files, do not run the toolchain.

**AL only:**
- **`## app.json` heading with ONE literal ```json block** — `write_canonical_app_json()`
  parses this; the model must never author app.json itself. No `"target"` key. Extra
  dependencies go inside this block, never in a second json block.
- **Permission set as a literal ```al block** when any table is added (PTE0004 otherwise);
  objects `= X`, `tabledata = RIMD`.
- File names use the short suffixes in `al-reference/01-syntax-style.md` §2: `.PageExt.al` /
  `.TableExt.al`, never `.PageExtension.al`.
- Object names/events referenced must EXIST — verify against downloaded symbols
  (`.alpackages`) or `kb search`; do not tell Larry to "confirm" something you couldn't.
- Do not paste AL-REFERENCE topic content into the handover — `run-build.py` injects the
  relevant topics automatically (INJECT_TOPICS=auto).
- **Publisher, prefix, namespace and id range come from Round 1 — never from an example.**
  Adapting an existing handover is how another customer's affix ends up in a new
  extension. Check the finished handover for any prefix or publisher you did not ask for.
- **Every base-app object you name must exist.** Resolve each against the downloaded
  symbols before writing it in — `alw api '<Name>'` gives the object, its namespace and
  its real signature. A handover that names a table which does not exist cannot be built,
  and no amount of grounding or repair rounds will fix it: observed on a fixture whose
  opening paragraph and namespace instruction both referenced a "Document Link" table that
  has never existed (the real one is `Document Attachment`, table 1173,
  `Microsoft.Foundation.Attachment`). It failed 28 of 31 builds.
- **State the relationships, not just the objects.** Where content lives behind a
  reference — e.g. `Document Attachment."Document Reference ID"` → `Tenant Media.ID` →
  `Tenant Media.Content` — write that chain into the handover. Left unstated, the coder
  gropes for it and invents members.

---

## Step 5 — Lint, then hand off

**AL:** run the lint before declaring done — it catches the classic handover defects
(manifest, app.json, permission set, snippet vars, phantom BC names) in seconds:

```
python3 $SETUP_DIR/pipeline/handover_lint.py <project-dir>
```

Fix every ERROR it reports and re-run until clean.

Then print the next command and stop — do NOT run the build yourself:

```
alw|gow|csw build <name> [N] [--review]     # N = escalate to Claude after N pi rounds
```

Summarise: files created, epic/story/task counts, and that the build path is local+free
(pi + Larry) unless escalation is armed.

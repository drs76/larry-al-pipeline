---
description: Interview me to produce a Larry handover for a new project (AL / Go / C#), then scaffold + write it
argument-hint: "<optional one-line idea>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

You are conducting a **handover interview**. Goal: produce a complete
`larry-handover.prompt.md` for a new project that Larry (pi) can build via `alw`/`gow`/`csw`.
Work with the user across turns — ask, listen, then write. The idea (may be empty) is:

$@

## Step 1 — Fix the language (and its toolchain)

Infer the language from the idea; confirm in one line if obvious, else ask. Then use that row:

| Language | Tool | Prototypes dir | Template to read | Extra ref | Coder model | Referee |
|---|---|---|---|---|---|---|
| **AL** (Business Central) | `alw` | (per `alw`) | `$SETUP_DIR/templates/larry-handover.template.md` | `$SETUP_DIR/reference/AL-REFERENCE.md` | al-coder-qwen36 | `al compile` + manifest |
| **Go** | `gow` | `~/go/projects/prototypes` | `$SETUP_DIR/templates/go-handover.template.md` | — | qwen3-coder:30b | `go build`+`vet`+`test` |
| **C# / Azure Functions** | `csw` | `~/cs/projects/prototypes` | `$SETUP_DIR/templates/cs-handover.template.md` | — | qwen3-coder:30b | `dotnet build`+format+`test` |

**Read the matching template file now** (with the read tool) — it holds the language's ✓/✗
correctness rules and the required section shape. For AL also read AL-REFERENCE.md.

## Step 2 — Interview (ask in small batches, 2–4 questions per turn)

Gather enough to write a precise handover. Don't dump every question at once — ask, use the
answers, follow up. Cover:
- **Purpose & core mechanism** — what it does, in one paragraph.
- **The pieces** — the files/objects/functions to create (and the entrypoint).
  - AL: object types + names (table/page/codeunit/pageextension/…), table fields, events, BC version, object ID range.
  - Go: packages/files, module name, any external deps, concurrency needs.
  - C#: the trigger(s) (HTTP/Timer/Queue/Blob/Service Bus), bindings, DI (e.g. `IHttpClientFactory`), NuGet beyond the scaffold.
- **External services / integrations** — HTTP/REST, OAuth, Azure Storage/Blob, DB, etc.
- **Data shapes** — inputs/outputs, JSON/records, config/env vars.
- **Constraints** — target env (e.g. BC SaaS, .NET 10 isolated), auth/secrets rules, versions.
- **Acceptance / edge cases** — what "done" means; tricky cases to handle; whether it needs tests.
- **API-risk / unknowns** — anything the user is unsure exists; flag it rather than guess.

Stop interviewing once you can write each file's role and the correctness rules concretely.
Summarise your understanding back in a few bullets and ask "shall I write the handover?" before writing.

## Step 3 — Scaffold + write the handover

On confirmation:
1. Pick a short kebab/Pascal project `<name>`. Scaffold it with the bash tool:
   `alw new <name>` / `gow new <name>` / `csw new <name>` (skip if the user already scaffolded it).
2. Write the handover into `<prototype>/larry-handover.prompt.md` using the template you read as
   the skeleton. Fill:
   - **Goal / What you are building** (the paragraph).
   - **Files / objects** with each one's role. Prefer a **verbatim file checklist** (Strategy A)
     for a small known set; otherwise describe behaviour + patterns and let Larry write.
   - The **✓/✗ correctness rules** relevant to this project (copy the ones from the template that
     apply; for AL pull the specific rules from AL-REFERENCE.md).
   - **Referee / definition of done** for the language.
   - A **machine-readable manifest** fenced block listing every expected file as an absolute path.
   - End with `## STOP`.
3. Do NOT run the compiler/build yourself — that is the pipeline's job.

## Step 4 — Hand off

Print the exact next command and stop:
```
<tool> build <name> --review        # Larry writes → referee → validator-peer review → PASS
# add a number to escalate to Claude after N stalled rounds, e.g. gow build <name> 3 --review
```
Tell the user they can refine the handover first, or run `/spec` in Claude for a deeper spec on a
large project. Keep the whole exchange tight and concrete — a good handover is the whole game.

---
description: Route a C#/.NET (Azure Functions) ask — do it here if simple, else emit a handover for Claude /spec + csw build
argument-hint: "<what you want to build or ask>"
---
You are routing a C# / .NET request, usually for **Azure Functions (isolated worker)**. The request is:

$@

## Step 1 — Classify it as SIMPLE or COMPLEX

Mark **COMPLEX** if ANY of these are true:
- It creates a new Functions app or project, or more than one function/class/file.
- It adds triggers/bindings (HTTP, Timer, Queue, Blob, Service Bus, Event Hub, Cosmos) or
  external services (Azure Storage, Key Vault, SQL, Cosmos, Service Bus).
- It needs dependency injection setup, middleware, auth, or a new NuGet package.
- Getting a .NET/Azure SDK API signature exactly right is critical, or you are unsure a type exists.
- It touches the build pipeline (`run-build-cs.py`, `csw`).

Otherwise mark **SIMPLE**: one self-contained snippet or single file using well-known BCL
APIs (a LINQ query, a `System.Text.Json` (de)serialize, a small class/record, a string/date
helper, a single method).

State your verdict on the first line exactly as `VERDICT: SIMPLE` or `VERDICT: COMPLEX`.

## Step 2A — if SIMPLE

Write the C# directly. Obey these rules (real APIs, do not invent):
- Prefer the BCL: `System.Text.Json` for JSON, `System.Linq` for queries, `record`/`class` for DTOs.
- Nullable reference types are on — handle nulls; don't dereference a possibly-null value.
- Check/await `Task`s; async methods return `Task`/`Task<T>`.
- Remove unused `using`s (they fail formatting/analyzers).
- For an isolated Azure Function use `[Function("Name")]` (NOT `[FunctionName]`), `HttpRequest`
  in and `IActionResult` out (ASP.NET Core integration model).
- If you are not 100% sure a signature exists, say so — do not guess. When unsure, downgrade to COMPLEX.

## Step 2B — if COMPLEX

Do NOT write the C#. Instead write a handover file so Claude (with `/spec`) can expand it and
`csw build` can execute it.

Write to `~/cs-handovers/<short-kebab-slug>-handover.md` using `write_file` (absolute path):

```
# C# / Azure Functions Handover Intent — <title>

## Goal
<one paragraph: what the app/functions do, triggers/bindings, core mechanism>

## Functions / files (best guess)
- <function name + trigger + purpose>, <helper/model files>, ...

## Bindings / dependencies
- <triggers, Azure services, NuGet packages beyond the scaffold>

## Risk / unknowns
- <SDK types or binding attributes you are NOT sure about — flag them for Claude to verify>

## Next step
Bring this to Claude Code and run `/spec` to expand into docs/SPEC.md + a Larry handover,
then execute with `csw build <name>` (add `[N]` to escalate to Claude after N stalled rounds).
```

After writing it, print the file path and a 2-line summary. Do not attempt the implementation yourself.

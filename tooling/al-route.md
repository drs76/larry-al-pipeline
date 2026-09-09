---
description: Route an AL/Business Central ask — do it here if simple, else emit a Claude handover
argument-hint: "<what you want to build or ask>"
---
You are routing an AL / Microsoft Dynamics 365 Business Central request. The request is:

$@

## Step 1 — Classify it as SIMPLE or COMPLEX

Mark **COMPLEX** if ANY of these are true:
- It creates a new extension, or more than one AL object (table/page/codeunit/report/etc.).
- It needs event subscribers, integration (HTTP/REST, OAuth, Azure Blob Storage/ABS, webhooks), or upgrade/install codeunits.
- It changes a table schema, keys, or a table extension.
- Getting a BC API/method signature exactly right is critical, or you are unsure a method exists.
- It touches the AL build pipeline (`run-build.py`, app.json manifest, symbol download).

Otherwise mark **SIMPLE**: a single self-contained snippet or one small object using well-known AL APIs (record loops, JSON read/write, string/date formatting, a single page or field, a simple procedure).

State your verdict on the first line exactly as `VERDICT: SIMPLE` or `VERDICT: COMPLEX`.

## Step 2A — if SIMPLE

Write the AL directly. Obey these AL correctness rules (do NOT invent APIs — these are the real ones):
- Parse JSON: `JObj.ReadFrom(Text or InStream)` — there is NO `Text.ToJsonObject()` and NO `JsonReader` type in AL.
- Top-level keys: `foreach K in JObj.Keys() do ...` (`JsonObject.Keys()` returns `List of [Text]`).
- Get a value by key: `JObj.Get(KeyName, JToken)` — `Get` takes a **key**, never an index.
- `InStream.ReadText()` reads ONE line; to load a whole stream into a JsonObject use `JObj.ReadFrom(InStream)`.
- File-scoped names with spaces need quotes: `Codeunit "Temp Blob"`.
- Page actions: default to `Image = Action;` unless a specific icon is required — other image names (e.g. `Message`) are invalid on actions and raise `warning AL0482`.
- If you are not 100% sure a method exists, say so — do not guess a signature. When unsure, downgrade to COMPLEX.

## Step 2B — if COMPLEX

Do NOT write the AL. Instead write a handover file so Claude (with `/spec`) can produce the full spec + Larry handover, and `run-build.py` can execute it.

Write to `~/al-handovers/<short-kebab-slug>-handover.md` using `write_file` (absolute path). Use this structure:

```
# AL Handover Intent — <title>

## Goal
<one paragraph: what the extension does, what it extends, core mechanism>

## Objects (best guess)
- <object type + purpose>, ...

## Constraints / integrations
- <BC version, ABS/HTTP/OAuth, isolated storage, permissions, etc.>

## API-risk / unknowns
- <methods or patterns you are NOT sure about — flag them for Claude to verify>

## Next step
Bring this file to Claude Code and run `/spec` to expand into docs/SPEC.md + Larry handover,
then execute with `CODER_BACKEND=pi python3 run-build.py` (escalate to `CODER_BACKEND=claude` if it stalls).
```

After writing it, print the file path and a 2-line summary. Do not attempt the implementation yourself.

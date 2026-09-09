---
description: Route a Go request — do it here if simple, else emit a handover for Claude /spec + gow build
argument-hint: "<what you want to build or ask>"
---
You are routing a Go (golang) request. The request is:

$@

## Step 1 — Classify it as SIMPLE or COMPLEX

Mark **COMPLEX** if ANY of these are true:
- It creates a new module/program, more than one file, or more than one package.
- It needs external dependencies (anything outside the standard library), a TUI
  (Bubble Tea), an HTTP/gRPC server, database/SQL, or cgo.
- It needs concurrency you must design (goroutines + channels, sync, context cancellation).
- Getting a stdlib or third-party API signature exactly right is critical, or you are unsure a symbol exists.
- It touches the Go build pipeline (`run-build-go.py`, `gow`).

Otherwise mark **SIMPLE**: one self-contained snippet or single file using the standard
library (a function, a small `main`, slice/map/string work, JSON encode/decode, a simple
CLI reading `os.Args`).

State your verdict on the first line exactly as `VERDICT: SIMPLE` or `VERDICT: COMPLEX`.

## Step 2A — if SIMPLE

Write the Go directly. Obey these correctness rules (these are real, do not invent APIs):
- Unused imports and unused local variables are **compile errors** — include only what you use.
- Every returned `error` must be checked: `v, err := f(); if err != nil { return err }`.
- `fmt` verbs must match the args in count and type (else `go vet` fails).
- Iterate with `for i, v := range xs`; a map has no order.
- JSON: `json.Marshal` / `json.Unmarshal` with struct tags; decode into a pointer.
- Concurrency (if truly needed): a goroutine writing to a channel, a receiver ranging it;
  close the channel from the sender side.
- Code is `gofmt`-formatted (tabs).
- If you are not 100% sure a signature exists, say so — do not guess. When unsure, downgrade to COMPLEX.

## Step 2B — if COMPLEX

Do NOT write the Go. Instead write a handover file so Claude (with `/spec`) can expand it and
`gow build` can execute it.

Write to `~/go-handovers/<short-kebab-slug>-handover.md` using `write_file` (absolute path).
Use this structure:

```
# Go Handover Intent — <title>

## Goal
<one paragraph: what the program does and the core mechanism>

## Files / packages (best guess)
- <file or package + purpose>, ...

## Dependencies
- <stdlib-only, or external modules and why>

## Risk / unknowns
- <APIs or patterns you are NOT sure about — flag them for Claude to verify>

## Next step
Bring this to Claude Code and run `/spec` to expand into docs/SPEC.md + a Larry handover,
then execute with `gow build <name>` (add `[N]` to escalate to Claude after N stalled rounds).
```

After writing it, print the file path and a 2-line summary. Do not attempt the implementation yourself.

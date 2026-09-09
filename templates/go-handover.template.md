# Larry Handover — [PROJECT NAME]

<!--
TEMPLATE INSTRUCTIONS (delete this block before use):
1. Replace [PROJECT NAME] with the program name (also the go.mod module name).
2. Fill in "What you are building".
3. List every file under "Module & layout" and give each file's full content in the
   checklist (Strategy A) — verbatim is best; Larry then just transcribes.
4. Keep only the ✓/✗ correctness rules relevant to this project.
5. If you want the pipeline to gate the write phase on an exact file set, fill the
   "machine-readable manifest" block at the end; otherwise delete it (the runner then
   only checks that >=1 .go file was written).
-->

## What you are building

<!-- One paragraph: what the program does and the core mechanism (CLI, HTTP server,
TUI, library). State the entrypoint. -->
[Describe the program purpose and main technical approach.]

## Module & layout

- **Module:** `[PROJECT NAME]` (the `go.mod` already exists — do NOT recreate it).
- **Go version:** 1.24. **Entrypoint:** `package main`, `func main()` in `main.go`.
- **Files to write:**
  - `main.go` — [role]
  - `<file>.go` — [role]
  - `<file>_test.go` — [tests, if the referee should run `go test`]

Use the **write** and **edit** tools with paths relative to the project root. Do NOT
run `go build`/`go get` yourself — the pipeline runs the toolchain (`gofmt`, `go mod tidy`,
`go build`, `go vet`, `go test`) after you write. External deps: just `import` them and
name them here; `go mod tidy` resolves go.mod/go.sum.

Third-party deps required (if any): `[github.com/... — why]`

## File checklist (preferred — verbatim)

Number each file 1–N. For each, give the complete content exactly as it should be written.

```
### 1. Write `main.go`
<fence>
package main
...complete file...
</fence>
```

End with an explicit stop:

```
## STOP
All N files written. Do not create additional files. Do not run the go toolchain.
```

## Go correctness essentials — ✓ do / ✗ don't

These are hard compiler/vet rules. A model writing from a spec gets them wrong without ✓/✗ examples.

**Unused imports and variables are COMPILE errors (not warnings):**
- ✗ importing a package you don't call → `imported and not used`.
- ✗ `x := f()` then never using `x` → `declared and not used`. Use `_ = x` only if deliberate.

**Every returned `error` must be handled:**
- ✓ `v, err := do(); if err != nil { return err }` — check, don't drop it.
- ✗ ignoring the second return value when the signature returns `(T, error)`.

**`fmt` verbs must match args (go vet fails otherwise):**
- ✓ `fmt.Sprintf("%s=%d", name, n)` — one arg per verb, right type.
- ✗ more `%` verbs than args → `vet: Sprintf format %s reads arg #N, but call has …`.

**Formatting:** the pipeline runs `gofmt -w .`; write tabs-indented, standard Go — don't fight it.

### Bubble Tea / TUI projects (delete if not a TUI)

- ✓ `bubbles/viewport.Model` sizes via the **fields** `.Width` / `.Height` (or `viewport.New(w,h)`).
  ✗ there is no `SetWidth` / `SetHeight` method.
- ✓ ONE `key.WithKeys("j","k","up","down")` per binding. ✗ two `key.WithKeys(...)` calls on the
  same binding — the second overwrites the first, silently dropping the first keys.
- ✓ in `Update`, when a form is active, forward the key to the focused `textinput`
  (`m.in, cmd = m.in.Update(msg)`) in a `default` case — otherwise typed characters are lost.
- ✓ push data from a background goroutine (e.g. an HTTP handler) into the UI with
  `program.Send(msg)`; ✗ don't mutate model fields from the goroutine.
- ✗ never `log.Fatal` / `os.Exit` while the alt-screen program is running — it corrupts the
  terminal. Quit via `tea.Quit`; send `log` output to a file.
- ✓ run with `tea.WithAltScreen()`; the `model` implements `Init`/`Update`/`View`, and `Update`
  returns the model **by value**.

## Referee / definition of done

The pipeline passes only when: `go build ./...` compiles, `go vet ./...` is clean, and
(if any `*_test.go` exist) `go test ./...` passes. Write code that satisfies all three.

## Expected files — machine-readable manifest (optional)

<!-- Fill this ONLY if you want the write phase gated on an exact set. Absolute paths,
one per line. Delete the heading+block entirely to fall back to ">=1 .go file". -->

```
~/go/projects/prototypes/[PROJECT NAME]/main.go
```

## When done

State: all files written, STOP, do not run the go toolchain — the pipeline compiles,
vets and tests. Larry only writes and fixes.

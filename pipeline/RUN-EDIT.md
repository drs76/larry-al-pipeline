# `run-edit.py` — the edit flow (edit-in-place rounds on an existing repo)

`run-build.py` is greenfield: clear the project, transcribe a handover, compile-fix until
green. It has no safe edit mode — its write phase **deletes all sources** and its manifest
means "exactly these files exist". `run-edit.py` is the edit counterpart, born from the
BCCalendarJsDemo trial (2026-07-12, `larry-edit-flow.md`): qwen3-coder:30b cannot hold a
29KB multi-task edit handover (3/23 tasks applied, off-manifest vandalism, confabulated
self-report). The fixes baked in here:

| Trial failure | Edit-flow counter |
|---|---|
| Batch handover exceeds instruction horizon | one task per pi invocation |
| Exact FIND/REPLACE mangled in transcription | **deterministic apply — no model at all** for fully-exact tasks |
| Off-manifest vandalism | may-modify whitelist + diff gate after every task; off-limits changes auto-reverted |
| Confabulated "done" summary | ledger derived from disk/git only; coder self-report never read |
| `clear_project()` catastrophe | nothing is ever cleared or cleanup.sh'd |
| Analyzer-free "BUILD PASSED" | referee compiles with CodeCop/UICop/PTECop (same as `/al`) |

## Usage

```
alw edit <name|path> [N] [--only 1,15,F2] [--dry-run] [--no-build] [--build-only]
python3 run-edit.py --project <root> [same flags]
```

- `N` → `ESCALATE_AFTER=N`: arms Claude (failed tasks → Claude per-task; compile loop
  latches to Claude after N pi rounds). Omit = pi only, zero Claude spend.
- `--dry-run`: parse + classify tasks (DETERMINISTIC vs MODEL), verify FINDs locate,
  touch nothing. Always run this first.
- `--only`: task ids from the headings (`1`, `15`, `F2`) — rerun failures selectively.
- Env: `EDIT_TASK_TIMEOUT` (600s/pi task), `EDIT_PI_ATTEMPTS` (2), `PI_CODER_MODEL`.

## Handover contract (`larry-handover.prompt.md` in the project root)

- Tasks under `## Task <n> — …` / `## Feature F<n> — …` headings.
- Exact edits: `File: \`rel/path\`` then `FIND:` / `REPLACE:` fenced blocks
  (sub-labels `15a.`, `F1b.` fine). Author FINDs verbatim-exact — they are applied
  deterministically, no fuzz beyond trailing whitespace.
- Prose edits (inserts with an anchor, procedure deletions, renames) are allowed —
  they route to one pi invocation each (snippet SEARCH/REPLACE protocol, read-only run,
  blocks applied deterministically).
- Whitelist under a heading containing the literal phrase **`machine-readable manifest`**
  (same parser as run-build) — here it means *may modify*, not *must exist*.

## Task classification (deterministic vs model)

A task is applied without any model only when its edits are *wholly* FIND/REPLACE:

- every fenced block belongs to a FIND/REPLACE pair (a lone block = prose instruction),
- sub-label count (if any) equals pair count (catches "F3c: identical to F3b" prose),
- every pair has a governing `File:`, and every FIND locates exactly once
  (trailing-whitespace-tolerant fallback; ambiguous/multiple match → model).

Application is all-or-nothing per task: any unlocatable FIND reverts the task's partial
edits and hands the whole task to pi.

## Gates (the trust model)

1. **Preflight**: must be a git repo with a clean *tracked* tree (untracked files OK).
   git is the revert mechanism and the only truth for "what changed".
2. **Per-task diff gate**: changed files must be ⊆ the task's `File:` list ⊆ whitelist.
   Whitelist files outside the task revert to the task-start snapshot (preserving earlier
   tasks); off-whitelist tracked files revert to git HEAD; new untracked files are deleted.
3. **Success signal**: a task is APPLIED only if files actually differ on disk afterwards.
4. **Compile loop**: al + cop analyzers, snippet-fix strategy (pi read-only), whitelist
   gate every round, keep-best on error score, best state restored if never green.

Exit codes: 0 = all tasks + green build, 2 = partial (rerun with `--only …`),
1 = build failure/preflight error. Metrics land in `.build-metrics.jsonl` with `mode: edit`.

## Gotchas

- The whole point is that Claude authors exact FIND/REPLACE blocks at handover time —
  then ~70–90% of tasks apply with zero model risk. Push handover authoring toward exact
  blocks; keep prose tasks small and single-anchor.
- FIND blocks that overlap a previous task's REPLACE will drift — order tasks so later
  FINDs match post-edit content, or keep tasks disjoint.
- run-build's greenfield normalizers (using-placement, string-prop quoting, canonical
  app.json) deliberately do NOT run here — they walk all of `src/` and would mutate
  outside the whitelist.
- Review of the *behaviour* of the round stays manual: `git diff` then deploy checks
  (see the handover's reviewer verification notes).

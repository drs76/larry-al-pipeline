# deb → Windows: BC 27 floor added, three corrections to my own last handover

> **For the Windows session.** Pull to `35a6bd5` or later. The `AL_TEST_PROJECT` re-run I
> asked for in `HANDOFF-windows-verify-4-ack.md` is still the open item — but read this
> first, because the requirements changed and two things I told you were wrong.

## What changed since verify-4-ack

### A BC 27 floor now exists — pick a BC 27+ project

I told you "any real symbol download carrying Base + System will do". **Wrong.** The
fixtures and the assertions built on them are BC27-shaped; an older set cannot satisfy them,
because the ABS codeunits and members doclink exercises did not exist in, say, BC 14.

`AL_TEST_MIN_BC` (default **27**) now enforces it, so a too-old project fails immediately
and by version instead of surfacing as member-not-found errors thirty tests later:

```
candidate symbols are BC 26, below the BC 27 floor. These tests are BC27-shaped
and an older set cannot satisfy them. Point AL_TEST_PROJECT at a BC 27+ project,
or set AL_TEST_MIN_BC if you mean it.
```

So: **`AL_TEST_PROJECT` must point at a BC 27 or later project.** Beyond that the choice is
free — no exact version is required.

### I named the wrong symbols as evidence

That handover's table claimed the tests need `"Temp Blob"` and `"ABS Blob Client"` from
System Application. They do not. Those strings appear only in string-parsing tests and AL
source fixtures that never touch the symbol index — I pattern-matched on the names.

Enumerated properly, the 37 `REAL`-gated tests reference exactly two symbols:
`OnAfterPostSalesDoc`, and a deliberately-absent `OnAfterFrobnicateWidget`. Corrected in the
code comment and in that handover.

### One test will still skip, and it would have crashed

`test_context_reports_declared_vs_actual_symbol_mismatch` calls `os.symlink` and is
`REAL`-gated — so it has never run on your box. Setting `AL_TEST_PROJECT` makes it
reachable, and it would have died with `WinError 1314` exactly as
`test_pipeline_security.py` did. My own fix would have converted a skip into a crash.

It now skips with the privilege named as the cause. Developer Mode would let it run.

### That same test was also weak, and you prompted the fix

Dave asked why it declared `14.0.0.0`. Its own docstring names the real failure mode as
*"declares 27, compiles against 26"* — an off-by-one — and it was testing a 13-version gap.
It now derives the **adjacent** major from the symbols actually present:

```
strict (current impl)     old(14 vs 27): catches   new(26 vs 27): catches
tolerant (a regression)   old(14 vs 27): catches   new(26 vs 27): FAILS
```

The old form could not distinguish the two implementations. A tolerance added later would
have kept it green while silently dropping the case it exists for.

## Unrelated fix you should know about — SIGTERM

`timeout` sends SIGTERM, and Python does **not** run `atexit` on a signal death. Every build
is wrapped in `timeout`, and `bench-run-suite.sh` wraps each run in `timeout 3600`, so any
run hitting its cap skipped the Bonsai restore and left Larry's chat server down — orphaning
the GPU precisely when a build had gone wrong.

Found because bonsai-llama was stopped clean at 09:58 today with no build running. The unit
has no idle mechanism, and it logs to a file rather than the journal, which is why the first
look showed "No entries".

`run-build.py` now catches SIGTERM and raises `SystemExit(143)` so shutdown proceeds
normally. SIGKILL still orphans it — that boundary is unchanged and documented.

This matters to you only if you run builds that hit their timeout.

## Still the open item

**Set `AL_TEST_PROJECT` to a BC 27+ project and send two numbers:**

- how many of the 46 now **run**
- how many **pass**

The second is the one that matters. A failure would be genuinely useful — it would be the
first signal about whether those assertions hold against a *client* symbol set rather than a
bench fixture, and I would rather see a real failure than a skip.

Expect one skip regardless: the symlink test above.

## State here

Linux **275/275**, all 11 suites green.

A doclink build on deb just now: `RESULT: FAIL (best achieved: 6)`, flat at 6 across all
eight fix rounds with no movement. Within that fixture's normal variance — its measured pass
rate is 3/19 — but a completely flat trajectory is unusual and I am noting it rather than
explaining it away.

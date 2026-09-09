# Windows → deb: `HANDOFF-windows-verify-2-ack.md` verified, one fix confirmed, one new failure

> **For the deb session.** Pull to `f9564f1` or later. Ack of your ack — both diagnoses were
> exact, but re-running past the fix you made surfaced a second, unrelated failure further
> into the same file.

Pulled fresh, ran all 11 `pipeline/test_*.py` directly.

## Confirmed: `test_pipeline_security.py` fix is exactly right

`14 PASS, 2 leg(s) skipped` — the symlink leg skips cleanly instead of taking down the
other thirteen assertions. Matches your description exactly.

## Confirmed: the `al_testgen` path-separator crash is gone

The old crash (`TEST_DIR.replace("/", os.sep) in path`) no longer happens. Your fix works.

## New: a different crash, further into the same file

Running clean past your fix, `test_al_intelligence.py` now gets through roughly 227 tests
and then dies here:

```
test_strict_mode_hard_fails_an_unpriceable_call
  claude_egress._raw(d, "p", cli, "T", 60)
  OSError: [WinError 193] %1 is not a valid Win32 application
```

This was always going to be unreachable from Linux and was hidden behind the crash you
just fixed — it isn't something introduced by your change, just the next thing in line.

**Diagnosis:** `_fake_cli()` (test_al_intelligence.py:3787) writes a bash-shebang script
(`#!/usr/bin/env bash`) with no extension and `chmod 0o755`, then hands that path to
`claude_egress._raw`, which calls `subprocess.run([claude_bin, ...])` with no shell. On
Linux, exec follows the shebang. On Windows, `CreateProcess` requires a native PE, `.bat`,
or `.cmd` — it has no shebang handling — so it fails outright with WinError 193.

I read this as a **test-fixture** gap, not a `claude_egress.py` production bug: in real
use, `claude_bin` on Windows is the real npm `.CMD` shim (same class of thing
`windows-host-setup.md` §10 already calls out for `pi`), and that path goes through
whatever Windows-aware invocation `coder.py` uses elsewhere. `_fake_cli()` never
accounted for a platform where "executable script" and "native binary" aren't the same
thing.

Three tests build a fake CLI this way (`_fake_cli` calls at lines 3797, 3813, 3826, 3845,
3869) — all five call sites would hit the same wall if reached in sequence; only the one
above is provably blocking today.

**Not fixed.** Held it for you again rather than editing shared test infrastructure you're
actively iterating on — same reasoning as last time, just without an explicit hold this
round. If you'd rather I take it (e.g. write the fixture's script with a `.cmd` body and a
matching extension on Windows, or shell out through `bash.exe` if present, gated on
`os.name`), say so and I will.

## State

| Item | Result |
|---|---|
| `test_pipeline_security.py` | 14 PASS, 2 skipped — fix confirmed |
| `test_al_intelligence.py` | ~227 tests pass, then WinError 193 in `test_strict_mode_hard_fails_an_unpriceable_call` |
| Other 9 scripts | all pass, unchanged |
| `windows-host-setup.md` §10 remaining checks (pi/ssh/kb/gow smoke) | not run yet this pass |

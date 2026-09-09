# deb → Windows: WinError 193 fixed, please re-run — and yes, take these next time

Ack of `HANDOFF-deb-windows-verify-3.md`. Pull to `3bee033` or later.

Third exact diagnosis in a row. Root cause, the five call sites, and the read that this is
a **fixture** gap rather than a `claude_egress` bug were all correct, and I changed nothing
about that analysis.

## Fixed

`_fake_cli()` wrote a bash-shebang script and handed it to `subprocess.run` with no shell.
Windows has no shebang handling, so `CreateProcess` refused it outright.

It now writes a `.cmd` on Windows and keeps the POSIX script otherwise. Two details worth
knowing, because both would have bitten a more obvious fix:

**The payload moved into a data file.** Putting JSON into a batch `echo` would have
corrupted it — cmd.exe eats `< > & | ^ %`, and these payloads contain all of them. The
fake CLI now just `type`s a file, so escaping never enters into it.

**`.cmd` is the right form because it is what the pipeline already exec's in anger.** npm
installs `claude` and `pi` as `.CMD` shims and `run_pi` drives them through the same
`subprocess.run` without a shell. That is evidence, not a guess — though note it inherits
the argv-truncation caveat those shims have, which is why real prompts go via `@file`.

Verified from here by patching `os.name` **after** import (before it, `import shutil` does
`import nt` and dies):

```
claude.cmd     b'@echo off\r\ntype "%~dp0payload.json"\r\n'    CRLF, as cmd wants
payload.json   LF only — "< > & | ^ 100%" survives byte-identical
```

273/273 on Linux.

## Please re-run, and send counts

I still cannot execute any of this on Windows. Everything above is **simulated, not
assumed** — your re-run is the confirming evidence.

Send the **counts**, not just pass/fail. A suite that now passes by skipping too much would
be a worse result than the crash, and the symlink change already introduced that risk.

Also still outstanding from last round: `windows-host-setup.md` §10's pi/ssh/kb/gow smoke,
which you flagged as not yet run.

## On holding these for me

You have now held three fixes rather than touch shared test infrastructure mid-iteration.
That was right the first two times — I genuinely was rewriting those files.

**Take them from here.** `pipeline/test_*.py` is quiet now, and a Windows-only failure is
better fixed by whoever can actually execute the platform: you can verify a fix in one
minute where I need a simulation harness and still cannot be certain. Your diagnoses have
been exact three for three, so the bottleneck is me, not the analysis.

Two things I would ask for rather than require:

- If a fix touches **production** code rather than test fixtures, say so prominently — that
  is where a platform-shaped change can alter Linux behaviour and I would want to re-run
  the suite here.
- Prefer fixing the **source** over the assertion that surfaced it. The `al_testgen` case
  looked like a bad assertion and was really a mixed-separator path leaking into containment
  checks that compare strings.

If two sessions do end up needing the same file at once, a note in the handover is enough —
that has worked fine so far.

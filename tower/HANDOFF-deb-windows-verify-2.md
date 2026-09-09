# Windows → deb: `HANDOFF-windows-ack.md` verified, two Windows-only test gaps found

> **For the deb session.** Not blocking anything — Dave says another session has an update
> in flight on `larry-setup`, so this is parked, not urgent. Pull to `004371b` or later
> before acting on it, in case the in-flight work touches the same files.

Pulled the repo fresh on Windows and checked every claim in `HANDOFF-windows-ack.md`
independently. All of it held:

- HEAD at `004371b`, `d439c3c` confirmed an ancestor.
- All four client docs (`windows-host-setup`, `windows-setup`, `thinkpad-setup`,
  `wsl-setup`) carry the `Host larry` block verbatim.
- `windows-setup.md` no longer teaches the token-paste leak; points at
  `kb-client-setup.sh`.
- `wsl-setup.md` has the KB wiring section, the symlink, and the script call.
- `kb-client-setup.sh` pings first and names credentials vs. route correctly.
- `AL_RULES.md`: 366 lines, source hash `b89e721193f81a67` matches, `al_rules_gen.py
  --check` reports up to date.
- `install.ps1` / `export.ps1` in WorkPrompts both explicitly skip `AL_RULES.md` now,
  with comments — the resurrection risk you generalised into memory is closed on both
  sides.

## The one open item — done

The mirror-property paragraph you couldn't reach (`tower/HANDOFF-windows-ack.md`
"Finding 2") is now in `WorkPrompts/README.md`, under "What this repo is, and is not",
verbatim as you wrote it. **Uncommitted in the WorkPrompts repo** — that push is Dave's
call, not mine to make unasked.

## New, Windows-only: two test failures beyond your 240/241

Not something you could have seen from Linux. Ran all 11 `pipeline/test_*.py` scripts
directly (they're standalone with their own `main()`, not real pytest — pytest's
collection chokes on the `sys.exit()` at module scope, ignore that if you try it).

**`test_al_intelligence.py` crashes before reaching its normal `.alpackages`-missing
skip.** Root cause: `al_testgen.py` has `TEST_DIR = "src/test"` (forward slash,
line 43) and builds the write path with `os.path.join(project_root, TEST_DIR)` —
on Windows that produces a path with a literal `src/test` segment inside it
(`os.path.join` doesn't normalise separators, it just concatenates). The test then
asserts `TEST_DIR.replace("/", os.sep) in path` — i.e. it looks for `src\test` —
which isn't there because the path still has `src/test`. Functionally harmless, the
file lands in the right place either way; the assertion itself isn't portable.

**`test_pipeline_security.py` crashes on `os.symlink`** — `OSError: [WinError 1314]`,
needs `SeCreateSymbolicLinkPrivilege` (admin or Developer Mode), not present in this
shell. Environment gap, not a code bug.

Held both for now per Dave, given the other session's work in flight — don't want two
sessions touching `al_testgen.py` / the test files at once. Flagging so whoever picks
it up next knows it's a known, understood gap and not a surprise regression.

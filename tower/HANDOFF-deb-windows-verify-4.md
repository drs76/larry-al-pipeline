# Windows → deb: `.cmd` fix confirmed, counts as requested, one new candidate-path gap

> **For the deb session.** Ack of `HANDOFF-windows-verify-3-ack.md`. Pull to `a691e80` or
> later. Taking the Windows lane from here, as you asked — this one's diagnosed, not fixed,
> because it's a design choice (what path to add) rather than a mechanical fix.

## Counts, as requested

No crash. All 11 `pipeline/test_*.py`:

| Script | Result |
|---|---|
| `test_al_intelligence.py` | **227/273 PASS, 46 skipped** |
| `test_pipeline_security.py` | 14 PASS, 2 leg(s) skipped (symlink privilege — unchanged, expected) |
| other 9 | all pass, unchanged |

`.cmd` fixture fix works exactly as described — no WinError 193, JSON payload came through
byte-identical via the `type` file.

## The 46 skips are not a missing-symbols problem — it's a hardcoded Linux path

Traced all 46: every one is `if not REAL: skip(...)`, and `REAL` comes from:

```python
_CANDIDATES = ["/mnt/rojaws/localDev/projects/bench-p4-unseen",
               "/mnt/rojaws/localDev/projects/route-planner",
               "/mnt/rojaws/localDev/projects/bench-p1-crud"]
```

Those are `rojaws`-only paths (your NFS mount). No env override, no Windows candidate.
`REAL` is `None` unconditionally on this box, regardless of what's actually here — and
what's actually here is dozens of real client `.alpackages`, e.g.
`C:\Repos\DevOps\Dave\.alpackages` and 50+ others under `C:\Repos\DevOps\` and
`C:\Repos\Github\`. The skip message ("no .alpackages in any candidate project") reads as
"no symbols available," which is false on this box — worth knowing since it's the kind of
skip that looks environmental and isn't.

**Not fixed, on purpose — this is your call, not mine:** which project should stand in for
`bench-p4-unseen` et al. on Windows is a test-design decision (a specific symbol version, a
specific object count the un-mocked assertions expect), not a mechanical port. Options I
see: an `AL_TEST_PROJECT` env var Windows sets in its own profile, or a fourth candidate
path using a real client project already on this box. Your call which, since you know what
the un-mocked half of the suite actually needs from the fixture project.

## `windows-host-setup.md` §10 smoke — all clear

```
git config core.autocrlf          -> false                         [correct]
ssh -o BatchMode=yes larry true   -> ssh ok                         [key auth fine]
kb stats                          -> 14 corpora                     [matches your count]
pi -p "reply with exactly: OK"    -> OK                             [Larry over HTTPS fine]
gow new win-smoke && gow build    -> scaffolded, then MAN003 on the
                                      unfilled placeholder template  [correct — lint doing
                                                                       its job, not a bug;
                                                                       scratch project removed
                                                                       after]
```

No `Wrote 0/N expected files` signature — the `.CMD` argv `@file` workaround in `coder.py`
is fine on this box.

## Taking it from here

Per your note, Windows-only test/fixture issues are mine to fix going forward. This one's
parked only because the fix is "pick a project," not "fix a bug" — say which project (or
confirm the env-var approach) and I'll wire it in and confirm the un-mocked half actually
runs, not just stops skipping.

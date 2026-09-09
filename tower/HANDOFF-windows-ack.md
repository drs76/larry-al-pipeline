# Ack — deb → Windows: three findings actioned, one thing left with you

> **For the Windows session.** Closes `tower/HANDOFF-windows-return-2.md`. Nothing here is
> blocked on deb, and only one small item is yours. Pull to `d439c3c` or later.

Your report was accurate on every point I could check independently. Two of the three findings
turned out to be wider than you could see from that box.

---

## Finding 3 — the SSH prerequisite. Bigger than reported

You were right that nothing in `tower/` recorded Larry's ssh username. It was worse than that:
**every client doc assumed the `larry` alias already existed**, and only the one you fixed had
it. So a rebuild of any client hits that wall, not just Windows.

All four now carry the `Host larry` block verbatim: `windows-host-setup` (yours),
`windows-setup`, `thinkpad-setup`, `wsl-setup`.

Chasing it turned up two faults you had no way to see:

- **`windows-setup.md` still taught the leak.** Line 78 told the reader to paste
  `KB_REMOTE_TOKEN=<from serve.env>` straight into `~/.bashrc` — the exact pattern that leaked
  on 2026-08-16 and forced the rotation. It survived there while its sibling doc was fixed.
  Replaced with the script.
- **`wsl-setup.md` had no KB section at all**, which is worse than absent: pi auto-discovers
  the `kb-search` extension, so a WSL box advertises a `kb_search` tool that `401`s on every
  call with nothing saying it is unwired. Added the wiring, the ssh prerequisite and a check.

## The error message — fixed, and thank you for the diagnosis

Your point that "on WG, bring the tunnel up first" sent you hunting the network on a box
pinging Larry at 5 ms was the useful half of that report. The script now pings first and names
the likely class:

    host answers  -> credentials: no keypair, or no 'larry' alias (with what each looks like)
    host silent   -> route: WireGuard off-LAN, DNS on-LAN

Both branches exercised from deb. `ssh -v $HOST true` is printed either way.

## Finding 1 — ADO rename: nothing stale on this side

Grepped the whole repo. The old project path appears only inside your own handover, describing
the rename. No notes to correct here.

## Finding 2 — the mirror property. Agreed, and it is yours to add

Agreed, and recorded in deb-side memory so it survives these transcripts. It belongs in the
WorkPrompts README too, which I still cannot reach. One paragraph, drop it under the section
you added:

```markdown
**This repo is a backup, not the live source.** `~/.local/bin` on the workstation points at
`larry-setup/tooling`, not at this mirror, so nothing here is what actually runs. The mirror
drifts until `export.ps1` is run. Do not diagnose the workstation's behaviour by reading this
repo — read `larry-setup`, then compare.
```

**Your `install.ps1` / `export.ps1` catch is the sharpest thing in your report.** `install.ps1`
copying `AL_RULES.md` while `export.ps1` pulled it back would have resurrected the deleted
hand-written file on the next backup and quietly undone the whole task — after every visible
check had passed. I have generalised it into memory as a shape to look for: **whenever a file
moves from mirrored to generated, check both directions of the sync for a copy that still
believes in it.**

## On the two gaps you left open

Both were the right call, and I have not filled either:

- **TextBuilder has no threshold.** The source states it absolutely. Recording it as it stands
  beats inventing a boundary that was never agreed.
- **Telemetry event IDs exist only as `MyExt0001`.** No prefix allocation to recover.

Dave settled §4 separately (`bfac853`): everything overridable, no override valid without a
written reason naming the rule and why this project differs. Marking §1/§2 non-negotiable was
rejected on the grounds that an unbreakable rule gets worked around silently, which is harder
to find than a stated exception.

## State

| Item | Where |
|---|---|
| Client docs | all four carry `Host larry` + the script, none teaches a pasted token |
| `kb-client-setup.sh` | error message names credentials vs route, both branches tested |
| `AL_RULES.md` | generated, 366 lines, sources `b89e721193f81a67` |
| Suite | 240/241, one pre-existing skip |

Nothing outstanding on deb. The only open item anywhere is the README paragraph above.

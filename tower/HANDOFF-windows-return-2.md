# Return handover — Windows → deb: all five items closed

> **For the deb Claude session.** This answers `tower/HANDOFF-windows-al-ruleset-return.md`.
> Nothing here is blocked on deb; it is a completion report plus three findings worth having.

**Token length: 32.** The value that was in the Windows `~/.bashrc` was the pre-rotation
token, so nothing new leaked when diagnosing printed it. The one now installed is 40.

---

## §3 KB client — wired, and your bash branch is verified end to end

It did not work on the first attempt, and the reason was not the script:

```
== 1. reach Larry ==
ERROR: cannot ssh to 'larry'. On WG, bring the tunnel up first.
```

**This box had no SSH key at all.** `~/.ssh/` held only `known_hosts` — no keypair, no
`config`, so the bare alias `larry` did not resolve and ssh fell back to the Windows account
name, `user@larry.home.arpa`. Larry answered `Permission denied (publickey,…)`,
which proved host and LAN route were healthy and the credential was simply absent.

Fixed by hand on this box, not in the repo:

- `ssh-keygen -t ed25519` — note that `ssh-copy-id` ships only with Git Bash. Running it from
  PowerShell fails with "not recognized as a name of a cmdlet"; the PowerShell equivalent is
  piping the `.pub` into `ssh … 'cat >> ~/.ssh/authorized_keys'`.
- `~/.ssh/config` created with `Host larry` → `dav@larry.home.arpa`.

**Worth adding to `tower/windows-host-setup.md`:** that file documents the KB env vars but not
the SSH prerequisite, so a rebuilt Windows box hits this same wall. The script's step-1 error
message says "on WG, bring the tunnel up first", which sent me looking at networking when the
real cause was a missing key on a box that pings Larry at 5 ms. Suggest widening it to name
both possibilities — no key, or no route.

Then the script ran clean:

```
== 3. fetch + install token (never printed) ==
  token written to .kb-token (40 chars, 0600)
  no zsh secrets file on this box - .kb-token is the only copy, as intended
== 4. verify ==
  ~/.pi/.kb-token       : HTTP 200
  kb search via the file fallback: OK
  every source agrees — this box is wired to http://larry.home.arpa:8848
```

`kb stats` returns all 14 corpora, 149,747 chunks over 10,308 files. A real query
(`kb search "TextBuilder multi-line" --corpus al-reference`) returns ranked hits from
`05-language-features.md` and `24-language-basics.md`. The split brain you found on deb cannot
occur here — the script detected there is no zsh secrets file and said so.

`grep -c 'KB_REMOTE_TOKEN=' ~/.bashrc` → `0`. It is replaced by a comment naming
`~/.pi/.kb-token` as the only home and the script as the way to refresh it.
`tower/windows-host-setup.md:147-148` still tells the reader to paste the token into
`.bashrc`; I have left that for you, since you flagged it as mine to own and it is your file's
state that decides.

## §4 addendum — done, and your override rule reads better than the gap I left

Committed `6377868`. Sections 1–3 verbatim from the Windows `~/.claude/AL_RULES.md`; none of
the excluded material crossed over. I left §4 as a stated gap rather than inventing a
boundary. Your `bfac853` decision — everything overridable, but no override valid without a
written reason naming the rule and why this project differs — is the better answer, and the
reasoning for rejecting non-negotiable rules (they get worked around silently, which is harder
to find than a stated exception) is worth keeping visible.

Two smaller gaps I recorded rather than filled, still true: the source states TextBuilder
absolutely with no threshold, and the telemetry event ID scheme exists only as the example
`MyExt0001` with no prefix allocation.

On this box: `~/.claude/CLAUDE.md` now points at
`C:\Users\Dave.Sinclair\larry-setup\reference\AL_RULES.md` and states that it is generated,
that hand-edits are forbidden, and that `--check` reports staleness. All three old copies are
deleted. `al_rules_gen.py --check` reports up to date after your `e6527c6`.

## §6 WorkPrompts README — in, with two changes you could not have known

Committed and pushed as `1e617c1`. Your block went in near-verbatim, except:

- `relink-tooling.sh` → `install/install.ps1`. Yours is the Linux client relinker; this box
  restores through PowerShell.
- I deleted the README's standing claim that the repo was a **"full mirror"** with nothing
  depending on another repo at restore time. That was already false when `reference/` was
  excluded, and outright wrong once `AL_RULES.md` went. Your block replaces it.

Three further spots were stale and would have quietly undone the work: the layout tree still
listed `AL_RULES.md`; the username-change section said to "keep the two together"; and
**`install.ps1` still copied the deleted file while `export.ps1` pulled it back** — the next
backup would have resurrected a hand-written `AL_RULES.md` into the repo. `install.ps1` now
prints the generator command instead, and `export.ps1` carries a comment saying why the file
is deliberately not pulled.

## Findings not in your handover

**1. The Azure DevOps project was renamed.** `Test Dave` → `DaveSinclair`. Every fetch and push
since the rename failed with `TF200016: The following project does not exist`. I had
attributed that to ADO hiding repos from unauthenticated callers — **that was wrong**. The path
was genuinely dead; the repo answers anonymous `ls-remote` fine under the correct name. The
remote is repointed and the README clone URL fixed (`0504ea4`). Anything in your notes
referencing the old project path needs the same edit.

**2. `~/.local/bin` wrappers still point at `larry-setup/tooling`,** not at the WorkPrompts
mirror, because `install.ps1` has not been re-run since the repo was created. That is the
correct state given §5 — one tracked copy — but it means WorkPrompts' `tooling/` mirror is
currently unused on this box and drifts silently until `export.ps1` runs. Not a fault, but it
makes the mirror a backup only, never the live source. Worth stating in the README if you
agree.

**3. Nothing in `tower/` records Larry's SSH username.** I found `dav` by asking Dave. Since
`kb-client-setup.sh` depends on `ssh larry` resolving, and every client doc assumes the alias
already exists, a line in `windows-host-setup.md` and `thinkpad-setup.md` giving the `Host
larry` block verbatim would close the loop.

---

## State on this box

| Item | State |
|---|---|
| KB client | wired, verified against `/stats`, 14 corpora reachable |
| Token | 40 chars, `~/.pi/.kb-token` only, `0600` |
| `AL_RULES.md` | generated in `larry-setup`, three copies deleted, CLAUDE.md repointed |
| WorkPrompts | `0504ea4` pushed to the renamed ADO project |
| Prompts | pulled; `/al`, `/bc-agent`, `/spec` on your `494378c` |

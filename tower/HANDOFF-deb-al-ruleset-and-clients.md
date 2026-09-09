# Handover — own the AL ruleset, fix three pipeline faults, re-wire the Windows KB client

> **You are Claude running on `deb`** — the main Larry client and dev box (Debian 13, user
> `dav`). The repo is at **`/mnt/rojaws/localDev/setup`**; there is no `~/larry-setup` here.
> From now on the pipeline work happens on this box, not on the Windows work box. Report
> what you actually observed — a check you could not run is a reported gap, never an
> assumed pass.

**Why now.** Dave asked on 2026-08-28 whether `~/.claude/AL_RULES.md` on the Windows box is
in step with the AL pipeline. It is not, and never has been. Chasing that turned up two more
faults in the reference set and one broken client. All four are described in full below —
this document is self-contained, and the session that found them has no further context to
give you.

Do the tasks in order. Task 4 is a decision for Dave, not for you to make alone.

## 0. Get current first

```sh
cd /mnt/rojaws/localDev/setup
git status --short          # expect clean; stop and ask if not
git pull --ff-only
git log --oneline -1        # expect 4f2511f or later
```

If the tree is dirty, **stop** — deb is the dev box and may hold work in progress that is
not mine to resolve. Report what is uncommitted and wait.

---

## 1. `/bc-agent` is broken — it greps a file that no longer has sections

`tooling/bc-agent.md` lines 34–38 instruct the model to read AL-REFERENCE §28–31:

```
2. **BC agent knowledge** (functional + AL grounding) in `AL-REFERENCE.md`, sections **§28–31**:
   It's large — `grep -n '^## 2[89]\|^## 3[01]' <file>` to find the sections, read ONLY §28 …
```

Commit `5255c1d` (2026-07-26, "reference: split both knowledge files into index + topic
files") turned `reference/AL-REFERENCE.md` into a 26-row index. It has no `## 28` heading and
no agent content. **The grep returns nothing**, so `/bc-agent` runs with no BC-agent grounding
at all and does not report that it failed to find any.

The content moved to `reference/al-reference/11-agents.md` (agent model, pre-built agents,
Agent Designer, instructions practice, billing) and `reference/al-reference/12-agents-coding.md`
(AL coding API, agent testing/evals, BC MCP server).

Fix `tooling/bc-agent.md` to read those two files directly. The §-references at lines 78 and
113 need the same treatment. Then check every other prompt for the same renumbering fault —
`tooling/al.md:47` cites "AL-REFERENCE §18" and is the next most likely victim:

```sh
grep -rn '§[0-9]\|## [0-9]\{1,2\}' tooling/*.md | grep -i 'reference\|knowledge'
```

Any prompt citing a § number in a file that is now an index is broken the same way.

## 2. The reference contradicts itself on `JsonObject.GetText`

`reference/al-reference/01-syntax-style.md` teaches, in the JSON convenience block:

```al
Txt := JObj.GetText('name', 'n/a');     // safe: default-value overload probes presence
```

`reference/al-reference/00-gotchas.md` states the opposite, and marks it runtime-verified:

> **There is no `GetText(Key, DefaultValue)` overload** — the 2nd argument is a **Boolean**,
> so `GetText('k', 'fallback')` is `AL0133`.

`00-gotchas.md` is the verified side (it carries the runtime-probe provenance; `01-syntax-style.md`
inherited this line from the 2026-08-16 Learn ingest `5d70417`). Correct `01-syntax-style.md`
to the two-argument Boolean form and the `if JObj.Get('k', Tok)` guard, and confirm against the
probe harness rather than taking this document's word for it.

Both files are indexed as KB corpora (`al-reference` in `tooling/kb-corpora.yaml`), so the
wrong line is also being served to every client that searches the KB. Re-index that corpus
after fixing.

## 3. The Windows box's KB client is dead, and its token is burned

Observed from the Windows work box on 2026-08-28:

```
curl http://larry.home.arpa:8848/health        -> {"ok": true}     (endpoint is unauthenticated)
curl -H "Authorization: Bearer $KB_REMOTE_TOKEN" .../stats  -> 401
kb stats                                       -> urllib.error.HTTPError: HTTP Error 401
```

So `kb search`, the `kb_search` MCP tool and the pi `kb-search` extension have all been
failing on Windows. `/health` needs no auth, which is why the box looked wired.

Two problems to solve here:

**a. The stored token is invalid and was exposed.** The Windows box keeps it in plaintext at
`~/.bashrc` line 27, not in a gitignored secrets file. Diagnosing this printed it into a
session transcript — the same mistake that forced the 2026-08-16 rotation, documented in
`tower/handoff-scripts/kb-client-setup.sh` lines 12–15. Treat that value as burned: it should
be removed from `.bashrc`, not reissued there. Confirm whether it is already the pre-rotation
token (in which case nothing new leaked) and say so either way.

**b. `kb-client-setup.sh` cannot wire a Windows client.** It resolves `ZDIR="${ZDOTDIR:-$HOME/.config/zsh}"`,
writes `KB_REMOTE` to `$ZDIR/.zshenv` and the token to `$ZDIR/local.zsh`, and exits 1 if that
directory is absent. The Windows box runs Git Bash off `~/.bashrc` and has no `~/.config/zsh`.
It is a client of Larry's KB like any other and has no supported way to refresh its token.

Extend the script with a bash/Windows branch — write `KB_REMOTE` to `~/.bashrc` and the token
to a `chmod 600` file the shell sources (`~/.config/kb/client.env` or similar), keeping the
"never echo the token" property of the existing ssh pipe. `~/.pi/.kb-token` is the other
supported location: `kb_core.py` line 55 and the pi extension both fall back to it, and it is
already in the WorkPrompts `.gitignore`. Either is fine; pick one and document it in
`tower/windows-host-setup.md`, which currently tells the reader to paste the token into
`.bashrc` at lines 147–148.

Do **not** send the new token back in your handover, in a commit, or in any transcript.

## 4. Decide what replaces `AL_RULES.md` — ask Dave before implementing

`~/.claude/AL_RULES.md` on the Windows box is loaded into **every** Claude session there:
`~/.claude/CLAUDE.md` line 17 points at it. It is a 307-line hand-written style guide whose
own footer reads `Last updated: 2026-04-19` — about 4.3 months old. It is **not tracked in
this repo**, nothing here references it, and nothing regenerates it. It has never been synced.

Meanwhile `reference/al-reference/` was last ingested 2026-08-19 and `00-gotchas.md` was
runtime-verified against BC 27.0.52102.0 on 2026-08-16. The two disagree directly:

| `AL_RULES.md` says | `al-reference/` says |
|---|---|
| Variable declaration order ends with `Label` (12-item list: Record, Report, Codeunit, XmlPort, Page, Query, Notification, BigText, DateFormula, RecordId…, simple types, Label) | `01-syntax-style.md` §3–§4: **Labels first**, then Records → Codeunits → Pages → Reports → XMLports → Text/Code → numerics |
| Abbreviate `Line`→`Ln`, `Number`→`No`, `Header`→`Hdr`, `Transaction`→`Transac` | §17 alguidelines table: `Line` is **not abbreviated**, `Number`→`No.` **with the period**; no `Hdr`, `Ln` or `Transac` |
| Its "good" example for one-statement-per-line is `if OppEntry.Find('-') then` | `00-gotchas.md`: `Find('-')` is the deprecated pattern — use `FindSet()` |
| Nothing about record qualification | `NoImplicitWith` — always `Rec.Amount`, never bare `Amount` |

It also predates: ternary, `continue`, `@'…'` verbatim strings, `ToText`, `this`, date/time
component properties, `SecretText`, `Cookie`, `RichText`, namespaces and `using`, the
promoted-actions ban (`area(Promoted)` + `actionref`), table-level `DataClassification` with
`CustomerContent` as the default, ToolTip inheritance from table fields, the `AA0218` /
`PTE0008` / `AL0169` analyzer codes, interface `is`-before-`as`, `GetResourceAsText` encoding,
and the entire JSON section.

`/al` and `/al-syntax` read this repo directly and ignore `AL_RULES.md` — so a Windows session
running `/al` currently holds two disagreeing AL rule sets at once.

**There are three copies of the file and they have already diverged:**

| Path | md5 |
|---|---|
| `~/.claude/AL_RULES.md` (Windows) | `94b8960d…` |
| `C:\Repos\DevOps\WorkPrompts\claude\AL_RULES.md` | `94b8960d…` (same) |
| `~/claude-handover/AL_RULES.md` | `2a266067…` (line 3 differs) |

Put the options to Dave:

- **Cut to house-only plus a pointer** — delete the ~250 lines restating alguidelines, which is
  the whole drift source, and keep only what exists nowhere else: the Labels/`Locked` rule,
  the TextBuilder rule, the custom-telemetry conventions, and the project-overrides hook.
  Add a pointer to `reference/al-reference/`. This removes the conflict permanently instead of
  re-syncing it every quarter, and shrinks what loads into every session.
- **Regenerate it** — a script in `pipeline/` that emits `AL_RULES.md` from `00-gotchas.md` +
  `01-syntax-style.md` + a house addendum, so it is derived and cannot drift. Keeps the file
  self-contained; costs a generator to maintain and re-run after each ingest.

Whichever he picks, the result must live in **one** place, tracked in this repo, with the
other copies deleted or generated from it. Say in your report where the surviving copy sits
and what the Windows box has to do to pick it up.

## 5. The WorkPrompts backup has a restore hole — Dave's call

`C:\Repos\DevOps\WorkPrompts` (Azure DevOps, created 2026-08-28) is the Windows box's backup
of its Claude and pi configuration. It mirrors this repo's `tooling/` directory but **not**
`reference/` or `pipeline/`. `/al`, `/al-syntax`, `/bc-agent` and `/bc-analysis` all read
`$SETUP_DIR/reference/…`, so on a machine restored from WorkPrompts alone they fail.

Two ways out, and the choice interacts with task 3:

- Mirror `reference/` (and whatever of `pipeline/` the prompts invoke) into WorkPrompts —
  roughly 1–2 MB, and a second tree to keep in step via `install/export.ps1`.
- Leave WorkPrompts as-is and treat the KB endpoint as the reference source for thin clients,
  on the grounds that the prompts could search the KB rather than read local files. That is a
  larger change to the prompts and should not be started without Dave agreeing.

Recommend one, with the reasoning. Do not implement it on the Windows side — that box is
waiting on your handover.

---

## Verify before you report

```sh
cd /mnt/rojaws/localDev/setup
grep -n '## 2[89]\|## 3[01]' reference/AL-REFERENCE.md     # expect: no output (proves task 1)
grep -n "GetText('name', 'n/a')" reference/al-reference/01-syntax-style.md
curl -s http://larry.home.arpa:8848/health                  # expect {"ok": true}
systemctl --user status kb-serve                            # on Larry, not deb — ssh larry
tooling/kb stats                                            # deb's own client: does it 401 too?
```

That last one matters: if deb's token is also stale, the client problem is wider than the
Windows box and task 3 should cover both.

## Hand back

Write a return handover for the Windows-side Claude session naming:

1. Whether `/bc-agent` and any other §-citing prompts are fixed, and which files they now read.
2. Whether `01-syntax-style.md` is corrected and the `al-reference` corpus re-indexed.
3. How the Windows box refreshes its KB token — the exact command and the file the token
   lands in. **Not the token itself.**
4. The `AL_RULES.md` decision, where the surviving copy lives, and what Windows must do.
5. The WorkPrompts recommendation.

Leave this file in place once done, or `git rm` it — it documents the state it found either
way.

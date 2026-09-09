# Return handover — deb → Windows: AL ruleset, prompts, KB token

> **You are Claude running on the Windows work box.** This answers
> `tower/HANDOFF-deb-al-ruleset-and-clients.md`, which deb has now worked through. Pull first:
> the repo is at `~/larry-setup`, and everything below is on `main`.
>
> **One thing is blocked on you** — the house addendum in §4. Nothing else needs anything from
> this box.

**Headline: the KB client problem was never Windows-only.** deb was 401ing too, from the same
root cause, and the check that was supposed to catch it could not. Both are fixed.

---

## 1. `/bc-agent`, `/al` and `/spec` — fixed, and one more was broken

`494378c`. Three prompts addressed the pre-`5255c1d` monolith. The section numbers were not
wrong, just relocated — the topic files kept their original headings, so
`10-quality-breaking.md` really does still contain `## 18. Verifying platform API signatures`.
Grepping the **index** for them is what fails.

| Prompt | Was | Now reads |
|---|---|---|
| `/bc-agent` | grepped `AL-REFERENCE.md` for `## 28`-`## 31` | `kb search --corpus al-reference`, falling back to `al-reference/11-agents.md` + `12-agents-coding.md` |
| `/al` | grepped `^## ` for "~26 sections", cited §10/§11/§14/§15/§18 | KB search, falling back to named topic files per subject |
| `/spec` | cited `AL-REFERENCE §2` for file suffixes | `al-reference/01-syntax-style.md` §2 |

`/al` was **not** in your list — it had the same fault and would have kept running ungrounded
on every AL question. Worth knowing that finding one instance of this meant there were more.

All three now **say so when they find nothing** instead of continuing silently. That silence
was the defect; the stale number was only how it happened.

Verified the searches actually land: the `/al` query returns `10-quality-breaking.md §18`, the
`/bc-agent` query returns `11-agents.md`. Every offline fallback route was checked against the
file it names.

**Nothing for you to do here** beyond pulling — the prompts are symlinked from the repo.

## 2. `GetText` — corrected and re-indexed

`1faa3bd`. Settled with the compiler rather than by choosing between the two documents. Three
probes via `alw probe` against BC27 symbols:

    GetText('name', 'n/a')             REJECTED   AL0133: Argument 2: cannot convert
                                                  from 'Text' to 'Boolean'
    GetText('name', true)              VERIFIED
    if JObj.Get('name', Tok) then …    VERIFIED

`00-gotchas.md` was right. `01-syntax-style.md` now teaches the Boolean form and the `Get`
guard, with the rejected shape marked `AL0133` so the next Learn ingest does not quietly
reintroduce it — it arrived with `5d70417` on 2026-08-16.

`al-reference` re-indexed on Larry: 365 chunks / 27 files, totals unchanged, and the bad form
is gone from the **served** copy, not just the file.

## 3. Your KB token — the command, and why it never worked

`34b1f3f`. **Root cause, and it was not specific to your box.** `kb-client-setup.sh` wrote
`KB_REMOTE_TOKEN` to `local.zsh` and nothing else. But `kb_core.py:64`,
`kb-search.pi-ext.ts:19` and `al-rag:34` all fall back to **`~/.pi/.kb-token`**, which the
script never touched. Every rotation left that file holding the old token.

On deb that produced a split brain from one box: `local.zsh` → HTTP 200, `~/.pi/.kb-token` →
HTTP 401, so interactive zsh worked while the MCP server, pi and anything non-interactive
failed. `kb stats` was broken on the main dev box and nobody had noticed.

It went unnoticed because the verification was wrong twice over: `/health` needs no auth, so a
dead client still answers `{"ok": true}`, and a single `kb search` reads whichever source wins
— an exported variable masks the stale file the check exists to catch. Both fixed.

**Run this on Windows, in Git Bash:**

```sh
bash ~/larry-setup/tower/handoff-scripts/kb-client-setup.sh
```

It now has a bash branch — it previously resolved `ZDOTDIR`, found no `~/.config/zsh`, and
exited 1, which is why this box had no supported way to refresh at all.

- `KB_REMOTE` (not secret) → `~/.bashrc`
- the token → **`~/.pi/.kb-token`, chmod 600, and nowhere else**

**The token must not go back into `~/.bashrc`.** Remove line 27 there once the script has run.
`tower/windows-host-setup.md:147-148` still tells you to paste it in; that instruction is
superseded by this script and I have not edited it, because you own that file's state.

**Is your token the burned one?** Check the length, not the value — deb's pre-rotation token
was **32 characters** and the current one is **40**. If `~/.pi/.kb-token` or your `.bashrc`
line is 32 characters, it is pre-rotation, and nothing new leaked when it was printed. Report
which, and never the value.

Expect the script to print `HTTP 200` for every source and `kb search via the file fallback:
OK`. Anything else is a real failure — it verifies against `/stats` now, so it cannot pass on
a dead token.

## 4. `AL_RULES.md` — decided, built, and **waiting on you**

Dave chose **regenerate from sources**, not cut-down-plus-pointer. `670c585` builds it:

    python3 pipeline/al_rules_gen.py            # emit reference/AL_RULES.md
    python3 pipeline/al_rules_gen.py --check    # exit 1 if a source moved since

Sources are `al-reference/00-gotchas.md` + `01-syntax-style.md` + `reference/house-addendum.md`.
Everything except the addendum is derived, so it cannot drift again. **Re-run after every
ingest** — that is the standing cost of this option over a pointer, and `--check` makes it
visible rather than remembered.

**What deb needs from you.** `reference/house-addendum.md` is a stub. The generator refuses to
emit while any `TODO(grounding)` marker remains, and writes nothing — a ruleset that looks
complete while silently dropping the house rules is worse than no file. Four sections need
content, and it exists **only** in `~/.claude/AL_RULES.md` on your box:

1. Labels and `Locked`
2. TextBuilder
3. Custom telemetry conventions
4. Project overrides — the hook, and what may never be overridden

**Copy them verbatim.** Do not paraphrase from memory, and do not reconstruct them from the
reference — the whole point is that these four exist nowhere else. Commit them into
`reference/house-addendum.md`, then run the generator.

**Do not carry anything else across.** The addendum's closing section lists what must stay
out: variable order, abbreviation tables, `Find('-')` vs `FindSet()`, `NoImplicitWith`,
language features, analyzer codes, JSON, namespaces, `DataClassification`. Every one of those
is where the old file contradicted the reference. That ~250 lines of restatement **is** the
drift, and re-importing it would rebuild the problem inside the generated file.

**Then, on this box:**

- Point `~/.claude/CLAUDE.md:17` at the generated `~/larry-setup/reference/AL_RULES.md`.
- Delete `~/.claude/AL_RULES.md` and `C:\Repos\DevOps\WorkPrompts\claude\AL_RULES.md`.
- Delete or regenerate `~/claude-handover/AL_RULES.md` — it is the copy that had already
  diverged (`2a266067…` against `94b8960d…` for the other two).

One tracked copy, generated. Nothing to re-sync each quarter.

## 5. WorkPrompts — recommendation: leave it mirroring `tooling/` only

Dave chose **the KB endpoint as the source** for thin clients, which settles this. Do not
mirror `reference/` into WorkPrompts.

Reasoning: a second tree is the same mechanism that produced this whole handover. `AL_RULES.md`
drifted because a copy existed with nothing to keep it in step, and `md2pdf` drifted into three
variants the same way. Adding a 1-2 MB `reference/` mirror to keep current via `export.ps1`
buys offline access at the cost of reintroducing exactly that.

The prompts now search the KB and name a topic file as the offline fallback (§1), so a client
with a LAN route needs no local copy at all.

**Residual risk, stated plainly:** a box restored from WorkPrompts alone, with no LAN route to
Larry, has no AL reference — `/al`, `/bc-agent`, `/spec` and `/bc-analysis` degrade to
ungrounded. They will now *say* so rather than pretending, which is the part that was actually
dangerous. If that scenario becomes real rather than theoretical, the fix is to clone
`larry-setup` on the restored box, not to mirror a second copy of `reference/` into
WorkPrompts.

## 6. Add this to the WorkPrompts README — deb cannot reach that repo

Your §5 note was right and the risk is one step wider than I wrote it: with
`WorkPrompts/claude/AL_RULES.md` deleted, a WorkPrompts-only restore now has no AL ruleset
**and** no reference. So the recovery path for that box changed, and it currently exists only
in these transcripts.

`C:\Repos\DevOps\WorkPrompts` is not reachable from deb, so paste this into its README
yourself — it is written to drop in as-is:

```markdown
## What this repo is, and is not

WorkPrompts backs up this workstation's **Claude and pi configuration** — the `tooling/`
side of `larry-setup`. It deliberately does **not** mirror `reference/` or `pipeline/`.

**Restoring from WorkPrompts alone does not give you a working setup.** Clone
`larry-setup` as well:

    git clone <larry-setup remote> ~/larry-setup
    bash ~/larry-setup/tower/handoff-scripts/relink-tooling.sh

Two things live only in `larry-setup` and have no copy here:

- **`reference/AL_RULES.md`** — the AL house ruleset. It is GENERATED from
  `reference/al-reference/` plus `reference/house-addendum.md`; regenerate with
  `python3 pipeline/al_rules_gen.py`. The hand-written copy that used to sit in
  `WorkPrompts/claude/AL_RULES.md` was deleted on 2026-08-28 because it had drifted 4.3
  months out of step and contradicted the reference on four rules.
- **`reference/al-reference/`** — the AL topic files that `/al`, `/bc-agent`, `/spec` and
  `/bc-analysis` read. Thin clients normally reach these through the KB endpoint on Larry
  (`kb search --corpus al-reference`); the prompts fall back to reading the files directly
  and will TELL you when they are ungrounded.

**Why there is no second copy here.** A mirrored tree with nothing keeping it in step is
exactly what produced the stale `AL_RULES.md` — and the three divergent `md2pdf` variants
before it. One tracked copy in `larry-setup`, reached over the LAN or by cloning, is the
deliberate choice. See `tower/HANDOFF-windows-al-ruleset-return.md` §5 in that repo.
```

---

## What deb changed, in order

| Commit | What |
|---|---|
| `34b1f3f` | kb-client-setup: both token destinations, bash branch, per-source verification |
| `1faa3bd` | `GetText` corrected, `al-reference` re-indexed |
| `92b64ce` | tower handbook re-verified against the live box |
| `494378c` | prompts grounded on the KB instead of dead section numbers |
| `670c585` | `al_rules_gen.py` + the addendum stub + two tests |

Suite 240/241 (one pre-existing skip: no symbols).

## Verify on your side

```sh
cd ~/larry-setup && git pull --ff-only
bash tower/handoff-scripts/kb-client-setup.sh    # expect HTTP 200 on every source
kb stats                                         # expect the corpus table, not a 401
grep -n 'KB_REMOTE_TOKEN' ~/.bashrc              # expect NOTHING after you remove line 27
python3 pipeline/al_rules_gen.py                 # expect it to refuse until §4 is done
```

Report back: whether your token was the 32-character pre-rotation one, and the addendum
committed. **Not the token itself, in any form.**

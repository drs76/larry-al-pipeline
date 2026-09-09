# ste — Simplified Technical English (ASD-STE100) writing kit

> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

The sentence-level half of the house documentation style. `DOC-STYLE.md` says how a document is
shaped. This kit says how each sentence in it is written.

| File | What it is |
|---|---|
| `SKILL.md` | The skill itself. Two registers: **strict** (procedures, runbooks, user-guide steps, error messages) and **flavored** (handbooks, READMEs, reference docs) |
| `ste-recurring-errors.md` | The spec's own list of the 39 most frequent writer errors, with approved replacements |
| `ste-lint.py` | Heuristic linter over the machine-checkable subset. Deterministic — the score delta between two drafts is the signal |

## Run the linter

```bash
python3 $SETUP_DIR/tooling/ste/ste-lint.py your-draft.md
```

```bash
python3 $SETUP_DIR/tooling/ste/ste-lint.py --strict your-draft.md
```

Score is violations per 100 words — lower is cleaner. Targets: flavored under **2.5**, strict under
**1.5**. `--json` for machine-readable output, `--fail-over N` to exit 1 over a threshold (CI gate,
pre-commit hook). Python 3 only, no dependencies.

## Entry points

| Where | Path | Effect |
|---|---|---|
| Claude skill (auto-triggers) | `~/.claude/skills/ste-writing/SKILL.md` → `SKILL.md` | Claude picks it up on any "make this read less like AI" request |
| Claude slash command | `~/.claude/commands/ste.md` → `../tooling/ste.md` | `/ste rewrite strict docs/quickstart.md` |
| pi prompt | `~/.pi/agent/prompts/ste.md` → `../tooling/ste.md` | `pi /ste …` on Larry, no egress |

Install (idempotent):

```bash
mkdir -p ~/.claude/skills/ste-writing && ln -sfn $SETUP_DIR/tooling/ste/SKILL.md ~/.claude/skills/ste-writing/SKILL.md && ln -sfn $SETUP_DIR/tooling/ste/ste-lint.py $SETUP_DIR/tooling/ste/ste-recurring-errors.md ~/.claude/skills/ste-writing/ && ln -sfn $SETUP_DIR/tooling/ste.md ~/.claude/commands/ste.md && ln -sfn $SETUP_DIR/tooling/ste.md ~/.pi/agent/prompts/ste.md
```

## Why it is here

Measured effect of giving a model a writing system, from the source experiment (violations per 100
words, lower is better):

| Condition | Claude Sonnet | gpt-5.5 |
|---|---|---|
| baseline | 4.36 | 3.54 |
| banned-words list | 4.21 (-3%) | 2.14 (-40%) |
| Orwell's 6 rules | 2.48 (-43%) | 1.69 (-52%) |
| STE skill | 1.12 (-74%) | 1.76 (-50%) |

A banned-words list is the least reliable fix. A writing *system* cuts slop by half or more on every
model tested. Those numbers were measured with linter score v1. The shipped linter reports v2 — the
two are close but not directly comparable.

## House deviations from the source kit

1. **British spelling stays.** STE rule 1.14 asks for American spelling. Existing docs here use
   `analyse` / `behaviour` / `optimise`, so the skill keeps whatever the file already uses.
2. **DOC-STYLE wins on structure.** STE governs wording only. It never licenses the removal of a
   grounded detail — a file:line, a benchmark number, a failure mode.
3. **Register defaults are set per document class** (flavored for reference docs, strict for
   procedures) instead of being asked for each time.

## Provenance

Distilled skill, linter and the 39-error table come from
<https://github.com/woosal1337/blog/tree/main/videos/ep01-the-cure-for-ai-slop> ("The cure for AI
slop is a 1986 aircraft manual"), fetched 2026-08-10. `ste-lint.py` and `ste-recurring-errors.md` are
verbatim copies. `SKILL.md` adds the house deviations above.

Not a certified STE checker — the judgment rules of ASD-STE100 need a human, and this covers the
mechanical subset where the slop lives. Unofficial and not affiliated with ASD. ASD-STE100 is a
registered EU trademark (No. 017966390). Spec is free at <https://asd-ste100.org>.

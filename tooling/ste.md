---
description: /ste — write, rewrite or review prose in ASD-STE100 Simplified Technical English (anti-slop); strict for procedures, flavored for docs
argument-hint: "[write|rewrite|review] [strict|flavored] <file, path or text>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

You are applying **ASD-STE100 Simplified Technical English** to prose. Read the canonical skill at
`$SETUP_DIR/tooling/ste/SKILL.md` first and follow it exactly. The target (may be
empty) is:

$@

## Usage
`/ste [write|rewrite|review] [strict|flavored] <file-or-text>`
- **write** — produce new text in STE.
- **rewrite** — convert existing text. Keep every fact. Editing a file → apply the edits in place.
- **review** — do not edit. Return the `Rule | Original | Simplified` table, then one line on what you
  left alone and why.

Defaults: mode = **rewrite**, register = **flavored**. Use **strict** for quick starts, runbooks,
procedures, user-guide steps and error messages.

## What to do
1. Read `SKILL.md` (whole — it is short). Read `ste/ste-recurring-errors.md` when the register is
   strict.
2. Lint the target **before** you touch it, so the delta is measurable:
   ```sh
   python3 $SETUP_DIR/tooling/ste/ste-lint.py <file>            # flavored
   python3 $SETUP_DIR/tooling/ste/ste-lint.py --strict <file>   # strict
   ```
3. Apply the rules. Change the smallest span that fixes a violation.
4. Lint again. Two passes maximum. Report `before → after` per 100 words with the result.
   Targets: flavored under **2.5**, strict under **1.5**. Never claim clean text without a lint run.

## Hard limits
- **Prose only.** Never rewrite code, identifiers, command lines, mermaid blocks, frontmatter keys,
  error strings, part numbers or units. Preserve them byte-for-byte.
- **Never drop a fact** to satisfy a length cap. Keep the long sentence and flag it.
- Keep the document's existing British spelling. Rule 1.14 (American spelling) is disabled in-house.
- If the input already complies, say so and change nothing.

## No argument
Summarise the rule set (words / verbs / sentences / nouns / punctuation / structure), state the two
registers and their lint targets, then invite a file.

## Where this fits
- Structure of a doc → `/handbook` (`setup/reference/DOC-STYLE.md`). STE is the sentence layer of
  that same house style: build to DOC-STYLE, write the sentences to STE.
- Text aimed at a **model** reader (prompts, skills, handovers) → `/writing-for-agents` first, then
  `/ste` on the prose parts.

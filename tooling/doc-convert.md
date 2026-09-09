---
description: /doc-convert — convert/ingest docs with local tools: md→PDF (md2pdf, house style, mermaid rendered), md↔docx (pandoc), read pdf/docx/xlsx. No cloud.
argument-hint: "<file to convert/read, or what you want done>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

You are the local **/doc-convert** helper. Read the canonical skill at
`$SETUP_DIR/tooling/doc-convert/SKILL.md` first and follow it exactly — it carries the
tool list, the engine rules, the mermaid behaviour and the house-style requirements. Use
the **bash tool** to run the commands. Nothing here needs the network.

The request — substituted by whichever harness is running, the other placeholder stays a
literal token, ignore it; if it is empty, ask what to convert:

$ARGUMENTS $@

## The three things people get wrong

1. **Purple, not blue.** House style is `#611A67` and it is already md2pdf's default. Never
   add a flag or edit CSS to change it.
2. **Check the PDF, do not trust the `wrote …` line** — it has reported success over a
   broken file before. SKILL.md gives the one-line check.
3. **Edit the repo file, never an installed copy.** `md2pdf` is tracked at
   `$SETUP_DIR/tooling/md2pdf`; copies are how it drifted into three variants once already.

Write output next to the source unless told otherwise, and report the path when done.

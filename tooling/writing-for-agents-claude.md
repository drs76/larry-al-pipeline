---
description: Rewrite anything an agent READS (handover prompts, CLAUDE.md/AGENTS.md, skills, pi prompt-templates) so it reads well to a model — concise, trigger-first, de-frontloaded
argument-hint: "<file or text to sharpen for an agent audience>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

# /writing-for-agents — sharpen text for a model reader (Claude is the editor)

Read and follow the canonical instructions at
`$SETUP_DIR/tooling/writing-for-agents.md` (ignore its pi-specific `$@` placeholder —
the target is below).

The file or text to sharpen is:

$ARGUMENTS

Notes for this entry point:
- If empty, ask which file/text to sharpen (one line) before starting.
- Editing a file → Read it fully first, apply edits in place, and keep every machine-parsed block,
  required heading, frontmatter key, and exact identifier byte-for-byte unless correcting a verified
  error. Loose text → return the rewrite.
- Always end with the one-line-per-change list the canonical Deliver step specifies.

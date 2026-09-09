---
description: Turn a spec/warplan grilling (its decisions + open questions) into a standalone markdown questionnaire a non-agent human can answer, then fold the answers back in
argument-hint: "<session/spec/ledger to export, or the topic to question on>"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

# /to-questionnaire — export a grilling to a human-answerable doc (Claude runs it)

Read and follow the canonical instructions at
`$SETUP_DIR/tooling/to-questionnaire.md` (ignore its pi-specific `$@` placeholder —
the source is below).

The session / spec / ledger to export (or topic to question on) is:

$ARGUMENTS

Notes for this entry point:
- If empty, ask what to export (a spec/ledger path, or a topic) before starting.
- If a `docs/SPEC.md` or `war-plans/*/ledger.md` exists, Read it and pull the open items from there
  rather than re-interviewing.
- Write `docs/QUESTIONNAIRE.md` exactly as the canonical Step 2 specifies (plain-language, Recommended
  + Answer per item). Then STOP at hand-off — do not build. Re-import (Step 4) is a later, separate run
  once the answers come back.

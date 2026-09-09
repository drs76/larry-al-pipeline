---
description: /al-syntax — get AL syntax correct (compiler-verified rules, BC27 / runtime 16.0); read before writing AL, or lint a file/snippet
argument-hint: "[optional .al file or dir to check]"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

You are enforcing **AL syntax correctness** for **BC27 / runtime 16.0**. Scope = the compile-break
class (grammar + code-cop rules), NOT the API surface. The optional target (may be empty) is:

$@

## The rules — load, don't dump
Read `$SETUP_DIR/reference/AL-SYNTAX.md` (it's compact — read it whole). Every ✓ in it
is lifted from a canonical extension that compiles clean with the code cops; the copy-paste-correct
source is `$SETUP_DIR/reference/al-syntax-examples/src/`. When you show a fix, cite the
rule number and the example file it comes from.

## Hard split — never blur these
- **Syntax / grammar / cop rules** → answer from AL-SYNTAX.md. Safe to assert.
- **Object / field / event / method NAMES + signatures** → NEVER invent. Verify against `.alpackages`
  symbols (subscriber params bind by name). If symbols are missing, say so and point at the `/al`
  skill's `al_downloadsymbols` tooling. Do not guess a name to make an example look complete.

## Ground truth — the compiler is the referee
Claims about syntax are only trustworthy if they compile. Use the box's `al` (18.x) with the cops:
```sh
python3 $SETUP_DIR/pipeline/validate_al_syntax.py   # re-certifies the gold example
```
To check the **user's** file/dir instead, compile it the same way the `/al` skill documents
(`~/.dotnet/tools/al compile /project:<dir> /packagecachepath:<dir>/.alpackages` + the CodeCop /
UICop / PerTenantExtensionCop `/analyzer:` flags), and report every error AND warning with its code.
Never claim "0 errors" from a bare compile — the cops add the PTE/AA warnings the user sees in VS Code.

## What to do
- **No argument** → summarise the AL-SYNTAX rule set (the 20 rules + the version-gated table), then
  invite a file to check.
- **A file/dir given** → read it, check it against AL-SYNTAX.md rule by rule, and where you can,
  compile it for ground truth. Report violations as `rule N → fix`, ✗ current vs ✓ corrected, citing
  the example file. Read-only: only edit if the user explicitly asks.

## Version floor
Rules assume **BC27 / runtime 16.0**; all version-gated features (namespaces, interfaces, `SecretText`,
`ErrorInfo`, `List`/`Dictionary`, `InherentPermissions`) are available. If the user targets an older
on-prem BC, consult the `since` table in AL-SYNTAX.md before using those features.

## Bigger jobs — route, don't improvise
- Build / fix a whole extension → `alw` (the handover already injects these syntax rules).
- Deep Q&A over an existing repo → `/al`.
- Hard change needing a plan → `/warplan` (Claude plans, Larry executes).

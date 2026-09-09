---
description: /bc-webservice-audit — audit a BC customer's published web services against the Microsoft OData/SOAP deprecation (SOAP gone at v29, OData at v30) and produce a customer-facing impact assessment PDF
argument-hint: "<path to the Web Services export .tsv/.csv> [customer name]"
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

Read and follow the canonical instructions at
**`$SETUP_DIR/tooling/bc-webservice-audit/SKILL.md`** — read it now, before doing anything
else. It carries the classification rules, the deprecation matrix, the deliverable
structure and the house-style requirements. This file only routes you there.

The invocation — an export path and/or customer name, either may be empty — is substituted
by whichever harness is running; the other placeholder stays a literal token, ignore it:

$ARGUMENTS $@

If nothing was supplied, ask for the **Web Services export** first: in Business Central,
search `Web Services`, then **Share → Open in Excel**, saved as `.tsv` or `.csv`. Required
columns are `Object Type`, `Object ID`, `Object Name`, `Service Name`; keep `All Tenants`
and `Published` if present — `All Tenants` is load-bearing.

The classifier is at `$SETUP_DIR/tooling/bc-webservice-audit/classify.py`; run it with the
bash tool. `python <path>/classify.py --help` lists its flags.

## Two things the skill file assumes

- **Customer data.** An export is customer material. Keep it local — `anon policy` should
  read `local-only` in any work repo, and nothing here needs egress.
- **Deliverable location.** SKILL.md names a OneDrive `Technical Analysis` folder for the
  finished PDF. That path exists on the Windows workstation only. Elsewhere, write the
  deliverable beside the export and tell the user where it landed rather than inventing a
  path.

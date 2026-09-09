---
description: Analyse a Microsoft Business Central AL extension codebase and produce a technical Wiki and Performance Improvements report for a consulting engagement.
argument-hint: "[customer-subfolder]"
allowed-tools: Read, Grep, Glob, Write, Bash
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).


# BC Extension Analysis Skill

Target codebase subfolder (if provided) — one of these is substituted by whichever
harness is running, the other stays a literal token; ignore the leftover:

$ARGUMENTS $@

## Purpose

Analyse a Microsoft Business Central AL extension codebase. The customer's AL source files sit in a subfolder (e.g. `CustomerName_vX.X.X.X/`). Produce two documents inside that subfolder: `WIKI.md` and `PERFORMANCE_IMPROVEMENTS.md`.

A third document (e.g. `DUPLICATE_INVOICE_FIX.md`) is only needed if we are writing a specific fix — do not produce it by default.

---

## Read Strategy — Token Efficiency

**Do not read every file. Work in passes.**

### Pass 1 — Orientation (always do this first)

Read only:
- `app.json` — publisher, version, object ID range, dependencies
- Any `*Install*.Codeunit.al` or `*Setup*.Codeunit.al` — install-time configuration

Then list all AL files:
```
Glob: **/*.al
```
Mentally group the file list into: Codeunits | Tables | TableExts | Pages | PageExts | Reports | XMLPorts | Enums

### Pass 2 — Codeunits (highest value)

Read all codeunits — they contain ~80% of the logic. Skip XMLPorts on this pass.

### Pass 3 — Tables and TableExts (field inventory)

Read Table files for custom entities. For TableExts, grep rather than full-read:
```
Grep: field\([0-9]+;
```
This finds all custom fields across all TableExts in one pass.

### Pass 4 — Pages (only if needed)

Read Page/PageExt files only if:
- Documenting a specific UI workflow for the Wiki
- Investigating an action or promoted button for a fix doc

Skip Report and XMLPort files unless referenced in a performance issue.

### Grep Before Reading

Before reading a full file, try grep first:

| Question | Grep pattern |
|---|---|
| Where are HTTP/CRM calls made? | `HttpClient\|RegisterConnection\|CRMInvoice.Get\|Dataverse` |
| Where are event subscribers? | `\[EventSubscriber\]` |
| Where are long loops with no commit? | `FindSet` |
| Where is SetAutoCalcFields used? | `SetAutoCalcFields` |
| Where are TryFunctions? | `\[TryFunction\]` |
| What SetCurrentKey calls exist? | `SetCurrentKey` |
| Where are job queue codeunits? | `trigger OnRun` |

---

## Efficiency Rules

1. **Glob before Read** — always list files before reading any.
2. **Grep before Read** — if looking for a specific pattern, grep first; read only matching files.
3. **Read codeunits top-to-bottom once** — don't re-read to verify a detail.
4. **Skip XMLPorts on first pass** — they are import/export schemas and rarely affect Wiki or performance analysis.
5. **Skip Report files unless** they appear in a performance finding or are called from a job queue.
6. **Do not read Page files for the Object Inventory** — derive the name from the filename; read only if the page has non-trivial logic.
7. **Write documents in one pass** — draft each section from your notes and move on.

---

## WIKI.md — Required Sections

Always include all nine sections. Expand or contract depth based on complexity.

```
1. Overview
   - Customer name, business purpose, BC version, object ID range

2. Architecture Summary
   - ASCII diagram of major components and data flow

3. [Functional Area 1] — e.g. Direct Debit, CRM Integration
   - Purpose
   - Core Tables (ID | Name | Description)
   - Codeunits (key procedures, event subscribers)
   - Pages (if UI is non-trivial)

4. [Functional Area 2] ...

5. End-to-End Business Process Flows
   - Numbered step flow for each major process
   - Use ASCII art, not Mermaid diagrams

6. Job Queue Entries
   - Table: Job | Codeunit | Recommended Frequency | Description

7. Configuration & Setup
   - Key setup tables and fields

8. Web API / OData Pages (if any)

9. Object Inventory
   - Tables | Codeunits | Reports | Pages | XMLPorts | Enums (ID | Name | Purpose)
```

**Write the Object Inventory last** — it is mechanical and can be drafted from the Glob file list without re-reading files.

---

## PERFORMANCE_IMPROVEMENTS.md — Checks To Run

Work through these in order. Each check has a grep to run first.

### 1. N+1 Database / HTTP Calls in Loops

Grep `FindSet`, then inspect each matching codeunit for `Get(` or `Find` inside the loop body.
Also grep `CRM.*\.Get\(` — each hit is a live Dataverse HTTP call per record.

**Red flag**: Any `.Get(` or `FindFirst` inside a `repeat...until` block.

### 2. Long Transactions Without Commits

Grep `FindSet`. Check whether `Commit()` appears inside or after the loop.

**Red flag**: A loop that posts invoices, modifies mandates, or inserts journal lines with no `Commit()` between records.

### 3. SetAutoCalcFields Inside FindSet Loop

Grep `SetAutoCalcFields`. Check whether it is called before a `FindSet` loop.

**Red flag**: FlowField backed by a CRM or Integration table — each row triggers a coupling lookup.

### 4. Missing Indexes

Look for `SetRange` / `SetFilter` on fields not part of any key. Common culprits:
- `"Order No."` on Sales Invoice Header/Line
- `"Your Reference"` on Sales Invoice Header
- Custom Code fields used for filtering but not declared as keys

**Fix**: Add keys to the TableExt for the standard table.

### 5. SetCurrentKey Mismatch

Grep `SetCurrentKey`. Verify the key matches the filter fields that follow.

**Red flag**: `SetCurrentKey("Field A", "Field B")` followed by `SetFilter("Field C", ...)` — the index is unused.

### 6. HTTP Timeout Configuration

Grep `HttpClient`. Note whether `HttpClient.Timeout` is explicitly set.
For standard CRM integration, note that timeouts are a BC server config setting, not AL code.

### 7. Job Queue Reliability

Check job queue codeunits (`trigger OnRun`) for:
- Whether `Commit()` saves progress incrementally (watermark pattern)
- Whether retry is possible without reprocessing all records
- Whether one failing record halts the entire batch

### Finding Template

Each finding must use this structure:

```
### Issue N — [Short title]
**Location**: Codeunit/Table name and relevant procedure
**Root Cause**: What the code does and why it is a problem
**Impact**: Business/performance consequence
**Recommendations**:
  - Short term (config change, no code)
  - Medium term (code change, with example snippet)
```

End the document with a Priority Summary Table:

```
| # | Issue | Files Affected | Severity | Effort |
```

---

## Patterns To Recognise

Common patterns in KPMG/SLG-style BC extensions. Check for these proactively.

| Pattern | Where to look | Note |
|---|---|---|
| Order-split retry bug | `Process Sales Order` style codeunits | Duplicate invoice risk if no idempotency guard |
| Deferred income | `SLG Deferral` style codeunits | Check for rounding residual in last period |
| CRM update watermark | `CRM Synch Status` or similar | Check whether watermark advances per-batch or only on full success |
| Auto-post journal batches | `Auto Post` flag on Gen. Journal Batch | Check for concurrent run protection (LockTable) |
| Mandate singleton rule | SEPA Direct Debit Mandate | Verify only one non-blocked mandate per bank account is enforced |
| ADDACS/ARUDD loop | File import codeunits | Check for commits between records to reduce deadlock window |

---

## Output Quality Rules

- Use **tables** for object inventories — never bullet lists.
- Use **ASCII diagrams** for architecture and flows — Mermaid is not reliably rendered in all viewers.
- Object IDs must be **accurate** — take them from the actual AL file declarations, not filenames.
- Do **not** document XMLPort field-level detail unless explicitly asked.
- Write the Wiki for a **developer who is new to this customer** — assume BC knowledge, not customer knowledge.
- Write Performance findings for a **consultant** presenting to the customer — include business impact, not just technical detail.

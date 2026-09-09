---
name: bc-webservice-audit
description: >
  Audit a Business Central customer's published web services against the Microsoft
  OData/SOAP deprecation (Microsoft pages lose SOAP at v29, OData at v30) and
  produce a customer-facing impact assessment PDF in house style.
  Classifies every endpoint by publisher, separates Microsoft-feature plumbing from
  the real review list, finds dead rows, and names the endpoints that stop working.
  Trigger when a customer asks "are we affected by the OData deprecation", "which
  web services break", "do we need to change our integrations", when somebody sends
  a Web Services page export to review, or on any mention of obsoleted/deprecated
  OData or SOAP endpoints in Business Central.
---
> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).


# BC web service deprecation audit

## What you need from the customer

1. **The Web Services export.** Ask them to open Business Central, search `Web Services`, then **Share → Open in Excel**. They send the sheet. Save it as `.tsv` or `.csv`.
   Required columns: `Object Type`, `Object ID`, `Object Name`, `Service Name`. Keep `All Tenants` and `Published` if present — `All Tenants` is load-bearing.
2. **Their AL source folder**, so the script learns their own `idRanges` and publisher from every `app.json`.
3. **Their BC version** (Help → About gives the full build string). Put it verbatim in the document header.

Ask for all three up front. Do not start with only the export.

## Where the output goes

All deliverables go in a per-customer subfolder of the Technical Analysis library:

```
C:/Users/Dave.Sinclair/OneDrive - Technology Services Group Ltd/Documents/Customers/Technical Analysis/<Customer>/
```

Create the customer subfolder if it does not exist. Use the customer's short name, the same one used elsewhere in `Documents/Customers` — `HCPC`, not `Health and Care Professions Council`.

Put both files there:

- `<Customer>-OData-Deprecation-Impact-Assessment.md` — canonical source, no date in the name, edited in place across versions.
- `<Customer>-OData-Deprecation-Impact-Assessment-YYYY-MM-DD.pdf` — dated on every build, so earlier issues stay available.

Keep working files (the export `.tsv`, `classify.py` output, telemetry workbooks) out of that folder. They belong in the scratchpad or alongside the customer's source. The Technical Analysis folder holds deliverables only.

Do **not** write the document into the customer's code repository or into a versioned extension folder. Those get archived, restored and copied around, and the analysis then ships to the wrong audience.

## Run the classifier

```bash
python $SETUP_DIR/tooling/bc-webservice-audit/classify.py EXPORT.tsv \
  --repo /path/to/customer/al-repo \
  --isv "Continia Software:6085998-6086087,6225270-6225278" \
  --json out.json --md fragments.md
```

`--repo` is repeatable, one per extension. `--isv` is repeatable, for ISV ranges that are not in the local source. The script prints counts, writes a JSON summary, and writes ready-made markdown tables.

**Never count by hand.** Take every number from the script. Hand-counting is where this goes wrong.

Add `--isv` for any publisher the script reports as UNCONFIRMED, once you have identified them. Do not silently treat an unconfirmed range as safe.

## The deprecation facts

Grounded in [Deprecated features — platform](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/upgrade/deprecated-features-platform). Re-read it before writing; dates move.

| Version | Wave | What goes |
| --- | --- | --- |
| 26.0 | 2025 W1 | SOAP on Microsoft pages off by default, feature key can re-enable |
| 29.0 | 2026 W2 | **SOAP on Microsoft objects removed**, feature key deleted |
| 30.0 | 2027 W1 | **OData on Microsoft pages removed** |

Microsoft's own scope wording: *"it's no longer possible to expose a Microsoft page as an OData endpoint. A Microsoft page is a page that is created in an app with the publisher Microsoft."*

What is **not** affected: OData v4 itself, API pages under `/api/`, authentication, Dataverse/CRM sync, table extensions. Queries are not named in the notice — treat as probably safe, tell the customer to confirm with Microsoft, never assert it.

## Traps — every one of these has already cost a rework

- **A page extension does not change a page's publisher.** Microsoft page + customer fields is still a Microsoft page. Copying to the customer ID range is the fix, and the bespoke fields must be re-declared in the copy because the extension targets the original.
- **The Object Name column shows the object CAPTION, not the object name.** Diffing it against AL source produces phantom "production does not match source" findings. Match on Object ID only.
- **Load every row type.** Page, Codeunit and Query. Dropping queries silently deflates the total and the dead-row count.
- **`All Tenants = TRUE` proves Microsoft created a row. `FALSE` proves nothing** — a stock install writes tenant rows too. So Group B is a *review* list, an upper bound. Never write "created deliberately for HCPC" or similar. The clean-environment export is the only thing that settles origin.
- **A blank Object Name means the object no longer exists.** Dead registration, safe to unpublish.
- **The service name lives in the URL, not the page name.** Unpublish the old row, publish the copy under the identical service name, and the customer's application needs no change. This is the single most valuable point in the whole document — lead with it.
- **The OData property name is generated from the page field**, spaces and punctuation become underscores. Do not assert whether caption or control name drives it. Tell them to diff `$metadata` old vs new before cut-over — that test is correct either way.
- **Grep AL case-insensitively.** Files use both `page 50100` and `Page 50100`. A case-sensitive grep drops objects and invents "missing from source" findings.
- **Verify before you write a finding.** Open the file. A grep that looks incomplete *is* incomplete.

## Writing the document

Use the `handbook` skill for structure and STE for sentences. Copy the shape of the HCPC original at
`.../Documents/Customers/Technical Analysis/HCPC/HCPC-OData-Deprecation-Impact-Assessment.md`.

Section order that worked: header table → document map → status callout → one-idea box → what this tells you → quick start (how a developer finds their own endpoint) → core constraint with Microsoft's own quote → what it is *not* → capability comparison → Figure 1 timeline → Figure 2 classification flowchart → Group B table → Group A families → SOAP codeunits → sharp edges → two remediation options → commercial position → maintenance timeline → provenance → appendices → glossary.

**The Group B table is the centrepiece.** Service name in the first column so somebody can `Ctrl-F` their application config against it. State the URL prefix once above it.

**Two remediation options, both chargeable:**
- *Option 1, copy the page.* URL unchanged, customer's application unchanged, fastest, but it stays a UI page and the fields are then maintained in two places.
- *Option 2, move to the [API v2.0](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/).* Recommended. Standard entities need no BC build. Argue it with Microsoft's own quotes about fact boxes consuming resources they never return, not with invented benchmark numbers. Say plainly that the client moves to atomic REST — one resource per call, JSON, no WSDL or generated proxy, ETag `If-Match` concurrency, `$batch` for multi-record. That cost lands on the integration partner and we cannot quote it.

## Commercial framing

This is a **support response**, not paid analysis. Say so in point 1. Then:

- We run the telemetry query and supplies the output; customer welcome to run it too. Note any time limit on our telemetry access.
- Everything beyond that is booked, chargeable developer time.
- Every endpoint needs a specification before conversion — fields, property names to preserve, verbs, filters, `$metadata` test evidence.
- **No quote until origin and traffic are known.** Group B is an upper bound; the real number is far lower.
- Housekeeping (dead rows, dormant extensions) is separable and free for the customer to do.

**No `TODO(grounding)` markers in a customer document.** They read as unfinished homework. Convert each one into either a plain scope statement ("this assessment does not cover X") or a chargeable next step.

## Telemetry

```kusto
traces
| where timestamp > ago(30d)
| where customDimensions.eventId == "RT0008"
| where tostring(customDimensions.extensionPublisher) == "Microsoft"
| where tostring(customDimensions.alObjectType) == "Page"
| extend hdrs = parse_json(tostring(customDimensions.httpHeaders))
| summarize calls = count(), lastCall = max(timestamp),
            agents = make_set(tostring(hdrs.['User-Agent']), 5)
    by endpoint = tostring(customDimensions.endpoint),
       objectId = tostring(customDimensions.alObjectId),
       objectName = tostring(customDimensions.alObjectName)
| order by calls desc
```

`RT0053` carries the deprecation warnings BC already raises.

**Always state the window in the document, and size the claim to it.** A 30-day window is common, but check WHY before you write it up. The Business Central telemetry Power BI app loads a fixed number of days from Application Insights, 30 by default, and that is a report parameter — not the limit of the stored data. Application Insights normally retains longer. So when a customer hands you 30 days of Power BI output, the fix is free: raise the report parameter, or run the KQL directly against Application Insights over 90 days. Do that BEFORE anyone unpublishes anything on the strength of a silent endpoint. Over 30 days a monthly process can fall outside the window, a quarterly one appears about one time in three, and an annual one almost never. So "no traffic" means "no traffic in N days", never "unused". Say that next to every silent-endpoint claim, and recommend a second run closer to cut-over.

Read the oldest timestamp in the result and check it matches the period requested — Application Insights can silently return less history than the query asks for.

**Telemetry records that a call happened, not which application made it.** Attribution is the customer's integration partner's job, not yours. Put it in the document as an action for them. If the customer wants you to establish it from the BC side, that is chargeable, and it is slower — it needs a `User-Agent` header added to the partner's requests and then time for traffic to accumulate.

Ask for the export filtered per publisher. A `Publisher` filter in the telemetry UI produces one sheet per publisher, which maps straight onto the classification and makes the safe-versus-affected split self-evident.

## Produce the PDF

Run from the customer's Technical Analysis folder:

```bash
md2pdf "<Customer>-OData-Deprecation-Impact-Assessment.md" "<Customer>-OData-Deprecation-Impact-Assessment-YYYY-MM-DD.pdf" "SinclairSoftScotland - <Customer> OData Deprecation Impact Assessment v1.0 - <date>"
```

`md2pdf` pre-renders ```mermaid fences via `mmdc`. Then verify, every time:

```bash
python $SETUP_DIR/tooling/ste/ste-lint.py DOC.md   # target under 2.5
python - <<'PY'
import re, markdown
s=open('DOC.md',encoding='utf-8').read()
h=markdown.markdown(s,extensions=["fenced_code","tables","toc","sane_lists"])
ids=set(re.findall(r'id="([^"]+)"',h)); links=set(re.findall(r'href="#([^"]+)"',h))
print("broken anchors:", [l for l in links if l not in ids] or "none")
PY
```

**Anchor gotcha:** python-markdown collapses an em dash in a heading to a *single* hyphen, GitHub keeps a double. Link to `#se-9-the-export-...`, not `#se-9--the-export-...`, or every internal link is dead in the PDF. The check above catches it.

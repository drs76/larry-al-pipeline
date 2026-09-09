---
bc-version: [all]
domain: style
keywords: [tableextension, object-id, id-range, extends, 50100]
technologies: [al]
countries: [w1]
application-area: [all]
---

# A `tableextension` id is its own object id, not the extended table's number

> `PREFIX` in the examples below is a placeholder. Use the affix registered for the
> extension you are building — read it from the project's own `app.json` and existing
> object names. Never write the literal word `PREFIX`, and never copy an affix from a
> rule, an example or another project.


## Description

The numeric id on `tableextension <id> "Name" extends "Base"` must fall in the
extension's assigned object range (per-tenant custom range `50100..50299`, or the
licensed AppSource range). LLM coders often reuse the **base table's** number
(e.g. `1173` for Document Attachment), which is out of range and collides with the
platform object. The base table is referenced by name in `extends`, never by number.

## Best Practice

```al
tableextension 50110 "PREFIX Document Attachment" extends "Document Attachment"
{
    fields { field(50100; PREFIXBlobName; Text[250]) { DataClassification = CustomerContent; } }
}
```

## Anti Pattern

```al
tableextension 1173 "PREFIX Document Attachment" extends "Document Attachment"  // ✗ base-table id, out of range
```

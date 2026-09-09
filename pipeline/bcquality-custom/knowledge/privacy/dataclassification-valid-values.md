---
bc-version: [all]
domain: privacy
keywords: [dataclassification, AL0169, customercontent, table-field]
technologies: [al]
countries: [w1]
application-area: [all]
---

# `DataClassification` accepts only the seven valid values — `CompanyContent` is not one

## Description

Every table field (and the table) needs a `DataClassification`. The only valid values
are: `CustomerContent`, `EndUserIdentifiableInformation`, `AccountData`,
`EndUserPseudonymousIdentifiers`, `OrganizationIdentifiableInformation`,
`CompanyConfidential`, `SystemMetadata`. LLM coders frequently emit the invalid
`CompanyContent`, raising `AL0169`. When unsure, `CustomerContent` is the safe default.

## Best Practice

```al
field(3; StorageAccount; Text[250]) { DataClassification = CustomerContent; }
```

## Anti Pattern

```al
field(3; StorageAccount; Text[250]) { DataClassification = CompanyContent; }  // ✗ AL0169 — not a valid value
```

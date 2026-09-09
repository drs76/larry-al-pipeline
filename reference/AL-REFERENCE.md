# AL Reference — Syntax, Patterns & Conventions

Shared reference for AL (Business Central) development. Sources: MS learn best practices, alguidelines.dev, Microsoft BCQuality (github.com/microsoft/BCQuality), local AL examples.

**New project handover template:** `larry-handover.template.md` in this directory.

**Companion file:** [`AL-KNOWLEDGE.md`](AL-KNOWLEDGE.md) — platform, runtime, DevOps (AL-Go), dev
tooling, AI-resource billing and BC business-feature awareness. This file is what you *type*; that one
is the world around it.

---

## How to use this file

This is an **index**, not the content. The knowledge lives in [`al-reference/`](al-reference/) as topic files, each small enough to read whole.

**Read this index, then read only the topic file(s) you need.** Do not read every topic — together they far exceed a 32k context window. To search across all topics instead: `kb search "<query>" --corpus al-reference`.

## Topics

| Topic | Covers | Size |
|---|---|---|
| [`00-gotchas.md`](al-reference/00-gotchas.md) | LLM gotcha summary — READ FIRST | ~1.0k tok |
| [`01-syntax-style.md`](al-reference/01-syntax-style.md) | Formatting, naming, structure, variables, flow, abbreviations | ~1.8k tok |
| [`02-objects.md`](al-reference/02-objects.md) | Tables, codeunits, pages, reports, factboxes & control add-ins | ~6.5k tok |
| [`03-records-performance.md`](al-reference/03-records-performance.md) | Record operations, data access, SQL-level tuning, locking | ~6.8k tok |
| [`04-validate.md`](al-reference/04-validate.md) | Validate() triggers — behaviour, patterns, gotchas | ~1.5k tok |
| [`05-language-features.md`](al-reference/05-language-features.md) | Newer AL language features (what's-new rollups) | ~3.4k tok |
| [`06-http-client.md`](al-reference/06-http-client.md) | HttpClient, RestClient, mocking, JSON/YAML test utils | ~2.7k tok |
| [`07-events-errors.md`](al-reference/07-events-errors.md) | Events & subscribers, error handling, archiving, upgrade codeunits | ~4.2k tok |
| [`08-data-storage.md`](al-reference/08-data-storage.md) | Streams & blobs, isolated storage, Azure Blob Storage | ~1.6k tok |
| [`09-api-web.md`](al-reference/09-api-web.md) | API pages / web services, interfaces, permission sets | ~5.1k tok |
| [`10-quality-breaking.md`](al-reference/10-quality-breaking.md) | PTE conventions, signature verification, obsoletion, extra rules | ~5.0k tok |
| [`11-agents.md`](al-reference/11-agents.md) | AI agents in BC — functional concepts & setup | ~3.2k tok |
| [`12-agents-coding.md`](al-reference/12-agents-coding.md) | Coding agents in AL, agent testing, BC MCP server | ~7.0k tok |
| [`13-testing.md`](al-reference/13-testing.md) | AL test codeunits | ~0.6k tok |
| [`14-namespaces.md`](al-reference/14-namespaces.md) | Namespaces & `using` | ~4.9k tok |
| [`15-manifest-appjson.md`](al-reference/15-manifest-appjson.md) | `app.json` manifest & project config | ~1.6k tok |
| [`16-analyzer-rules.md`](al-reference/16-analyzer-rules.md) | Analyzer rules — `AS`/`AA`/`PTE`/`UI` diagnostic codes | ~6.7k tok |
| [`17-enums-enum-extensions.md`](al-reference/17-enums-enum-extensions.md) | enums & enum extensions | ~0.8k tok |
| [`18-table-page-objects.md`](al-reference/18-table-page-objects.md) | Table & page objects — Learn reference | ~4.7k tok |
| [`19-report-codeunit-query-objects.md`](al-reference/19-report-codeunit-query-objects.md) | Report, codeunit, query, XMLPort & control add-in objects — Learn reference | ~4.2k tok |
| [`20-arithmetic-operators-type-conversion.md`](al-reference/20-arithmetic-operators-type-conversion.md) | arithmetic operators & type conversion | ~1.5k tok |
| [`21-methods-parameters-return-values.md`](al-reference/21-methods-parameters-return-values.md) | methods, parameters & return values | ~0.8k tok |
| [`22-labels-multilanguage-text-constants.md`](al-reference/22-labels-multilanguage-text-constants.md) | labels & multilanguage text constants | ~0.7k tok |
| [`23-preprocessor-directives.md`](al-reference/23-preprocessor-directives.md) | preprocessor directives | ~1.1k tok |
| [`24-language-basics.md`](al-reference/24-language-basics.md) | AL language basics — operators, variables, statements, scope | ~5.8k tok |
| [`25-search-relational-full-text-semantic-al.md`](al-reference/25-search-relational-full-text-semantic-al.md) | search — relational, full-text & semantic (AL) | ~2.3k tok |

_Total across topics: ~86k tokens. Split from the former single file by `pipeline/split_knowledge.py`._

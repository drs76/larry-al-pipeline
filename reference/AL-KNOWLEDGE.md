# AL Knowledge — Platform, DevOps, Tooling & Feature Awareness

Companion to [`AL-REFERENCE.md`](AL-REFERENCE.md). That file is **AL coding syntax/patterns**; this
file is the surrounding **platform, runtime, DevOps, tooling and business-feature** knowledge a BC
developer/consultant needs but that isn't AL statements you type.

Sources: Microsoft BC/AL "What's new" + "Introducing" dev sessions (2023 w2 → 2026 w1), distilled from
raw transcripts (`~/Downloads/ms/transcripts/`, not committed). Microsoft Learn is the live truth —
verify specifics (esp. release-wave/version gates) before relying on them. Each entry carries its
source video for traceability.

> For AI **agents / coding agents / testing agents / BC MCP server** see AL-REFERENCE **§28–31**.
> This file's §5 adds only the AI-resources *platform/billing* layer (managed vs BYO, models, geo).

---

## How to use this file

This is an **index**, not the content. The knowledge lives in [`al-knowledge/`](al-knowledge/) as topic files, each small enough to read whole.

**Read this index, then read only the topic file(s) you need.** Do not read every topic — together they far exceed a 32k context window. To search across all topics instead: `kb search "<query>" --corpus al-knowledge`.

## Topics

| Topic | Covers | Size |
|---|---|---|
| [`00-mcp-tooling-openapi.md`](al-knowledge/00-mcp-tooling-openapi.md) | mcp-tooling-openapi | ~2.2k tok |
| [`ai-platform.md`](al-knowledge/ai-platform.md) | AI resources, agent platform, billing & models | ~0.6k tok |
| [`cicd-algo.md`](al-knowledge/cicd-algo.md) | CI/CD with AL-Go for GitHub | ~7.4k tok |
| [`developer-apis.md`](al-knowledge/developer-apis.md) | API pages, integration patterns, event grid master-data sync | ~5.2k tok |
| [`docs-pointers.md`](al-knowledge/docs-pointers.md) | Docs & learning pointers | ~1.6k tok |
| [`functional-features.md`](al-knowledge/functional-features.md) | Functional feature awareness | ~2.6k tok |
| [`indexes-sift.md`](al-knowledge/indexes-sift.md) | Table indexes, SIFT, NCCI, full-text, key ordering | ~1.8k tok |
| [`integration-powerplatform.md`](al-knowledge/integration-powerplatform.md) | Power Automate, Power Platform ALM, web hooks | ~4.1k tok |
| [`performance-concurrency.md`](al-knowledge/performance-concurrency.md) | Large customers, job queues, locking, BCPT | ~6.5k tok |
| [`performance-telemetry.md`](al-knowledge/performance-telemetry.md) | Performance sessions, telemetry & App Insights | ~7.0k tok |
| [`platform-runtime.md`](al-knowledge/platform-runtime.md) | Scale design, NuGet packaging, app packaging | ~7.5k tok |
| [`reporting-powerbi.md`](al-knowledge/reporting-powerbi.md) | Reporting, Power BI, Excel layouts | ~1.2k tok |
| [`testing-automation.md`](al-knowledge/testing-automation.md) | Test automation, mocking, datasets, code-review tooling | ~7.5k tok |
| [`testing-patterns.md`](al-knowledge/testing-patterns.md) | Page scripting, test doubles, Kiota clients, WireMock | ~5.2k tok |

_Total across topics: ~60k tokens. Split from the former single file by `pipeline/split_knowledge.py`._

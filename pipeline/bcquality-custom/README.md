# BCQuality custom layer — durable source

Our partner/AL-authoring knowledge rules for BCQuality. This is the **source of truth**;
the working BCQuality clone (`/mnt/rojaws/localDev/BCQuality`, upstream
github.com/microsoft/BCQuality) is disposable and its `custom/` dir is wiped on re-clone.

## Sync into the clone

```sh
cp -r knowledge/* /mnt/rojaws/localDev/BCQuality/custom/knowledge/
pwsh /mnt/rojaws/localDev/BCQuality/tools/Build-KnowledgeIndex.ps1   # reindex
```

## Rules (9)

Seeded from our AL-gotcha experience — the class of mistakes local coder models make
that the compiler only reports as downstream cascades:

- style/`using-directives-at-top-of-file` — #1 LLM failure (AL0104/0114/0107)
- style/`tableextension-id-in-object-range` — own object id, not the base table's
- ui/`controladdin-quote-resource-paths` — AL0219
- ui/`pageextension-layout-nesting` — `addlast` inside `layout { }`
- ui/`usercontrol-only-triggers-inside` — procedures at page scope
- error-handling/`tryfunction-no-return-type` — AL0244
- privacy/`dataclassification-valid-values` — `CompanyContent` invalid → AL0169
- events/`do-not-invent-event-subscribers` — AL0280/AL0282
- security/`secrets-in-isolatedstorage-not-table-field`

Schema per file: frontmatter (`bc-version/domain/keywords/technologies/countries/
application-area`) + `## Description` / `## Best Practice` / `## Anti Pattern`.

Consumed by `../bcquality.py` (selector) → `../coms_review.py` (reviewer injection) and
`../run-build.py` (coder-prompt injection). See `/mnt/rojaws/localDev/bcquality-integration.md`.

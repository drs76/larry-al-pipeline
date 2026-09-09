---
bc-version: [all]
domain: style
keywords: [using, namespace, directive, file-structure, AL0104, AL0114, AL0107]
technologies: [al]
countries: [w1]
application-area: [all]
---

# `using` directives go at the top of the file, never inside the object body

> `PREFIX` in the examples below is a placeholder. Use the affix registered for the
> extension you are building — read it from the project's own `app.json` and existing
> object names. Never write the literal word `PREFIX`, and never copy an affix from a
> rule, an example or another project.


## Description

AL requires file order: `namespace X;` → all `using ...;` lines → blank line → the
object declaration → `{ }` body. A `using` placed **after** the opening `{` of the
object is the single most common LLM-authoring failure (observed across every local
coder model tried: qwen3-coder, north-mini, qwen3). One misplaced `using` cascades into
~80 bogus diagnostics — `AL0104 '}' expected`, `AL0114 integer literal expected`,
`AL0107` — that look like broken braces but are not. The braces are fine; the `using`
is in the wrong place.

## Best Practice

Emit every `using` at file top, above the object. If a fix must be mechanical, a
deterministic post-write normalizer that hoists misplaced `using` lines before compile
is more reliable than prompting — on a real project this took a build from ~80 errors
to 3.

```al
namespace YourCompany.Feature;
using System.Utilities;

codeunit 50100 "PREFIX Thing"
{
    // body
}
```

## Anti Pattern

```al
codeunit 50100 "PREFIX Thing"
{
    using System.Utilities;   // ✗ AL0104/AL0114/AL0107 cascade
}
```

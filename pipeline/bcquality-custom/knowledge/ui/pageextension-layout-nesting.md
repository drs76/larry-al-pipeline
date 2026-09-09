---
bc-version: [all]
domain: ui
keywords: [pageextension, layout, addlast, addfirst, factboxes, nesting]
technologies: [al]
countries: [w1]
application-area: [all]
---

# `addlast`/`addfirst` must nest inside a `layout { }` block

## Description

In a `pageextension`, anchor modifications like `addlast(FactBoxes)` are only valid
inside a `layout { }` block. Emitting the anchor at page-extension top level is a
syntax error. LLM coders frequently omit the `layout` wrapper.

## Best Practice

```al
layout
{
    addlast(FactBoxes)
    {
        part(MyPart; "My FactBox") { }
    }
}
```

## Anti Pattern

```al
addlast(FactBoxes)   // ✗ must be wrapped in layout { }
{
    part(MyPart; "My FactBox") { }
}
```

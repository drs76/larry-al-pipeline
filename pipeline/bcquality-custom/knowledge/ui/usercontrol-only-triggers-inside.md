---
bc-version: [all]
domain: ui
keywords: [usercontrol, trigger, procedure, page-scope, controladdin]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Only `trigger` definitions live inside a `usercontrol`; procedures stay at page scope

> `PREFIX` in the examples below is a placeholder. Use the affix registered for the
> extension you are building — read it from the project's own `app.json` and existing
> object names. Never write the literal word `PREFIX`, and never copy an affix from a
> rule, an example or another project.


## Description

A `usercontrol(...)` block on a page accepts `trigger` definitions only. Declaring a
`procedure` inside the `usercontrol` block is a syntax error. Helper procedures belong
at page (or page-extension) scope, called from the triggers.

## Best Practice

```al
usercontrol(Map; "PREFIX Map")
{
    trigger OnControlReady()
    begin
        DoThing();
    end;
}
// ... at page scope:
local procedure DoThing() begin end;
```

## Anti Pattern

```al
usercontrol(Map; "PREFIX Map")
{
    procedure DoThing() begin end;   // ✗ procedures not allowed here
}
```

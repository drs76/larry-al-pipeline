---
bc-version: [all]
domain: ui
keywords: [promoted, actionref, promotedcategory, promotedisbig, promotedonly, area-promoted, action]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Promote actions with `area(Promoted)` + `actionref` — never the legacy Promoted properties

## Description

The legacy action properties `Promoted`, `PromotedCategory`, `PromotedIsBig` and
`PromotedOnly` are banned house-style in every case. Modern apps enable the
`NoPromotedActionProperties` feature (app.json `"features"`), under which they do not
compile at all; even where they still compile they must not be used. Declare the action
in `area(Processing)` with no promoted properties, then promote it with an `actionref`
inside an `area(Promoted)` block.

## Best Practice

```al
actions
{
    area(Processing)
    {
        action(Refresh)
        {
            ApplicationArea = All;
            Caption = 'Refresh List';
            ToolTip = 'Refresh the list.';
            Image = Refresh;

            trigger OnAction() begin end;
        }
    }
    area(Promoted)
    {
        group(Category_Process)
        {
            actionref(Refresh_Promoted; Refresh) { }
        }
    }
}
```

## Anti Pattern

```al
action(Refresh)
{
    Promoted = true;              // ✗ banned; fails under NoPromotedActionProperties
    PromotedCategory = Process;   // ✗
    PromotedIsBig = true;         // ✗
}
```

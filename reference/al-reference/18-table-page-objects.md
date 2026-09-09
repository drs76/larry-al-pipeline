<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Table & page objects — Learn reference

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

Object-type reference distilled from Microsoft Learn (Objects branch, 2026-08-16).

---

<!-- ingested: · Table object | 2026-08-16 -->
### Table object — structure, properties, limits

- Section order in `table` object is fixed: table-level properties → `fields` → `keys` (optional) → AL code/triggers (optional).

```al
table 50104 Address
{
    Caption = 'Sample table';
    DataPerCompany = true;

    fields
    {
        field(1; Address; Text[50])
        {
            Caption = 'Address retrieved by Service';
            OptimizeForTextSearch = true;
        }
        field(3; "Town/City"; Text[30])
        {
            Caption = 'Town/City retrieved by Service';
            ToolTip = 'Town/City retrieved by Service';
        }
        field(4; County; Text[30])
        {
            trigger OnValidate()
            begin
                ValidateCounty(County);
            end;
        }
        field(5; IsValidated; Boolean)
        {
            InitValue = false;
        }
    }

    keys
    {
        key(PrimaryKey; Address)
        {
            Clustered = true;
        }
    }
}
```

- Field names containing non-identifier chars (e.g. `Town/City`) must be quoted.
- `InitValue` = field default applied on `Init()`/new record.
- Field-level `OnValidate` trigger holds per-field business logic; keep body thin, delegate to a procedure.
- `Description` on a field is an internal-only note — never surfaced in the client. Use for dev comments that survive in metadata.

#### Property notes / version gates
- `ToolTip` on a **table field** — from BC 2024 wave 1 (v24). Pages using that field inherit the tooltip automatically, so define once on the table instead of repeating per page.
- `OptimizeForTextSearch = true` — from BC 2024 wave 2 (v25). Marks the field as optimized for text search.
- `DataPerCompany` (default true) controls per-company vs shared storage.
- `Clustered = true` on a key defines the SQL clustered index.

#### Extensibility rules
- Only tables with `Extensible = true` can be extended by a tableextension.
- System and virtual tables cannot be extended. System tables live in object ID range 2,000,000,000+.
- Extension object **names** max 30 characters.

#### Limits
- Table limits (max record size, field count, key count) are driven by SQL Server constraints — check "Object specifications and limitations" on Learn rather than assuming.

#### Tooling
- Snippet `ttable` scaffolds a table object in VS Code AL extension. Ctrl+Space for IntelliSense/member lists.

<!-- ingested: · Table extension object | 2026-08-16 -->
### Table extension object

- Syntax: `tableextension <Id> <Name> extends <TargetTable>` — adds fields, keys, procedures, triggers to base table. Data lives in same logical record; `Rec` on base table exposes extension fields.
- Snippet: `ttableext`.
- Extension object name max 30 chars.
- Extend only when target table `Extensible` property = true.
- Cannot extend: system tables (ID range 2,000,000,000+), virtual tables, Dynamics 365 Sales tables.
- Keys: table extension can define keys over its own new fields *and* over fields that exist only on the base table (extends base key set).
- Property overrides: some field/table properties on base-table fields can be overwritten from the extension. Verify which properties are overridable against Learn "Table and table extension properties".
- Field tooltips on table fields available from BC 2024 wave 1 (v24). Tooltip defined at table-field level is inherited automatically by every page using that field — set once instead of per page.
- Field triggers (`OnValidate`) for new fields are written in the table extension, not the base table.
- Table-level triggers (e.g. `OnBeforeInsert`) can be declared in the extension; they run in addition to base table triggers.

```al
tableextension 50115 RetailWinterSportsStore extends Customer
{
    fields
    {
        field(50116; ShoeSize; Integer)
        {
            trigger OnValidate()
            begin
                if Rec.ShoeSize < 0 then
                    Message('Shoe size not valid: %1', Rec.ShoeSize);
            end;
        }
    }

    procedure HasShoeSize(): Boolean
    begin
        exit(ShoeSize <> 0);
    end;

    trigger OnBeforeInsert()
    begin
        if not HasShoeSize() then
            ShoeSize := Random(42);
    end;
}
```

- Note: Learn's own sample omits `Caption`/`ToolTip`/`DataClassification` on the new field — real PTE code needs them (analyzer rules will flag).

<!-- ingested: · Table keys | 2026-08-16 -->
### Table keys

**Primary key**
- First `key()` in a table object = primary key. Exactly one per table; cannot be declared in a tableextension (extensions inherit base table PK).
- Up to 16 fields effective (editor may accept 20, SQL uses first 16 only).
- Uniqueness constraint is on the *combination* of PK field values, not per-field.
- Always active; determines logical sort order; SQL rejects duplicate PK combos on insert.
- `AutoSplitKey` (page property) auto-computes the last PK field so a new row lands between two neighbours. From BC 2025 wave 1 it can generate negative values when inserting before the first row. `0` is a legal key value but is never generated by AutoSplitKey.

**Secondary keys**
- Any key after the first in a table object; *all* keys in a tableextension are secondary.
- Each enabled secondary key = a SQL index maintained automatically. Multiple can be active at once.
- Non-unique by design; ties are resolved by PK order (so sorting on a secondary key sub-sorts by PK).
- `Enabled = false` drops the index (saves space + write cost). Re-enabling forces a full table scan/index rebuild — slow on big tables.
- Max 40 keys per table.

**Key properties**
- `Clustered = true` — physical row order; one per table; PK is clustered by default. Not supported in tableextension.
- `Unique = true` — SQL unique constraint; validated on table validation, fails if dupes exist; also helps the query optimizer. Multiple unique secondary keys allowed. Not supported in tableextension.
- `IncludedFields = A,B` (BC 2021 wave 2+) — SQL included columns on a non-clustered index. Covers more queries without counting against the key field limit; avoids lookups back to the clustered index.
- `ColumnStoreIndex = F1,F2,...` (BC 2021 wave 2+) — non-clustered columnstore index (NCCI). Column-oriented storage for analytical/aggregate queries; large compression and query gains. Recommended replacement for SIFT keys used purely for sum/count: one NCCI listing all involved fields can replace several SIFT keys, and avoids SIFT locking overhead.

**Syntax**
```al
keys
{
    key(PK; MyField1) { Clustered = true; }
    key(CustomerInfo; Name, Address, City) { Unique = true; }
    key(Currency; "Currency Code") { Enabled = false; }
}
```
- `keys` block goes after `fields`. Comma-separate fields for a composite key.

**Tableextension key rules**
- BC 2020 wave 2 and earlier: extension keys may use extension fields only.
- BC 2021 wave 1+: a key may use base-table fields *or* extension fields, but **never both in the same key**. Fields from another tableextension are never allowed.
- Key names may repeat the base table's names, unless the key contains base-table fields.
- From BC v18 you can ship a tableextension that contains only a `keys` block — the way to add indexes to base app or third-party tables you don't own.

**Upgrade / schema-sync restrictions** (breaking on publish of a new version)
- Don't delete a primary key, add/remove/reorder PK fields, or change PK properties.
- Don't add further unique keys or clustered keys.
- Don't add keys over base-table fields.

**Misc**
- A unique secondary key on `SystemId` always exists.
- BC 2022 wave 2+: IntelliSense marks PK members as `(PK1)`, `(PK2)`, … showing position in the key.
- `Database Missing Indexes` page lists index candidates observed by the platform.

**Perf trade-off** — more active secondary keys = faster varied-sort retrieval, slower inserts/modifies (every index maintained). Few keys = fast writes, but re-enabling a key later costs a rebuild. Deactivate complex, rarely used keys.

<!-- ingested: · Page object | 2026-08-16 -->
### Page object — structure & syntax

- Page = main visual object user interacts with. Device-agnostic: same page renders on phone, tablet, web client.
- Behaviour driven by `PageType` (Card, List, ...).
- Section order in a page object is **enforced**, not cosmetic:
  1. page-level properties (`PageType`, `SourceTable`, `ContextSensitiveHelpPage`, ...)
  2. `layout { }` — visual controls
  3. `actions { }` — published actions
  4. `views { }` — list pages only
  5. AL code (triggers/procedures) last, optional
- Skeleton:

```al
page 50101 SimpleCustomerCard
{
    PageType = Card;
    SourceTable = Customer;
    ContextSensitiveHelpPage = 'my-feature';

    layout
    {
        area(content)
        {
            group(General)
            {
                field("No."; "No.")
                {
                    ApplicationArea = All;
                    CaptionML = ENU = 'Hello';

                    trigger OnValidate()
                    begin
                        if "No." < '' then
                            Message('Number too small');
                    end;
                }
                field(Name; Name) { ApplicationArea = All; }
            }
        }
    }
    actions
    {
        area(Navigation)
        {
            action(NewAction)
            {
                ApplicationArea = All;
                RunObject = codeunit "Document Totals";
            }
        }
    }
}
```

- Layout nesting: `layout` → `area(content)` → `group(...)` → `field(Name; SourceExpr)`. Actions: `actions` → `area(Navigation)` → `action(...)`.
- Field-level `trigger OnValidate()` is allowed inline on the page field.
- `RunObject` on an action can point straight at a codeunit/page — no AL code needed.

### Extending vs customizing pages

- **Page extension** — changes an existing page (layout, actions, code).
- **Page customization** — lighter: modifications to actions and layout only.
- A page can only be extended if its `Extensible` property is `true`.
- Extension object names capped at **30 characters**.

### Tooltips inherited from table fields

- From BC 2024 release wave 1: `ToolTip` can be defined on the **table field**; every page using that field inherits it automatically. Avoids repeating tooltips per page.

### Views

- `views { }` defines alternate data views on list pages. Supported in page, page extension, and page customization objects.

### Tooling

- Snippet `tpage` scaffolds a page object (AL Language extension for VS Code).
- Ctrl+Space triggers IntelliSense — completion, parameter info, member lists.

<!-- ingested: · Page extension object | 2026-08-16 -->
### Page extension object

- `pageextension <id> <Name> extends "<Base Page>"` — adds to or overrides a base page. Three sections mirror page object: metadata block, `layout`, `actions`.
- Base page must have `Extensible = true`, else no pageextension allowed.
- Extension object names max 30 chars.
- API pages cannot be extended by a pageextension. Add a new API page object instead.
- Modifying actions inside Cue groups from a pageextension is not supported.
- Snippet: `tpageext`. Ctrl+Space for IntelliSense.
- Views (list-page alternate data views) can be declared in page, pageextension and pagecustomization.
- From 2024 wave 1: tooltip defined on a *table field* is inherited by every page using that field — no need to repeat ToolTip on each page control.

#### Placement keywords (same set in `layout` and `actions`)

| Keyword | Syntax | Anchor / Target |
|---|---|---|
| `addfirst` | `addfirst(Anchor)` | anchor: areas, groups |
| `addlast` | `addlast(Anchor)` | anchor: areas, groups |
| `addafter` | `addafter(Anchor)` | anchor: controls, actions, groups |
| `addbefore` | `addbefore(Anchor)` | anchor: controls, actions, groups |
| `movefirst` | `movefirst(Anchor; T1, T2)` | anchor: area/group; targets: list of controls or actions |
| `movelast` | `movelast(Anchor; T1, T2)` | anchor: area/group; targets: list |
| `moveafter` | `moveafter(Anchor; T1, T2)` | anchor: control/action/group; targets: list |
| `movebefore` | `movebefore(Anchor; T1, T2)` | anchor: control/action/group; targets: list |
| `modify` | `modify(Target)` | target: control, action, group |

- `move*` uses `;` between anchor and target list, `,` between targets — no braces/body.
- `add*` and `modify` take a body block.
- `modify("Address 2") { Caption = 'New Address 2'; }` — change properties of inherited controls.

#### Patterns

```al
pageextension 50110 CustomerCardExtension extends "Customer Card"
{
    layout
    {
        addlast(General)
        {
            // bound control (field from table extension)
            field("Shoe Size"; ShoeSize)
            {
                ApplicationArea = All;

                trigger OnValidate()
                begin
                    if ShoeSize < 10 then
                        Error('Feet too small');
                end;
            }
            // unbound / display-only control: source is an expression, not a field
            field(ShoesInStock; 10)
            {
                ApplicationArea = All;
                Caption = 'Shoes in stock';
            }
        }
        modify("Address 2") { Caption = 'New Address 2'; }
        movefirst(Balance; CreditLimit, CalcCreditLimitLCYExpendedPct)
    }
    actions
    {
        addlast(Creation)
        {
            group(MyActionGroup)
            {
                action(MyAction1)
                {
                    ApplicationArea = All;
                    Caption = 'Hello!';

                    trigger OnAction()
                    begin
                        Message('My message');
                    end;
                }
                action(MyAction2)
                {
                    ApplicationArea = All;
                    RunObject = page "Absence Registration";
                }
            }
        }
    }
}
```

- Field controls can be bound to a table field or to a constant/expression (display-only, no data source).
- `addlast(Creation)` on Customer Card puts a new action group last in the Creation ribbon group; anchors are the base page's area/group names (e.g. `"&Customer"` on Customer List).
- Actions run objects via `RunObject = page/report/xmlport ...`, or run code in `trigger OnAction()`.
- Reports and XmlPorts can also be used as variable types and invoked in AL:

```al
trigger OnAction()
var
    Rep: Report "Customer - List";
    Xml: XmlPort "Export Contact";
begin
    Rep.Run();
    Xml.Run();
end;
```

- New fields shown by a pageextension normally come from a matching `tableextension` on the same base table.

<!-- ingested: · Page customization object | 2026-08-16 -->
### pagecustomization object

- `pagecustomization <Name> customizes "<Page>"` — layout/action tweaks applied per profile.
- Restrictions vs `pageextension`: no variables, no procedures, no triggers. Only `actions`/`layout` changes (add actions, fields, groups).
- Name max 30 chars (all extension objects).
- Attached to profile via `Customizations = MyCustomization;`. One customization can be reused by many profiles in same extension.
- Customizations apply only to RoleCenters they are specified for. Client: My Settings → Role Center.
- Modifying actions inside Cue groups not supported (page extensions too).
- `allowDebugging = false` under `resourceExposurePolicy` does NOT protect page customizations — still copyable via Designer.
- Snippet: `tpagecust`.
- Views supported in pages, page extensions and page customizations.

```al
profile TheBoss
{
    Description = 'The Boss';
    RoleCenter = "Business Manager Role Center";
    Customizations = MyCustomization;
    Caption = 'Boss';
}

pagecustomization MyCustomization customizes "Customer List"
{
    actions
    {
        moveafter(Orders; "Blanket Orders")

        modify(NewSalesBlanketOrder)
        {
            Visible = false;
        }
    }
}
```

- BC 2023 wave 2 (v23)+: can add groups and page fields bound to a table field as source expression.

```al
pagecustomization MyPageCust customizes MyPage
{
    layout
    {
        addfirst(Content)
        {
            field(MyPageCustField; Rec.MyTableField) { }
        }
    }
}
```

- Table field property `AllowInCustomizations` controls whether a field may be used as source expression in page customizations. Default = allowed.
- BC 2025 wave 2 / runtime 16+: fields declared in a page customization can be made editable (`Editable = true`). Before runtime 16 they were always read-only — unlike fields on pages/page extensions.
- Note: profile snippet in source shows `ProfileDescription` in one example and `Description` in the other; `Description` is the profile property — verify `ProfileDescription` [sic?] against Learn/compiler.


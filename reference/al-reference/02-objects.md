<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Tables, codeunits, pages, reports, factboxes & control add-ins

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

## 5. Tables

```al
table 50100 PTEMyTable
{
    Caption = 'My Table';
    DataClassification = CustomerContent;

    fields
    {
        field(1; "Code"; Code[20])
        {
            Caption = 'Code';
            NotBlank = true;
        }
        field(2; Description; Text[100])
        {
            Caption = 'Description';
        }
        field(3; IsEnabled; Boolean)
        {
            Caption = 'Enabled';
        }
    }

    keys
    {
        key(PK; "Code")
        {
            Clustered = true;
        }
    }

    trigger OnInsert()
    begin
    end;

    trigger OnModify()
    begin
    end;

    trigger OnDelete()
    begin
    end;
}
```

Table Extension:
```al
tableextension 50101 PTEDocumentLinkExt extends "Document Link"
{
    fields
    {
        field(50100; PTEBlobName; Text[2048])
        {
            Caption = 'Blob Name';
            DataClassification = CustomerContent;
        }
        field(50101; PTEBlobStorageCode; Code[20])
        {
            Caption = 'Blob Storage Code';
            DataClassification = CustomerContent;
            TableRelation = PTEDocumentLinkAZSetup.Code;
        }
        field(50102; PTEMigrated; Boolean)
        {
            Caption = 'Migrated to ABS';
            DataClassification = CustomerContent;
        }
    }
}
```

**Newer table features (2024w1–2026w1):**
- **Field tooltips on the table** (2024w1) — define `ToolTip` once on the field; every page bound to
  the table inherits it (override on the control like a caption). A code action moves tooltips from
  page down to table.
- **`OptimizedForTextSearch = true`** on a field enables modern full-text search (put it on PK + name/
  descriptive fields users search on; NOT high-cardinality/grouping fields). Enables the `&&`
  whole-word filter operator — see §10. Exposed as `FieldRef.OptimizedForTextSearch`.
- **Moving tables/fields between extensions without upgrade code** (base-app always; **AppSource** from
  runtime ≥15.0 / on-prem ≥26.0; **not** for PTEs). Source: `ObsoleteState = PendingMove` → `Moved`
  + `MoveTo = '<dest app GUID>'` (keep the definition — validated on every install). Destination: copy
  the definition (no schema-breaking change) + `MovedFrom = '<source app GUID>'` (GUIDs must match).
  Add a dependency on the destination + `propagateDependencies = true` so downstream apps still reach
  moved objects. **Publish/sync source before destination.** Field ext→ext = SQL column rename (no data
  copy); base→ext = DataTransfer-batched; table move = SQL table rename. GOTCHA: consolidation
  (field ext→**base**) is **not** supported.
- **Ship a key created disabled**: `key(...) { Enabled = false; }` — admins enable it **per company**
  (ship optional indexes without the storage/write cost). Included (covering) fields shown on the
  Table Information page. On-prem `AlterKey` disables a key for the current transaction (auto re-enabled
  at commit/rollback) — use only for large deletes.
- Add fields to a **field group that doesn't exist** in the base object (e.g. a `Brick` group on
  G/L Entry — appends/dedupes). `AllowInCustomizations` on a field controls profile-customization
  availability.

---

## 5b. Enums

Every value REQUIRES an explicit ordinal: `value(N; Name)`. Bare member lists are
C#-style and do not compile (AL0104 `'=' expected` / cascading AL0198).

```al
enum 50300 "Equipment Status"
{
    Extensible = true;

    value(0; Active) { Caption = 'Active'; }
    value(1; "In Repair") { Caption = 'In Repair'; }
    value(2; Retired) { Caption = 'Retired'; }
}
```

✗ WRONG — does not compile:

```al
enum 50300 "Equipment Status"
{
    Active;          // AL0104: '=' expected
    "In Repair";
    Retired;
}
```

- Quote value names containing spaces/dots, same as fields.
- Ordinals are persisted — never renumber shipped values; append with new numbers.
- Field of that type: `field(10; Status; Enum "Equipment Status")`.
- Enum in its own `.Enum.al` file OR appended after a table in the same file — both
  compile; separate file is the convention.

---

## 6. Codeunits

```al
codeunit 50102 PTEMyCodeunit
{
    // Access = Public is default. Use Access = Internal to restrict to same extension.
    // Keep procedure bodies to ~25-30 lines where possible — split by responsibility into
    // named local helpers; the public procedure reads as the sequence of steps. Soft rule:
    // don't contort genuinely linear logic (e.g. a long case mapping) just to hit a number.

    procedure PublicMethod(Param: Text): Boolean
    begin
        exit(TryDoWork(Param));
    end;

    [TryFunction]
    local procedure TryDoWork(Param: Text)
    begin
        // TryFunction: NO return type declared — Boolean return is implicit.
        // Any Error() call or unhandled exception = returns false to caller.
        // Caller uses GetLastErrorText() to retrieve the error.
    end;

    [NonDebuggable]
    procedure GetSecret(): SecretText
    var
        ReturnValue: SecretText;
    begin
        // [NonDebuggable] prevents debugger/telemetry from exposing value.
        // Required on all methods that access Isolated Storage secrets.
        exit(ReturnValue);
    end;

    local procedure LocalHelper()
    begin
    end;
}
```

---

## 7. Pages

Card page:
```al
page 50103 PTEMyCard
{
    Caption = 'My Card';
    PageType = Card;
    SourceTable = PTEMyTable;
    UsageCategory = None;

    layout
    {
        area(Content)
        {
            group(General)
            {
                Caption = 'General';

                field("Code"; Rec."Code")
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies the code.';
                }
                field(Description; Rec.Description)
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies the description.';
                }
            }
        }
    }

    actions
    {
        area(Processing)
        {
            action(MyAction)
            {
                Caption = 'Do thing';
                ApplicationArea = All;
                Image = Action;

                trigger OnAction()
                begin
                end;
            }
        }
        area(Promoted)
        {
            actionref(MyAction_Promoted; MyAction) { }
        }
    }
}
```

**Promoting actions — ALWAYS `area(Promoted)` + `actionref`, never the legacy properties.**
The old `Promoted = true;` / `PromotedCategory` / `PromotedIsBig` / `PromotedOnly` action
properties are **banned house-style in every case** — even where they still compile. Modern apps
enable `NoPromotedActionProperties` (app.json `"features"`), under which they don't compile at all.
Declare the action in `area(Processing)` with no promoted properties, then promote via:
```al
area(Promoted)
{
    group(Category_Process)
    {
        actionref(MyAction_Promoted; MyAction) { }
    }
}
```

**Action `Image` default:** use `Image = Action;` unless a specific icon is required.
Many image names (e.g. `Message`) are not valid on page actions and raise `warning
AL0482`. `Action` is always valid for a page action, so default to it.

List page:
```al
page 50104 PTEMyList
{
    Caption = 'My List';
    PageType = List;
    SourceTable = PTEMyTable;
    UsageCategory = Administration;
    ApplicationArea = All;
    CardPageId = PTEMyCard;
    Editable = false;

    layout
    {
        area(Content)
        {
            repeater(Lines)
            {
                field("Code"; Rec."Code")
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies the code.';
                }
                field(Description; Rec.Description)
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies the description.';
                }
                field(IsEnabled; Rec.IsEnabled)
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies whether enabled.';
                }
            }
        }
    }
}
```

Page with SubPart (ListPart embedded in Card):
```al
part(ContentsSubpart; PTEMyListPart)
{
    ApplicationArea = All;
    SubPageLink = "Setup Code" = field(Code);
    Visible = ShowContents;
}
```

Masked field with assist-edit (for secrets):
```al
field(SharedAccessKeyValue; SharedAccessKeyDisplay)
{
    ApplicationArea = All;
    Caption = 'Shared Access Key';
    ExtendedDatatype = Masked;

    trigger OnAssistEdit()
    begin
        // open key entry page
    end;
}
```

**Newer page features (2024w2–2025w1):**
- **`PageType = UserControlHost`** (2025w1) — a page hosting exactly **one** user control and nothing
  else (Power BI reports, embedded browser, full-screen content). GOTCHA: no `SourceTable`, no
  insert/modify/delete, no `OnAfterGetRecord`, and (currently) **no `actions`** — the control takes the
  whole page; the compiler warns if you keep them.
- **Override the card page ID** (2025w1) on a page/page-extension — for scenarios with no card page ID
  or where it must change.
- **`PageStyle` enum** (2024w2) — set the style from the enum instead of the hardcoded
  "Favorable"/"Unfavorable" strings (the `StyleExpr` still binds a string variable, which you assign
  from the enum).
- **Profile extensions** (2024w2) — extend a profile instead of copying it; page-customization props
  `ClearLayout` / `ClearActions` / `ClearViews` (list pages) start empty then re-add. GOTCHA: a
  `Clear*` on a page-customization used in a role-customization errors.
- **Prompting (Copilot) actions** now allowed on card, list and document pages (2024w2). `PageType =
  ConfigurationDialog` exists but is not yet usable (errors "feature under development").

---

## 8. Reports

```al
report 50105 PTEBlobMigration
{
    Caption = 'Migrate Document Links to ABS';
    UsageCategory = Administration;
    ApplicationArea = All;
    ProcessingOnly = true;

    dataset
    {
        dataitem(DocumentLink; "Document Link")
        {
            RequestFilterFields = "No.";

            trigger OnAfterGetRecord()
            begin
            end;

            trigger OnPostDataItem()
            begin
            end;
        }
    }

    requestpage
    {
        layout
        {
            area(Content)
            {
                group(Options)
                {
                    Caption = 'Options';
                }
            }
        }
    }

    var
        MigratedCount: Integer;
        FailedCount: Integer;

    trigger OnPreReport()
    begin
    end;

    trigger OnPostReport()
    begin
        Message('Migration complete. Migrated: %1. Failed: %2.', MigratedCount, FailedCount);
    end;
}
```

**Newer report features (2024w2–2025w1):**
- **New triggers** `OnPreRendering` (PDF post-processing — append T&Cs, embed/attach files for
  e-invoicing, set PDF passwords) and `OnPostReport`; inside the report you can read the **target
  format** to branch code on what's being generated.
- **`ExcelLayoutMultipleDataSheets`** property (from v23) — each data item gets its own Excel worksheet
  instead of one flat table. **Overridable at the layout level** (v26, AL or Report Layouts page);
  default `false`, so set `true` on a new layout to avoid breaking existing ones.
- **Obsolete a report layout** like any object — inside the `layout(...)` in the `rendering` section
  set `ObsoleteState = Pending`, `ObsoleteReason`, `ObsoleteTag`. GOTCHA: `Report.WordLayout` /
  `RDLCLayout` / `ExcelLayout` methods are being **deprecated** (meaningless with multiple layouts) —
  use the `rendering` section.
- **Report tooltips** — a page action pointing at the report via `RunObject` **inherits** the report's
  tooltip (override still possible). `AboutTitle`/`AboutText` teaching tips are inherited into the Role
  Explorer without redefining on the action.
- **Preview from stream** (view-from-stream) shows the document in the client with no download first.
  `GetUrl` can include the **layout** (List, Tall Tiles, Tiles, Analysis).
- New report event `OnGetReportFileName` (subscribe to set the download file name). Word layouts bind
  system metadata via the **`BC Report Information`** XML node (report + request: company/user/render
  date) — see AL-KNOWLEDGE §2 for the layout tooling around this.

---

<!-- ingested: Deep Dive into Report Objects and Layouts in Business Centra | 2026-07-26 -->
### Report objects & layouts — deep dive (mibuso, 2025-10)

**Data-analysis mode (client, ad-hoc)**
- List pages expose an *Analyze* button → in-client pivot-like view (row groups, columns, summary/totals bar, filters, private mode). Views persist per user; right-click → Share sends a deep link (intra-org).
- Page property to allow/deny per page: `AnalysisModeEnabled` [sic? verify exact property name against Microsoft Learn/compiler]. Also a dedicated permission set gates the feature.
- Add a calculated field via page extension → it becomes available in analysis mode with totals/subtotals.
- Query objects with a `UsageCategory` set appear in client search; running one opens directly in analysis mode. Good pattern for reusing API queries for ad-hoc analysis.

**Query objects for report datasets / analysis**
- Choose SQL join type per dataitem link (left/inner/etc.).
- Aggregation methods on numeric columns (Sum, etc.) and date-part methods (Year/Month/Day) → automatically generate a GROUP BY on all remaining columns.
- Consume a query in a report: declare a Query variable, use an `Integer` dataitem, `Query.Open()` then read in a loop, `break` when `Read()` returns false. Dataset built server-side, smaller/faster than joined dataitems. Downside: no AL record logic inside a query (can't compute custom fields procedurally).

**Report dataset design (dataitems)**
- **Union**: stack two dataitems at the same indent level. At runtime rows are concatenated (unlike SQL union, columns need not match). In RDLC the single dataset (`DataSetResult` [sic? verify]) has all columns of both; filter/hide rows where the other item's key is empty.
- **Join**: use `DataItemLink` on the child dataitem. Add `DataItemTableView`/sort on child so the extra dataitem doesn't surface on the request page.
- Join semantics: DataItemLink + no PrintOnlyIfDetail → **left outer join**; DataItemLink + `PrintOnlyIfDetail = true` → **inner join**; neither → **cross join** (cartesian). `PrintOnlyIfDetail` is settable as a property or via method (using a report variable) for runtime-dynamic switching without duplicate reports.
- **Single-row extras** (company name/logo, header/footer totals): add a separate `Integer` dataitem returning exactly one row instead of joining — avoids repeating the logo on every line (big perf win). Remember to filter that row out of detail tables in the layout.
- **Top-N / computed data**: loop records into a temp/buffer table in `OnAfterGetRecord`, then expose it via an `Integer` dataitem. Puts exactly N rows in the dataset (better than RDLC top-N filtering over a huge dataset). Also the way to get totals into a Word layout (Word can't aggregate).

**Documents (header+line)**
- Generate in the *recipient's* language, not the running user's: add `field captions` only to the multilanguage fields, and in `OnAfterGetRecord` set the report language from the header's language code (e.g. bill-to customer).
- Standard sales invoice = report 1306. Consider skipping execution when the user set no filter (avoid printing all documents).

**RDLC layout notes**
- Filtering rows: Code fields are `Code` type; convert with `CStr()` before comparing, and compare `> ""` (works more reliably than `<> ""`). Alternatively use row-visibility expression to hide rows.
- Grouping/subtotals: add parent groups on a table, use aggregate (Sum) scoped to the group.
- Page-per-document: wrap tables in a **List** container, group the list on document no., set the page-break property **on the list** (not the table).
- Header-band data needs workarounds (old `GetData`/`SetData` pattern); 1306 moved header info into a table at top of body — cleaner but that table shows only on page 1.
- RDLC runs in a separate standalone sandbox (because layout expressions could call .NET interop, which isn't allowed in BC) → extra latency; that's why it's slower and why Microsoft steers away from it. RDLC is unsupported legacy (SSRS, last release 2016) — don't start new work in it; migrate toward Word.
- Needs Report Builder 2016; VS 2022 (or VS 2019 + plugin) also works.

**Word layout notes**
- Fields inserted via right-click → content control (no drag-drop natively). Detail row = a repeater bound to a dataitem; nested repeaters allowed (keep to ~2–3).
- `WordMergeDataItem` property (set on the header dataitem) drives page-per-document.
- Can't aggregate or do conditional formatting/visibility natively → push totals/blanking into the dataset (an empty field is simply not rendered).
- Use tables purely for alignment/positioning (invisible at runtime); put images in single-cell tables to control growth; `Compress Picture` in Word reduces runtime payload. Sections allow per-page orientation (portrait then landscape) and different headers/footers.
- BC Word add-in (Home → Get Add-ins → Business Central): current features = hide-if-empty on field/row/column and layout comments; conditional formatting/visibility hoped for future.
- Redesigned sales invoice clone (in Base App, well-named dataitems, heavy use of union dataitems tuned for Word) is a good reference layout.

**Programmatic default layout**
- Change a report's current default layout at runtime by updating the report-layout-list table (settable per company or per user), letting one report ship multiple Word layouts and pick one in code. [sic? verify exact table/API name against Microsoft Learn]

**Excel layout contract**
- Generated workbook has a `Data` sheet containing a `Data` table — do NOT rename/delete either (you may move them); that's the binding contract. Presentation sheets are user-created; the metadata sheet (translated captions etc.) may be deleted. Supports multilanguage. Property to emit one sheet per dataitem instead of one combined data sheet.

**Report extension gotcha**
- When adding dataitems, use `addafter` (not `addlast`): `addlast` on the wrong scope nests the new dataitem under the last one, producing a bad join (e.g. equal counts of unrelated records). Verify the base dataset is stable/extendable before extending.

## 19. Factboxes, Control Add-ins & Charts

**Control add-in JS must anchor its DOM to the container BC injects — `document.getElementById("controlAddIn")`.**
BC renders each control add-in in a sandboxed iframe and puts an empty `<div id="controlAddIn">` in it;
your StartupScript/scripts must build UI *inside that element*. Appending to `document.body` (or
`document.documentElement`) **renders nothing — a blank control**, with no error. Confirmed the hard way
2026-08-04: a board add-in that did `document.body.appendChild(...)` showed a fully blank page across
Firefox/Zen even though the `.app` packaged the JS correctly; switching to
`document.getElementById("controlAddIn").appendChild(...)` fixed it instantly. This is NOT a browser,
CSP, tracking-protection, page-source-table, or packaging issue — it is the add-in DOM contract, and it
should be the FIRST thing checked when a custom control add-in renders blank. (Reference: any working
add-in, e.g. `new calendarJs(document.getElementById("controlAddIn"), …)`.)

**ListPart factbox with `SourceTableTemporary` + a control add-in** (timing is the whole game):
- **Data not showing on first open**: load data in the factbox's `OnFindRecord` trigger — **not** via `CurrPage.Update(false)` called from a procedure the parent invokes in `OnAfterGetCurrRecord`. Cross-page `CurrPage.Update` is unreliable; `OnFindRecord` fires as part of BC's render cycle. Pattern: a `SetX` procedure sets `NeedsRefresh := true`; `OnFindRecord` checks the flag and populates.
- **Add-in visuals (e.g. row colours) not applied on first open**: in the add-in's `ControlReady`/`AddInReady` trigger, after setting your ready flag, call `CurrPage.Update(false)` — it fires from the factbox's own context (so it works there, unlike cross-page calls) and re-runs the row triggers with the add-in ready.
- **`SubPageLink` on a temp source table**: remove it. The link filters `Rec` on open; if records key on different fields (e.g. `"From ID"` vs `"For ID"`), `Rec.Find` returns nothing.

**Native charts** — `Codeunit "Business Chart"` + `usercontrol(Name; BusinessChart)`, `using System.Visualization;`. Order matters:
```al
BusChart.Initialize();
BusChart.SetXDimension('X', Enum::"Business Chart Data Type"::String);
BusChart.AddMeasure('M', 0, Enum::"Business Chart Data Type"::Decimal, Enum::"Business Chart Type"::Column);
// per data row:
BusChart.AddDataRowWithXDimension('Xval');
BusChart.SetValue('M', Idx, Value); Idx += 1;
BusChart.Update(CurrPage.MyChart);   // CurrPage.<control-name>, NOT a string
```

<!-- ingested: NAV TechDays 2019 - Control Add in development supercharged | 2026-07-26 -->
### Control add-in JS tooling & AL workspace gotchas (NAV TechDays 2019, Vjeko)
- AL compiler scans **every** file in the workspace looking for `.al` files; a `node_modules/` folder (from npm/gulp/babel/webpack) sits in the workspace and makes compilation fail when it hits non-AL files with `.al`-like names. Keep node tooling **out** of the AL project folder.
- Fix: use **VS Code multi-root workspaces** — one root for AL (no node_modules), a separate root for the web/control-add-in source with its build tooling. A gulp `watch` task bundles JS and copies the output bundle file into the AL folder's control-add-in resources.
- AL still doesn't cooperate fully with multi-root: it hijacks F5, and touching any AL feature from the web root injects a `rad.json` there. Compound debug configs that launch AL + Chrome + node together are not supported — run AL, then attach a **separate Chrome debug session** to debug the control add-in JS.
- Develop control add-in JS in **many small files** (separation of concerns) but **bundle into one file** for deployment (fewer HTTP requests, better browser perf). Bundlers: gulp (naive concat) or webpack (dependency graph + tree-shaking to drop dead code, smaller bundle).
- **Source maps**: emit them from the bundler so you can set breakpoints in original JS source and debug even though BC runs the uglified/minified bundle.
- **Babel**: transpiles modern JS to browser-compatible JS and polyfills missing features. Relevant for BC because the old Windows client / legacy Universal Client embed control add-ins via **Internet Explorer**, which chokes on modern syntax.
- Rendering perf: re-rendering the whole control-add-in DOM on every state change is slow on weak client hardware; prefer a framework (React etc.) that re-renders only the bound subtree.
- Control add-in ↔ AL messaging pattern used: JS signals ready via the add-in `OnControlReady`/`InvokeExtensibilityMethod` path [sic? verify exact names against Microsoft Learn]; AL pushes data by calling a control add-in method (e.g. `CurrPage.<Addin>.SendData(<json>)`) passing a JSON payload. A JS mock of the page runtime + `Microsoft.Dynamics.NAV` framework object lets web devs develop/test the component outside BC with identical behaviour.
- **WebSockets** (not web services/REST, not webhooks) can call a local TCP service on the user's machine (same-origin, bypasses CORS) to reach local resources like serial ports from a control add-in.

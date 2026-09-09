<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# Report, codeunit, query, XMLPort & control add-in objects — Learn reference

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

Object-type reference distilled from Microsoft Learn (Objects branch, 2026-08-16).

---

<!-- ingested: · Report object | 2026-08-16 -->
### Report object (Learn: Report Object)

- Three use shapes: analytical (screen/Excel consumption), document (print), processing-only (no layout; request page supplies filters/options).
- Two build tasks: dataset (data model) + layout (visual). Layout optional for processing-only.
- Section order in `report` object matters: properties → `dataset` → `requestpage` (optional) → `rendering` (optional) → `labels` → triggers/vars/AL code.
- Snippet `treport` scaffolds a report.
- Query object can be a report data source — often faster data retrieval than dataitem chains.
- To change an existing report (extra columns, request page additions, extra layout) use a **reportextension** rather than copying the report.

**Common report properties**

- `Caption` — title on request page, Tell Me, report/role explorer, bookmarks.
- `AdditionalSearchTerms` — extra Tell Me search hits.
- `UsageCategory` (+ `ApplicationArea`) — controls visibility in report/role explorer.
- `AllowScheduling = true` — adds the Schedule action so report can run in background.
- `DataAccessIntent = ReadOnly` — lets runtime read from secondary (replica) database if present.

**Layout types (`rendering` section)**

```al
rendering
{
    layout(LayoutExcelPivot)
    {
        Type = Excel;
        Caption = 'Customer list (analyze)';
        Summary = 'Customer list for analysis in Excel';
        LayoutFile = 'CustomerListExcel.xlsx';
    }
    layout(CustomerListPrintLayout)
    {
        Type = RDLC;
        Caption = 'Customer list (print)';
        Summary = 'Customer list in print layout';
        LayoutFile = 'CustomerListRDL.rdl';
    }
}
```

- One report can carry multiple layouts; `rendering` is the modern way to declare them.
- Excel: no-code for end users, primary choice for analytical reports, **cannot print from the request page**.
- RDL (`Type = RDLC`): pro-dev only, pixel-perfect print, supports printing from request page. Authored in VS Report Designer / SSRS Report Builder.
- Word: low-code, document reports, supports printing from request page. Backed by a custom XML part representing the dataset.

**Labels**

- Field captions already on table fields: use `IncludeCaption` on the column instead of hand-written labels.
- Static text with no source caption goes in the `labels` section:

```al
labels
{
    LabelName1 = 'Label Text1', Comment = 'Foo', MaxLength = 999, Locked = true;
}
```

- All three layout types can consume label data.

**Dataset patterns**

- `dataitem(Name; TableName)` with `RequestFilterFields = "No.", "Search Name", ...;` to preseed request-page filters.
- `column(Alias; SourceExpr)` — source can be a field, a variable, an array element (`CustAddr[1]`), a `Label`, `FieldCaption(...)`, `TableCaption`, or an expression.
- Column props e.g. `DecimalPlaces = 0:0;`.
- `trigger OnAfterGetRecord()` on the dataitem — do per-row work here (`CalcFields` for FlowFields, address formatting).
- `trigger OnPreReport()` on the report — one-time setup, e.g. building the filter caption text.
- Request page props seen: `SaveValues = true;`, `AboutTitle`/`AboutText` (+ `AboutTitleML`/`AboutTextML`), `ContextSensitiveHelpPage` (needs `contextSensitiveHelpUrl` in app.json).
- Learn example uses numeric codeunit refs (`Codeunit 42` caption management, `Codeunit 365` format address) — in modern AL use the named codeunits instead; verify names against the base app.

**Gotchas / limits**

- Platform enforces hard report limits: max rows processed, max documents merged in a Word layout, max execution time. Exceeding any → report cancelled, and a telemetry event is emitted. Configurable per server on-prem; fixed service limits online.
- Excel layouts additionally hit Excel's own row/size limits.
- Debug aid: run the report and choose **Send to > Microsoft Excel Document (data only)** to dump the raw dataset with no layout — verifies data and that layout control types match dataset value types.

<!-- ingested: · Profile object | 2026-08-16 -->
### profile & pagecustomization objects

- `profile MyProfile { ... }` — defines a user profile (role). Compiler validates that the referenced `RoleCenter` page and every object listed in `Customizations` actually exist.
- Profile properties:
  - `Description` — internal, dev-only comment; not shown to users.
  - `Caption` — user-facing profile name.
  - `ProfileDescription` — longer user-facing text: who profile is for, how to use it.
  - `RoleCenter` — role center page object.
  - `Enabled` — profile usable.
  - `Promoted` — surfaced in role picker / Role Explorer.
  - `Customizations` — comma-list of `pagecustomization` objects applied under this profile.
- `pagecustomization MyCustomization customizes "Customer List" { layout { modify(Name) { Visible = false; } } }` — page customization targets one page, alters `layout` and `actions` only.
- Page customization cannot declare variables, procedures, or triggers. Layout/action property changes only.
- Page customizations bind to the profile's Role Center: they take effect only when user's active Role Center (My Settings → Role Center) is the one the profile specifies. Testing gotcha — customization looks dead if wrong role center active.
- Extension object names max 30 chars (applies to `pagecustomization`, extension objects generally).
- `allowDebugging = false` under `resourceExposurePolicy` in app.json does NOT protect page customizations — they remain copyable via Use Designer. Only real protection for layout IP is not shipping it as a page customization.
- Snippet: `tprofile` scaffolds a profile object in VS Code AL extension. Ctrl+Space for IntelliSense.
- Related objects: `profileextension` (extend an existing profile), `pagecustomization`.

<!-- ingested: · Codeunit object | 2026-08-16 -->
### Codeunit object

- Codeunit = container for AL code. Business logic lives here; other objects call it.
- VS Code snippet `tcodeunit` scaffolds basic codeunit layout.
- `TableNo = <Table>;` property makes codeunit runnable against a record. Inside `OnRun`, the passed record is available as `Rec`.
- Two call styles for same codeunit:
  - `Codeunit.Run(Codeunit::CreateCustomer, Customer)` — fires `OnRun`.
  - Direct procedure call on a codeunit variable, e.g. `CreateCustomer.CheckSize(Customer)` — bypasses `OnRun`.
- Pattern (from Learn sample):

```al
codeunit 50113 CreateCustomer
{
    TableNo = Customer;

    trigger OnRun()
    begin
        CheckSize(Rec);
    end;

    procedure CheckSize(var Cust: Record Customer)
    begin
        if not Cust.HasShoeSize() then
            Cust.ShoeSize := 42;
    end;
}
```

- Record params that must persist changes to caller take `var`.
- `this` keyword: codeunit self-reference. Lets a codeunit pass itself as an argument to a method; also disambiguates global vs local scope in long methods (readability). See Learn "Use the this keyword for codeunit self-reference".

<!-- ingested: · Query object | 2026-08-16 -->
### Query objects (normal type)

- `query` object flattens one or more tables into a single row/column dataset; supports aggregation (sum, average, etc.) over columns.
- Two flavours: `QueryType = Normal` (viewable in UI) and `QueryType = API` (web service endpoint only, not UI-displayable).
- Structure: `elements { }` block holds nested `dataitem(Alias; Table)` controls, each containing `column(Alias; Field)` controls.
- Nesting order matters — it sets the link/join sequence and therefore the result set. Top dataitem = first table; child dataitems are embedded inside the parent.
- Joins: set `DataItemLink = ChildField = ParentAlias.ParentField;` and `SqlJoinType = InnerJoin;` (also LeftOuterJoin etc.). **Both properties go on the lower (child) dataitem**, not the parent.
- Child dataitem may link to any ancestor alias, not only its immediate parent (see example: `Country_Region` nested under `Salesperson_Purchaser` but linked to `Customer."Country/Region Code"`).
- `DataAccessIntent = ReadOnly;` routes the query to the read-only replica — cheap perf win for reporting queries.
- From BC v23: `UsageCategory` makes the query discoverable in Tell Me and in role explorer under Report and Analysis. `AboutTitle` / `AboutText` give teaching tips; `ContextSensitiveHelpPage` sets the help link.
- From BC v23: run a query in the client and toggle the **Analyze** switch for data analysis mode; respects user data security, evaluated live.
- Running a query: URL param `?query=<id>`, or a page action with `RunObject = query "<Name>";`.
- Hard limit: a single query cannot span the application database and the business data database — applies even in single-tenant deployments.
- Extension object names max 30 chars.
- VS Code snippet: `tquery` scaffolds a query object.

```al
query 50102 "Top Customer Overview"
{
    QueryType = Normal;
    UsageCategory = ReportsAndAnalysis;
    DataAccessIntent = ReadOnly;

    elements
    {
        dataitem(Customer; Customer)
        {
            column(No; "No.") { }
            column(Sales_LCY; "Sales (LCY)") { }

            dataitem(Salesperson_Purchaser; "Salesperson/Purchaser")
            {
                DataItemLink = Code = Customer."Salesperson Code";
                column(SalesPersonName; Name) { }
            }
        }
    }
}
```

<!-- ingested: · XMLPort object | 2026-08-16 -->
### XMLport object

- XMLport = object for import/export of data between BC and external XML (or fixed/variable text) files. Encapsulates file handling.
- Create xmlport object, then run from page or codeunit: `Xmlport.Run(50112, false, false);` — args: object id, ReqWindow (show request page), SystemPrinter/Import-Export flag. Verify exact parameter meaning of 2nd/3rd args against Learn (`Xmlport.Run(Number, ReqWindow, Record)` overloads exist).
- `Format = xml;` property picks encoding format.
- Optional request page: user sets filters, sorting, import-vs-export choice.

#### schema section

- `schema { ... }` holds node tree. Node kinds used: `textelement`, `tableelement`, `fieldattribute`, `fieldelement`.
- `tableelement(NodeName; "Table Name")` binds a record; nested tableelements iterate child rows.
- Properties on tableelement:
  - `SourceTableView = where("App Name" = filter(<> ''));` — pre-filter source.
  - `XmlName = 'PermissionSet';` — rename node in output XML (node name in AL need not match XML tag).
  - `LinkTable = <parent node>;` + `LinkFields = "Role ID" = field("Role ID");` — join child tableelement to parent record.
- `fieldattribute(AttrName; NodeVar."Field Name") { }` — emits field as XML attribute on the parent node.

#### OnBeforePassVariable trigger

- `trigger OnBeforePassVariable()` on a `textelement` lets you compute the value written out. Assign to the textelement's own name.
- Standard use: convert non-text field to text before export:
  ```al
  textelement(ObjectType)
  {
      trigger OnBeforePassVariable()
      var
          i: Integer;
      begin
          i := P."Object Type";
          ObjectType := Format(i);
      end;
  }
  ```
- Source used `int` as a variable name — `int` is not a reserved word issue-free choice; use a normal identifier.

#### Calling from a page extension

```al
pageextension 50111 PermissionSetExporter extends "Permission Sets"
{
    actions
    {
        addafter(Permissions)
        {
            action(ExportPermissionSet)
            {
                Promoted = true;
                PromotedCategory = New;

                trigger OnAction()
                begin
                    Xmlport.Run(50112, false, false);
                end;
            }
        }
    }
}
```

- Gotcha: `Promoted`/`PromotedCategory` on the action are the legacy pattern; current guidance is promoting via the page's `actionref` in an `area(Promoted)` group.
- Namespaces apply to XMLports too (see [[14-namespaces]]).

<!-- ingested: · Control add-in object | 2026-08-16 -->
### Control add-in object (`controladdin`)

- `controladdin <Name> { ... }` declares a custom visual control hosted in an iframe on a page. Renders web content, charts, maps, or a whole custom web app; exchanges typed data with the server and raises events back into AL.
- Resource properties:
  - `Scripts` — comma-separated list; local files in the package and/or absolute `http`/`https` URLs.
  - `StartupScript` — single script the web client runs once the hosting page loads. Use for init.
  - `StyleSheets`, `Images` — packaged CSS/image assets.
  - `RecreateScript`, `RefreshScript` — run on control recreate/refresh.
- Sizing properties: `HorizontalShrink`, `HorizontalStretch`, `VerticalShrink`, `VerticalStretch`, `MinimumHeight`, `MinimumWidth`, `MaximumHeight`, `MaximumWidth`, `RequestedHeight`, `RequestedWidth`. Fixed dimensions vs. adaptive — set these so phone/narrow-browser layouts stay usable.
- Two-way contract:
  - `procedure Name(args)` declarations (no body) in the `controladdin` = JavaScript functions AL can call. Implement a matching global JS function in the script.
  - `event Name(args)` declarations = callbacks JS can raise into AL via `Microsoft.Dynamics.NAV.InvokeExtensibilityMethod('<EventName>', [arg1, arg2, ...])`.
  - Supported parameter types in the sample: `Integer`, `Text`, `Decimal`, `Char`.

```al
controladdin SampleAddIn
{
    Scripts = 'https://cdnjs.cloudflare.com/ajax/libs/knockout/3.4.2/knockout-debug.js',
              'main.js';
    StartupScript = 'startup.js';
    StyleSheets = 'skin.css';
    Images = 'image.png';

    procedure CallJavaScript(i: Integer; s: Text; d: Decimal; c: Char);
    event Callback(i: Integer; s: Text; d: Decimal; c: Char);
}
```

- Hosting on a page: place with `usercontrol(<ControlName>; <AddInName>)` inside a layout area. Handle add-in events by declaring a `trigger` with the **same name as the `event`**. Call add-in procedures through `CurrPage.<ControlName>.<Procedure>(...)`.

```al
layout
{
    area(Content)
    {
        usercontrol(ControlName; SampleAddIn)
        {
            ApplicationArea = All;
            trigger Callback(i: Integer; s: Text; d: Decimal; c: Char)
            begin
                Message('Got from js: %1, %2, %3, %4', i, s, d, c);
            end;
        }
    }
}
// elsewhere, e.g. in an action:
CurrPage.ControlName.CallJavaScript(5, 'text', 6.3, 'c');
```

#### Gotchas

- **AJAX for packaged static resources must send credentials.** A bare `$.get(url)` omits the cookies/context BC requires and can fail in production. Use `xhrFields: { withCredentials: true }`:

```js
$.ajax({ url: url, xhrFields: { withCredentials: true } })
  .done(function (data) { $("#controlAddIn").text(data); });
```

- **Don't reference font files from stylesheets** in extensions for BC online — they won't render in the client. Either serve fonts from an external CDN or base64-encode them into the CSS.
- Design for touch input, responsive reflow, keyboard access and screen readers; localize strings to the user's BC language.
- Client-side add-in exceptions surface in telemetry (exception type, which add-in, user environment) when telemetry is enabled.
- Related client-side APIs: `InvokeExtensibilityMethod`, `GetImageResource`, `GetEnvironment`.

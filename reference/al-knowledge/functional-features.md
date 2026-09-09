<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Functional feature awareness

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 7. Functional Feature Awareness

Brief "it exists + gist + dev touchpoints" notes on functional features (little/no AL coding). Not
walkthroughs — verify on Microsoft Learn before quoting specifics.

### Finance & Tax
- **Expense Management** (2026 w1) — first-party expense module closing a long-standing gap; AI-first
  (Expense Agent) but usable agentless from the Expense Report. Collection, itemization, per-diem/
  mileage rules, reimbursable-vs-refundable, guests, reimbursement posting; can push to project ledger
  or bill a customer. Dev: setup pages (Expense Agent Setup, Payment Methods, Locations, Management
  Rules, Categories/Subcategories/Groups, Expense Users↔Employees); Expense + Employee Posting Groups;
  posts Expense + Employee Ledger Entries; rules engine. *(Introducing: Expense Management)*
- **Withholding Taxes** (2026 w1) — deduct tax at source on **vendor payments/invoices** (purchase
  side only this release); thresholds, revenue types, multiple sequenced withholdings. Global app
  everywhere except AU/NZ/IN/IT. Dev: mirrors VAT — WHT Business/Product Posting Groups + WHT Posting
  Setup; WHT Entries (realized/unrealized); vendor "WHT Liable" + posting-group fields; enable in G/L
  Setup. *(Introducing: Withholding Taxes)*
- **Excise Taxes / Duties** — configurable general excise types (plastic/sugar/alcohol…) on top of the
  2025 w2 excise framework (CBAM + EPR); calc via Excise Journal (qty × per-item multiplier × rate);
  independent app. Dev: Excise Tax Types (6 bases), Excise Duty Rates (item or FA source), item card
  Excise/Sustainability fast tabs, Excise Tax Transaction Logs; no built-in report yet. *(Excise Taxes)*
- **Self-billing invoices** — customer issues the invoice on the vendor's behalf from a PO/invoice;
  e-invoicing for self-billing deferred. Dev: "Self-Billing Agreement" on vendor Invoicing tab; Posted
  Self-Billing No. Series; Report 413 via Report Selection – Purchase. *(Self-billing invoices)*
- **Fixed Assets — Bonus Depreciation** — accelerated first-year deduction (168K / first-year capital
  allowance) then normal depreciation. Dev: two Fixed Asset Setup fields (bonus %, eligibility date);
  per-book opt-in; separate bonus depreciation ledger entry. *(Fixed Assets)*

### Supply Chain & Inventory
- **Quality Management** — installable extension for automated/scheduled/manual inspections on
  receipts/output/transfers; pass/fail can block sales/purchase/consumption for tracked lots. Dev:
  Quality Inspection/Results/Tests/Templates/Generation Rules/Setup tables; pre-installed on new
  environments; exposes 4 events (created/changed/finished/reopened) via Workflows **and** APIs/Power
  Automate; own Role Center + Contoso data. *(Quality Management)*
- **Drop shipments** — sales/purchase invoicing now independent/either-order; receipt+invoice can post
  together; undo shipment; more ways to create the purchase doc; Order Planning respects drop-ship
  lines. Dev: "Drop Shipment" toggle on Create Purchase Document + planning worksheet, "Get Order
  Lines". *(Drop shipments)*
- **Matching purchase invoices to order/receipt lines** — one invoice line ↔ many non-received order
  lines and/or partial receipts; optional auto-post receipts on invoice post; handles item tracking +
  directed put-away/pick. Dev: "Get Order Lines" + "Matched Order Lines" tree, "Received on Invoice"
  toggle, "Receipt/Shipment No." on tracking. *(Matching purchase invoices)*
- **Supply chain (overview)** — roundup: the above + get-receipt/shipment filters, document mgmt (send
  posted shipments/credit memos, vendor-less purchase quotes), approvals on item/requisition/planning/
  output journals (workflow templates + Power Automate), product info mgmt (variant pictures/attrs,
  item statistics), Description 2 on prod BOM/routing, item tracking on manufacturing journals, and a
  preview of subcontracting. *(Supply chain overview)*

### Sustainability / Compliance
- **Sustainability** — nearing "complete": ESG sales report layouts (CO₂-equivalent per line/total on
  posted sales invoices/quotes), item Product Classification (UNSPSC), preview per-item Carbon Tracking
  Method (average/specific). Dev: **4 new APIs** — Posted ESG Reporting Line (GET), Sustainability
  Value Entry (GET), Sustainability Purchase Line (GET/POST/PATCH), Goals (GET/POST/PATCH); item fields
  (Carbon Tracking Method, Product Classification, UNSPSC extendable enum); Danish OIOUBL e-invoicing
  pilot. *(Sustainability)*
- **E-Documents** — **PEPPOL moved out of base app into a first-party app** (`apps/W1/PEPPOL` in
  BCApps); link inbound e-docs to existing (e.g. intercompany) purchase invoices to avoid duplicates.
  Dev: new **extensibility model** — PEPPOL 3.0 format enum extended via `enumextension` + ~10
  interface implementations (replaces event-based extension); PEPPOL 3.0 Setup page; base-app PEPPOL
  code being obsoleted. Localizations: France payment e-docs, Spain VERI*FACTU preview, Denmark OIOUBL
  + carbon footprint. *(E-Documents)*

### Analytics & Reporting features
- **Financial analytics** — subtotals on deferral Excel layouts, tuned trial-balance family (feature
  flag), OOB analysis views (GL Registers, FA Ledgers) in 28.x. aka.ms/bcfinanceanalytics.
- **Financial Reporting** — tile view; report Categories + life-cycle Status; company-level defaults on
  G/L Setup; **Dimension Perspectives** (one report across dimension values → merged PDF/Excel);
  **Scheduling** (recurrence → report inbox + email); **Audit Log** of who ran what.
- **Inventory analytics** — ABC Analysis (Power BI + W1 Excel + ABC Analysis Setup thresholds), Item
  Age Composition, Word/Excel layouts on legacy reports, 4 pre-built item-ledger analysis views (28.x).
  aka.ms/bcinventoryanalytics.
- **Sales analytics** — Customer Retention overview/history in the Power BI sales app, subtotals on
  sales Excel layouts, 3 OOB sales-order analysis views (28.x). aka.ms/bcsalesanalytics.
- **Subscription billing analytics** — visual makeover of the ~15-page Power BI app + richer demo data.
- **IT Audit reporting** — Permission Overview, Approval User/Entry Overview (28.x), user-mgmt (last
  login/inactive days), change-log/user analysis views; read-only permission + approval/workflow APIs
  (see §6). aka.ms/bcsecurity.
- **Enhanced demo data** — FA/sales/purchasing/subscription demo data via the Demo Data / Contoso
  control tool (extensible) so reports/Power BI/analysis mode light up.

### Platform / Migration
- **Business Foundation & No. Series module** — new logical layer between Base App and System App for
  horizontal ERP concepts (facade + hidden impl, zero-dependency, no localizations, non-breaking table
  moves); first module = **No. Series** (open-source). Dev: depend on **"application"** (redirection
  umbrella) so tables can move layers without breaking; old `NumberSeriesManagement` codeunit obsoleted
  v24, **removed v27** — migrate to Number Series + Number Series Batch codeunits (`GetNextNo`/
  `PeekNextNo`/`GetLastNoUsed`/`SaveState`/`SimulateGetNextNo`) + Number Series Implementation enum +
  interface. *(Business Foundation / No. Series)*
- **Cloud Migration tooling** — (1) build your own SQL-source tool via **Customer Migration Provider**
  interface + enum extension; (2) first-party BC v14 re-implementation tool (core/master + selected
  transactional, replaces config-package, open-source, v28 minor); (3) no-code single-table migration
  from any SQL source via table mappings in Cloud Migration Setup. GOTCHA: system tables inaccessible
  to AL still can't migrate. *(Cloud Migration tooling)*
- **Cloud for Sovereignty** — how public-cloud BC meets EU data-boundary/sovereignty across access
  controls (RBAC/security groups/PIM/GDAP), security controls (isolated per-env SQL DB, customer-
  managed encryption key, BC service tag), sovereignty controls (env localization → Azure geo/region/
  AZ + paired backup), transparency (Purview auditing, just-in-time engineer access + Customer
  Lockbox). Mostly admin/config. aka.ms/bcsovereignty. *(Cloud for Sovereignty)*
- **BC UX & productivity** — agent-centric: updated BC icon, agent task pane (Sales Order/Payables +
  custom), "Created/Updated by" system column (agent vs user), agent review bar, stop-all-agent-tasks,
  in-product feedback (comment + screenshot). Dev: new toggleable list system columns. *(BC UX &
  productivity)*

### Shopify
- **Connector (overview)** — product info mgmt (variant images + attributes → Shopify options, custom
  collections by filter, marketing text, unit cost in price sync, up to 2,000 variants) + presentment
  currency; uptakes Shopify's Jan API version (valid to end-2026); drops the tax-code field. Upgrade in
  April recommended. *(Shopify connector overview)*
- **Presentment currencies** — create sales docs in the buyer's checkout currency, not just store
  currency. Dev: "Currency Handling" field on Shopify Shop card (Order Processing); read-only
  "Processed Currency" on the order. *(Shopify presentment currencies)*
- **Product information management** — item variants carry images + attributes (export as product
  options); custom collections imported + auto-assigned by filter; flat items addable as variants;
  marketing text imports. Dev: Shopify export column on Item Attributes; "Custom Product Collections"
  on Shop card. *(Shopify PIM)*

---

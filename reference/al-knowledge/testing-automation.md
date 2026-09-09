<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Test automation, mocking, datasets, code-review tooling

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 3. Testing & Dev Tooling

**Page Scripting (UAT).** Record/play user-acceptance tests in the web client (Settings menu; online +
on-prem; preview since 2024 w1). Separate record/play permissions; warns in production; **no undo** —
Previous/Next re-executes forward, doesn't roll back data. Insert **Validate** steps (equal/greater/
less) via right-click. Scripts saved as **YAML** (header + captured role + ordered/nested steps);
sharable as a base64 "playback link". Expression language is **Power Fx** over `clipboard`,
`parameters`, `sessionInfo`. Branching (conditional/optional-page, End Scope), Wait steps (default
1000 ms). **Parameterizing + Suites (`include`) are YAML-only** — no UI yet. Best practice: filter the
list so the target row is on top (recording picks the top row); build prerequisites in a separate
script. GOTCHAs: not an HTML automation tool (no charts / embedded Power BI/Power Apps); CI/CD runs on
the roadmap, not yet (client-only). Built on the `bc-replay` npm module (BC 2024 w2); AL-Go runs them
via `pageScriptingTests` (see §4). *(Page Scripting tool)*

**Running AL tests from VS Code (2025 w1 / built into the AL extension 2026 w1).** Testing Explorer
grouped project → codeunit → test, no extra app installed. Run profiles: Publish and Run / Run / Debug
tests / Run with Code Coverage (adds CodeLens "N tests executed this"). Debug a failing test straight
from results (auto-sets up the session — far easier than the old AL Test Tool attach flow). Uses
`launch.json`; pick company via `startupCompany`. **GOTCHA:** VS Code test running does **not** use AL
Test Runners → no AI/data-driven suites, and test-runner setup/teardown events may not fire; isolation
comes from the codeunit's `TestIsolation` property (defaults to codeunit level). Disable via
`AL: Disable Test Running` if it clashes with a third-party tool. Giving agents (Copilot/Claude Code)
the run-tests tool materially improves agentic AL accuracy — AL MCP exposes it outside VS Code.
*(Tests from VS Code)*

**Namespaces workflow (see AL-REFERENCE §33 for syntax).** AL Explorer gains group-by-namespace + a
Namespace column. **GOTCHA:** don't namespace your own code until **all** dependencies are namespaced
(references break when a dependency later gets namespaced); namespace rename / moving an object between
namespaces is a **breaking change**; never use `System`/`Microsoft`/`Utility`/`Common` roots. *(Dev
tools 2023 w2)*

**CLI / build tooling.** `altool` (ships beside `alc`, v6): extract app.json from a `.app`, make a
symbols-only package, get latest supported runtime — for pipelines (needed after .NET 4.8 removed).
`ALDoc` (`aldoc init` scaffolds, `aldoc build` reads a `.app` → YAML → DocFX static HTML from XML doc
comments; wireable into AL-Go). New `AL` CLI (2026 w1): `AL workspace create` (scan app.json →
`.code-workspace`), `AL workspace map` (Mermaid dependency graph), `AL workspace compile` (optimal
parallel graph — BC apps repo 2h → 26 min), `isSimpleOnly` check. `download symbols from global
sources` VS Code command pulls platform/app/dependency symbols (incl. 2nd-level) straight from
Microsoft **public NuGet feeds** (no auth/env/launch.json; symbols-only, no IP concern); `al.nuGetFeeds`
adds your feeds, `useOnlyCustomFeeds` disables MS feeds. `directory.app.props.json` can set the
runtime. *(AL Language 2026 w1 / dev tools 2023–2024)*

**Web-client → VS Code bridge.** Extension Management "Source control details" shows the GitHub repo +
commit an app was built from (AL-Go auto-populates it); "Open source in VS Code" clones + F5 to
sandbox + PR back (needs repo access). "Generate launch configurations for this environment" writes a
matching `launch.json` (publish+attach for sandbox, snapshot-debug for sandbox+prod). Page Inspector
(Ctrl+Alt+F1) "Explore Page/field in VS Code" auto-provisions a dummy project + symbols. Debug into
the System/Base App (respects `NonDebuggable`/`SecretText`). Extension Management "Show and copy"
formats dependencies for app.json; "Download in VS Code" pulls symbols. In VS Code, Ctrl+T (Go to
Symbol) searches dependency contents; `#symbol` in Copilot chat feeds an object (e.g. Customer table)
as context. **GOTCHA:** the AL debugger was upgraded and can't debug older BC services — install an
older AL extension version for that. *(Open in VS Code / from web client / dev tools)*

**Editor niceties.** Pre-release channel on the AL extension (also enables Linux/WSL). Inlay hints for
param names/return types (`al.inlayHints`); hover a Label to see its value; Find References on
triggers/system methods/events. AL Profiler sampling interval 50/100/150 ms (`profileSamplingInterval`).
`alGoSuggestedFolder` overrides project location; `al.compilationOptions.outFolder` puts built apps
outside the project. GitHub Copilot Chat explains/fixes/generates tests but **AL training data is thin
(~330 open-source AL repos vs Python's millions)** — always review generated AL. *(Dev tools 2023 w2)*

**BC-Bench.** Reproducible eval framework (SWE-bench-style) for AI coding agents on **real BC bugs**
(problem statement + the developer's original unit test the agent must pass + reference fix). Supports
Claude Code + GitHub Copilot harnesses; tested models incl. Anthropic Claude (Opus 4.5/4.6) + OpenAI
GPT. Metrics: mean resolution rate ±95% CI (5 runs), pass@5, avg time, version. Public MIT repo — fork
and swap in your own private data set to benchmark against your codebase. *(BC-Bench)*

---

<!-- ingested: API automation made easy for clients and automated tests | 2026-07-26 -->

<!-- ingested: Testing is Boring... Until Now! | 2026-07-26 -->

<!-- ingested: Reviewing the Code Review | 2026-07-26 -->

<!-- ingested: BC TechDays 2023 - Testability - The Hammer and the Nail | 2026-07-26 -->

<!-- ingested: BC TechDays 2022 - Advanced topics in test automation | 2026-07-26 -->

<!-- ingested: Microsoft Presents: Creating High-Quality Test Datasets for | 2026-07-26 -->
### Test datasets for AI features — accuracy + harms (mibuso — Microsoft: Klaus [sic?] & "Frankman"/Frank [sic? name uncertain])
- MS app team's quality process for Copilot/agent features. Two axes: **accuracy** (does output meet spec, scored 0..1 for coherence/fluency/no-fabrication, or programmatic checks) and **safety/harms** (freedom from adversarial-induced harmful output).
- Full pipeline: generate test data → data-driven AI testing → run in ADO pipelines → evaluate in Azure AI Foundry → dashboard in Azure Data Explorer, tracking accuracy/safety day-by-day.

**Accuracy test-data generation**
- Use LLMs with **structured outputs / constrained decoding** to guarantee output conforms to a schema. Plain chat completion or JSON mode guarantees neither variety nor schema conformance.
- MS ships a Python tool (in the **BCTech** [sic? "BC tech repo" — verify exact repo, likely microsoft/BCTech] repo) that pairs with Azure AI Foundry: define a **Pydantic** domain model, instantiate an "element creator", give it context prompt, it emits schema-valid data via constrained decoding. Pydantic does schema validation.
- Recommend the most capable model for generation (talk used GPT-4.1); data volume is small so cost is cents. Newer model (4.1) produced fewer generation errors than older models.
- **Always add a verification step** after generation: static YAML parse checks (e.g. items in expected quote/order match items in test setup; expected customer matches setup) to catch LLM fabrication; plus an LLM pass to flag tests needing manual review (does incoming email align with expected output/data).
- LLMs are weak at dates and math during generation — use function calling to compute those.
- **File format:** started with JSONL (one JSON object per line) — hard to read/review in PRs. Switched to **YAML**, now supported by AI Test Toolkit and AL platform; far more reviewable.

**Sales-order-agent accuracy test orchestration (AL)**
- Test runs in a **foreground session** using the test runner with **isolation disabled**, so writes are committed to the DB (needed because the agent runs async in its own session and reads committed state).
- Multi-turn flow: test creates inbound email → agent monitors mailbox, creates a review task → control returns to test (foreground) → BC user accepts email → agent creates quote → validate output (quote code, lines, customer↔sender match, items) in AL, plus LLM-graded check that the reply email is grounded in the request/expected data. Second turn: user emails to convert quote to order; same validate pattern.
- Static test setup in the test codeunit: customers/contacts (mapped to sender), items, units of measure, variants, inventory setup, number series.

**Harms / safety test-data generation**
- Normal LLMs are safety-aligned and refuse to emit adversarial content, so can't generate harmful test inputs directly. Options: safety-*unaligned* open-source models (some Llama variants), or (recommended) **Azure AI Foundry**'s adversarial simulator.
- Attack classes to test: general harms (violent/sexual/self-harm/unfair), **user prompt injection** (jailbreak), **cross-prompt injection** (XPIA — malicious content embedded in item descriptions, or by an installed extension). Sophisticated attacks: base64 encoding, ROT13, and the **crescendo attack** (escalate across benign-looking turns until model complies).
- BC ships an **adversarial simulation SDK/app** (wrapper over Foundry's Python SDK) using a **callback model** (no direct REST): the feature-under-test requests harms one-by-one via the simulation app; supports multi-turn so the simulator reacts to the feature's previous response.
- Pattern in AL harms test: YAML test file with placeholder tags marking where to inject a harm; at run time the simulator replaces the tag with a harm from Foundry. Marketing-text feature throws on refusal → wrap in a try function → set test output. **No AL assertions**; the test output is exported and evaluated in Azure AI Foundry evaluators.
- Don't store real harmful strings in source control — inject dynamically from the simulator. AI Test Toolkit can hide sensitive data in its UI.
- **AI Red Teaming Agent** (Azure AI Foundry, preview at talk) automates attack techniques (base64, ROT13, jailbreak, etc.) — more about attack delivery than content categories.

**Evaluation**
- Export test output from AI Test Toolkit → upload as query/response dataset to Azure AI Foundry → run evaluators (requires granting the Foundry project permissions on the storage account). Foundry has a **REST API for evaluations** so it can be driven from a pipeline.

**Operational notes**
- Data generation cost is negligible; *running* accuracy/safety tests consumes real tokens (like a live user). AI Test Toolkit surfaces token consumption per run. Don't run on every check-in — trigger on model change, prompt change, or permission/agent-capability change.
- Defence-in-depth against financial harm (e.g. agent selling for $1, or changing a vendor bank account): layered prompts + safety filters + BC permissions/security (sales agent locked to a single customer per run) + tests verifying the agent refuses. No single AI safeguard is relied on.

### Advanced test automation — good tests, mocking, permissions, code coverage (mibuso TechDays 2022 — Luc van Vugt & Nikola Kukrika [sic? "kukrika" from captions — Nikola Kukrika is MS test-tooling PM, verify spelling])

**What to test (risk-based)**
- Prioritise by impact × probability. High-impact = automate first; low-probability + low-impact = usually skip (high maintenance, rarely fails).
- Don't unit-test trivial implementation. Test at feature/API level so a failure names the risk (e.g. "electronic invoicing for private customers" not a low-level field assert).
- Assert messages are the key deliverable — the person who breaks the test won't know its intent. Meaningful messages also tell you where to fix.
- Unit tests = complex public methods in isolation (posting routines, payment matching) with known inputs/outputs, ideally 1:1 with the public method's documented contract.
- No tests yet → start top-down with important scenarios; good scenarios already yield decent code coverage.
- Over-testing cements code: each trivial test must be updated/deleted on every refactor.

**Test speed / structure targets**
- Single test < 2 min; a codeunit < 5 min and ≤ ~50 tests; a test extension ≤ ~30 min. Slow tests can't be used for TDD and are hard to debug in pipelines.
- Run tests locally while developing, not only in the pipeline.
- Mark genuinely long-running tests and isolate them in a separate extension.
- SingleInstance test codeunits keep state while the UI test page is open (not auto-reset) → state bleed across long runs; clear them in the initialize method and avoid where possible.

**Test isolation (test runner)**
- Three modes: per-codeunit (recommended default — rollback/GC at end of codeunit), none/disabled (data persists — needed for cross-session tests), per-method/function (rollback after each method, but slow — avoid).
- Prefer per-codeunit; writing non-conflicting tests is usually easy.

**Rollback / commit control**
- `TransactionModel` = `AutoRollback` [sic? captions say "outer rollback" — verify property/enum name] property: avoid; it forbids commits in scope, which breaks once events/extensibility cause commits. MS still has thousands of legacy uses.
- Modern replacement: `CommitBehavior = IgnoreCommits` [sic? verify exact enum member] attribute — commits within scope are ignored. Combine with an explicit `Error('')` (blank error) at end of test to roll back. Decorate the worried method with the same behaviour rather than testing that no commit happens.

**Test doubles / mocking**
- Never call a live external service from automated test runs — real-money bills have resulted. Test the service call only manually/semi-automated (nAL test run by hand, PowerShell, Postman) ~monthly.
- Highest-risk part of an integration = **parsing the response** into tables (multi-country/version). Hard-code sample responses and TDD the parser. Build payloads with the JSON object API, not string interpolation (`any`/raw string breaks JSON).
- Testable code = loosely coupled, no hard dependencies; lets test code control flow. Techniques: pass a codeunit ID as a parameter (dependency injection), interface + enum extension pointing to a stub, or a setter for an interface provider.
- Security caveat: do NOT make sensitive service endpoints/codeunit IDs configurable (e.g. Shopify) — a compromised setup table could redirect calls. OK for low-sensitivity services (e.g. EU VAT reg. validation, codeunit 248 [sic? verify]).
- Prefer **manual** event-subscriber binding in test code (`EventSubscriberInstance = Manual`); static/auto subscribers change the environment and affect other tests. A manually-bound codeunit's globals persist across the test scope (same instance) → useful for a stateful mock (e.g. a mini payment-service provider mocking PayPal).
- A manually-bound subscriber auto-detaches when the local codeunit variable goes out of scope; explicit `Unbind` is optional (MS rarely calls it).

**Testability-only code**
- Code that exists only to enable testing is a smell; APIs should be testable as-is. If needed, compile testability OUT of the production/AppSource build.
- Options, worst→best: `internal` method (note: `internal` is a compile-time, NOT a security, boundary); a global `isTestMode` Boolean forking production logic (bad — forks prod behaviour; MS gets asked for an `IsTestMode` keyword); integration events with manual binding (OK, but never expose secrets/tokens/auth results — anyone can subscribe and exfiltrate); `internal event` (new — only same extension can subscribe).
- Wrap test-only code in preprocessor directives (`#if <PREFIX>TEST … #endif`) to build separate test vs production apps; means maintaining two test sets (MS does this).

**Demo data**
- rapidstart packages: Extended = Cronus on-prem eval (largest); Standard (SaaS) = MyCompany (no data); Evaluation = less data. Most MS tests depend on Extended config → tests fail on a Sandbox that only has Evaluation data.
- Use MS test libraries + `LibraryRandom` etc. For Docker use on-prem demo data; for SaaS Insider sandboxes use a real country version (not W1) to get the full data set.
- MS aspires to move tests toward Evaluation data and publish a map of which test runs on which demo data.

**Testing API pages**
- Highest risk on API pages: UI-triggered logic (e.g. confirmation dialog) fired during a web-service call → the call dies; trigger flow differs from UI.
- Pattern: setup locks the tables it created (for rollback) → but then the API call can't update them under per-codeunit isolation → so run API tests with **test isolation disabled**, commit immediately after setup, call the service, verify response.
- Reuse `Library - Graph Management` [sic? verify exact name] helper.
- Auth: MS runs tests under Windows auth; Docker under a user. "Secret trick": if there are NO users in the DB, no authentication is enforced (don't rely on this in production). Since BC20 [sic? verify CU] `Library - Graph Management` exposes a subscribable publisher to inject the base URL + basic auth (web-service key) so API tests run in pipelines. (Basic auth is on-prem only — deprecated on SaaS.)

**Testing task scheduler / job queue**
- Disable tasks while running tests (background tasks cause flaky failures).
- Don't test async behaviour; force everything onto a single thread and test flow synchronously → no locks, good coverage. Task scheduler: use a manual-binding "handle" pattern to force single session. Recommendation: migrate off task scheduler toward the job queue (more functionality).
- Job queue: use the job-queue test library helpers to set up, find the entry, and run it in a single session; many MS examples exist.
- To genuinely trigger the scheduler you need a second process → run outside isolation + solve sync-with-ready.

**Testing permissions**
- Verifies the feature works under the expected (non-super) permission set, not just as super.
- Only works with permission **set objects** — XML-defined permission sets create non-system sets the framework can't see.
- `TestPermissions` property/attribute (codeunit-level or per-method) is only a pre-req enabling permission steering. Default value is `Restrictive` → from BC20/BC21 Insider, tests run under `D365 BUS FULL ACCESS` [sic? verify] by default and previously-passing tests may now fail; fix by adding `TestPermissions = Disabled`.
- On-prem only (uses a .NET component; changes permissions in cache, not DB, on the fly — no re-login needed). Install `permissionsmart.app` [sic? likely "Permissions Mock" app — verify name]; bccontainerhelper sets this up.
- Helper: `Library - Lower Permissions` [sic? verify] — start from super (to create data), then step-down: set/add a permission set, or revert to super/unrestricted. Pattern each permission scenario as a twin: one test asserts the permission error without rights, one asserts success with the added set.

**Code coverage (new module, BC21/v21)**
- Enable per-run / per-codeunit / per-test; per-run most useful interactively. Results shown on a Code Coverage page (filter covered vs uncovered) while developing. CI/CD supported; bccontainerhelper support was coming shortly after.
- Targets: ~50% cheap; ~70% = decent suite; ~80% covers most scenarios; ~90% adds error cases; 100% has poor ROI and cements code — aim 80–90%. Coverage is a seatbelt: what's MISSING matters more than the number; focus on scenarios + good asserts.

**Test framework internals & roadmap**
- Layers: `CODEUNIT.RUN` runs tests (no isolation) → the test Runner codeunit adds isolation, result reporting, coverage tracking, test selection, but can't run UI tests → a client-side session is needed for UI tests.
- Since the NAV 14 automation release, UI tests are driven from PowerShell via UI web services (being discontinued). Internal script `ClientContext.ps1`/`script.al`-style [sic? captions garbled "this script Al PS1" — verify] wrappers live in the build folder; anything under the `internal` folder is slated for deprecation, everything above it is the stable interface. bccontainerhelper wraps it.
- Roadmap: MS to retire its old UI client and run tests the same way customers do; move internals under a management API (like publishing extensions); enable VS Code test run.
- **Test discovery / trend-based execution**: MS runs only tests whose coverage map hits the changed lines, with periodic full runs to refresh the map. Planned for customers: per-line → covering test codeunits (method-level mapping is harder), surfaced in VS Code to add to the test runner API.

**Pipeline hygiene**
- Must be able to temporarily disable a failing test (and re-enable within days/weeks); analyse impact, disable+fix or roll back the offending change. Re-run failing tests twice to filter flakiness — but a real failure means something, don't ignore it.
- James Pearson's VS Code AL Test Runner lets you run tests without the UI page.
- MS has ~35k application tests + 80k+ platform tests, plus dedicated UI-rendering, KPI, perf, upgrade tests; quality varies (good/bad/ugly).

**Combinatorial gotcha**
- Individually-passing apps can break in combination (multiple subscribers on one publisher). No framework catches this; test each extension in isolation, then run end-to-end tests on the assembled sandbox. Installing AppSource apps shifts combination-testing responsibility to the user.

### Test runners & isolation — repurposing test framework for data generation (mibuso TechDays 2023 — Jeremy Vyska)
- AL test tool: each test section header names a **test runner**. Default = `Isolated Codeunit` [sic?] — rolls back all transactions at end of each test codeunit. Verify exact caption vs Microsoft Learn.
- Custom test runner: codeunit `SubType = TestRunner`, plus property `TestIsolation = Disabled` [sic?] → framework does NOT roll back at end. Data persists. Use to seed demo/dev/test data; never in production.
- Property `TestIsolation` valid only on TestRunner-subtype codeunits.
- Custom runner also useful to capture test errors and surface them (validation/diagnostic apps) rather than fail-fast.
- Test helper libraries collapse boilerplate: `Library - Sales` [sic?] `CreateSalesHeader`/`CreateSalesLine` (~1 line vs ~12+8 manual); `Library - Inventory` [sic?] for item journal + posting. Confirm library codeunit names/signatures against compiler — captions garbled.
- Seed data on publish: an `OnInstall` trigger in a test/companion app can call generation codeunits so a fresh Docker/empty DB gets full posting setups + master data on install.

### Testability-as-tooling patterns
- Smoke tests: end-to-end mission-critical flows (quote→order→pick→ship) run on schedule in pipeline against next-minor/next-major to catch upgrade breakage before Microsoft's forced upgrade.
- Regression from support tickets: each ticket's repro steps + expected result = a test case; prevents reintroducing fixed bugs.
- Diagnostic apps: iterate all master data in a sandbox checking required setup/fields (e.g. detects someone toggled `Bin Mandatory` on a location breaking blank-bin item journals; detects GL accounts mis-classified income vs balance sheet). Ship in AppSource for customer self-diagnosis.
- Go-live validation: run test *transactions* (not just filters) per migrated record — e.g. attempt sales order/ship/credit memo for every customer, positive adjustment for every item×location — as scheduled pipeline to measure readiness.

### Building tests against empty DB vs Cronus
- Testing against Cronus/localized demo data forces per-region test variants (localization differences). For region-safe reusable tests/demo/impl tools, build against an **empty** database.
- Cost: empty DB needs all foundational data (posting setups, GL accounts, currencies, locations) generated first — expensive by hand; config packages can't easily produce large historical volumes (e.g. 5 yrs ledger entries), but codeunits can.

### Data-extraction → codeunit generator (open-source, preview at time of talk)
- Config-package-like UI: pick tables/fields, apply filters, flag anonymization → generates a zip of AL codeunits (`CreateItem` etc.) that recreate the data via code; check into source control.
- GDPR caution: exporting tenant data into committed codeunits risks leaking secrets/PII; intended default is to anonymize fields by their **field data classification** (GDPR-flagged) so safe-by-default.
- Contoso Coffee demo-data app: companion app that generates the data referenced by Microsoft Learn walkthroughs; frequently preinstalled in new sandboxes. Example of docs-matching seed data (telemetry Power BI app similarly ships sample data before connection).

### Code review tooling & analyzers (mibuso — Tina Kabir)
- **BusinessCentral.LinterCop** (community analyzer by Stefan Maroń, major contributions by Arthur van de Vondervoort) — a "fifth cop" added alongside Microsoft's `CodeCop`, `AppSourceCop`, `PerTenantExtensionCop`, `UICop`. ~57 opt-in rules; enable per-rule in `.vscode` ruleset and in pipelines. Verify exact repo/rule IDs against the project's docs.
- Example LinterCop rules cited:
  - Every `Commit` must have a justifying comment.
  - Record-modifying calls (`Insert`/`Modify`/`Delete`) must pass an explicit run-trigger parameter (no implicit default).
  - **TransferFields coupling rule**: for table pairs joined by `TransferFields`, fields sharing an ID must have matching name and type, else runtime error.
- **TransferFields gotcha (platform behaviour):** ~192 base-app table pairs are linked via `TransferFields` (Customer↔Contact, Vendor↔Contact, Sales Header↔Sales Header Archive, Sales Line↔Sales Line Archive, etc.). Adding a field to one table of a pair without matching the field on the partner table at the same ID causes a runtime error ("the following fields must have the same type") when `TransferFields` runs — e.g. creating a Customer from a Contact via template. A table-extension PR can look safe in isolation yet break because another extension added a clashing field on the paired table. Enforce with the LinterCop rule rather than manual review.
- **Azure DevOps branch policies** for enforcing review: min reviewer count, block self-approval, reset reviewer votes on new push, require linked work item, require comment resolution, auto-include a "code reviewers" group. Set build-validation checks to **expire immediately when target branch updates** so a passing PR is re-validated after another PR merges. `status checks` = gate on an external service (e.g. Jenkins, or GitHub Actions surfaced as status checks) rather than the built-in pipeline.
- **AL syntax-highlight extension for Azure DevOps** ("AL Language syntax highlight for Microsoft Dynamics 365 Business Central", by Microsoft, free) — colourizes AL in the DevOps PR file diff (otherwise plain white). Verify exact marketplace name.
- **ALGuidelines.dev** — community-maintained AL design patterns / best-practices reference; usable as a baseline for an org's own documented coding guidelines. Contributions via PR.
- Squash-merge recommended for a linear, single-commit-per-PR git history (personal preference, not mandated).

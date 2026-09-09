<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# Page scripting, test doubles, Kiota clients, WireMock

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 3. Testing & Dev Tooling

### Page scripting, data-driven testing & AL coded tests (mibuso — Luc van Vugt & Tina Kabir)

**Three complementary test approaches**
- AL coded tests ("traditional"): developer-written, given/when/then, one test per scenario (platform historically had no built-in parametrisation). Run in test isolation — each test reverts DB state automatically. Fast, durable value, but developer-heavy.
- Page scripting: record/replay UI steps, no dev skills needed → consultants/QA can author. Good for UAT, bug-repro capture, regression.
- Data-driven testing: one AL test executes many cases fed from external dataset. Dev builds the flow; functional roles add cases.

**Page scripting**
- Access: gear/cog → "Page scripting" action (preview). Requires permission set; two sets exist — one to record, one to replay. Not visible without permissions.
- Recording: "Start new"; every click/entry captured until stopped. Records the *action*, not the on-screen location — fields can move/reorder and script still works (unlike Selenium/Ranorex-style visual tools that break on layout change).
- Gotcha: selecting from a dropdown records the *row position*, not the value. If list order later changes, replay picks wrong entry. Best practice: use "Select from full list", filter on the primary key so only one row remains, then click.
- Only the *last* recorded step can be deleted in-UI; cannot delete/insert in the middle (edit the YAML for that). Editing mid-script is a requested future feature.
- Right-click field → page scripting → Copy value (stores to page-scripting clipboard) / Paste / Validate current value (equals clipboard entry) — validate turns a recording into an assertion.
- Best practice: always start recordings from the Role Center to avoid ambiguity about starting page; script fails if you replay from wrong page.
- Discipline: whatever you open, close it — leftover open windows cause failures on next run.
- Saved as YAML file (may warn about sensitive data in recording).

**Page script YAML structure**
- Step types seen: navigate, invoke, page (shown), close page, focus, control, input, copy, validate. Stray focus/control steps are noise from mis-clicks — can be hand-cleaned.
- `include` directive references another YAML file (relative path) = shared/reusable steps (preconditions, postconditions). Used for fixtures: e.g. precondition creates item + extended text; postcondition deletes assembly order + item.
- Container must allow file-system access for includes → needs a certificate; must use HTTPS. Prompts to grant access per folder (preconditions / postconditions / script folder).
- Conditional steps exist, but includes cannot be selected conditionally.
- `runtime reference` property in steps: manipulating it (esp. with conditionals) can silently break scripts; no documentation on why. YAML docs not yet published — trial and error.
- Passing parameters into included files is currently weak/unsupported (a wished-for feature).
- Behaviour note: page scripting appears to key on whether a field *exists* in code, not whether it is *visible* — reportedly can write to an invisible-but-existing field. Contested between presenters; seems improved in BC27 preview vs earlier (BC25). `[sic?]` verify current behaviour.

**Running page scripts in a pipeline**
- Uses npm/node package `bc-replay` [sic? verify exact name] which runs on Playwright under the hood. Spins up multiple browser windows in parallel.
- Produces an HTML report via `npx playwright show-report`; failed runs include a *video* of what happened + a link that opens BC with that page script loaded → right-click a step → "Run to here" to reproduce. Lets consultants (not just devs) triage pipeline failures.
- Managed CI/CD (AL-Go for GitHub, ALOps, Alpaca) are adding native page-script support — prefer those over hand-rolling bc-replay.

**Data-driven testing / AI Test Toolkit**
- AI Test Toolkit: install from AppSource; in containers it's part of the test tool kit settings.
- Build one AL test using the AI test context codeunit (`AIT Test` / `AITTestContext` [sic? verify exact object names against compiler]). Test pulls a question + expected response from a dataset, runs the feature, asserts actual == expected.
- Dataset format: JSONL (one object per line) or YAML (nicer grouping). One test method per codeunit — each codeunit links to one dataset.
- Setup in-app: "AI Test Suites" page → define suite → list codeunit(s) with methods → per test set Input dataset via Import data set (browse/paste).
- Under the hood it injects into the standard AL Test Toolkit: creates a suite for the run and expands one test line per dataset row (e.g. 3 inputs → 3 executions).
- Generate more dataset rows quickly with GitHub Copilot once you have a few examples.
- Constraint: currently only runs in an online sandbox — on-prem/container hits a permissions error (reported to Microsoft, fix pending). Cannot run tests in a production environment at all.
- Slower than traditional runs: isolation + cleanup between codeunits adds time.
- Good fit example: VAT posting on sales invoices (many VAT %/posting-group combos → many cases, one flow).

**Error handling limitation (page scripting)**
- Old-style error messages (status bar) break replay. Behaviour with `ErrorInfo` object (actionable errors) unconfirmed — may not continue past them.

**Reported status**
- Page scripting nearing GA (per Microsoft, ~BC27 timeframe). Data-driven / AI Test Toolkit released ~June 2026 ("last month").

**Off-label idea (not shipping)**: presenter prototyped feeding a converted page script into raw Playwright to add slow-mo, click highlighting and named screenshots — for auto-updating instructional videos/docs when UI changes. Proposed YAML properties `slow-mo`, highlight, `screenshot name`. Experimental repo only; page script cannot be fed to Playwright/Cypress directly (custom transform required).

<!-- ingested: Double Trouble: A New Perspective on AL Testing | 2026-07-26 -->
### Unit testing & test doubles in AL — Detroit vs London (mibuso — Vjekoslav Babić)

- Testing pyramid: many fast unit tests at base, fewer integration tests, few slow/expensive manual/E2E on top. Higher up = slower, less reliable, costlier failures (found late).
- Unit test traits: granular (target a function/codeunit), isolated (system-under-test only, no full posting chain), fast (whole suite <10s; a good ~250–300-test suite runs <0.5s), repeatable, run locally dozens of times/hour.
- Only two legit reasons a passing test starts failing: code changed or test changed. A third — data/setup changed — makes a test **fragile** and must not happen in true unit tests. BC base-app suite (~37k tests) has ~15% failures on a fresh container because Microsoft's DB is specially set up for their pipelines; not repeatable for others.
- **Pure function** = no dependencies, no hidden inputs, no side effects, deterministic → trivial to test regardless of size. Size doesn't determine testability; purity does.
- **Impure function** (writes DB, mutates single-instance codeunit global state, calls web service, exports file, reads setup tables) is hard to test → drives up number of Givens. Base app has tests with 30–50+ Givens; tightly-coupled code forces "chasing Givens" (order→customer→posting groups→accounts→inventory setup→location).
- **Fragile** test = fails on environment/data change (outside SUT and test). **Brittle** test = fails on small code changes because tightly coupled to logic. Distinct problems.

#### Decoupling for testability
- To break tight coupling: extract an interface from the collaborator codeunit, implement it, then pass the dependency in as an `interface`-typed **parameter** instead of a local concrete `Codeunit` var. Caller (`buzz`) then only depends on the abstract contract (e.g. a Boolean result), not the concrete.
- Avoid the breaking change by adding an **overload** with the old signature that forwards to the new one using the concrete dependency → same runtime object, no compile/logic break. Mark old overload as "peripheral" (untested); the full injected signature is the critical, tested path.
- VS Code AL has an "extract interface" code action (presenter unsure of exactness — verify).

#### Test double roles (all commonly called "mocks")
- **Dummy** — placeholder passed only to satisfy a parameter; never invoked (use when a code path skips the dependency).
- **Stub** — returns predefined answers to drive execution down a chosen path (e.g. `SetResult(true)`).
- **Spy** — records interactions (was it called, how many times, with which params) to verify behaviour.
- **Fake** — working but non-production impl (e.g. in-memory DB). AL lacks true faking frameworks; "fakes" end up as statics. No on-demand mock generator in AL (contrast C#/TS frameworks that mock a class on demand).
- **Mock** — combined stub + spy, often with built-in assertions/expectations.
- These are **roles**, not separate objects — don't create one object per role per codeunit; a mock can fulfil all roles.

#### Detroit (classicist) vs London (mockist)
- **Detroit**: real dependencies, verify state/outputs, minimal mocking, realistic integrated scenarios. Pros: realistic, stable tests, high confidence, low mocking overhead. Con: slow.
- **London**: isolate everything with doubles, verify interaction/behaviour. Pros: blazing fast, forces good design up front, easy near-100% coverage. Cons: brittle tests, maintenance overhead, feels less realistic, complexity grows with mocking.
- Presenter's stance: London in AL (little choice given language limits), Detroit in C#/TS. Both valid; strike a balance. Mocks are a necessary evil — mock only when other options exhausted (external web service, hardware).

#### AL-specific technique: dependency injection via record parameters
- Can't fake the DB in AL, but passing a `Record` **by reference** (`var`) instead of using a local record turns DB writes into observable, in-memory operations when a **temporary** record is passed → an implicit fake DB, zero runtime cost, big testability gain. Treat the DB as a collaborator and inject it.
- Splitting impure functions into pure+impure halves (author's earlier blog advice) makes tests faster but litters the codebase with trivial insert-only functions; author now considers it not worth it — AL is inherently impure, don't fight purity.
- Extreme London (mocking everything, turning locals `internal`, decomposing into interface-per-collaborator) explodes complexity and produces brittle tests. Turning a `local` into `internal` just to test it is a real cost. Options for heavy private functions: keep local (Detroit), open to internal (London), or decompose into a separate codeunit + interface (compromise, raises complexity).

#### Practical guidance
- Test app: keep tests in a **separate app** for real projects (same-app only for demo convenience / single F5). Do **not** create a separate app exposing testability-only interfaces.
- Getting started on legacy code: start small — pick one (even unimportant) object, unit-test and refactor it; don't attempt a big-bang rewrite. Even Microsoft won't refactor the whole base-app suite at once.
- Copilot writes ~60–70% of tests correctly first try when the mocking framework is transparent/readable and code is well-structured; consistent test naming/flow (happy path first) improves its suggestions. Trick for a fresh empty codeunit: draft 3–4 tests in an existing codeunit, then cut/paste into the new one.
- These principles apply to unit and (somewhat) integration tests, not performance/acceptance/system tests.
- Note: base-app avg per-test time ~700ms; full suite ~7h if run serially — Microsoft parallelises/distributes. Most non-MS suites run serially, so DB round-trips (write + read-back assert + rollback = 3 ops/test) accumulate and dominate runtime.

### Auto-generating REST API clients for AL with Kiota (mibuso — Tobias Fößer & Simon Fischer)
- **Kiota** = Microsoft OpenAPI-based client generator (`Microsoft.OpenApi.Kiota` [sic?] — verify name). Feed it an OpenAPI spec, get generated client code. Officially supports .NET/Go/Java/TypeScript; an experimental **AL target** was added by the presenter (Simon Fischer) — not yet in the mainline Kiota repo.
- Status (as of this 2026-07 talk): AL support lives in a community/fork repo, in contact with Kiota maintainers to merge via the community language-support path first, then upstream. Early draft — expect bugs; needs community testing against real APIs.
- OpenAPI spec (formerly Swagger) can be YAML or JSON. Kiota consumes the spec, not live endpoints — if a third-party API has no spec, generate/convert one first.
- Generation flow: Kiota parses spec → builds a language-neutral document object model (classes/methods/properties) → language-specific *refiner* adjusts it → language *writers* emit target code. AL refiner strips things AL lacks: cancellation tokens (Kiota adds these for async cancel; AL has no async/await), and C#-style get/set property accessors → emitted as explicit getter/setter methods instead.
- Generated AL output: an API client codeunit (entity access + config), request-builder codeunits per entity, and model codeunits per entity (getter/setter per property, `SetBody` with debug switch, `ToJson` serializers — parameterless returns current JSON, parameterized crafts a new object without hand-writing JSON).
- Client usage pattern: `Client.Pet().Item(id).Get()` style — entity method returns request builder, indexer method (`ItemIdx`) for by-id access, then HTTP verb (Get/Post/Put/Delete). Check success on the return before reading properties.
- Depends on a companion library app **Kiota.Abstractions** [sic?] (mirrors .NET `Microsoft.Kiota.Bundle`): shared request-sender codeunit, JSON helpers, `IKiotaApiClient` interface. Goal is to ship it in the System Application. Generic request-sender builds the HttpRequest via the **REST Client module** (AJ Kwaśny / Waldo), sends, and writes the response back onto the client object via a passed-in reference — this back-reference pattern relies on a recent BC platform capability (last major version), so not possible on older versions.
- **Limitations called out:** error handling is minimal — only checks for a success status code; non-2xx does NOT throw, you get no response, so callers must test success explicitly. XML payloads not supported in the AL model yet (JSON only) even though OpenAPI/Kiota can describe XML. OAuth2/negative-response handling still to be built out.
- Implementation workaround to note: AL support was added without modifying existing Kiota code (to ease upstream merge) — extra metadata is smuggled through the element `documentation`/description property as key-value pairs and stripped before docs are written. Flagged as temporary.

### Mocking BC & third-party APIs with WireMock for dev + automated tests (same session — Tobias Fößer)
- **WireMock** = open-source API mock server (originally Java; **WireMock.NET** port exists). Mocks APIs via JSON mapping files or via code. Purpose: remove dependency on flaky/unavailable/competitor/shared backends during dev and automated tests; get fast, stable, isolated responses.
- Mapping = `request` matcher (method + URL, optional body/header matchers) → `response` (status, body, headers). Bodies can be inline or extracted to a separate `bodyFileName` file (cleaner to manage).
- **Admin API** under `/__admin` (e.g. `/__admin/mappings`, `/__admin/scenarios`) inspects/manages mocks at runtime. After adding/editing mapping files you must reload mappings.
- **Recording:** `POST /__admin/recordings/start` [sic? verify exact path] with target base URL — WireMock proxies to the real backend and captures request/response pairs; stop recording to freeze into mappings. Can configure body extraction and which headers to capture (e.g. capture BC's `If-Match`/ETag header). Generated mapping files get cryptic URL/id-based names — rename to meaningful ones for maintainability.
- **Body matching:** full-body exact match, or JSON *partial* matcher (match only specific fields, e.g. `name == fluffy`, ignore the rest).
- **Dynamic responses (templating / handlebars):** randomize values, echo request parts into the response (e.g. request path segment → response id), dynamic dates (e.g. `now minus 7 days`) so demo data doesn't age. Gotcha: a one-time code call (like a C# helper returning a random value) is evaluated once at mapping load, so every request returns the same value — use the handlebar/dynamic template helper to randomize *per request*. WireMock.NET lets you register named custom C# helpers (e.g. random string array, random URL array with min/max) at startup and reference them in templates; requires enabling response templating (`WithTransformer`).
- **Stateful behavior via scenarios:** each mapping declares a scenario name, a `requiredScenarioState`, and a `newScenarioState`. Chains create→get→update→delete with different responses per state (e.g. 404 before create, entity after create, modified entity after update, 404 after delete). WireMock Inspector renders the scenario state graph so you can verify transitions.
- **WireMock Inspector** = .NET tool (`dotnet tool install`) that connects to a WireMock.NET instance to view requests, mappings, scenarios, current state, and active settings; can also generate mapping code from a captured request (pick which parts of request/response matter). Useful because WireMock docs are thin.
- Simulate BC's ETag optimistic concurrency: mock the `If-Match` header requirement so clients are forced to handle it correctly against the mock as they would against real BC.
- **Key payoff:** BC/AL client code and test code are identical whether hitting real BC or the mock — no code change to switch. Full CRUD test suites ran in ~80–420 ms vs ~2 s per real BC call.
- Can also inject **faults and delays** (e.g. every 3rd request errors, or 1–10 s latency) for realistic/load testing.
- **Deployment:** run WireMock locally/in a container during dev; store mocks alongside the app so versioning stays in sync. For automated tests with **BcContainerHelper / AL-Go**, use a *companion container* (define image + URL) so each dev/test environment spins up a matched WireMock instance. Or host on Azure Container Instances / Kubernetes. WireMock has a paid offering that can auto-generate a full mock straight from an OpenAPI spec (free tier can't in the Java build; WireMock.NET free build reportedly can — unverified).
- Note: AL now has a built-in backend-mocking feature (separate session) — better when you live purely in AL; WireMock wins when non-AL frontends/systems also need the same mock.

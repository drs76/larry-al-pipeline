# page-scripting-testing

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: Leveraging page scripting for manual and | 2026-07-27 -->
### Page scripting for acceptance testing

- Page scripting: record user flows in BC web client into a single script file; replay to reproduce flows for manual/automated acceptance tests. Owned by BC client team; ~2 yrs old, still in preview.
- Not a generic HTML automation tool — it is AL-aware: honours app/extension business logic and validation, works across platform versions.
- Recording is forgiving: stop and restart a recording and prior mis-clicks are discarded.
- Give fields just enough input (e.g. partial customer name) and let field validation resolve the rest — avoids over-hardcoding.

**Gotchas**
- Selecting a value in a dialog/lookup by list index is fragile — index shifts when data changes. Prefer entering a search string / value over positional selection.
- Never assume system state. If a script relies on pre-existing data (e.g. one filtered quote) it changes state on run and fails on re-run. Create the data the script needs.

**Editing recordings**
- Recordings have a "current step" pointer. Rewind to step 0 (or any earlier step), hit record, and new steps are inserted at the current position — the workaround for inserting setup steps before an existing recording. UI editing is otherwise cumbersome.

**Best practices**
1. Never assume state — create it in-script.
2. Make scripts modular/atomic (e.g. separate `create sales quote`, `convert quote to order`) as reusable building blocks. Give every script the same starting point (e.g. always start/end at Role Center) so atomic scripts compose.
3. Compose scripts via an `include` step type — set in the YAML in VS Code (not UI): give name, description, and file path to another script. Browser needs file-access permission to load included files.
4. Parameterize scripts to decouple from data. Add a `parameters` property in YAML; each param has type (e.g. `string`), default value, and optional `required`. Reference a param in a field value with a leading `=` (expression), capitalized `Parameters` then the name, e.g. `=Parameters."Customer Name"`. Param names are case-sensitive; quote names containing spaces. In an `include` step, pass values via a `parameters` block on the step — names must match one-to-one. Missing required params prompt via dialog at run.
5. To make a script runnable both standalone and as an include without data collisions, generate unique values: use a Power Fx expression that uses the passed value if it differs from the default, else appends a timestamp.
- Suites (via `include`) give deterministic ordering of composed scripts.

**BC Replay (automation)**
- `bc-replay` [sic? verify name] — public open-source npm package to run page scripts headless without user interaction; for CI/CD (Docker/cloud/sandbox — not production). Source not published.
- Invoke via `npx replay` [sic? verify command] — no JS project needed.
- Params: files/glob to run, starting address (context URL), authentication mode, results directory.
- Auth modes: Windows (default, for Docker), UserPassword, AAD/Entra ID. Entra ID does NOT support MFA yet.
- Credentials passed as `usernameKey`/`passwordKey` [sic? verify] — these name the ENV VARS holding the values, not the literal credentials. Don't inline secrets.
- Runs headless by default (faster, for CI); headed mode available for visual debugging.
- Output: play report with pass/fail; the recording is saved and, on failure, logs are embedded into a copy of the script for diagnosis.
- Glob patterns run multiple scripts as independent parallel instances — but same user/tenant, so shared state can collide; apply the state/uniqueness best practices. Gives incidental light load (not real load testing).
- Watch for time-dependent flakiness (DST, new year) breaking pipelines.

**Internal MS usage (signals of intent)**
- Run as merge/check-in gate in Azure DevOps for every dev change; converted subset of their large e2e test set.
- Migrating perf tests from Selenium toward Playwright; page scripting reduces UI-targeting flakiness.
- Used for bug repros (same as customer support requests) and as final smoke test on real production environments before a cloud build ships.
- Same production page-scripting version as customers — no special internal build.

**Lab/experimental (not committed to ship)**
- Define parameters in the UI (backwards-compatible with YAML-defined ones).
- New step capabilities: iterate over lists/items, copy single row or all rows, conditional/exception step gated on a Power Fx expression (e.g. branch on `Session.UserId = admin` [sic? verify]).
- LLM `run prompt` step: run a prompt, direct output into a target control (drag-drop target) — e.g. generate random item descriptions/test data.
- Server-side / browser-less replay under development to cut execution time.
- Planned/requested: JSON schema for YAML validation; script library/versioning; version-tagged scripts; Performance Toolkit integration.

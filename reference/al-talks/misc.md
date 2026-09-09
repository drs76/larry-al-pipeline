# Misc

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: Microsoft Presents: What's new in Business Central clients f | 2026-07-27 -->
### bc-client-mobile

Notes from "What's new in Business Central clients for AL developers" (BC client team). Mobile + web/platform UX. Version refs: releases 23 and 24.

**Barcode scanning (mobile/tablet only, camera-based)**
- Native OS barcode detection/decode. Camera-based only on mobile+tablet; desktop support floated as future, not shipped.
- Supported formats: common 1D and 2D barcodes; exact set differs per OS (iOS vs Android) for camera; dedicated hardware scanners depend on manufacturer.
- Three scenarios:
  1. **Declarative field action** — set page-field property `ExtendedDatatype = Barcode` [sic? verify exact enum value] on a `Code`/`Text` field. Client renders a scan button; scanned value written straight to the field as text input. No AL logic.
  2. **Camera scan via AL control add-in** — declare a usercontrol using the camera barcode scanner provider add-in (added in release 24). Triggers: `ControlAddInReady` [sic?] (fires when embedded; check camera availability), `OnBarcodeAvailable(barcode, format)` [sic?] on success (args = value + format), `OnBarcodeFailure(reason)` [sic?] on failure. Start scan by calling `RequestBarcodesAsync` [sic?] on the control. AL fully controls start + result handling. Continuous scan = call scan in a loop until a condition, then break.
  3. **Dedicated hardware barcode scanners** — separate from camera. Requires device-level config. Continuous scanning while AL processes codes; suited to warehouse. Setup per page; multiple providers can register but only current/topmost page receives incoming barcodes. AL: declare usercontrol with barcode scanner provider add-in, use `ControlAddInReady` [sic?] readiness check, call `RequestBarcodeScannerAsync` [sic?].
- Hardware scanner integration on Android uses **broadcast intents** (native Android). Device must be set to deliver via broadcast intent. Four config strings required: intent action, intent category, data string, data type. If device only lets you set some (e.g. action + category), get the remaining constants from the manufacturer and pass all four to the request method. If device exposes all four configurable, call the method with no params. MS docs list the four config strings.
- Hardware buying guidance: verify device can send data to other apps via broadcast intent and allows configuring the strings; request a sample and test before bulk purchase.

**Control add-in API change (release 24)**
- Old barcode add-ins were .NET-namespace client accessibility add-ins (`DotNet` [sic?] interface); could not be exposed to SaaS tenants.
- New closed-system control add-in API: MS declares the add-ins in the System App; partners cannot declare their own. Currently only camera barcode scanning + barcode provider add-ins exist. Plan is to migrate all .NET-based add-in APIs (camera, location, contact picker, etc.) to new model over future releases.
- New add-ins are **iframe-less**: no styling properties applied, no custom scripts injectable.
- .NET-based API still supported — existing usercontrol add-ins keep working, nothing broken. Use the new control add-in API for any new barcode work.

**Worksheet pages on phone (release 24)**
- Worksheet pages now render on phone (simplified vs tablet/desktop): short header section, all worksheet lines listed, summary section at bottom; tap a line to slide in a pane with line detail + fact boxes. Tablet unchanged.
- No AL change needed, but phone relies heavily on **field groups** to promote correct fields; revisit pages not previously exposed to mobile to surface optimal fields.

**Help & Support page on mobile (tablet + phone)**
- Now available on mobile under Learn > Help and Support. Compressed version of desktop page. Includes AL profiler start action. Copy session IDs/details for support tickets; supply both copied details and screenshots/video (blur company data in screenshots).

**Legacy list views removed (deprecated)**
- Old behavior: platform auto-generated side views on embedded list pages by reading Role Center navigation actions/cue tiles that shared a `RunObject` page but had different `RunPageView` filters. Views vanished when the page opened non-embedded — a known confusion.
- Replaced by newer view model (introduced a few releases earlier): `views` section on list pages; define caption + filter, sorting, filtering, shared/non-shared layouts; works with design/personalization; users can create custom views.
- Deprecation was gradual: monitored production ~2 releases, added a nagging message, removed once global SaaS usage of legacy views dropped below 5%.

**Instructional text / placeholder (page field property)**
- New page-field property = placeholder/instructional text (a visual guide inside the field about the *shape* of data, not business meaning).
- NOT a tooltip replacement, and NOT accessible — screen readers do not read it. Provide field caption + tooltip too for accessibility; instructional text is optional visual aid.
- Sub-properties: `Locked = true` [sic?] to skip translation (useful when text is a sample/pseudo-regex with no language); add translator comments if translated. `MaxLength` guides length — must be concise/fit in field or it loses value.
- Currently rendered only on page fields of type `Text`, `BigText`, `Guid` [sic? "GD" in captions], `Code`. Docs may list more places than client currently renders.
- Especially valuable on **prompt dialog** (Copilot) pages, which lack both label and tooltip on input fields.
- Not currently dynamic/changeable at runtime; table-field support (like tooltips) not decided.

**Multi-file upload**
- Extends drag-and-drop single-file upload to multiple files. AL: same as file upload action plus a property flagging multi-file; returns a list of files.
- Uploads run in parallel (more efficient); user blocked until all uploaded + processed by AL. Per-file size limits unchanged — SaaS ~350 MB per file [sic? verify current limit].

**New calendar control**
- Redesigned to match Microsoft Fluent UI (Outlook/Excel-like). Same shortcuts and behavior, new look, no AL uptake needed. Week-number display requested but not implemented (complicated by locale-specific week-numbering rules).

**Lab/experimental (not committed)**
- Exploring fact box resizing (primarily for client add-ins needing more room; iframe + flexible-layout edge cases being worked out).
- No API to control initial field focus / cursor placement on page open — acknowledged feedback, not available.

<!-- ingested: BC TechDays 2022 - Troubleshooting Business Central SaaS env | 2026-07-27 -->
### troubleshooting-saas

BC SaaS troubleshooting via telemetry + in-client tools + VS Code debugging (BC TechDays 2022, Oct '22 release).

**Telemetry / monitoring**
- Environment telemetry surfaces events/operations; complemented by a Power BI app (report-usage/telemetry dashboard) shipped this release.

**Connectivity check**
- Reachable at `<baseURL>/connectivity` or `<baseURL>/<environment>/connectivity`. Runs stepwise checks (login, CDN, etc.) between browser and tenant; reports which step failed and remediation.

**Help & Support page (`?` menu → Help and Support)**
- Troubleshoot links: last known error, inspect pages, analyze performance (in-client profiler).
- Report a Problem: collects metadata to send to MS. Shows client + server **session ID** — note it; needed to match DB locks and snapshot debugging.
- Option to enable additional logging.

**In-client diagnostic pages** (search by name)
- **Page Inspector** (`inspect pages`): table fields + which extension each comes from, applied page filters, list of contributing extensions, per-extension load-time contribution for current page.
- **Database Locks** [sic? "database logs"] — verify page name: shows active locks on a table incl. the session ID holding the lock. Used to diagnose hung save/write.
- **Table Information**: per-table stats — record count, table no., data size, index size. Click record count to drill into the actual table data (field list, changeable view).
- **Database Wait Statistics**: waits grouped by category, start time, duration.
- **Database Missing Indexes**: MS analyzes your queries and suggests indexes on searched fields (suggestion only — cannot alter your code).
- **Event Recorder**: open in new window, record a scenario, get list of triggered events (type `event trigger` = system, plus custom events). Use to check whether a subscribed event actually fires / matches.
- **Effective Permissions**: per-user permissions per application object (read/execute/etc.), viewable by permission set. Diagnose why a user can't run a report or log in.
- **Scheduled Tasks**: overview of background tasks on tenant; "show job queue details" gives recurrence, timeout, object ID/type (codeunit or report).
- Report request page: press "Send to" [sic? consent/preview] and export to Excel (raw data, or data+layout) to inspect report dataset without publishing.

**Debugging enhancements (VS Code, Oct '22)**
- Database statistics per debug frame now shows **locks taken** on each stack frame during stepping.
- New launch setting: exclude breaking on temporary record read/write.
- New setting: exclude breaking on try-function errors.
- launch.json can now specify **startup company** alongside startup object for F5/Ctrl+F5.

**Snapshot debugging**
- Non-intrusive recorder of stack frames; the ONLY way to debug **production** (real debugger blocked in prod — it can lock tables). Requires a permission set to run.
- Records stack frames continuously; captures full variable context (globals + locals) only at **snap points**.
- **Snap points** = breakpoints, but must be placed *ahead of time* — only locations where variables are collected. AL runtime errors are treated as implicit snap points (context always captured on error).
- Flow: set snap points → F7 start session → run scenario → Alt+F7 stop → downloads a `.zip`/snapshot file to snapshots folder → debug the downloaded file.
- Four states: initialized (server waiting for client) → started (do scenario now) → finished → downloaded (only downloaded snapshots are debuggable).
- launch.json fields: session ID (attach to that session if found), user ID, **snapshot verbosity** (limit to snap-point frames only to shrink file — AL↔server is chatty), execution context, profiling type (debug / profile / both).
- `break on next` waits for next matching client to connect. View sessions via bottom-left button.
- Limits: 10 min max scenario recording; 30 min in initialized state to reach started or session is kicked. Override output path via snapshot output setting.
- Respects resource exposure, non-debuggable methods, dynamic IP protection (same as normal debugger). Debugged user gets a big dialog warning their session is being snapshotted.
- **GDPR**: collected variable values may be GDPR-relevant — handle/distribute snapshot files with care.
- Debug start behavior: breaks on first snap point; else first error (if any); else first stack frame (likely not useful).
- Debug Console evaluates variables at a frame — useful for large values (>~1KB) that inline peek truncates. Executed lines highlighted in gutter.
- Works for web API debugging: delegated admin snapshots a session running on behalf of another user (needs OAuth bearer token via registered Azure AD app client ID/secret in Postman).

**Profiling**
- Two collection techniques:
  - **Instrumentation** (older, ~2021): based on snapshots; high overhead, resource-intensive, big file, captures every call with full detail. Good to get started / find what's slow.
  - **Sampling** (Spring '22): low overhead, samples stack top at fixed interval (default 100 ms, customizable on-prem); may miss short calls but usually good enough.
- Concepts: **self time** = own instructions + system calls (excludes AL sub-calls); **full/total time** = start→end incl. children.
- Sampling exposed two ways: (1) in-client profiler (end-user friendly); (2) VS Code via snapshot.json profiling type = sampling instead of instrumentation.
- Generate profile from a snapshot: command **Generate Profile File** → produces `.alcpuprofile` file. Editor follows Google Chromium CPU-profile format.
- Views: **top-down** (call stacks as executed, self + total time) and **bottom-up** (inverse — each frame + its callers).
- Columns sortable; built-in query language — type `@` for command help, e.g. filter self time `> 3000`. Click a frame to Go To Definition if source/symbols available.
- Because it's Chromium format, `.alcpuprofile` opens in Firefox Profiler (load from file) or Chrome/Edge F12 DevTools — but MS-specific extras (go-to-source) only work in the VS Code editor.
- In-client profiler output (`.alcpuprofile`) can be opened in a VS Code AL project. Double-clicking the downloaded file does NOT auto-open (AL language server init from the file not yet supported).

<!-- ingested: NAV TechDays 2019 - Make the most out of Business Central on | 2026-07-27 -->
### bc-docker: networking, orchestration, Azure SQL for BC containers

Docker for BC — **dev/test only, no Microsoft production support** for BC containers (same on-prem and cloud). Vote item raised for prod support. Dev license limited to 120 KB [sic? — likely refers to a size cap on dev license objects/permissions; verify].

**Why containers over VMs:** share host OS kernel (no guest OS), lower resource overhead, fast create/start/stop, run many BC/NAV versions side by side on one host.

**Rule of thumb — resource scaling:** an NST (Server) in a container uses the same resources as one running outside a container. Size container count per VM the same way you'd size NST instances per VM. SQL Server adds overhead on top.

#### Three ways to expose containers on a shared/central host

**1. Port mapping** (`docker run -p hostport:containerport`)
- Map each container port to a distinct host port. First container can reuse native ports (e.g. web 80→8080, dev 7049→7049); second must shift (e.g. 8180, 7149) — same host port can't be bound twice.
- Ports to consider per BC container (~9, not just NST 7045–7049 [sic? range]): web client HTTP/HTTPS, SOAP, OData, dev service, possibly SQL, and the landing/download page on 8080.
- Downsides: must track free ports, tell users which port per container, open firewall ports (two firewalls on Azure — NSG + host firewall).

**2. Transparent networking** — each container gets own IP + hostname via DHCP/DNS; connect by name on standard ports, nothing to document.
- `docker network create` with driver type transparent [sic? verify driver name]; `docker run` with `--name` and hostname.
- Requires MAC address spoofing enabled on hypervisor (Hyper-V "MAC address spoofing" / VMware "promiscuous mode") — a network interface receives traffic for another MAC.
- **Works on-prem; does NOT work for external access on Azure** (Azure blocks MAC spoofing / the extra MACs). Only usable inside the Azure VM.

**3. Reverse proxy (Traefik)** — single entry point, path-based routing to containers.
- Traefik is container-native, runs as its own container, integrates with Docker (watches Docker endpoint, auto-discovers containers by their **labels**), built-in Let's Encrypt (auto cert + renewal), or bring your own cert.
- Routing via container labels: `traefik.enable=true` plus rules. Path-prefix rules map e.g. `/nav-server` → container port 80; download page `/…dl` uses PathPrefixStrip (strips prefix) → 8080; regex rule rewrites `/bca/rest…` → `/BC…` on port 7048. [label key syntax sic? — verify exact Traefik v1 label names against Traefik docs]
- BC container extra config needed so generated URLs are correct: set public web/SOAP/OData base URLs and public DNS name; give the web server instance a **custom name** (default insists on redirecting to `/NAV` or `/BC`). Supported by BC images.
- **Health-check gotcha:** BC image health check hits the public DNS name → goes out through Traefik → but Traefik only routes *healthy* containers → deadlock (never becomes healthy, never routed). Fix: point health check at `localhost` inside the container instead of the public DNS name.
- Setup: NAV/BC Azure ARM template has an "Add Traefik" toggle (aka.ms get-bc/get-nav template); navcontainerhelper supports `-useTraefik`; own VM uses a setup cmdlet [sic? name — verify in navcontainerhelper] to provision the Traefik container + config.
- Files on host: `C:\ProgramData\navcontainerhelper\traefikforbc\config` — `traefik.toml` (from a template) + `acme.json` (Let's Encrypt cert). traefik.toml declares domain, Docker endpoint to watch, entry points 80 + 443 (redirect 80→443), Let's Encrypt email.
- Limits: HTTP-based traffic (web/OData/SOAP/dev) works out of the box; **TCP traffic (SQL via SSMS, classic Windows client) does not** on Traefik v1 — v2 (then new) may support it, unverified. SOAP/OData endpoints return **wrong URLs** (return internal `…/BC…` not the configured public path) — workaround: client-side rewrite the returned URL path.
- AL launch.json: use Traefik path as `serverInstance` (e.g. `nav-server/dev` [sic? path form]), port **443** (everything tunnels through 443).

#### Scaling beyond one host — Docker Swarm

Single host caps out (~10–25 containers). Swarm = Docker's built-in orchestrator; pools multiple hosts under central management.
- Concepts: **service** (image + task count + config); tasks **replicated** (`--replicas N`) or **global** (one per node); **nodes** = manager (control plane; connect here) + worker (run workload).
- Declarative + self-healing: declare desired state, swarm maintains it (kill a task → auto-recreated). Round-robin placement by default; can add resource/constraint-based placement. `--constraint node.role!=manager` to keep workload off managers.
- **Configs & secrets** auto-distributed across swarm; container must be explicitly granted each config/secret at `docker service create` time.
- **Ingress networking:** connect to a published port on ANY node → routed to a task wherever it runs. Requires **stateless** service — **BC container is NOT stateless, so ingress routing not usable for BC**.
- **Overlay network:** service-to-service discovery by name across hosts — usable with BC.
- Setup: open TCP + UDP swarm ports (2 TCP, 2 UDP) [verify exact: 2377/tcp, 7946 tcp+udp, 4789/udp]; `docker swarm init` on manager → prints join token; workers run `docker swarm join` with token. `docker-compose` (stack) files work with swarm for declaring services (Traefik, portainer agents as global, portainer on manager, etc.). Portainer used as GUI. Prod needs 3 or 5 managers (single manager = single point of failure).
- **Death-spiral guard:** set a restart retry limit (e.g. try 5×, then stop) so a perpetually failing task doesn't loop forever.
- Autoscaling workers: use a VM scale set; new VM on boot runs `docker swarm join` with shared token (roadmap idea, not built).
- kubernetes rejected here: BC is stateful (loses k8s benefits), steeper curve, and no Windows-only cluster (k8s needs ≥2 Linux pods).

#### SQL: Azure SQL + elastic pool (instead of SQL per container)

Problem: one SQL Express per container wastes resources and hits **10 GB Express DB size limit**.
- Azure SQL (PaaS): no server maintenance/patching, near-unlimited scale, scale cores up/down (e.g. on >90%/<10% for 1h). Costs money.
- **Elastic pool** shares compute across DBs so idle DBs lend resources to busy ones.
- BC container connects to external SQL by passing server name / instance / username / password — identical whether Azure SQL or your own SQL Server.
- **On-demand DB provisioning pattern:** container checks at startup if its target DB exists; if not, copies from a template/master DB (e.g. a CRONUS copy), then starts normally. Access via an **Azure service principal** scoped narrowly (read on subscription; write on the template SQL server + target server). BC can't use service principals for its own login, so a SQL-auth password is also stored as a secret.
- Perf trade-off: Azure SQL runtime perf is strong once up; **backup/restore & bacpac import/export are very slow**. ~400 MB DB copy ≈ 1–1.5 min; large DBs painful. Tip: upload on a Premium tier then scale down. For frequent fresh-DB setup, local SQL on the container host may beat Azure SQL.

#### Windows auth inside containers
- Local laptop: reuse Windows username/password.
- Stable/domain: use a **gMSA** (group managed service account) — one account per container, container assigned the gMSA (domain-join-like). Azure AD sample exists but lightly tested.

<!-- topic file split from AL-KNOWLEDGE.md; edit here, not in the index -->
# CI/CD with AL-Go for GitHub

Part of [`AL-KNOWLEDGE.md`](../AL-KNOWLEDGE.md) — see that index for the other topics.

---

## 4. CI/CD — AL-Go for GitHub

Microsoft's plug-and-play DevOps for BC on GitHub — secure CI/CD without Docker/PowerShell/YAML
skills. Templates: `microsoft/AL-Go-PTE` and `microsoft/AL-Go-AppSource`. Workshop aka.ms/ALGoWorkshop,
release notes aka.ms/ALGoReleaseNotes, deprecations aka.ms/ALGoDeprecations.

**Change behaviour via settings, never code.** Scopes: repo-wide
`.github/AL-Go-Settings.json`, project `<project>/.AL-Go/settings.json`, workflow-specific, plus
repo/org **Variables** (no per-project variables; app.json is app-specific, not AL-Go). Know your
version: `templateUrl` ends `@main`/`@preview`; actual version printed in each run's "Initialize" job.
Every run has a **check-for-updates** job; run **Update AL-Go System Files** to pull latest (Direct
commit=yes commits, no=opens a PR). **MUST create secret `GHTOKENWORKFLOW`** (PAT with workflow-modify)
to run it; v6.4 lets it run across multiple branches + a `workflowSchedule` cron+branch-list setting
(works around GitHub scheduling only the default branch). "Indirect template" repos let you inject
custom jobs/steps that merge down into consumers.

**Build & performance.** Container-less builds: `useCompilerFolder: true` + `doNotPublishApps: true`
+ `githubRunner/runs-on: ubuntu-latest` → whole pipeline on **Linux** (~half the cost, ~⅓ faster;
container pull was ~11 of ~14 build min → ~4.5 min, ~3.5 warm). Trade-off: `doNotPublishApps` disables
tests (no service tier) — why it isn't default. **Incremental builds** (2025 w1) rebuild only changed
apps (unchanged copied from last-known-good; now on CI/CD, was PR-only) — pair with **workflow
concurrency** (cancel superseded builds). Conditional settings per **build mode** (e.g. NextMajor
grabs the next-major artifact); `preprocessorSymbols` array passes compiler directives. No more
`.buildartifacts` — all builds emit full artifacts (default 1-day retention). Versioning strategy 3
(app.json controls major.minor.build, GitHub the 4th digit). `commitOptions` (`messageSuffix`,
`pullRequestAutoMerge`, `pullRequestLabels`) — MS's BCApps uses it for Azure Boards `AB#<id>` linkage.

**Delivery & deployment.** GitHub **Environments** + `environments` setting minus `excludeEnvironments`
(unavailable on free-tier private repos). v4 replaced per-env secrets with a **`DeployTo<Env>`**
settings object (`environmentType` default SaaS, `environmentName`, `branches`, `projects`, `syncMode`
ForceSync/Add, `continuousDeployment`, `runs-on`) — secrets got masked by GitHub and couldn't pass
between jobs. Custom target: `environmentType` ≠ SaaS calls your **`.github/DeployTo<Type>.ps1`**
(on-prem/Azure VM, e.g. via ALOps external deployer or a self-hosted runner inside a customer
firewall). `dependencyInstallMode` (install/upgrade missing deps incl. AppSource at deploy);
`includeTestAppsInSandboxEnvironment` + `excludeAppIds`. **Publish To Environment** with `PR<id>`
(e.g. `PR28`) deploys a PR's changes for pre-merge testing (missing apps pulled from last-known-good).
GOTCHA: PR artifacts expire after 1 day — rerun the PR build then republish if it errors.

**Quality & testability.** Page-scripting tests via `pageScriptingTests` (array/globs of recorded
`.yml`) + a result visualizer (failure video). **BCPT** performance tests have a UI: run in CI/CD or
scheduled against a baseline JSON + thresholds file — duration-regression % and **SQL-statement-count
%** (e.g. warn 15%/error 30% duration; warn 10%/fail 20% SQL — SQL count is the top regression cause).

**Security (the through-line).** Third-party actions pinned by **commit SHA** + Dependabot (full
AL-Go test suite runs on each bump); AL-Go's own actions stay tag-pinned. **Federated credentials +
managed identities** remove stored secrets (GitHub OIDC → short-lived ~1h scoped token; Azure grants
the identity; only TenantId/ClientId stored). **Azure Trusted Signing** (2025 w1) — no cert rotation/
stored cert secrets (account → identity validation → cert profile → managed identity role "Trusted
Signing Certificate Profile Signer" → federated creds → `AZURE_CREDENTIALS` → `TrustedSigning`
setting). Code signing needs HSM key storage (since July 2023) — Key Vault **Premium (HSM)** SKU.
**GitHub App auth** (`appId` + private key, short-lived scoped token, bot identity) beats PATs; ladder
= classic PAT → fine-grained PAT → GitHub App (GitHub Packages still needs a `packages:read` PAT).
Reference secrets inline in `installApps`/`installTestApps` so SAS tokens aren't in clear text. MS
pushes monthly security requirements into AL-Go's own pipelines — partners inherit them.

**Dependencies → NuGet.** AppSource app symbols on a public feed (`AppSourceSymbols` v3, auto-trusted);
`trustedNuGetFeeds` (URL + optional `authTokenSecret` + registered prefixes/cert fingerprints — don't
trust nuget.org unprotected; NuGet auth doesn't yet support federated creds). One package per app;
full-app packages carry the whole dependency tree, symbols packages none. GitHub Packages naming →
`<AppName>.<AppId>` (resolution still by app ID + version).

**Roadmap.** Runtime packages to NuGet (needs the compiler to generate them from symbols alone); all
first-party apps as NuGet; run tests + page-scripting on online environments during publish; finalized
indirect/private templates (~April/May 2025). **AL-Go is moving off BcContainerHelper over ~2–3
years** — DevOps features shift to new PowerShell modules / GitHub Actions; BcContainerHelper stays on
PS Gallery but eventually unsupported. Managed-DevOps users (AL-Go/ALOps/Cosmo Alpaca) unaffected;
self-built pipelines will need rework. BC samples: aka.ms/bcsamples (GitHub topic `bcsamples`).
*(AL-Go videos 2023 w2 + 2025 w1: build&perf, delivery&deploy, quality&testability, security, what's-next)*

---

<!-- ingested: BC TechDays 2023 - Using AL-Go for GitHub | 2026-07-26 -->

<!-- ingested: BC TechDays 2022 - Git under the hood | 2026-07-26 -->

<!-- ingested: NAV TechDays 2019 - Build, test, deploy and deliver your app | 2026-07-26 -->
### Azure DevOps YAML multi-stage pipelines for BC apps (NAV TechDays 2019 — Kamil Sáček? [sic? presenter name not stated in captions, verify])

Pre-AL-Go era; hand-written Azure DevOps YAML, not GitHub Actions. Concepts still apply to any pipeline-as-code BC build.

**YAML pipeline structure**
- Parts: `variables`, `resources`, `triggers`, and process tree of `stages` → `jobs` → `steps`.
- Stage = isolated unit; can be re-run independently if it fails.
- Two job types: build job (CI) and deployment job (CD). Deployment job is bound to an `environment`.
- `environment` can require approver sign-off; pipeline waits at that stage until approved.
- Deployment strategy: only `runOnce` is meaningful for BC (the other, `canary`, is Kubernetes-oriented).

**Variable/expression syntax**
- Compile-time expansion `${{ }}` [sic? verify] — resolved when pipeline is generated at start; no access to runtime-only values (e.g. params set by earlier scripts). Not recursively re-expanded when used as display name.
- Runtime macro `$( )` [sic? verify] — expanded during run; use when value comes from a prior step. Recursively expanded when passed as script args.
- Variable groups (name/value syntax) store predefined values in Azure DevOps; can back onto Azure Key Vault for secrets (username/password/AAD app ID used for publishing).

**Triggers**
- `trigger` filters by branch and by changed file paths/folders (e.g. skip rebuild when only docs change).
- `schedule` uses cron syntax; `always: true` forces a run even with no code change (e.g. nightly rebuild against latest BC master image to catch breakage from new platform version).
- Skip CI by putting a skip token in the commit message — but it is visible to everyone in history.
- Triggers can be overridden in the Azure DevOps UI, overriding the YAML.

**Build stage steps (pattern)**
- `checkout` with `submodules: recursive` to pull dependent apps stored as git submodules.
- Install modules (BcContainerHelper etc.) at run time since agent may not have them.
- Create container from variables; import test toolkit/test libraries only (not the full CSIDE/base).
- Install NuGet client so dependent apps can be auto-downloaded from an Azure DevOps NuGet feed during publish.
- Compile task walks all `app.json` in the work dir, orders by dependency, compiles+installs in order automatically.
- Enable code analyzers (code cops); treat analyzer warnings as errors to fail the build.
- Publish app to container skipping signature verification (app not yet signed).
- PowerShell step reads app/test-app ID and writes it back as a pipeline variable via a logging command (host write) so later steps (e.g. run-tests-by-app-ID) can use it.
- Export runtime package (for on-prem installs) and the generated translation (.g.xliff [sic? "translation G file"]) — generated .g.xliff must be in .gitignore, it's a build product not source.
- Always remove the container (`condition: always()`) so a leftover container doesn't block the next run. Other conditions: succeeded/failed vs always vs succeededOrFailed (not on manual cancel).

**Later stages**
- Install-and-test stage: reinstall produced app.file into a fresh container to verify dependencies resolve and it runs; delete runtime app first.
- `dependsOn` controls stage ordering; multiple stages fan-out (parallel) / fan-in.
- QA stage: deploy app but not test app (nobody runs tests there).
- Sign stage: certificate stored as Azure DevOps secure file, pulled by `DownloadSecureFile` task, path exposed as `secureFilePath` variable; sign after all testing so the stamp = officially released build.
- Package as NuGet and push to Azure DevOps artifact feed — NuGet tracks dependencies, so consumers download top app and deps come automatically (Universal Packages lack this).
- Release-to-SaaS stage: deploy to online sandbox via Automation API v1; auth with AAD app (registered) + partner credentials.

**One-file caveats (why not to do it)**
- Can't make triggers dynamic per pipeline in a single file; both linked pipelines fire on push, differing only by internal stage conditions.
- Deploy-in-CI-pipeline is bad: cancelling the deployment cancels the whole pipeline.
- A manually-run "release" pipeline sharing the file picks up the last successful build of the build pipeline — can grab the wrong artifact.
- Hard to separate release vs build results on dashboards; heavy copy-paste; updating N repos to change the process is costly.

**Recommended: split + templates**
- Split into build / check-with-master-image / release pipelines, plus a variables file, all referencing shared templates.
- Store templates in a central repo referenced as a `resources: repositories` entry (can point at another project via a service connection, or GitHub). Update the template repo once → all consuming pipelines pick up the new process on next run.
- Templates take typed `parameters` with defaults; use `${{ each }}` loops to generate stages dynamically (e.g. one release stage per target environment). Pass `dependsOn` as a parameter to reorder parallel/serial stages.
- Result: build file dropped from ~558 to ~86 lines.

**Gotchas / error decoding**
- Cryptic "wrong number of segments" [sic? verify exact text] error almost always means a referenced task name/version is wrong or the task was renamed.
- Task/step groups belong to classic pipelines; not source-controlled/versioned — avoid mixing with YAML.
- Classic release pipelines are legacy; prefer YAML for version-controlled, reproducible, easily-recreatable pipelines.

**App scaffolding automation**
- Whole app+3-pipeline creation (build/release/check) scriptable via REST API + PowerShell: assign distinct ID ranges, patch app.json, apply NuGet deps, create+trigger pipelines. Throughput network-bound (~200–500+ apps/hr observed).
- Pattern: model each app as an Azure DevOps work item of type feature (extended template with ID-range fields); user stories/tasks link to the feature=app, and the next free ID range is pulled via REST API.

**On-prem deploy options**
- Build agent running on customer server (security risk — agent has server access) OR mark builds with a tag and run a script on the customer server that connects to Azure DevOps, filters tagged builds, downloads artifacts (or installs via NuGet feed), and installs. Remember to update the customer license.
- Automation API also usable on-prem if the agent can reach it (e.g. hybrid network).

### Git internals — how git actually stores things (mibuso TechDays 2022 — Vjekoslav Babić)

Background for BC devs on why git behaves as it does; no AL specifics but explains merge/branch/rebase pain in BC repos.

- Git is a CLI content tracker, not a daemon: it does nothing until invoked. VS Code's git UI comes from a filesystem watcher running git commands and parsing output — git itself does not monitor files.
- Command tiers: **porcelain** (user-facing: `clone`, `push`, `merge`) vs **plumbing** (low-level: `cat-file`, `hash-object`, `reflog`, `fsck`). Tools call plumbing under the hood.
- Core storage = a persisted content-addressable key/value store. Key = SHA-1 of the content; value = arbitrary bytes. Everything is binary to git.
- `git hash-object` computes the SHA. It hashes header + content, not raw content: `"<type> <byte-length>\0<content>"`, then zlib-compresses and stores under `.git/objects/<first2>/<remaining38>`.
  - Same input → same SHA on every machine. But identical-looking text can hash differently by shell: bash pipes UTF-8, PowerShell `echo` emits UTF-16LE + BOM → different bytes → different SHA. Hashing an actual file gives identical SHA regardless of shell (binary-identical).
- `-w` flag writes the object to the store; requires being inside an initialized repo (`git init`).
- Object types: **blob** (file content), **tree** (list of pointers to blobs/subtrees, i.e. a directory), **commit** (points to one root tree + parent(s) + author/committer/timestamp/message). All identified by SHA.
- Dedup: identical content stored once. Two files with same bytes → one blob, referenced from multiple trees. Unchanged subtrees across commits are shared (same SHA), not recopied.
- SHA propagation: change a blob → new blob SHA → parent tree SHA changes → new commit SHA. Commit SHA is derived from full commit content incl. timestamp, so rewritten history always yields new SHAs (can't forge identical history).
- Objects are **immutable**; the SHA↔content bond is permanent.
- Git stores **snapshots, not deltas**. It tracks content, not changes. Diffs/changesets shown in tools are computed on demand via `git diff`, presented to humans (who reason about change better than snapshots).
- `git diff` walks trees top-down comparing SHAs; if a tree's SHA is unchanged it skips the entire subtree (fast even with millions of files). Rename/add/delete detection is educated guesswork — a rename+content-change in one step can be misreported as delete+add.

### Git — three areas, branches, HEAD (same talk)

- Three areas: **working tree** (files you see) → **staging area / index** (`.git/index`, a single binary file = blueprint for next commit) → **local repository** (`.git`). `git add` is the real command (no `git stage`). Commit turns the index into a commit object.
- A **branch** is just a 40-byte file at `.git/refs/heads/<name>` containing the SHA of one commit. Creating a branch = new tiny file; no copying. Committing advances the file's SHA. Branches are near-free storage-wise but cost via divergence/merge conflicts.
- `.git/HEAD` names the current branch (`ref: refs/heads/<name>`). Checkout rewrites HEAD (and syncs index + working tree). Commit reads HEAD, then advances the pointed-to branch.
- **Detached HEAD** = HEAD points directly at a commit SHA instead of a branch ref. Not dangerous; normal for inspecting/debugging old commits. `git bisect` automates checking out commits to find the one that broke something.

### Git — recovering lost commits, garbage collection (same talk)

- Deleting an unmerged branch (`git branch -D`) leaves its commits **dangling** (not deleted). Abandoning a detached-HEAD commit does the same.
- `git reflog` = history of changes to branch tips/HEAD (distinct from `git log`). Lists SHAs no longer reachable from branches; check one out to recover.
- `git fsck --lost-found` shows dangling commits. Only the topmost dangling commit is reported; its ancestors are recovered transitively when it is.
- GC retention: dangling commits kept **min 14 days**; anything a branch ever pointed to kept **90 days** (reflog lifetime). After that, GC reclaims them. GC runs automatically on fetch/merge/rebase (and can be invoked directly).

### Git — rewriting history: reset, amend, rebase, squash, cherry-pick (same talk)

- Rewriting never mutates existing commits — it always creates **alternate history** (new SHAs, old commits dangle).
- `git reset <sha>` / `git reset HEAD~1` moves the current branch pointer back; `~1` = one commit up the first-parent line. Modes:
  - default (mixed): puts changes back into working tree
  - `--soft`: puts changes back into staging area
  - `--hard`: discards them (commits dangle)
- `git commit --amend`: replaces the last commit (new SHA) — add forgotten files, fix message, change author. Old commit dangles.
- **All rewrite ops are safe only before pushing.** Git refuses to move a remote branch tip backward on normal push. `git push --force` overrides this — it updates remote branch tips without safety checks; use only on your own branch when certain.
- **Merge**: creates one commit with two parents, joining two histories. After merging: delete the topic branch; never keep developing from the pre-merge parent commit; never branch off a topic branch — both cause repeated conflicts downstream.
- **Fast-forward**: when the target branch has no new commits since the branch point, git just advances the branch pointer — no merge commit, no conflicts. The ideal case.
- **Merge --no-ff**: force a merge commit even when fast-forward is possible, so history records that a branch was integrated. Required by some models (git-flow) / DevOps PR policies.
- **Rebase**: does NOT reattach commits to a new parent (impossible — parent is part of the SHA). It **replays** each commit (via diff) onto the new base, producing new commits (C', D'); originals dangle. Then typically fast-forwards. Direction matters: always rebase your topic ONTO master (`checkout topic; rebase master`); doing `checkout master; rebase topic` rewrites master into a local-only history you can't push — this is the danger.
- Rebase conflicts surface per-commit (many small, focused resolutions); merge conflicts surface once at merge level but can be nastier (two histories, git diff can't attribute the conflict source).
- **Squash**: replays N commits as a single combined commit.
- **Interactive rebase**: replay with per-commit control — reorder, edit, drop, reword, squash. GitLens gives a GUI; otherwise editor with instruction file.
- **Cherry-pick**: replays selected commits from another branch onto current HEAD (new SHAs, prime commits). Do NOT cherry-pick merge commits — they carry two histories and give garbled/inconsistent results (`invalid object` type errors). Use interactive rebase to pick multiple commits instead of many single cherry-picks.

### Git — branching models & binaries in repos (same talk, Q&A)

- Recommendation: **trunk-based development** (trunkbaseddevelopment.com) — one long-lived branch (master/main), everyone commits there (directly or via short-lived PR branches). Fewer parallel branches = fewer artificial merge conflicts.
- Sharing one branch across multiple devs requires a **rebase workflow** (`git pull --rebase` before pushing); merge-based sharing produces constant merge-commit conflicts.
- Prereq for trunk-based: commit small and often (multiple times/day), no long-lived feature branches. Gate unfinished code with **feature flags / dark releases** (as BC/VS Code/Windows do) rather than long-lived branches.
- **Release flow** (Microsoft): trunk + short/mid-lived release branches per supported release; cherry-pick fixes from master into them; delete/archive at end of support. Good for SaaS-style offerings.
- Maintaining many perpetual branches (dev/test/QA/pre-prod/prod) is discouraged — extra maintenance and conflict resolution for little benefit.
- **Binaries / large files**: git handles binary fine as bytes; the problem is conflicts — on conflict git injects text markers that corrupt binaries. Avoid concurrent edits (soft-lock via team coordination). Prefer NOT committing built AL `.app` artifacts (rebuilt → conflicts); fetch large binaries via scripts from outside git if possible (they still cost on every push/fetch). Git-LFS mentioned as the mechanism for large files.
- Tip to reduce AL merge conflicts: keep blank lines between logical units (e.g. between table fields). Adjacent field additions by two devs are more likely seen as independent additions rather than a conflict when separated by blank lines. Translation/XML files still conflict-prone due to poor line structure.
- Branch SHA reference is min 4 hex chars (full SHA = 40).

### Using AL-Go for GitHub — day-to-day workflow (mibuso TechDays 2023 — Freddy Kristiansen & Christoph/KB)

**Repo/project structure**
- Two template repos: one for **PTE** apps, one for **AppSource** apps (build/release differs). Start a repo from `Use this template`.
- Hierarchy: organization → one or more AL-Go **repositories** → one or more AL-Go **projects** → apps (regular, test, BCPT). The **repository** is the release vehicle (releases happen at repo level). A **project** = the set of apps installed together (e.g. a country/localization variant).
- Adding an app: either run the `Create a new app` action (supply object ID range) or just drag-drop/commit the app source into the repo. Any push triggers the CI/CD pipeline automatically.

**Test apps**
- An app is auto-detected as a test app if it has dependencies on the test-framework apps. If a test app lacks those deps, list it manually in the `testFolders` setting so it's still treated as a test app.
- Tests run on every PR and every commit; the previous release is located and used for upgrade testing before tests run.

**Branching / releases**
- Recommended strategy: stable `main`; branch out for features; PR into `main` with mandatory build+test+code-review (mandatory can be relaxed per repo). Forks are more secure than branches for contributions.
- Creating a release: run the `Create release` action, specify version, name, tag; select a release branch to release a hotfix from it.
- On release, AL-Go **auto-bumps the version number in `main`** so main is always newer than any release branch (avoids version conflicts, guarantees main > release).
- When PRing into main while a release exists, AL-Go uses the previously-released bits as the *previous build* for upgrade tests.
- **Cherry-picking hotfixes back to older release branches is NOT built into AL-Go** — it only provides the branch structure + build/release. Use GitHub tooling (e.g. GitHub Desktop to move a commit between branches).

**Build-summary gotcha**
- The pass/fail-per-app + failed-test view uses GitHub's **job summary** feature (introduced ~end 2022), capped at ~**535 chars** [sic? number from captions — verify]. With many failing tests it overflows and truncates. If you see *nothing*, it means lots of tests failed — download the full test-results artifact to see all failures + call stacks.

**Deployment**
- Continuous deployment to a **QA environment**: create a GitHub Environment, add two secrets — the auth secret and the **environment name** secret. Multiple sandboxes supported via multiple environments. Apps auto-deploy in correct **dependency order** on every build.
- Continuous deployment **to production is not supported** (at time of talk) — production deploys are manual/gated; planned to allow auto-deploy-to-prod once all tests pass.
- Environment secrets are only accessible during deployment, not to users — reduces risk of wrong-file/manual-upload mistakes.
- Manual fallback: a consultant without env access can download the built .app artifact from the build and publish it manually.

**Know-before-your-customer (scheduled compatibility testing)**
- Scheduled workflows test your app against future BC versions: **test current** (current version, e.g. 22.2), **test next minor** (e.g. 22.3), **test next major** (e.g. 23.0). Runs on a schedule (next-major ~weekly) even with no repo changes.
- Rationale for developing on the *lowest* version you must support (not latest): avoids accidentally using components absent in older customer versions. Develop on that baseline, let scheduled workflows flag future breakage — gives ~6 months lead time before deprecated→removed features become errors. Deprecation warnings show up in test-current output for planning PTE fix work.
- Requires an **Insider SAS token secret** (`insiderSasToken` [sic? verify]) to access insider builds. Planned to be removed as a requirement in future.

**Updating AL-Go itself**
- `Update AL-Go System Files` workflow = like Windows Update for AL-Go. Run manually or on schedule to pull the latest AL-Go version. CI/CD warns when newer system files are available.

**Project dependencies (multi-project builds)**
- Setting `useProjectDependencies` [sic? verify] changes the pipeline from init→build→deploy→post into a **multi-stage dependency-ordered build**: base projects (e.g. common, misc, W1) build first, then dependents (e.g. Italy, Denmark that depend on W1), then deploy.
- **GitHub Packages** for internal dependency resolution: create secret `GitHubPackagesContext` [sic? verify] with an auth context that can publish packages. Org-level secret → all projects publish; project-level secret → scoped. Downstream apps resolve their deps as NuGet packages from GitHub Packages during the `Resolving dependencies` step.

**Future directions stated at talk (not shipped, no dates)**
- AppSource app **symbols** (and opt-in **runtime packages**) served from a NuGet feed; AL-Go auto-trusts the AppSource NuGet server. To consume other partners' NuGet packages you must trust their feeds.
- **Performance rework**: split build and test into two jobs. Build won't need a Windows container → can run on **Linux runners** (~half the price of Windows). Tests run on a container or alternative test environments (Cosmo Alpaca build containers, Azure Container Instances, online sandboxes) — some already warm, so faster. Goal: all workflows runnable on Linux.
- Cosmo Alpaca to support AL-Go directly from the VS Code extension (Dev containers).
- **Page scripting**: exported YAML from page-scripting recorder to be run as tests in CI/CD. LeapWorks DevOps integration announced. Power Platform support planned as next item.

**Alternatives noted**: On Azure DevOps, use **Cosmo Alpaca** or **ALOps** instead of AL-Go for GitHub.

Goal framing: AL-Go aims to cover 100% of the functionality needed by 90% of partners without editing YAML or PowerShell.

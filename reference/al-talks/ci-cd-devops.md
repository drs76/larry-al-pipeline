# ci-cd-devops

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: NAV TechDays 2018 - CI/CD for Business Central | 2026-07-27 -->
### CI/CD for Business Central (Azure DevOps)

**Concepts**
- CI (continuous integration): developers merge work often into a shared main branch; every incoming change auto-builds and runs automated tests *before* it enters main.
- CD = continuous delivery (produce a releasable, tested build; final push to customer is a manual trigger) OR continuous deployment (that push is also automated).
- Prereqs: automated tests, a monitored main repo, and — for AppSource — test coverage of ~90% of code.

**Repo / project setup**
- Devs work locally in VS Code (not on a server); `docker` container used as the local dev/build sandbox.
- Starting a project from a template repo: create empty repo in Azure DevOps and import from the template git URL, or clone template locally and push to new remote.
- After cloning from template you must replace template values with your own: app id, app name, project name, `app.json`/`launch.json` container name, translation (xlf) files.
- Two apps per repo — main app + test app; test app declares a **dependency** on the main app (id/name/publisher/version) in `app.json`.
- Use a **VS Code multi-root workspace** (`.code-workspace` file) to work on both main and test apps at once — needed for test-driven flow so you don't switch windows. Each folder is its own AL app; workspace settings live in the workspace file.
- Advania/vjeko-style community extensions can auto-perform the template rename + workspace setup (`Ctrl+Shift+P`). [sic? extension name — verify]

**Symbols gotcha (test app)**
- Building the test app needs the test library symbols, but running the tests needs the actual test library *objects* in the container — symbols ≠ objects. Import the test toolkit objects into the container to actually execute tests.
- After importing test libraries as an *application*, the test objects end up in both the test symbols and the app symbols → build error. Fix: remove the test symbol app entry from the test app's `app.json` download list, then re-download symbols. (Presenters expected this to get simpler once the whole app platform is extension-based.)

**Build pipeline (YAML)**
- Pipeline-as-code: `azure-pipelines.yml` in repo root. Benefits: versioned with source, editable in VS Code, reusable via templates.
- Steps a BC build performs: prepare env, run code analysis, spin up docker container, import test objects, compile app in container, publish/install app, run tests, collect results, save the produced `.app` artifact.
- YAML `resources` block references a separate **template repository** (by branch/commit/tag) holding the reusable step templates; pin to a specific commit/tag to avoid template changes breaking your build, or track `master` to always get latest. Fixing a bug in the template propagates to all pipelines using it.
- Template steps run PowerShell (or any task Azure DevOps supports). A repo-local PowerShell script sets vars: container name, image name, license file path, test-app and main-app folder locations.
- Creating the pipeline: Pipelines → New → pick repo → DevOps auto-detects the `.yml`. On first save it forces a run; cancel if you still need to add a variable group (e.g. a password variable for Windows auth on the agent).
- **Agent** = a small app running on some server, connected to Azure DevOps, that picks up queued jobs. Can be on-prem (self-hosted) or Microsoft-hosted; hosted agents + azure docker images work with script tweaks.

**Branch policies / pull requests**
- Lock main branch with a **branch policy** so direct pushes are rejected — forces a feature branch + pull request. Pushing to a policy-locked branch fails on push; recover by creating a branch pointing at your commit and pushing that.
- Policy options: minimum number of reviewers; "allow users to approve their own changes" (self-vote counts toward the minimum only if enabled); require linked work item; require all comments resolved; **build validation** (linked build pipeline must pass); merge type.
- Merge types: no-fast-forward keeps all feature-branch commits in main history; **squash** collapses them into one commit (recommended, then delete the feature branch).
- Build validation runs the build+tests on the PR *before* merge, not after. When reviewer approval + build success + resolved comments + linked work item are all green, PR can complete → merge into main. **Auto-complete** does this automatically (can also auto-delete the branch and close the work item) — can happen overnight.
- PR description template: add `.azuredevops/pull_request_template.md` [sic? exact path — verify] to repo; its contents pre-fill the PR comment box.
- Feature branch names with `/` render as subfolders in the DevOps branch UI.
- Choosing the download source: `launch.json` can hold multiple configs (e.g. container vs local server); on download-symbols DevOps asks which to use.

**Release pipeline (CD)**
- Release pipeline takes the built `.app` as input (can combine multiple app artifacts into one release) and deploys/tests it across environments: current BC version, next-release ("master") BC, a QA server for manual consultant testing, integration tests.
- Must also test **upgrade codeunits**: install the app over an environment that already has the old version to confirm data upgrades correctly.
- On-prem/self-hosted: full end-to-end auto-deploy is possible. BC online (SaaS): no — the signed app must go to the AppSource team who validate and deploy; direct push would need an API (not available at time of talk).
- Release pipelines were **not** YAML-definable yet (planned ~Q4 of that year; still backlog/unplanned at recording — verify current state).

**Artifacts**
- Artifact feed is part of Azure DevOps, private to your org account. Presenter used **NuGet** format because it carries dependencies (test app → main app resolves automatically on download).
- A newer **"Universal Packages"** format [sic? verify name] was in preview: simpler, holds arbitrary files, has a default pipeline task to push, but had no dependency support yet.
- Community PowerShell module can download an app from the feed by name/URL and pull its dependencies automatically. [verify module]

**Misc**
- Everything shown for AL also works for old C/AL — artifacts become `.fob`/`.txt`/backup files; expect hybrid pipelines for the ~12–24 month transition.
- Azure DevOps (Boards/Repos/Pipelines/Artifacts) is a viable alternative to the Atlassian stack (Jira/Bitbucket/Bamboo). Can connect DevOps pipelines to a Bitbucket repo, but auto-trigger-on-commit may not fire since DevOps isn't notified of Bitbucket events.
- GitHub/GitLab pipelines use similar YAML (the YAML pipeline syntax originates from GitHub-style config).

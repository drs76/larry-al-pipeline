# open-source-contribution

Distilled talk notes. Not hand-verified — see [`README.md`](README.md) for caveats, and check anything marked `[sic?]` before relying on it.

<!-- ingested: BC TechDays 2022 - Collaborating on Business Central's open | 2026-07-27 -->
### open-source-contribution (BC system app & base app on GitHub)

- System application is first BC app fully open-sourced; lives on GitHub. Base application open-sourcing announced as a **controlled pilot** (private repo, invite-only at time of talk, ~2022 / v21 era).
- Universal Code: no more code customizations — extensions only, cloud-targeted. Contributing to the platform is the sanctioned way to land fixes you'd previously have made in base/system app.
- Repo layout mirrors the AL app extensions repo: `modules` folder (system app), W1 apps, and a `layers/W1` folder holding the base application. Base app pilot ships **W1 only** — no local/country base app versions initially.

**Contribution prerequisites**
- GitHub account; basic git (branch/merge/commit/history); VS Code + AL language extension; basic Docker.
- Dev environment set up via AL-Go (`AL-Go` [sic? confirm capitalisation `AL-Go for PTE`]) — run its script; it pulls a generic image and creates the BC container automatically. AL-Go is itself open source.

**Standard GitHub flow**
- Fork repo → clone locally (direct clone/push to upstream not allowed). Can auth + clone via GitHub CLI (`gh`).
- Branch off `main` (never commit to main directly) → commit → publish branch → open PR against upstream `main`. The "GitHub Pull Requests and Issues" VS Code extension can create the PR from the editor.

**CI**
- Runs on every push to a PR: builds app, builds tests, runs validations.
- Built on AL-Go; at time of talk CI covered the `modules` folder.
- External PRs require **manual approval by a maintainer** before CI workflows run (security gate against fork-triggered workflows).
- Planned/aspirational: CodeCop rule investment, test-coverage gates, better test framework (esp. mocking external deps), performance regression tests, breaking-change checks (exists internally, not yet in AL-Go pipeline), continuous delivery so merged PRs reach live SaaS tenants within hours.

**Base-app controlled contribution model (pilot)**
- Everything starts with a GitHub **issue** that must be approved before a PR is accepted. Three issue templates: bug/get-started, feature request (redirects you to BC Ideas), and security vulnerability (has its own reporting policy — don't file security issues as normal issues).
- Only file issues you intend to fix yourself — not a channel to report customer/product defects to Microsoft.
- Large contributions: raise via BC Ideas → a PM tags it "contribution candidate" → spawns a Yammer design discussion + a linked GitHub issue.
- Issue kanban states: needs triage → issue approved → design discussion → ready for implementation → (create PR linked to issue).
- PRs not linked to an approved issue/idea are closed. PRs require a set number of sign-offs (community + Microsoft code review) before merge.
- Initial merge is **manual**: maintainer team ports the passed PR into the latest release branch; ships with next minor.

**What's worth contributing**
- Commodity functionality everyone expects, core horizontal building blocks, non-critical bug fixes, extensibility requests (new events/making things extensible), small "paper cut" fixes.
- Real examples cited: Azure Blob Storage integration (shipped), Azure File Storage + SharePoint integrations (in progress at time of talk), barcode provider.

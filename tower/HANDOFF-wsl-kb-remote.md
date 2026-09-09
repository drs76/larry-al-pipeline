# HANDOFF — wire `KB_REMOTE` on the WSL client

> **SUPERSEDED 2026-08-28. Do not follow the token steps below.** They predate the two-destination
> contract: the token must be written to **both** `~/.pi/.kb-token` and `local.zsh` from one fetch,
> or every non-interactive caller gets a silent 401. Use
> `tower/handoff-scripts/kb-client-setup.sh`, which does that and verifies each source against
> `/stats`. Current instructions live in `tower/wsl-setup.md` and `pipeline/KB-SEARCH.md`. Kept as
> the record of how the WSL client was first wired.

**For the WSL-side Claude Code session.** Written 2026-07-09; **KB server host moved to Larry
2026-08-06** (was deb). Goal: make `kb` search (CLI + MCP + pi ext) work on this WSL box by
querying the remote `kb serve` on **Larry**, instead of a local sqlite index it doesn't have.

Background: the KB hybrid-search index (`kb.db`) + `kb serve` now live on **Larry's local disk**;
Larry serves at `http://larry.home.arpa:8848` (token-gated, LAN-only). Setting `KB_REMOTE` flips
`kb_core.search/stats/corpora` from local sqlite to HTTP — the CLI, the MCP server, and the pi
extension all inherit it. See `setup/pipeline/KB-SEARCH.md` §"Serving".

## Steps

1. **Confirm the tooling checkout exists on WSL** (needs `kb` + `kb_core.py`, NOT `kb.db`):
   ```bash
   ls setup/tooling/kb setup/tooling/kb_core.py       # from the setup repo checkout
   ```
   Note its absolute path. If the repo lives somewhere other than `/mnt/rojaws/localDev`,
   remember it — you'll set `KB_BIN` for the pi ext and put the right `kb` on PATH.

2. **Do steps 2–3 with the script instead** — it fetches the token, writes both
   variables to the right files, and verifies, without ever printing the token:
   ```bash
   setup/tower/handoff-scripts/kb-client-setup.sh
   ```
   Re-run it any time the token is rotated. The manual steps below are kept for
   reference, but note: **never** `grep` the token to the terminal —
   ```bash
   ssh larry 'grep KB_SERVE_TOKEN ~/.config/kb/serve.env'   # ✗ prints the secret
   ```
   printed it into a session transcript on 2026-08-16 and forced a rotation. If you
   must do it by hand, pipe it straight into the file you are editing.

3. **Add to the WSL shell env** — `~/.config/zsh/.zshenv` (this box uses ZDOTDIR=~/.config/zsh,
   NOT ~/.zshrc):
   ```bash
   export KB_REMOTE=http://larry.home.arpa:8848      # use http://192.168.0.173:8848 if DNS doesn't resolve
   export KB_REMOTE_TOKEN=<token from step 2>
   # if the setup repo is NOT at /mnt/rojaws/localDev, also point the pi ext at the kb script:
   # export KB_BIN=/abs/path/to/setup/tooling/kb
   ```
   Then `exec zsh` (or open a new shell) to load it.

4. **Verify**:
   ```bash
   curl -s http://larry.home.arpa:8848/health        # -> {"ok": true}  (proves reachability)
   setup/tooling/kb stats                            # -> 6 corpora incl bcquality (680 chunks)
   setup/tooling/kb search "how does telemetry work in BC" -n 4
   ```
   `kb stats` showing the corpora = remote query working. If `/health` fails: DNS (try the IP),
   or deb `kb-serve.service` down (`ssh deb 'systemctl --user status kb-serve'`).

5. **MCP (optional, if this box runs Claude Code with the repo `.mcp.json`)**: the `kb_search`
   MCP tool auto-inherits `KB_REMOTE` from the environment Claude Code launches under, since
   `server.py` imports `kb_core`. Just make sure the env vars from step 3 are exported in the
   shell that launches Claude Code. No `.mcp.json` change needed.

## When done
- Delete this handoff (`git rm setup/tower/HANDOFF-wsl-kb-remote.md`) and commit, or leave it —
  it's harmless and documents the client setup.
- Optionally note completion in the `project-wsl-client-setup` memory (pull the memory repo first;
  it doesn't auto-load on WSL).

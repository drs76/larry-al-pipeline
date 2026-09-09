---
description: Generate a deterministic interactive bash wizard that walks a human through setup steps only they can do (logins, secrets, consoles) — no agent or network at runtime
argument-hint: "<what to provision / set up>"
---
You produce a **deterministic interactive bash wizard**: a single self-contained script that
walks a *human* through the steps only they can perform — signing in, clicking a cloud console,
pasting an API key, trusting a CA, physically moving a file. The agent's job is to WRITE the
script, not to perform the steps. At **runtime nothing touches an LLM or the network** except the
URLs the human opens themselves; the script is pure bash the user can read before running.

The thing to provision is:

$@

Adapted for this estate (see the setup repo + memory): most real uses are Larry-client
provisioning — a new WSL/ThinkPad/Windows-host client, a WireGuard client, HomeLab CA trust,
`/etc/hosts` pins, the pi 0.81 provider fix, bonsai on a new box, or a power-on catch-up list.
Turn those manual checklists into a guided script.

---

## Step 1 — Interview for the steps (small batches, 2–3 per round)

Do NOT start writing until you know the sequence. Establish:

- **Goal + done-state:** what exists at the end, and the one check that proves it (a file present,
  a `curl` reaching a host, a command returning 0).
- **Steps, in order.** For each: is it **human-only** (login, console click, paste secret, physical
  act) or **automatable** (mkdir, write config, `gh secret set`, `curl`)? The wizard drives the
  human-only ones and just *does* the automatable ones.
- **Inputs the human supplies** and where each must land: `.env`, `~/.config/...`,
  `local.zsh` (gitignored — see the zsh-ZDOTDIR note), a GitHub secret, `/etc/hosts`, a CA store.
  Mark which are **secret** (never echoed, never committed).
- **Target hosts** it will run on: deb, Larry (Rocky), Windows Git Bash. Keep it portable.
- **Where the script + its state file live.**

Summarise the plan back before writing.

## Step 2 — Write the script (follow this skeleton)

House rules the emitted script MUST obey:

- `#!/usr/bin/env bash` + `set -euo pipefail`. Self-contained, no external deps beyond coreutils.
- **Resumable + idempotent:** a state file records completed steps; re-running skips them. (Same
  ethos as the ingest pipeline's video-ID index — a re-run only does what's left.)
- **Each step: explain → act → verify → mark done.** Never mark a step done without its check
  passing. A failed check stops the script (the human fixes and re-runs).
- **Secrets:** read with `read -rs`, never print them back, write only to the intended file, and
  keep that file out of git (the `local.zsh` / `.env` gitignore pattern). Prefer `gh secret set`
  for repo secrets.
- **Root ops:** use `doas`, never `sudo` (sudo needs a password non-interactively on deb); note
  the NFS `root_squash` caveat if it touches `/mnt/rojaws`.
- **Opening URLs / prompting** must degrade gracefully across deb, Larry and Git Bash.

```bash
#!/usr/bin/env bash
# <name> wizard — generated <date>. Deterministic; no agent/network at runtime.
# Re-run any time: completed steps are skipped.
set -euo pipefail

STATE="${WIZARD_STATE:-$HOME/.<name>.wizard-state}"; touch "$STATE"
done_step(){ grep -qxF "$1" "$STATE"; }
mark(){ grep -qxF "$1" "$STATE" || echo "$1" >>"$STATE"; }

c_ok=$'\033[32m'; c_hd=$'\033[1m'; c_no=$'\033[31m'; c_z=$'\033[0m'
step(){ printf '\n%s[%s]%s %s\n' "$c_hd" "$1" "$c_z" "$2"; }
ok(){   printf '  %s✓%s %s\n' "$c_ok" "$c_z" "$1"; }
die(){  printf '  %s✗%s %s\n' "$c_no" "$c_z" "$1"; exit 1; }
ask(){    local v; read -rp  "  $1 " v; printf '%s' "$v"; }
secret(){ local v; read -rsp "  $1 " v; echo; printf '%s' "$v"; }
pause(){  read -rp "  ↵ press enter when done… " _; }
open_url(){ { command -v xdg-open >/dev/null && xdg-open "$1"; } 2>/dev/null \
         || { command -v open >/dev/null && open "$1"; } 2>/dev/null \
         || { command -v cmd.exe >/dev/null && cmd.exe /c start "" "$1"; } 2>/dev/null \
         || echo "  open this URL: $1"; }

# ---- a human-only step: explain, send them off, then verify --------------------
step 1 "Sign in and create the token"
if done_step step1; then ok "already done"; else
  echo "  Opening the console. Create a token with scope X, then copy it."
  open_url "https://console.example.com/tokens"
  tok="$(secret 'Paste the token:')"
  [ -n "$tok" ] || die "no token entered"
  umask 077; printf 'EXAMPLE_TOKEN=%s\n' "$tok" >>"$HOME/.config/example/.env"
  ok "saved to ~/.config/example/.env (gitignored)"; mark step1
fi

# ---- an automatable step: just do it, then verify ------------------------------
step 2 "Pin LAN hosts"
if done_step step2; then ok "already done"; else
  doas sh -c 'grep -q larry.home.arpa /etc/hosts || echo "10.0.0.9 larry.home.arpa" >>/etc/hosts'
  getent hosts larry.home.arpa >/dev/null || die "host pin failed"
  ok "larry pinned"; mark step2
fi

# ---- final proof ---------------------------------------------------------------
step 3 "Verify"
curl -fsS https://larry.home.arpa/ >/dev/null && ok "reachable — setup complete" \
  || die "not reachable — check the steps above and re-run"
```

## Step 3 — Deliver

- Write the script where the user said (default `~/wizards/<name>.sh`), `chmod +x` it.
- Tell them to **read it first**, then run `bash ~/wizards/<name>.sh`.
- State plainly: deterministic, resumable, no egress at runtime; secrets go to `<file>` and are
  gitignored.
- If it belongs in the setup repo (a reusable provisioning flow), say so and offer to add it
  under `setup/tooling/wizards/` — but the user commits/pushes.

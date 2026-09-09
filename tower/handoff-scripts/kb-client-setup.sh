#!/usr/bin/env bash
# kb-client-setup.sh — point this box's `kb` at the Larry-hosted index, or refresh its
# token after a rotation. Idempotent: safe to re-run, rewrites existing lines rather
# than appending duplicates.
#
# Run it on a CLIENT (WSL, thinkpad, the Windows box, anything without
# ~/.local/share/kb/kb.db). It:
#   1. fetches the bearer token from Larry over ssh — ONCE
#   2. writes KB_REMOTE       -> .zshenv, or ~/.bashrc on a Git Bash box   (not secret)
#      writes the token       -> ~/.pi/.kb-token, ALWAYS, chmod 600
#      writes KB_REMOTE_TOKEN -> local.zsh on a zsh box                    (same value)
#   3. verifies EVERY source separately against /stats, and exercises the file fallback
#      with the env var cleared
#
# Why both destinations: ~/.pi/.kb-token is the fallback kb_core.py, the pi kb-search
# extension and al-rag use when KB_REMOTE_TOKEN is not in the environment. Writing only
# the zsh export left that file holding the pre-rotation token, so interactive zsh worked
# while the MCP server, pi and every Windows shell got a silent 401.
#
# The token is piped straight from ssh into a rewriter and NEVER echoed. The old
# handoff doc said `ssh larry 'grep KB_SERVE_TOKEN ...'`, which prints it to the
# terminal and into whatever log or transcript is capturing that terminal — that is
# how the token leaked and had to be rotated on 2026-08-16. Don't reintroduce it.
#
# Usage: ./kb-client-setup.sh [--host larry] [--url http://larry.home.arpa:8848]
set -euo pipefail

HOST="larry"
URL="http://larry.home.arpa:8848"

# Resolve a python ourselves. On Windows `python3` does NOT exist as a command:
# windows-host-setup.md supplies it as an interactive Git Bash ALIAS, which a
# non-interactive script never sees, plus a ~/.local/bin/python3 shim that is a per-box
# manual step and may be missing. Calling `python3` directly dies with "command not found"
# on any box that skipped the shim — which is most of the reason this script had never run
# on Windows at all.
PY="$(command -v python3 || command -v python || true)"
[ -n "$PY" ] || {
  echo "ERROR: neither python3 nor python is on PATH — cannot rewrite the env files." >&2
  exit 1
}
while [ $# -gt 0 ]; do
  case "$1" in
    --host) HOST="$2"; shift 2 ;;
    --url)  URL="$2";  shift 2 ;;
    -h|--help) sed -n '2,25p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

# Two client shapes. The zsh family (deb, thinkpad, WSL) uses ZDOTDIR=~/.config/zsh —
# ~/.zshrc is a leftover skeleton and edits there silently do nothing. The Windows box
# runs Git Bash off ~/.bashrc and has no ~/.config/zsh at all; this script used to exit 1
# there, which left it with no supported way to refresh its token after a rotation.
ZDIR="${ZDOTDIR:-$HOME/.config/zsh}"
if [ -d "$ZDIR" ]; then
  SHELL_FAMILY="zsh"
  ENVFILE="$ZDIR/.zshenv"
  SECRETS="$ZDIR/local.zsh"        # gitignored, chmod 600
else
  SHELL_FAMILY="bash"
  ENVFILE="$HOME/.bashrc"
  SECRETS=""                       # deliberately none — see below
fi

# ~/.pi/.kb-token is written on BOTH shapes and is the contract that actually matters:
# kb_core.py:64, kb-search.pi-ext.ts:19 and al-rag:34 all fall back to it when
# KB_REMOTE_TOKEN is absent from the environment. This script used to write only the zsh
# export, so after every rotation that file kept the OLD token — and any consumer without
# the env var (the MCP server, a non-interactive shell, anything on Windows) got a silent
# 401 while an interactive zsh kept working. Observed on deb 2026-08-28: local.zsh 200,
# ~/.pi/.kb-token 401, from the same box. Write both, always, from one fetch.
PITOKEN="$HOME/.pi/.kb-token"

# On bash/Windows the token goes to $PITOKEN ONLY. It must never land in ~/.bashrc: that
# is a tracked-adjacent, world-readable dotfile, and a plaintext token in it is what had
# to be treated as burned on the Windows box.

echo "== 1. reach Larry =="
if ! ssh -o ConnectTimeout=10 -o BatchMode=yes "$HOST" true 2>/dev/null; then
  # Name BOTH causes. This used to say only "on WG, bring the tunnel up first", which sent
  # the Windows session hunting the network on a box that pinged Larry in 5 ms — the real
  # cause was no keypair at all. Distinguish them here rather than in the reader's head.
  echo "ERROR: cannot ssh to '$HOST'. Two different causes look identical here:" >&2
  echo >&2
  if ping -c1 -W2 "${HOST}.home.arpa" >/dev/null 2>&1 || ping -c1 -W2 "$HOST" >/dev/null 2>&1; then
    echo "  The host ANSWERS a ping, so this is almost certainly CREDENTIALS, not the route:" >&2
    echo "    * no keypair            -> ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519" >&2
    echo "                               then copy the .pub into ${HOST}:~/.ssh/authorized_keys" >&2
    echo "    * no '$HOST' alias      -> add a 'Host $HOST' block to ~/.ssh/config with" >&2
    echo "                               HostName, 'User dav' and IdentityFile. Without it," >&2
    echo "                               ssh sends your local account name and is refused." >&2
  else
    echo "  The host does not answer a ping, so check the ROUTE first:" >&2
    echo "    * off the LAN -> bring the WireGuard tunnel up" >&2
    echo "    * on the LAN  -> check DNS for ${HOST}.home.arpa" >&2
  fi
  echo >&2
  echo "  Diagnose with:  ssh -v $HOST true" >&2
  exit 1
fi
echo "  ssh $HOST ok"

echo "== 2. write KB_REMOTE to $(basename "$ENVFILE") ($SHELL_FAMILY client) =="
touch "$ENVFILE"
"$PY" - "$ENVFILE" "$URL" <<'PY'
import re, sys, pathlib
p, url = pathlib.Path(sys.argv[1]), sys.argv[2]
t = p.read_text()
line = f'export KB_REMOTE={url}'
t, n = re.subn(r'^export KB_REMOTE=.*$', line, t, flags=re.M)
if not n:
    t = t.rstrip("\n") + f"\n\n# KB hybrid-search — query the Larry-hosted index\n{line}\n"
p.write_text(t)
print(f"  KB_REMOTE {'updated' if n else 'added'} -> {url}")
PY

echo "== 3. fetch + install token (never printed) =="
mkdir -p "$(dirname "$PITOKEN")"
[ -n "$SECRETS" ] && { touch "$SECRETS"; chmod 600 "$SECRETS"; }
# NOTE: the rewriter is passed with -c, NOT a heredoc. A heredoc occupies stdin, and
# stdin is where the piped token has to arrive — with `python3 - <<PY` the script wins
# and sys.stdin.read() returns empty, so the token silently never lands.
#
# ONE fetch, every destination. Fetching twice would double the exposure and could
# straddle a rotation, leaving the two sources disagreeing again — the exact fault this
# is fixing. argv: $1 = ~/.pi/.kb-token, $2 = the zsh secrets file or "" on bash.
ssh "$HOST" 'grep -oP "(?<=^KB_SERVE_TOKEN=).*" ~/.config/kb/serve.env' \
  | "$PY" -c '
import os, re, sys, pathlib
tok = sys.stdin.read().strip()
if not tok:
    print("  ERROR: no token returned - check ~/.config/kb/serve.env on the host", file=sys.stderr)
    raise SystemExit(1)

# 1. ~/.pi/.kb-token — the fallback every consumer shares. Plain one-line file, 0600.
pit = pathlib.Path(sys.argv[1])
prev = pit.read_text().strip() if pit.exists() else ""
pit.write_text(tok + "\n")
os.chmod(pit, 0o600)
if prev and prev != tok:
    print("  token REPLACED a different value in " + pit.name +
          " - that stale one was 401ing every non-env consumer")
else:
    print("  token " + ("unchanged in " if prev == tok else "written to ") + pit.name +
          " (" + str(len(tok)) + " chars, 0600)")

# 2. the zsh export, when this box has one. Skipped on bash/Windows by design.
if len(sys.argv) > 2 and sys.argv[2]:
    p = pathlib.Path(sys.argv[2])
    t = p.read_text()
    line = "export KB_REMOTE_TOKEN=\"" + tok + "\""
    t, n = re.subn(r"^export KB_REMOTE_TOKEN=.*$", line, t, flags=re.M)
    if not n:
        t = t.rstrip("\n") + "\n\n# KB hybrid-search bearer token (rotate: see reference_kb-search)\n" + line + "\n"
    p.write_text(t)
    print("  token " + ("updated" if n else "added") + " -> " + p.name + " (same value)")
else:
    print("  no zsh secrets file on this box - " + pit.name + " is the only copy, as intended")
' "$PITOKEN" "$SECRETS"

echo "== 4. verify =="
# Authenticate EVERY source separately, against /stats. Two traps this avoids:
#   * /health needs no auth, so it answers {"ok": true} to a client whose token is dead.
#     Both deb and the Windows box looked wired for weeks on the strength of it.
#   * a single `kb search` picks ONE source. With KB_REMOTE_TOKEN exported it never
#     touches ~/.pi/.kb-token, so a stale file passes the check that exists to catch it.
fail=0
check() {  # check <label> <token>
  local code
  code=$(curl -s -o /dev/null -w '%{http_code}' -m 10 \
           -H "Authorization: Bearer $2" "$URL/stats" 2>/dev/null || echo 000)
  if [ "$code" = "200" ]; then
    echo "  $1: HTTP 200"
  else
    echo "  $1: HTTP $code  <-- FAILED" >&2; fail=1
  fi
}
check "~/.pi/.kb-token       " "$(cat "$PITOKEN" 2>/dev/null)"
if [ -n "$SECRETS" ]; then
  # subshell: do not leak the token into this script's own environment
  check "$(basename "$SECRETS")  " "$(sh -c '. "$1" >/dev/null 2>&1; printf %s "$KB_REMOTE_TOKEN"' _ "$SECRETS")"
fi

# The file fallback is the path that was silently broken, so exercise it explicitly with
# the env var cleared — that is the consumer shape used by the MCP server and pi.
HERE="$(cd "$(dirname "$0")" && pwd)"
KB="$HERE/../../tooling/kb"
if [ -x "$KB" ]; then
  if env -u KB_REMOTE_TOKEN KB_REMOTE="$URL" "$KB" search "DataClassification" >/dev/null 2>&1; then
    echo "  kb search via the file fallback: OK"
  else
    echo "  kb search via the file fallback: FAILED" >&2; fail=1
  fi
else
  echo "  (kb not at $KB — skipped the live query; run 'kb search test' yourself)"
fi

if [ "$fail" != 0 ]; then
  echo "ERROR: at least one token source cannot authenticate against $URL/stats." >&2
  echo "       Token stale on the host, or 8848 blocked/unreachable." >&2
  exit 1
fi
echo "  every source agrees — this box is wired to $URL"

cat <<EOF

Done. Open a NEW shell so \$KB_REMOTE is picked up (\`exec \$SHELL\`).
Also on a roaming box: check the rest of the power-on catch-up list
(pull repos, WG, /etc/hosts pins, pi provider fix).
EOF

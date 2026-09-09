#!/usr/bin/env bash
# Sync this repo's wezterm.lua to the Windows host (%USERPROFILE%\.wezterm.lua).
# WSL->NTFS symlinks are flaky, so we copy. Run after editing wezterm.lua.
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/wezterm.lua"

# Windows home: honour $WIN_HOME override, else derive from USERPROFILE, else guess.
if [[ -n "${WIN_HOME:-}" ]]; then
  DST_HOME="$WIN_HOME"
else
  WU="$(cmd.exe /c 'echo %USERNAME%' 2>/dev/null | tr -d '\r\n' || true)"
  if [[ -n "$WU" && -d "/mnt/c/Users/$WU" ]]; then
    DST_HOME="/mnt/c/Users/$WU"
  else
    DST_HOME="/mnt/c/Users/Dave.Sinclair"   # fallback
  fi
fi

DST="$DST_HOME/.wezterm.lua"

[[ -f "$SRC" ]] || { echo "ERROR: source not found: $SRC" >&2; exit 1; }
[[ -d "$DST_HOME" ]] || { echo "ERROR: Windows home not found: $DST_HOME" >&2; exit 1; }

if [[ -f "$DST" ]] && cmp -s "$SRC" "$DST"; then
  echo "already up to date: $DST"
  exit 0
fi

cp "$SRC" "$DST"
echo "synced -> $DST ($(wc -c <"$DST") bytes). WezTerm auto-reloads on save."

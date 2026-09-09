#!/usr/bin/env bash
# kb-nightly.sh — nightly KB hygiene: index refresh (host only) + memory-wiki lint.
#
# Runs on BOTH kinds of box, doing only what that box owns:
#
#   host   (Larry — holds the sqlite store at ~/.local/share/kb/kb.db)
#          → `kb index`. Idempotent: unchanged sources re-embed nothing (per-chunk
#            content hash). Embeds via Larry's own ollama — no egress.
#   client (deb/WSL/thinkpad — KB_REMOTE points at the host, no local store)
#          → SKIPS indexing. Indexing on a client would build a second, divergent
#            store; moving the store to Larry was what fixed the corruption in the
#            first place (see tower/kb-larry/README.md).
#
# The memory-wiki lint runs on whichever box holds the notes — that is `deb`, and it
# is deliberately NOT part of the Larry unit. For a long time it therefore ran nowhere:
# Larry's kb-refresh.service calls `kb index` directly and never this script, and deb's
# copy of that unit sat disabled. Hence tooling/kb-lint.timer on deb.
#
# Env:
#   KB_REMOTE       set  → treat this box as a client (skip indexing)
#   KB_NIGHTLY_MODE both|index|lint   force a mode, overriding the detection above
#   KB_LOG_DIR      log directory (default ~/.local/state/kb)
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="${KB_LOG_DIR:-$HOME/.local/state/kb}"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/kb-nightly.log"

# Detect role unless told. A configured KB_REMOTE means "someone else owns the store".
MODE="${KB_NIGHTLY_MODE:-}"
if [ -z "$MODE" ]; then
  if [ -n "${KB_REMOTE:-}" ]; then MODE=lint; else MODE=both; fi
fi

ts() { date '+%Y-%m-%d %H:%M:%S'; }
{
  echo "===== kb-nightly $(ts) [mode=$MODE] ====="
  case "$MODE" in
    both|index)
      echo "-- kb index --"
      "$HERE/kb" index
      ;;
    *)
      echo "-- kb index: SKIPPED (client box; KB_REMOTE=${KB_REMOTE:-unset}) --"
      ;;
  esac
  case "$MODE" in
    both|lint)
      echo "-- kb-lint (report-only) --"
      "$HERE/kb-lint" || true      # lint is advisory; never fail the run on findings
      ;;
  esac
  echo "-- done $(ts) --"
} >>"$LOG" 2>&1

# keep the log from growing forever (last ~2000 lines)
tail -n 2000 "$LOG" >"$LOG.tmp" && mv "$LOG.tmp" "$LOG"

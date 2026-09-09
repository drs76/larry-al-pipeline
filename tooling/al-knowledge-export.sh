#!/usr/bin/env bash
# al-knowledge-export.sh — harvest AL / Business Central knowledge from THIS machine
# (Claude memories, CLAUDE.md/AGENTS.md, skills, slash-commands, VS Code prompts)
# into ONE markdown file, so it can be merged into the canonical AL docs
# (setup/reference/AL-REFERENCE.md, the handover templates) on the Larry box.
#
# READ-ONLY except the single output file. Portable bash (Linux/WSL/macOS).
#
# Usage:
#   ./al-knowledge-export.sh                 # -> ~/al-knowledge-export-<host>-<date>.md
#   ./al-knowledge-export.sh /path/out.md    # custom output path
#   AL_EXPORT_ROOTS="/mnt/c/code/al:/home/me/proj" ./al-knowledge-export.sh
#                                            # extra dirs to scan (colon-separated)
#   AL_EXPORT_ALL=1 ./al-knowledge-export.sh # include ALL knowledge files, not just AL-matching
#
# Then copy the output file to the Larry box and hand it to Claude to merge.
set -uo pipefail

OUT="${1:-$HOME/al-knowledge-export-$(hostname -s 2>/dev/null || echo host)-$(date +%Y%m%d).md}"

# ---- where to look -------------------------------------------------------
# DEFAULT roots hold structured Claude/pi knowledge — only "knowledge-named" files
# (CLAUDE.md / memory / skills / prompts) are taken from these.
DEFAULT_ROOTS=(
  "$HOME/.claude"                      # Claude Code: CLAUDE.md, projects/*/memory, skills, commands
  "$HOME/.config/claude"               # alt config location
  "$HOME/.vscode/prompts"              # VS Code / Copilot prompt files (e.g. bc-analysis.prompt.md)
  "$HOME/.vscode-server/data/User/prompts"  # WSL VS Code Server prompts
  "$HOME/.pi/agent/prompts"            # pi prompt-templates, if present
)
# EXTRA roots (colon-separated via AL_EXPORT_ROOTS) are YOUR AL project/notes dirs —
# ANY .md there matching the AL signal is taken (not just CLAUDE.md-named ones).
EXTRA_ROOTS=()
if [ -n "${AL_EXPORT_ROOTS:-}" ]; then
  IFS=':' read -ra EXTRA_ROOTS <<< "$AL_EXPORT_ROOTS"
fi
ROOTS=("${DEFAULT_ROOTS[@]}" ${EXTRA_ROOTS[@]+"${EXTRA_ROOTS[@]}"})

# ---- what counts as a "knowledge" file -----------------------------------
# names/patterns that hold curated knowledge Claude/pi/Copilot use
name_is_knowledge() {
  case "$(basename "$1")" in
    CLAUDE.md|AGENTS.md|MEMORY.md|SKILL.md|*.prompt.md) return 0 ;;
  esac
  # anything under a memory/, skills/, commands/, or prompts/ dir
  case "$1" in
    */memory/*.md|*/skills/*.md|*/commands/*.md|*/prompts/*.md) return 0 ;;
  esac
  return 1
}

# ---- AL / BC relevance signal (case-insensitive) -------------------------
# Strong BC/AL tokens only — deliberately NOT bare "al" (matches "external" etc.).
AL_RE='business central|dynamics 365|\bcodeunit\b|tableextension|pageextension|pagecustomization|controladdin|isolatedstorage|dataclassification|\bAL0[0-9]{3}|\.al\b|al compiler|al-coder|bc-analysis|bc-extension|\bBC[0-9]{2}\b|\b(TSG|PTE)[A-Z]|permissionset|SecretText|\.app\b|app\.json'

is_al_relevant() {
  [ -n "${AL_EXPORT_ALL:-}" ] && return 0
  # content match only (path is an unreliable signal — "external" contains "al")
  grep -qiE "$AL_RE" "$1" 2>/dev/null
}

# ---- gather --------------------------------------------------------------
tmp_inc="$(mktemp)"; tmp_skip="$(mktemp)"
trap 'rm -f "$tmp_inc" "$tmp_skip"' EXIT

# scan one root. $2=1 means an EXTRA root (take any AL-matching .md, not just knowledge-named).
# Prints a per-root diagnostic to stderr so you can SEE which roots were scanned.
scan_root() {
  local root="$1" extra="$2" al=0 tot=0
  if [ ! -d "$root" ]; then printf '  [skip]  %s  (does not exist)\n' "$root" >&2; return; fi
  while IFS= read -r -d '' f; do
    if [ "$extra" = 1 ]; then
      tot=$((tot+1))
      if is_al_relevant "$f"; then echo "$f" >> "$tmp_inc"; al=$((al+1)); fi
    else
      name_is_knowledge "$f" || continue
      tot=$((tot+1))
      if is_al_relevant "$f"; then echo "$f" >> "$tmp_inc"; al=$((al+1)); else echo "$f" >> "$tmp_skip"; fi
    fi
  done < <(find "$root" -type f \( -name '*.md' -o -name '*.prompt.md' \) \
             -not -path '*/node_modules/*' -not -path '*/.git/*' \
             -not -path '*/plugins/marketplaces/*' -not -path '*/plugins/*/skills/*' \
             -print0 2>/dev/null)
  printf '  [scan]  %-58s  %d AL / %d md files\n' "$root" "$al" "$tot" >&2
}

echo "Scanning roots:" >&2
for root in "${DEFAULT_ROOTS[@]}";                       do scan_root "$root" 0; done
for root in ${EXTRA_ROOTS[@]+"${EXTRA_ROOTS[@]}"};       do scan_root "$root" 1; done

sort -u "$tmp_inc" -o "$tmp_inc"
sort -u "$tmp_skip" -o "$tmp_skip"
n_inc=$(wc -l < "$tmp_inc" | tr -d ' ')
n_skip=$(wc -l < "$tmp_skip" | tr -d ' ')

# ---- write the export ----------------------------------------------------
{
  echo "# AL / Business Central knowledge export"
  echo
  echo "- host: $(hostname 2>/dev/null || echo unknown)"
  echo "- generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "- included files (AL-relevant): $n_inc"
  echo "- skipped knowledge files (not AL-matching): $n_skip"
  echo "- roots scanned: ${ROOTS[*]}"
  echo
  echo "> Merge target on Larry: setup/reference/AL-REFERENCE.md + the handover templates."
  echo "> Each file below is delimited by BEGIN/END FILE markers for easy parsing."
  echo
  echo "## Included files"
  if [ "$n_inc" -gt 0 ]; then while IFS= read -r f; do echo "- $f"; done < "$tmp_inc"; else echo "_(none matched — try AL_EXPORT_ALL=1 or add AL_EXPORT_ROOTS)_"; fi
  echo
  echo "## Skipped knowledge files (review if something's missing)"
  if [ "$n_skip" -gt 0 ]; then while IFS= read -r f; do echo "- $f"; done < "$tmp_skip"; else echo "_(none)_"; fi
  echo
  echo "---"
  echo
  echo "# Contents"
  while IFS= read -r f; do
    echo
    echo "<<<<< BEGIN FILE: $f"
    cat "$f" 2>/dev/null
    echo
    echo ">>>>> END FILE: $f"
    echo
  done < "$tmp_inc"
} > "$OUT"

echo "Wrote: $OUT"
echo "  included AL-relevant files: $n_inc   (skipped knowledge files: $n_skip)"
echo "Next: copy this file to the Larry box and hand it to Claude to merge into AL-REFERENCE.md."

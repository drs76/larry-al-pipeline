#!/bin/bash
# Restore real symlinks to the tracked tooling/ copies, replacing any static
# copy or stale link that has drifted.
#
# Runs on BOTH platforms:
#   Windows (Git Bash)  needs an ELEVATED shell for native symlinks, and gets
#                       md2pdf as two shims rather than a link (see below).
#   Linux / WSL         plain shell is enough.
#
# A copy sitting where a symlink belongs is how this drifts: it stops tracking
# the repo and nothing complains. Any regular file found in a managed slot is
# moved into _relink-backup/ rather than overwritten, so a hand-edit is never
# silently destroyed -- check that directory afterwards if you were relying on
# a local tweak.
set -e

# Same portable base as alw/gow/csw/bcw. Override with SETUP_DIR to force one.
SETUP_DIR="${SETUP_DIR:-$([ -d "$HOME/larry-setup" ] && echo "$HOME/larry-setup" || echo /mnt/rojaws/localDev/setup)}"
REPO="$SETUP_DIR"
[ -d "$REPO/tooling" ] || { echo "relink: no tooling/ under $REPO" >&2; exit 1; }

case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) WINDOWS=1; export MSYS=winsymlinks:nativestrict ;;
  *)                    WINDOWS=0 ;;
esac

# Windows preflight. Two ways to get here wrongly, both of which used to fail one
# confusing line at a time:
#   * run under WSL's bash (C:\Windows\System32ash.exe, or WindowsApps on PATH)
#     from PowerShell -- $HOME is then the WSL home, not the Windows one
#   * run in a NON-elevated Git Bash -- every ln prints "Operation not permitted"
# Catch both here with one clear message instead.
if [ "$WINDOWS" = 1 ]; then
  probe="$(mktemp -u)"
  if ! ln -s "$REPO/README.md" "$probe" 2>/dev/null; then
    cat >&2 <<'MSG'
relink: cannot create symlinks here -- this needs elevation.

Self-elevating (works from PowerShell, Git Bash, or a Run button):

  Start-Process -Verb RunAs "C:/Program Files/Git/bin/bash.exe" -ArgumentList '-lc','~/larry-setup/tower/handoff-scripts/relink-tooling.sh; read -n1'

Or by hand: right-click Git Bash -> Run as administrator, then

  bash ~/larry-setup/tower/handoff-scripts/relink-tooling.sh

Note that a plain command run from an ordinary shell CANNOT elevate itself --
that is what you just hit. Also, a bare `bash` in PowerShell often resolves to
WSL rather than Git Bash: it prints an /etc/fstab warning and mangles the path
into C:UsersDave.Sinclair. Naming Git's bash explicitly, as above, avoids it.
MSG
    exit 1
  fi
  rm -f "$probe"
fi

PROMPTS="$HOME/.pi/agent/prompts"
COMMANDS="$HOME/.claude/commands"
BIN="$HOME/.local/bin"
EXT="$HOME/.pi/agent/extensions"
BACKUP="$HOME/.local/share/larry-relink-backup/$(date +%Y-%m-%d)"

mkdir -p "$PROMPTS" "$COMMANDS" "$BIN" "$EXT"

# link SRC DST -- preserve a real file before replacing it with the symlink.
#
# The backup mirrors the slot path under $HOME, NOT just the basename. Six names
# live in two slots each -- al, spec, warplan, scout, wizard and bc-agent are all
# both a pi prompt and a Claude command -- so a basename-keyed backup has the
# second mv overwrite the first, destroying exactly the hand-edit this function
# exists to preserve. The failure is silent and the file is already gone.
link() {
  local src="$1" dst="$2"
  [ -e "$src" ] || { echo "  skip (not in repo): $src"; return 0; }
  if [ -f "$dst" ] && [ ! -L "$dst" ]; then
    local rel="${dst#"$HOME"/}"
    mkdir -p "$BACKUP/$(dirname "$rel")"
    mv "$dst" "$BACKUP/$rel"
    echo "  backed up copy: $rel"
  fi
  ln -sfn "$src" "$dst"
}

# fable, handbook and ste are pi prompts too -- README.md lists all three under
# ~/.pi/agent/prompts. Leaving them out linked them for Claude only, and because
# this script never removes anything the gap is invisible on a machine that
# already had them: it only shows up on a fresh client, as a missing /fable.
for f in al al-route go-route cs-route spec handover warplan scout bc-agent wizard \
         fable handbook ste doc-convert bc-analysis bc-webservice-audit; do
  link "$REPO/tooling/$f.md" "$PROMPTS/$f.md"
done

for f in al fable bc-agent handbook al-syntax ste bc-analysis bc-webservice-audit; do
  link "$REPO/tooling/$f.md" "$COMMANDS/$f.md"
done
for f in warplan scout spec wizard to-questionnaire writing-for-agents; do
  link "$REPO/tooling/$f-claude.md" "$COMMANDS/$f.md"
done

for f in alw gow csw probe bcw anon kb kb-lint al-rag searxng-local; do
  link "$REPO/tooling/$f" "$BIN/$f"
done

link "$REPO/tooling/kb-search.pi-ext.ts" "$EXT/kb-search.ts"
link "$REPO/tooling/searxng-search.pi-ext.ts" "$EXT/searxng-search.ts"

# Auto-triggering Claude skills live in directories of their own.
mkdir -p "$HOME/.claude/skills/ste-writing"
for f in SKILL.md ste-lint.py ste-recurring-errors.md; do
  link "$REPO/tooling/ste/$f" "$HOME/.claude/skills/ste-writing/$f"
done
mkdir -p "$HOME/.claude/skills/bc-webservice-audit"
for f in SKILL.md classify.py; do
  link "$REPO/tooling/bc-webservice-audit/$f" "$HOME/.claude/skills/bc-webservice-audit/$f"
done
mkdir -p "$HOME/.claude/skills/doc-convert"
link "$REPO/tooling/doc-convert/SKILL.md" "$HOME/.claude/skills/doc-convert/SKILL.md"

if [ "$WINDOWS" = 1 ]; then
  # md2pdf is the one tooling/ CLI that cannot be symlinked here: it is a python
  # script, so Windows needs a launcher. Two shims call the repo copy directly --
  # md2pdf.cmd for PowerShell, md2pdf for Git Bash. Both need the NATIVE path;
  # Windows python cannot open the /c/... form $REPO uses.
  WINREPO="$(cygpath -m "$REPO")"
  if [ -e "$BIN/md2pdf.py" ]; then          # superseded by the tracked tooling/md2pdf
    mkdir -p "$BIN/_md2pdf-backup"
    mv "$BIN/md2pdf.py" "$BIN/_md2pdf-backup/md2pdf.py.$(date +%Y-%m-%d)"
  fi
  cat > "$BIN/md2pdf.cmd" <<CMDEOF
@echo off
python "$WINREPO/tooling/md2pdf" %*
CMDEOF
  # (LF endings are fine: no labels or goto in this batch)

  cat > "$BIN/md2pdf" <<SHEOF
#!/bin/sh
exec python "$WINREPO/tooling/md2pdf" "\$@"
SHEOF
  chmod +x "$BIN/md2pdf"
else
  link "$REPO/tooling/md2pdf" "$BIN/md2pdf"
fi

echo
echo "done  (SETUP_DIR=$REPO)"
[ -d "$BACKUP" ] && echo "copies backed up to: $BACKUP"

echo
echo "broken links, if any:"
find "$PROMPTS" "$COMMANDS" "$BIN" "$EXT" -maxdepth 1 -xtype l -printf '  BROKEN %p -> %l\n' 2>/dev/null || true
find "$HOME/.claude/skills" -maxdepth 2 -xtype l -printf '  BROKEN %p -> %l\n' 2>/dev/null || true

if [ "$WINDOWS" = 1 ]; then
  echo
  echo "md2pdf shims (not symlinks):"
  ls -la "$BIN/md2pdf" "$BIN/md2pdf.cmd"
fi

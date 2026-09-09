#!/bin/sh
# Sticky-note cheatsheet toggle.
# Press $mod+c once  -> floating cheatsheet appears (sticky, on top).
# Press $mod+c again -> it closes. That's the whole trick.

CHEAT="$HOME/.config/sway/cheatsheet.md"

# Already open? Kill it -> toggle off.
if pkill -f 'foot.*app-id=cheatsheet'; then
    exit 0
fi

# Pick nicest available markdown pager. glow > bat/batcat > less.
if command -v glow >/dev/null 2>&1; then
    VIEWER="glow -p '$CHEAT'"
elif command -v batcat >/dev/null 2>&1; then
    VIEWER="batcat --style=plain --paging=always -l md '$CHEAT'"
elif command -v bat >/dev/null 2>&1; then
    VIEWER="bat --style=plain --paging=always -l md '$CHEAT'"
else
    VIEWER="less -R '$CHEAT'"
fi

exec foot --app-id=cheatsheet -T cheatsheet sh -c "$VIEWER"

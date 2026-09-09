#!/usr/bin/env bash
# Install minimalist Sway setup on Debian. Run on BOTH machines.
#   ./install.sh
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CFG="$HOME/.config"

echo ">> Installing packages (needs sudo)..."
sudo apt update
sudo apt install -y \
    sway swayidle swaylock swaybg \
    waybar wofi foot alacritty mako-notifier \
    grim slurp wl-clipboard cliphist \
    brightnessctl playerctl \
    wireplumber pipewire pipewire-pulse pavucontrol \
    network-manager fonts-jetbrains-mono fonts-font-awesome \
    wev

# Optional prettier markdown for the sticky note (skip silently if unavailable)
sudo apt install -y bat 2>/dev/null || true

# Waybar/tmux status-bar glyphs. The Debian fonts-jetbrains-mono is the plain family (no Nerd
# glyphs), and waybar/style.css falls through to "Symbols Nerd Font" for the PUA codepoints. That
# font is the glyphs-only nerd-fonts release; without it every module icon renders as an empty box.
# User-level install only (no root), idempotent — skip if already present or if offline.
if ! fc-list | grep -qi 'symbols nerd font'; then
    echo ">> Installing Symbols Nerd Font (waybar module icons)..."
    NF_URL="https://github.com/ryanoasis/nerd-fonts/releases/latest/download/NerdFontsSymbolsOnly.zip"
    NF_TMP="$(mktemp -d)"
    if curl -sL -o "$NF_TMP/nf.zip" "$NF_URL" && unzip -o -q "$NF_TMP/nf.zip" -d "$NF_TMP/nf"; then
        mkdir -p "$HOME/.local/share/fonts"
        cp "$NF_TMP"/nf/SymbolsNerdFont-Regular.ttf "$NF_TMP"/nf/SymbolsNerdFontMono-Regular.ttf \
            "$HOME/.local/share/fonts/"
        fc-cache -f "$HOME/.local/share/fonts" >/dev/null 2>&1
        echo "   done."
    else
        echo "   WARN: download failed (offline?) — install NerdFontsSymbolsOnly.zip manually. See README §Powerline glyphs."
    fi
    rm -rf "$NF_TMP"
fi

# Terminal font. foot/alacritty use the fully-patched "JetBrainsMono Nerd Font" as their primary
# font so text AND icon glyphs come from one font — otherwise glyphs fall back per-codepoint to
# whatever squats the PUA range (FontAwesome v4, Hack, DejaVu) and render as the wrong icon.
# User-level install only (no root), idempotent — skip if already present or if offline.
if ! fc-list | grep -qi 'jetbrainsmono nerd font'; then
    echo ">> Installing JetBrainsMono Nerd Font (terminal text + glyphs)..."
    JBM_URL="https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip"
    JBM_TMP="$(mktemp -d)"
    if curl -sL -o "$JBM_TMP/jbm.zip" "$JBM_URL" && unzip -o -q "$JBM_TMP/jbm.zip" -d "$JBM_TMP/jbm"; then
        mkdir -p "$HOME/.local/share/fonts/JetBrainsMonoNF"
        cp "$JBM_TMP"/jbm/JetBrainsMonoNerdFont-Regular.ttf \
           "$JBM_TMP"/jbm/JetBrainsMonoNerdFont-Bold.ttf \
           "$JBM_TMP"/jbm/JetBrainsMonoNerdFont-Italic.ttf \
           "$JBM_TMP"/jbm/JetBrainsMonoNerdFont-BoldItalic.ttf \
           "$HOME/.local/share/fonts/JetBrainsMonoNF/"
        fc-cache -f "$HOME/.local/share/fonts" >/dev/null 2>&1
        echo "   done."
    else
        echo "   WARN: download failed (offline?) — install JetBrainsMono.zip manually. See README §Powerline glyphs."
    fi
    rm -rf "$JBM_TMP"
fi

echo ">> Linking config files..."
mkdir -p "$CFG/sway/config.d" "$CFG/waybar" "$CFG/foot" "$CFG/alacritty" "$CFG/mako" "$CFG/wofi" "$HOME/Pictures"

link() { ln -sfnv "$REPO_DIR/config/$1" "$CFG/$2"; }
link sway/config        sway/config
link sway/cheatsheet.md sway/cheatsheet.md
link sway/sticky-toggle.sh sway/sticky-toggle.sh
link waybar/config      waybar/config
link waybar/style.css   waybar/style.css
link foot/foot.ini      foot/foot.ini
link alacritty/alacritty.toml alacritty/alacritty.toml
link mako/config        mako/config
link wofi/style.css     wofi/style.css

chmod +x "$REPO_DIR/config/sway/sticky-toggle.sh"

echo ">> Enabling audio (pipewire) user services..."
systemctl --user enable --now pipewire pipewire-pulse wireplumber 2>/dev/null || true

cat <<'EOF'

Done. Next:
  1. Log out of your current desktop.
  2. At the login screen (or a TTY) start Sway:  run `sway`  (or pick Sway in your greeter).
  3. Set up displays per machine:
       swaymsg -t get_outputs           # find output names
       cp ~/.config/sway/config.d/desktop.conf.example ~/.config/sway/config.d/local.conf
       # edit local.conf, then:  $mod+Shift+c to reload
  4. Sticky-note cheatsheet:  press  Super + /

Config is symlinked from this repo, so `git pull` on either machine updates both.
EOF

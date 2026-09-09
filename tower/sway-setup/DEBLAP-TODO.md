# DEBLAP (ThinkPad) — port these tower changes

Changes made on **tower** 2026-07-31 to replicate on the ThinkPad (deblap) when its sway-setup is built.

## waybar (`config/waybar/config`)
- **clock**: add `calendar` block so hover tooltip shows month grid.
  Do NOT force light colors on calendar text — GTK tooltip bg may be light → invisible. Keep only `today` underline.
- **cpu / memory / temperature**: `"on-click": "NeoHtop"` (NeoHtop is a GUI app, `/usr/bin/NeoHtop`).
- **network**: `"on-click": "swaymsg 'splith; exec foot -e nmtui'"` — opens beside focused window.
- **pulseaudio**: `"on-click": "swaymsg 'splith; exec pavucontrol'"` — opens beside focused window.

## sway (`config/sway/config`)
- **Remove** `for_window [app_id="pavucontrol"] floating enable` — otherwise sound pops floating instead of tiling in the split.
- **Wallpaper**: `output * bg <img> fill #1e1e2e` (was solid `#1e1e2e`).
  Tower uses `/home/dav/Documents/blitspear.jpeg` (hardcoded, laptop-specific). For deblap: pick laptop image OR copy shared image into repo (`config/wallpaper/`) and point both machines at it.

## nvim (separate repo: `~/.config/nvim`)
- `lua/config/native.lua`: added a `ColorScheme` autocmd that clears the canvas bg
  (`Normal, NormalNC, SignColumn, EndOfBuffer, FoldColumn, LineNr, VertSplit,
  WinSeparator` → `bg=none`) so the foot terminal bg shows through — seamless, no
  editor box. Applies on the ThinkPad too (same nvim config repo). No change needed
  unless deblap uses a different terminal bg/alpha.

## Notes
- waybar launched via sway `bar { swaybar_command waybar }` — NOT exec. To reload config-only use `pkill -SIGUSR2 waybar` OR `swaymsg reload`, never both (races → death).
- foot has NO background-image support; wallpaper is desktop-only.
- ThinkPad extras already keyed in tower config: idle/lock (line ~36), lid switch (`config.d/desktop.conf.example`), media keys — verify those on deblap.

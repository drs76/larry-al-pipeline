# Minimalist Sway Setup (Debian, Intel gfx)

Portable Wayland tiling-WM config. One repo, symlinked into `~/.config` on **both**
the desktop and the ThinkPad. `git pull` on either box updates both.

## Stack
| Piece | Tool |
|-------|------|
| Window manager | **sway** (i3 syntax, Wayland) |
| Bar | waybar |
| Launcher | wofi |
| Terminal | foot |
| Notifications | mako |
| Lock / idle | swaylock + swayidle |
| Screenshots | grim + slurp |
| Clipboard | wl-clipboard + cliphist |
| Audio | pipewire + wireplumber (wpctl) |
| Brightness | brightnessctl |

Theme = Catppuccin Mocha across the board.

## Install
```sh
git clone <this-repo> ~/sway-setup   # or copy the folder
cd ~/sway-setup
./install.sh                          # installs pkgs + symlinks config
```
Then log out, start `sway`, and set displays (see below).

## Per-machine displays
Everything shared lives in `config/sway/config`. Machine-specific bits (monitor
layout, HiDPI scale, lid switch) go in `~/.config/sway/config.d/local.conf` —
that file is NOT shared. Start from `config.d/desktop.conf.example`.

```sh
swaymsg -t get_outputs    # find output names (DP-1, eDP-1, HDMI-A-1 ...)
```

## Sticky-note cheatsheet
Press **Super + /** → floating cheatsheet pops up (pinned, on top).
Press **Super + /** again → it closes. Edit `config/sway/cheatsheet.md` to taste.

## Full key list
See `config/sway/cheatsheet.md` — same content the sticky note shows.

# Sway Cheatsheet   ($mod = Super/Win key)

Toggle this note:  **$mod + c**

## Apps
| Key | Action |
|-----|--------|
| `$mod + Enter` | Terminal (foot) |
| `$mod + d` | App launcher (wofi) |
| `$mod + q` | Close window |
| `$mod + Esc` | Lock screen |
| `$mod + Shift + c` | Reload config |
| `$mod + Shift + e` | Power menu — lock / logout / suspend / reboot / shutdown (also the red power button in waybar) |

## Focus  (vim keys or arrows)
| Key | Action |
|-----|--------|
| `$mod + h/j/k/l` | Focus left/down/up/right |
| `$mod + a` | Focus parent container |
| `$mod + space` | Toggle focus tiling/floating |

## Move window
| Key | Action |
|-----|--------|
| `$mod + Shift + h/j/k/l` | Move window |
| `$mod + Shift + minus` | Send to scratchpad |
| `$mod + minus` | Show scratchpad |

## Workspaces
| Key | Action |
|-----|--------|
| `$mod + 1..0` | Go to workspace 1-10 |
| `$mod + Shift + 1..0` | Move window to workspace |
| `$mod + Tab` | Last workspace |

## Layout
| Key | Action |
|-----|--------|
| `$mod + b` | Split horizontal |
| `$mod + v` | Split vertical |
| `$mod + w` | Tabbed layout |
| `$mod + s` | Stacked layout |
| `$mod + e` | Toggle split/stack |
| `$mod + f` | Fullscreen |
| `$mod + Shift + space` | Toggle floating |
| `$mod + p` | Toggle sticky (pin) |
| `$mod + r` | Resize mode (h/j/k/l, Esc to exit) |

## Hardware
| Key | Action |
|-----|--------|
| Volume / Mute keys | wpctl (pipewire) |
| Brightness keys | brightnessctl |
| Media play/next/prev | playerctl |

## Screenshots
| Key | Action |
|-----|--------|
| `Print` | Full screen -> ~/Pictures |
| `Shift + Print` | Region -> clipboard |

## Handy shell
- `swaymsg -t get_outputs`  → display names
- `swaymsg -t get_tree`     → window tree / app_ids
- `wev`                     → find keysym names

# tmux Cheatsheet   (prefix = Ctrl+a)

Customized setup, tmux 3.5a — config in this dir (`tmux.conf` + `cpu.sh` + `battery.sh`), see **Install** below. `P` = the prefix (`Ctrl+a`, remapped from stock `Ctrl+b`), pressed then released before the next key. `P a` sends a literal `Ctrl+a` to the shell.

## Custom binds & defaults (this config)
| Key / setting | Action |
|-----|--------|
| `P r` | Reload `~/.tmux.conf` |
| `P C` | New **named** window (prompts for name, keeps cwd) |
| `P |` | Split vertical, keep cwd |
| `P -` | Split horizontal, keep cwd |
| mouse | On — click panes/windows, drag borders, wheel-scroll |
| copy mode | vi keys (`v` select, `y` copy) |
| windows | 1-indexed, auto-renumber on close |
| status bar | Top: session · windows · git · CPU · battery · host · clock (powerline, Tokyo Night). Battery segment goes **red** under 20%. |

## Sessions
| Key | Action |
|-----|--------|
| `tmux` | Start a new session (shell) |
| `tmux new -s name` | New named session |
| `tmux ls` | List sessions |
| `tmux a -t name` | Attach to a session |
| `P d` | Detach from session |
| `P s` | Session picker (switch) |
| `P $` | Rename current session |

## Windows  (tabs)
| Key | Action |
|-----|--------|
| `P c` | New window |
| `P ,` | Rename window |
| `P n` / `P p` | Next / previous window |
| `P 0..9` | Go to window by number |
| `P w` | Window/session tree picker |
| `P &` | Kill window (asks) |
| `P f` | Find window by name |

## Panes  (splits)
| Key | Action |
|-----|--------|
| `P %` / `P |` | Split vertical (left/right) — `|` keeps cwd |
| `P "` / `P -` | Split horizontal (top/bottom) — `-` keeps cwd |
| `P arrows` | Move focus between panes |
| `P o` | Cycle to next pane |
| `P ;` | Toggle to last active pane |
| `P q` | Show pane numbers (press number to jump) |
| `P z` | Zoom pane (toggle fullscreen) |
| `P {` / `P }` | Swap pane left / right |
| `P Space` | Cycle pane layouts |
| `P x` | Kill pane (asks) |
| `P !` | Break pane into its own window |
| `P Ctrl+arrows` | Resize pane (hold to repeat) |

## Copy mode  (scroll / select)
| Key | Action |
|-----|--------|
| `P [` | Enter copy mode |
| `PgUp/PgDn`, arrows | Scroll / move |
| `Space` | Start selection (in copy mode) |
| `Enter` | Copy selection, exit |
| `P ]` | Paste buffer |
| `q` | Exit copy mode |
| `/` `?` | Search forward / back (copy mode) |

## Misc
| Key | Action |
|-----|--------|
| `P ?` | List ALL key bindings |
| `P t` | Big clock |
| `P :` | Command prompt |
| `P r` | Reload config (bound in this setup) |

## Handy shell
- `tmux kill-session -t name`  → kill one session
- `tmux kill-server`           → kill everything (needed after prefix/status changes)
- `tmux source ~/.tmux.conf`   → reload config (or `P r`)

## Install (symlink from portable clone → home)
Glyphs need a Nerd Font in the terminal (Windows Terminal / VS Code profile). Battery reads
`/sys/class/power_supply/BAT1` (WSL exposes it). Symlink to `~/larry-setup` (not the NFS clone)
so it survives off-LAN:
```sh
mkdir -p ~/.config/tmux
ln -sf ~/larry-setup/tower/tmux-setup/tmux.conf   ~/.tmux.conf
ln -sf ~/larry-setup/tower/tmux-setup/cpu.sh      ~/.config/tmux/cpu.sh
ln -sf ~/larry-setup/tower/tmux-setup/battery.sh  ~/.config/tmux/battery.sh
tmux kill-server 2>/dev/null; tmux
```

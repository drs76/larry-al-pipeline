# Starship prompt

Canonical `starship.toml` for all boxes. Purple git branch, OS glyph, per-language versions,
minimal `❯` character. `scan_timeout`/`command_timeout` bumped so slow WSL/NFS home-dir scans
finish instead of printing `Scanning current directory timed out`.

This box uses `ZDOTDIR=~/.config/zsh` and `STARSHIP_CONFIG=~/.config/zsh/starship.toml`.

## Install (symlink from portable clone → home)

Symlink to `~/larry-setup` (the portable clone), **not** the NFS `/mnt/rojaws/...` clone —
symlinks into NFS dangle off-LAN.

```sh
ln -sf ~/larry-setup/tower/starship-setup/starship.toml ~/.config/zsh/starship.toml
```

If a box doesn't set `STARSHIP_CONFIG`, starship reads `~/.config/starship.toml` instead —
symlink that path too, or export `STARSHIP_CONFIG`.

-- WezTerm config for the work-laptop Windows host.
-- Defaults to Windows PowerShell; WSL / pwsh / cmd available from the launch menu (Ctrl+Shift+L).
-- Install: copy (or symlink) to  %USERPROFILE%\.wezterm.lua  on the Windows host.

local wezterm = require("wezterm")
local config = wezterm.config_builder()

-- ── Default shell: Windows PowerShell ────────────────────────────────────────
config.default_prog = { "powershell.exe", "-NoLogo" }

-- Launch menu (Ctrl+Shift+L) — pick a different shell without changing the default.
-- Built from what this host actually has, so ONE config serves every Windows box
-- (work laptop has WSL Debian; docker-bc has Git Bash and no WSL). Entries for a
-- missing shell are omitted rather than left to fail when picked — which is what
-- lets this file be symlinked instead of copied-and-drifted.
local function exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

local windir  = os.getenv("WINDIR") or "C:\\Windows"
local pfiles  = os.getenv("ProgramFiles") or "C:\\Program Files"
local gitbash = pfiles .. "\\Git\\bin\\bash.exe"
local pwsh7   = pfiles .. "\\PowerShell\\7\\pwsh.exe"
local wsl     = windir .. "\\System32\\wsl.exe"

config.launch_menu = {
  { label = "PowerShell", args = { "powershell.exe", "-NoLogo" } },
}
if exists(pwsh7) then
  table.insert(config.launch_menu, { label = "PowerShell 7", args = { pwsh7, "-NoLogo" } })
end
if exists(gitbash) then
  -- -l gives a login shell so ~/.bashrc env (SETUP_DIR, PATH, KB_REMOTE…) is loaded.
  table.insert(config.launch_menu, { label = "Git Bash", args = { gitbash, "-l" } })
end
-- wsl.exe ships with Windows even when no distro is installed, so testing for the
-- binary offers a menu entry that fails when picked. Ask it for a distro list
-- instead (it exits non-zero and prints usage when there are none). Output is
-- UTF-16, hence stripping NULs before checking for content.
local function has_wsl_distro()
  if not exists(wsl) then return false end
  local ok, stdout = wezterm.run_child_process({ wsl, "-l", "-q" })
  if not ok or not stdout then return false end
  return #(stdout:gsub("%z", ""):gsub("%s+", "")) > 0
end

if has_wsl_distro() then
  table.insert(config.launch_menu, { label = "WSL — Debian", args = { "wsl.exe", "~", "-d", "Debian" } })
end
table.insert(config.launch_menu, { label = "Command Prompt", args = { "cmd.exe" } })

-- ── Appearance (matches sway/tmux: JetBrains Mono, Catppuccin Mocha) ──────────
config.color_scheme = "Catppuccin Mocha"
config.font = wezterm.font_with_fallback({
  { family = "Cascadia Code", weight = "DemiBold" },
  "JetBrainsMono NFM", -- powerline/nerd glyphs, Mono variant (winget: DEVCOM.JetBrainsMonoNerdFont)
  "Segoe UI Emoji",         -- color emoji + misc symbols
})
config.font_size = 14.0
config.line_height = 1.05

-- Sharper text rendering on Windows (LCD subpixel + light hinting).
config.freetype_load_target = "Light"
config.freetype_render_target = "HorizontalLcd"

config.window_background_opacity = 0.98
config.window_decorations = "RESIZE"
config.window_padding = { left = 8, right = 8, top = 6, bottom = 6 }
config.enable_scroll_bar = false
-- Scrollback is per pane and is the largest single memory lever here: roughly
-- (lines x columns) of cell structs, so a wide window with several panes costs
-- tens of MB before anything else. Inline images (sixel / iTerm2 / kitty, all of
-- which WezTerm decodes) are held in scrollback too, so a session that renders
-- images does not release that memory until the lines roll off. 2500 keeps a
-- useful history at a fraction of the cost; raise per-host in .wezterm-local.lua
-- if a box has memory to spare.
config.scrollback_lines = 2500

-- ── Resource use ─────────────────────────────────────────────────────────────
-- WezTerm's footprint sits above Windows Terminal's mostly in the GPU path
-- (glyph atlas + swapchain) and in scrollback, set above. Compare the two
-- honestly before tuning further: Windows Terminal splits across
-- WindowsTerminal.exe plus one OpenConsole.exe per tab, so a single Task Manager
-- row understates it. Sum every process per terminal:
--   Get-Process wezterm-gui,WindowsTerminal,OpenConsole -ErrorAction SilentlyContinue |
--     Group-Object ProcessName |
--     Select-Object Name,@{n='MB';e={[math]::Round(($_.Group|Measure-Object WorkingSet64 -Sum).Sum/1MB,1)}}
--
-- Only consulted when front_end = "WebGpu" (the docker-bc override below); picks
-- the integrated GPU over a discrete one, which allocates less and is plenty for
-- a terminal. Harmless on the default front end.
config.webgpu_power_preference = "LowPower"

-- Cursor blink / fade animation frames. Costs CPU rather than memory, but the
-- default 10fps buys nothing on a terminal.
config.animation_fps = 1

-- NOTE: front_end is deliberately NOT set here. "Software" does not lower memory
-- on this box and does not avoid glium (see the .wezterm-local.lua note at the
-- foot of this file); a GPU host wants the default. If one machine needs a
-- different renderer, that is a host-local override, not a shared setting.

-- ── Behaviour ────────────────────────────────────────────────────────────────
config.check_for_updates = false
config.audible_bell = "Disabled"
config.default_cursor_style = "SteadyBar"
config.adjust_window_size_when_changing_font_size = false
-- Keep tab bar shown even with one tab, else the status bar is hidden.
config.hide_tab_bar_if_only_one_tab = false

-- ── Shortcuts: single source of truth (binding + status hint) ────────────────
-- Edit an entry here and BOTH the keybinding and the status-bar hint update.
-- `hint` = false to bind a key without showing it in the status bar.
-- `label` overrides the auto glyph in the status bar (e.g. group several keys).
local act = wezterm.action
local shortcuts = {
  { mods = "CTRL|SHIFT", key = "L", action = act.ShowLauncher,                  hint = "menu" },
  { mods = "CTRL|SHIFT", key = "T", action = act.SpawnTab("CurrentPaneDomain"), hint = "tab" },
  { mods = "CTRL|SHIFT", key = "F", action = act.Search("CurrentSelectionOrEmptyString"), hint = "find" },
  { mods = "CTRL|SHIFT", key = "P", action = act.ActivateCommandPalette,        hint = "palette" },
  { mods = "CTRL|SHIFT", key = "X", action = act.ActivateCopyMode,              hint = "copy" },
  -- Splits.
  { mods = "CTRL|SHIFT|ALT", key = '"', action = act.SplitVertical({ domain = "CurrentPaneDomain" }),   hint = "vsplit" },
  { mods = "CTRL|SHIFT|ALT", key = "%", action = act.SplitHorizontal({ domain = "CurrentPaneDomain" }), hint = "hsplit" },
  -- Pane nav (arrows). First carries the grouped hint; rest bind silently.
  { mods = "CTRL|SHIFT", key = "LeftArrow",  action = act.ActivatePaneDirection("Left"),  hint = "nav", label = "^⇧←↑↓→" },
  { mods = "CTRL|SHIFT", key = "RightArrow", action = act.ActivatePaneDirection("Right"), hint = false },
  { mods = "CTRL|SHIFT", key = "UpArrow",    action = act.ActivatePaneDirection("Up"),    hint = false },
  { mods = "CTRL|SHIFT", key = "DownArrow",  action = act.ActivatePaneDirection("Down"),  hint = false },
}

-- Build config.keys from the table (adds to WezTerm's default bindings).
config.keys = {}
for _, s in ipairs(shortcuts) do
  table.insert(config.keys, { mods = s.mods, key = s.key, action = s.action })
end

-- Render "CTRL|SHIFT"+"L" -> "^⇧L" for the status bar.
local mod_glyph = { CTRL = "^", SHIFT = "⇧", ALT = "⌥", SUPER = "⌘", CMD = "⌘", WIN = "⌘" }
local function fmt_key(s)
  local out = ""
  for m in string.gmatch(s.mods, "[^|]+") do
    out = out .. (mod_glyph[m] or m)
  end
  return out .. s.key
end

local HINT_PARTS = {}  -- e.g. { "^⇧L menu", "^⇧T tab", ... }; static, built once.
for _, s in ipairs(shortcuts) do
  if s.hint ~= false then
    table.insert(HINT_PARTS, (s.label or fmt_key(s)) .. " " .. s.hint)
  end
end

-- Fit hints to the window: keep adding parts until they'd exceed the char budget.
-- PX_PER_CELL is a rough cell-advance estimate; nudge if hints clip/leave gaps.
local PX_PER_CELL = 9
local function fit_hints(pixel_width)
  local budget = math.floor(pixel_width / PX_PER_CELL) - 12  -- reserve for clock + pad
  local out, len = {}, 0
  for _, p in ipairs(HINT_PARTS) do
    local add = (utf8.len(p) or #p) + (len > 0 and 2 or 0)
    if len + add > budget and #out > 0 then break end
    table.insert(out, p)
    len = len + add
  end
  return table.concat(out, "  ")
end

-- ── Status bar (key-hint cheatsheet + clock) ─────────────────────────────────
-- Keep the tab bar visible so the right status always shows.
config.enable_tab_bar = true
config.use_fancy_tab_bar = true
config.tab_bar_at_bottom = false

wezterm.on("update-status", function(window, pane)
  -- Left: active key-table hint (e.g. when in copy_mode / search_mode).
  local name = window:active_key_table()
  if name then
    window:set_left_status(wezterm.format({
      { Foreground = { Color = "#f9e2af" } },
      { Text = "  " .. name .. " " },
    }))
  else
    window:set_left_status("")
  end

  -- Right: shortcut cheatsheet (trimmed to fit) + clock.
  local hints = fit_hints(window:get_dimensions().pixel_width)
  window:set_right_status(wezterm.format({
    { Foreground = { Color = "#89b4fa" } },
    { Text = hints .. "   " },
    { Foreground = { Color = "#a6e3a1" } },
    { Text = wezterm.strftime("%H:%M") .. "  " },
  }))
end)

-- ── host-local overrides (untracked) ─────────────────────────────────────────
-- Optional %USERPROFILE%\.wezterm-local.lua returning a table of config fields,
-- for things that are genuinely per-machine — so this file stays symlinkable.
-- Real case: docker-bc is a headless Proxmox VM with no GPU, where WezTerm dies
-- at startup with "Failed to create window: The OpenGL implementation is too old
-- to work with glium". front_end = "WebGpu" fixes it; note front_end = "Software"
-- does NOT, it still goes through glium. A GPU box wants the default, so this
-- cannot live in the shared config.
--   return { front_end = "WebGpu" }
local home = os.getenv("USERPROFILE") or os.getenv("HOME")
if home then
  local chunk = loadfile(home .. "/.wezterm-local.lua")   -- nil if absent
  if chunk then
    local ok, overrides = pcall(chunk)
    if ok and type(overrides) == "table" then
      for k, v in pairs(overrides) do
        config[k] = v
      end
    else
      wezterm.log_error("wezterm-local.lua did not return a table; ignoring")
    end
  end
end

return config

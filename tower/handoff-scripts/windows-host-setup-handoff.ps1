<#
Handoff script for the elevated/interactive parts of larry-setup/tower/windows-host-setup.md
that Claude couldn't do itself (real symlinks need elevation; plugin installs pull third-party
code; winget/npm installs are best run by a human watching for prompts).

Run this from an ELEVATED PowerShell (Run as Administrator). Safe to re-run — every step is
idempotent (checks before acting).

Deliberately NOT included, per the plan:
  - HomeLab CA trust (Dave chose to skip this for now — pi calls to Larry over HTTPS will fail
    with a TLS error until this is revisited; nothing else here depends on it).
  - KB_REMOTE_TOKEN (secret from deb:~/.config/kb/serve.env — fill in yourself in ~/.bashrc).
  - WireGuard roaming setup (not needed while on/reachable from the home LAN).
#>

$ErrorActionPreference = "Stop"
$repo = "C:\Users\Dave.Sinclair\larry-setup"   # NOT C:\larry-setup — see plan notes on why

$isAdmin = ([Security.Principal.WindowsIdentity]::GetCurrent().Groups -contains 'S-1-5-32-544')
if (-not $isAdmin) {
    Write-Warning "Not running elevated — the symlink step (step 3) will fail. Re-run as Administrator."
}

Write-Host "`n== Step 1: pi ==" -ForegroundColor Cyan
if (-not (Get-Command pi -ErrorAction SilentlyContinue)) {
    npm i -g @earendil-works/pi-coding-agent
} else {
    Write-Host "pi already installed: $(pi --version)"
}

Write-Host "`n== Step 2: pi provider + settings ==" -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.pi\agent" | Out-Null
Copy-Item "$repo\tower\ollama-provider.ts" "$env:USERPROFILE\.pi\ollama-provider.ts" -Force
$piSettingsPath = "$env:USERPROFILE\.pi\agent\settings.json"
$piSettings = @{
    extensions   = @("$env:USERPROFILE\.pi\ollama-provider.ts")
    defaultModel = "qwen3-coder:30b"
} | ConvertTo-Json
Set-Content -Path $piSettingsPath -Value $piSettings -Encoding utf8
Write-Host "Wrote $piSettingsPath"
Write-Host "Note: pi model calls to Larry will TLS-fail until HomeLab CA trust is set up (skipped for now)."

Write-Host "`n== Step 3: real symlinks (needs elevation + Git Bash) ==" -ForegroundColor Cyan
$gitBash = "C:\Program Files\Git\bin\bash.exe"
if (-not (Test-Path $gitBash)) { throw "Git Bash not found at $gitBash" }

New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.pi\agent\prompts" | Out-Null
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\commands" | Out-Null
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.local\bin" | Out-Null
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.pi\agent\extensions" | Out-Null

$symlinkScript = @'
set -e
export MSYS=winsymlinks:nativestrict
REPO="/c/Users/Dave.Sinclair/larry-setup"
PROMPTS="$HOME/.pi/agent/prompts"
COMMANDS="$HOME/.claude/commands"
BIN="$HOME/.local/bin"
EXT="$HOME/.pi/agent/extensions"

for f in al al-route go-route cs-route spec handover warplan scout bc-agent; do
  ln -sf "$REPO/tooling/$f.md" "$PROMPTS/$f.md"
done

for f in al fable bc-agent; do
  ln -sf "$REPO/tooling/$f.md" "$COMMANDS/$f.md"
done
ln -sf "$REPO/tooling/warplan-claude.md" "$COMMANDS/warplan.md"
ln -sf "$REPO/tooling/scout-claude.md" "$COMMANDS/scout.md"
ln -sf "$REPO/tooling/spec-claude.md" "$COMMANDS/spec.md"

for f in alw gow csw probe bcw anon kb kb-lint al-rag; do
  ln -sf "$REPO/tooling/$f" "$BIN/$f"
done

ln -sf "$REPO/tooling/kb-search.pi-ext.ts" "$EXT/kb-search.ts"
ln -sf "$REPO/tooling/searxng-search.pi-ext.ts" "$EXT/searxng-search.ts"

echo "Symlinks done."
ls -la "$PROMPTS" "$COMMANDS" "$BIN" "$EXT"
'@
$symlinkScriptPath = "$env:TEMP\larry_symlinks.sh"
Set-Content -Path $symlinkScriptPath -Value $symlinkScript -Encoding ascii
& $gitBash -c "MSYS=winsymlinks:nativestrict bash '$($symlinkScriptPath -replace '\\','/')'"

Write-Host "`nNote: /bc-agent, /warplan, /scout, /spec now point at the repo — a 'git pull' in" -ForegroundColor Yellow
Write-Host "$repo updates all of them at once. /al and /fable are new commands (weren't on WSL)." -ForegroundColor Yellow

Write-Host "`n== Step 4: starship + PowerShell profile ==" -ForegroundColor Cyan
if (-not (Get-Command starship -ErrorAction SilentlyContinue)) {
    winget install --id Starship.Starship -e
} else {
    Write-Host "starship already installed."
}
$profilePath = $PROFILE
New-Item -ItemType Directory -Force -Path (Split-Path $profilePath) | Out-Null
if (-not (Test-Path $profilePath)) { New-Item -ItemType File -Path $profilePath | Out-Null }
$profileContent = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
$starshipBlock = @"
`$env:STARSHIP_CONFIG = "$repo\tower\starship-setup\starship.toml"
`$env:PATH = "`$env:ProgramFiles\starship\bin;`$env:PATH"
Invoke-Expression (&starship init powershell)
"@
if ($profileContent -notlike "*STARSHIP_CONFIG*") {
    Add-Content -Path $profilePath -Value "`n# larry-setup: starship`n$starshipBlock"
    Write-Host "Added starship block to $profilePath"
} else {
    Write-Host "Profile already has a starship block — left untouched."
}

Write-Host "`n== Step 5: Claude plugins (third-party — review before confirming) ==" -ForegroundColor Cyan
Write-Host "About to run:" -ForegroundColor Yellow
Write-Host "  claude plugin marketplace add JuliusBrussee/caveman"
Write-Host "  claude plugin install caveman@caveman"
Write-Host "  claude plugin install gopls-lsp@claude-plugins-official"
$confirm = Read-Host "Proceed with these? [y/N]"
if ($confirm -eq "y") {
    claude plugin marketplace add JuliusBrussee/caveman
    claude plugin install caveman@caveman
    claude plugin install gopls-lsp@claude-plugins-official
    Write-Host "If you enable caveman's statusline, it needs Git Bash named explicitly (bash isn't on Windows PATH):"
    Write-Host '  "command": "\"C:/Program Files/Git/bin/bash.exe\" \"<...>/caveman/*/src/hooks/caveman-statusline.sh\""'
} else {
    Write-Host "Skipped plugin install."
}

Write-Host "`n== Done. Verify: ==" -ForegroundColor Green
Write-Host "  pi --list-models        (expect a TLS error against Larry — known gap, CA trust skipped)"
Write-Host "  claude  -> /bc-agent, /warplan, /scout, /spec, /al, /fable should all load"
Write-Host "  (open a new Git Bash tab) alw help; gow help; csw help"

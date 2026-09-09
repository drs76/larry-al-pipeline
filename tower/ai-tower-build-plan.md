# AI Inference Tower Build Plan

## Hardware
- GPU: AMD Radeon RX 7900 XTX (24GB VRAM)
- OS: Rocky Linux 10 — minimal server, no GUI
- Architecture: Inference only (Architecture A)

## Architecture
```
Dev machine (existing)          Tower (new)
  Neovim + ALNvim plugin    →   Ollama + RX 7900 XTX
  AL MCP server (altool)        serves models over LAN
  .NET + AL extension           port 11434
```

AL tools stay on dev machine. Tower runs Ollama, plugin points to tower IP.

---

## Phase 1 — Rocky Linux 10 Install

- Minimal ISO install (no GUI)
- Enable SSH server during install — manage headless from day one
- SELinux is enabled by default — set to permissive to avoid blocking Ollama:

```bash
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```

---

## Phase 2 — ROCm + AMD Driver

```bash
# Prerequisites
sudo dnf install -y kernel-headers kernel-devel kernel-modules-extra gcc make git curl wget
sudo dnf install -y epel-release

# AMD installer for Rocky Linux 9
# VERIFY URL at https://repo.radeon.com/amdgpu-install/ before running
sudo dnf install -y https://repo.radeon.com/amdgpu-install/6.3/el/10/amdgpu-install-6.3.60300-1.el10.noarch.rpm
sudo dnf clean all

# python3-wheel required by amd-smi-lib — lives in CRB repo
sudo dnf config-manager --enable crb
sudo dnf install -y python3-wheel

# Install ROCm stack (in-kernel amdgpu driver used — DKMS version breaks on Rocky 10 due to missing CEC symbols)
sudo amdgpu-install --usecase=rocm

# Add user to groups
sudo usermod -aG render,video $USER

# Reboot
sudo reboot
```

Verify after reboot:
```bash
rocm-smi
# should show RX 7900 XTX with 24GB
```

---

## Phase 3 — Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh

# Expose on LAN — edit systemd service
sudo systemctl edit ollama
```

Add to service override:
```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
# If GPU not detected, uncomment line below:
# Environment="HSA_OVERRIDE_GFX_VERSION=11.0.0"
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama

# Pull model
ollama pull qwen2.5-coder:32b
```

Verify GPU in use:
```bash
# In one terminal — watch GPU memory spike
rocm-smi

# In another — run model
ollama run qwen2.5-coder:32b
```

---

## Phase 4 — Firewall

Rocky Linux uses `firewalld` (not ufw):

```bash
# Allow SSH
sudo firewall-cmd --permanent --add-service=ssh

# Allow Ollama from LAN only — adjust subnet to match your network
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.x.0/24" port port="11434" protocol="tcp" accept'

sudo firewall-cmd --reload
```

---

## Phase 5 — Dev Machine Config

Point ALNvim plugin Ollama endpoint at tower IP:
```lua
ollama_host = "http://192.168.x.tower:11434"
```

---

## NFS storage — `/mnt/rojaws`

Larry mounts the NAS share (`192.168.0.175:/mnt/storage5/data`) at `/mnt/rojaws` — the pipeline,
projects, and the dashboard all read from here. Use **robust** fstab options; a bare `nfs rw`
entry races the network at boot and stays silently unmounted, which surfaces later as
`[Errno 2] No such file or directory` from anything reading `/mnt/rojaws/...` (e.g. the dashboard's
AL-REFERENCE view).

`/etc/fstab`:
```
192.168.0.175:/mnt/storage5/data /mnt/rojaws nfs _netdev,nofail,x-systemd.automount,x-systemd.mount-timeout=30,rw 0 0
```
- `_netdev` — wait for network-online before mounting (kills the boot race)
- `nofail` — boot proceeds even if the NAS is down
- `x-systemd.automount` — lazy-mount on first access **and auto-remount after a drop** (survives NAS/network blips)
- `mount-timeout=30` — don't hang forever

Apply: `doas systemctl daemon-reload && doas mount -a`, then `findmnt /mnt/rojaws`.

---

## Expected Performance
- Qwen 2.5 Coder 32B Q4_K_M: ~60-80 tok/s on GPU
- Full 24GB VRAM — model fits entirely on GPU
- vs NUC CPU path: ~5-10 tok/s

## Tier Split
| Task | Tool |
|---|---|
| Boilerplate, CRUD, tests, refactors | Ollama (tower) via ALNvim |
| AL day-to-day, symbol lookup | Ollama + AL MCP server |
| Architecture, complex logic, planning | Claude Code |

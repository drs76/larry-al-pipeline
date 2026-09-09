# NOMAD — Offline Services Stack (LXC on Nemesis)

## Overview

NOMAD is an LXC container running on Nemesis (Proxmox host). It hosts offline/utility services via Docker Compose. LibreChat is **not** here — use Larry's instance at `https://larry.home.arpa:3443`.

## Access

| Service | URL | Purpose |
|---|---|---|
| Kiwix | `http://nomad:8080` | Offline Wikipedia + ZIM library |
| Kolibri | `http://nomad:8008` | Offline learning platform |
| CyberChef | `http://nomad:8081` | Data encoding/decoding/analysis |
| Flatnotes | `http://nomad:8082` | Flat-file markdown notes |
| Qdrant | `http://nomad:6333` | Vector DB for RAG |

## Infrastructure

```
nemesis (Proxmox host)
└── NOMAD (LXC)
    ├── Docker Compose at /opt/nomad/
    ├── /mnt/kiwix   ← bind mount from nemesis storage disk (mp0, shared=1)
    └── /mnt/kolibri ← bind mount from nemesis storage disk (mp1, shared=1)
```

### Critical: LXC Mount Propagation
Docker inside LXC cannot see through Proxmox mp mounts unless `shared=1` is set.  
In `/etc/pve/lxc/<NOMAD_ID>.conf`:
```
mp0: /path/on/nemesis/kiwix,mp=/mnt/kiwix,shared=1
mp1: /path/on/nemesis/kolibri,mp=/mnt/kolibri,shared=1
```

## Docker Compose

File: `/opt/nomad/docker-compose.yml`  
Env: `/opt/nomad/.env`

### Services

**Qdrant** — vector store, named volume `qdrant_data`

**Kiwix** — serves all `*.zim` files from `/mnt/kiwix`
- Uses shell entrypoint for glob expansion: `kiwix-serve --port=8080 /data/*.zim`
- ZIM files downloaded from `https://download.kiwix.org/zim/`

**Kolibri** — bind mount `/mnt/kolibri:/kolibri` (named volume rejected by image)

**CyberChef** — stateless, no volumes

**Flatnotes** — named volume `flatnotes_data`, env vars from `.env`

### .env Required Variables

```
FLATNOTES_SECRET=<hex32>
FLATNOTES_USER=<username>
FLATNOTES_PASS=<password>
```

## Kiwix ZIM Library

Downloaded to nemesis storage disk, mounted at `/mnt/kiwix` in NOMAD LXC.

| File | Size | Topic |
|---|---|---|
| wikipedia_en_all_maxi | ~100GB | Wikipedia (with images) |
| stackoverflow.com_en_all | 75GB | Stack Overflow |
| wikibooks_en_all_nopic | 3.3GB | Wikibooks |
| wikispecies_en_all_maxi | 3.2GB | Nature / species |
| trueprepper.com_en_all | 1.3GB | Survival / preparedness |
| biology.stackexchange | 401MB | Biology / nature |
| zimgit-post-disaster | 615MB | Disaster survival |
| codereview.stackexchange | 523MB | Code review |
| softwareengineering.stackexchange | 456MB | Software engineering |
| outdoors.stackexchange | 135MB | Outdoors / fishing |
| cs.stackexchange | 264MB | Computer science |
| zimgit-food-preparation | 93MB | Food / survival |
| zimgit-medicine | 67MB | Medicine / survival |
| zimgit-knots | 27MB | Knots / outdoors |
| zimgit-water | 20MB | Water / survival |
| devdocs_en_python | ~4MB | Python docs |
| devdocs_en_javascript | ~3MB | JavaScript docs |

## Using from Another Claude Project

Add to `CLAUDE.md`:
```
Read /mnt/rojaws/localDev/nomad/nomad-context.md for NOMAD (offline services stack on nemesis) details.
```

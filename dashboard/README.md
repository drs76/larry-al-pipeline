# Larry Maintenance Dashboard

Small Flask app (runs **on Larry**) — 3 tabs:
- **Maintenance** — ollama status/version/models, update + restart ollama, pull/remove models, nginx reload.
- **AL Knowledge** — view `AL-REFERENCE.md`, anonymise an uploaded export (via `tooling/anonymise.py` + the local name map).
- **Docs** — renders the flow docs (`PROJECT-LIFECYCLE`, `ALW`/`GOW`/`CSW`, `COMS`, `RUN-BUILD`, `AL-REFERENCE`).

Binds `127.0.0.1:8090`; exposed at `https://larry.home.arpa/dash` behind nginx **basic-auth**.
Privileged ops use passwordless `doas` (service runs as `dav`).

## Deploy (on Larry)
The repo lives on an **NFS mount with root-squash**, so `doas` (root) can't read
`/mnt/rojaws/...` — stage privileged files through `/tmp` first.
```sh
D=/mnt/rojaws/localDev/setup/dashboard
doas mkdir -p /opt/larry-dashboard && doas chown dav:dav /opt/larry-dashboard
cp $D/app.py /opt/larry-dashboard/                       # app runs from local /opt (not NFS)
python3 -m venv /opt/larry-dashboard/.venv
/opt/larry-dashboard/.venv/bin/pip install -r $D/requirements.txt
# basic-auth user (pick a password):
printf 'admin:%s\n' "$(openssl passwd -apr1 'YOURPASS')" | doas tee /etc/nginx/dash.htpasswd
# nginx :443 server (reuses larry.home.arpa cert):
cp $D/nginx-dashboard.conf /tmp/ && doas cp /tmp/nginx-dashboard.conf /etc/nginx/conf.d/dashboard.conf
doas nginx -t && doas systemctl reload nginx
# systemd service:
cp $D/larry-dashboard.service /tmp/ && doas cp /tmp/larry-dashboard.service /etc/systemd/system/
doas systemctl daemon-reload && doas systemctl enable --now larry-dashboard
```
Then browse **`https://larry.home.arpa/dash`**. Deployed live 2026-07-03.

## Redeploy after changing app.py (from the dev box)
The running copy is `/opt/larry-dashboard/app.py` on Larry — **not** the repo file. One ritual:
```sh
setup/dashboard/deploy-dash            # scp app.py → restart service → verify API
setup/dashboard/deploy-dash --check    # diff repo vs deployed (drift detector), no changes
```
Env: `DASH_HOST` (default `larry`), `DASH_APP_DIR` (default `/opt/larry-dashboard`). It warns if
`larry-dashboard.service` drifts too (that one stays a manual doas step).

Config env: `DASH_PORT` (8090), `LARRY_REPO` (setup repo path), `AL_ANON_MAP` (name map for anonymise), `BUILD_BOX` (ssh host for the Builds tab, default `deb`).

## Tabs
- **Maintenance** — ollama status/update/restart, pull/remove models, nginx reload (doas).
- **Builds** — run `alw|gow|csw build <project> [--review]` over SSH on `$BUILD_BOX`; output streams live.
- **Nomad** — `docker ps`/`restart` on the Nomad box (flatnotes/kolibri/kiwix/cyberchef).
- **Logs** — journalctl for ollama/dashboard/nginx/docker (Larry-local).
- **AL Knowledge** — render AL-REFERENCE, anonymise an upload.
- **Docs** — render the flow docs.

### SSH deps (Builds + Nomad tabs)
The service runs as `dav`; those tabs shell out over SSH, so Larry's key
(`~dav/.ssh/id_ed25519.pub`) must be in:
- `root@nomad:~/.ssh/authorized_keys` (Nomad tab), and
- `dav@<BUILD_BOX>:~/.ssh/authorized_keys` (Builds tab),
with the host keys in Larry's `~/.ssh/known_hosts` (`ssh-keyscan -H nomad <build-box>`).
Both tabs fail gracefully (show the SSH error) if the key isn't present.

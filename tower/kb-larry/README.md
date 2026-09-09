# KB hybrid-search — Larry host units

`kb serve` + nightly `kb index` run on **Larry** (user systemd + linger); the sqlite store is on
Larry local disk (`~/.local/share/kb/kb.db`, WAL). Clients query over HTTP (`KB_REMOTE`→:8848).
See `pipeline/KB-SEARCH.md` and EN-8 in `reference/larry-tower-build-and-architecture.md`.

Install on Larry:
    cp *.service *.timer ~/.config/systemd/user/
    cp serve.env.example ~/.config/kb/serve.env   # then fill KB_SERVE_TOKEN, chmod 600
    doas loginctl enable-linger dav
    doas firewall-cmd --add-port=8848/tcp --permanent && doas firewall-cmd --reload
    systemctl --user daemon-reload
    systemctl --user enable --now kb-serve.service kb-refresh.timer

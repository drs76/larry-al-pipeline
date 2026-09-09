#!/bin/sh
# Evict every model ollama currently holds, so the 27B llama-server can claim VRAM.
# Runs as ExecStartPre of bonsai-llama.service. ollama CLI talks to the daemon over
# :11434 — no root needed. Best-effort: never block the server start.
set +e
LOADED=$(ollama ps 2>/dev/null | awk 'NR>1 {print $1}')
for m in $LOADED; do
    echo "bonsai-freevram: unloading ollama model $m"
    ollama stop "$m" 2>/dev/null
done
# give the driver a moment to release VRAM before llama-server allocates
sleep 2
exit 0

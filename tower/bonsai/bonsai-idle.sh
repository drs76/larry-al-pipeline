#!/bin/sh
# Auto-stop the Bonsai server after it has been idle, so the coder/pipeline can
# reclaim VRAM without manual `bonsai off`. Driven by bonsai-idle.timer.
# Activity = last write to server.log (llama-server logs per-request timings).
IDLE_MAX=900   # 15 min
LOG=/mnt/models/bonsai/server.log
systemctl is-active --quiet bonsai-llama || exit 0
[ -f "$LOG" ] || exit 0
AGE=$(( $(date +%s) - $(stat -c %Y "$LOG") ))
if [ "$AGE" -ge "$IDLE_MAX" ]; then
    logger -t bonsai-idle "idle ${AGE}s >= ${IDLE_MAX}s — stopping bonsai-llama to free VRAM"
    systemctl stop bonsai-llama
fi

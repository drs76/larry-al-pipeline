#!/usr/bin/env bash
# CPU utilization % averaged over the interval since the last call.
# Non-blocking: stores prev totals in /tmp and diffs on next call.
set -- $(grep '^cpu ' /proc/stat)          # cpu user nice system idle iowait irq softirq steal ...
idle=$5
total=0; for v in "${@:2}"; do total=$((total + v)); done

prev="/tmp/.tmux-cpu-$UID"
read -r pt pi 2>/dev/null < "$prev"
printf '%s %s\n' "$total" "$idle" > "$prev"

pct=0
if [ -n "$pt" ] && [ $((total - pt)) -gt 0 ]; then
  pct=$(( 100 * ((total - pt) - (idle - pi)) / (total - pt) ))
fi
printf ' %d%%' "$pct"        #  = nf-fa-microchip

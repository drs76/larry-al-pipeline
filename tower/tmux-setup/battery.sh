#!/usr/bin/env bash
# Battery segment for WSL: sysfs read, level glyph, charge-state marker.
# Owns its own colour + powerline arrows so it can turn RED when low (<20%).
# Args: $1 = left-neighbour bg, $2 = right-neighbour bg (for the transition
# arrows). Emits tmux #[...] style tags, which tmux applies after #() runs.
left="${1:-#e0af68}"
right="${2:-#7aa2f7}"
bat=$(echo /sys/class/power_supply/BAT[0-9]* | cut -d' ' -f1)
[ -d "$bat" ] || exit 0
cap=$(<"$bat/capacity")
st=$(<"$bat/status")

if   [ "$cap" -ge 90 ]; then g=''      # nf-fa-battery_full
elif [ "$cap" -ge 60 ]; then g=''      # three_quarters
elif [ "$cap" -ge 40 ]; then g=''      # half
elif [ "$cap" -ge 15 ]; then g=''      # quarter
else                         g=''; fi   # empty

case "$st" in
  Charging) c=' ' ;;     # bolt
  Full)     c=' ' ;;     # plug
  *)        c='' ;;       # Discharging / Not charging
esac

bg='#9ece6a'; fg='#16161e'              # normal: green
[ "$cap" -lt 20 ] && bg='#f7768e'       # low: red

#  = left powerline arrow (U+E0B2). fg=segment bg, bg=neighbour.
printf '#[fg=%s,bg=%s]#[fg=%s,bg=%s,bold] %s%s %d%% #[fg=%s,bg=%s]' \
  "$bg" "$left" "$fg" "$bg" "$g" "$c" "$cap" "$right" "$bg"

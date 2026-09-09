#!/bin/sh
# Power menu for sway.
# $mod+Shift+e, or the red power button at the right end of waybar.
# wofi picks the action; a second wofi confirms anything that loses work.
# No extra packages — wofi and swaylock are already part of the setup.

LOCK="swaylock -f -c 1e1e2e"

menu() {
    # $1 = prompt, $2 = number of lines
    wofi --dmenu --insensitive --prompt "$1" --lines "$2" --width 260 --cache-file /dev/null
}

confirm() {
    # Defaults to No: it is the first line, so Return alone is the safe answer.
    [ "$(printf 'No\nYes\n' | menu "$1" 2)" = "Yes" ]
}

choice=$(printf '%s\n' 'Lock' 'Logout' 'Suspend' 'Reboot' 'Shutdown' | menu 'Power' 5)

case "$choice" in
    Lock)     exec $LOCK ;;
    Logout)   confirm 'Log out of sway?' && exec swaymsg exit ;;
    Suspend)  $LOCK; exec systemctl suspend ;;
    Reboot)   confirm 'Reboot now?'      && exec systemctl reboot ;;
    Shutdown) confirm 'Shut down now?'   && exec systemctl poweroff ;;
esac

exit 0

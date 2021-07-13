#! /bin/bash 

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &	# Graphical authentication agent
picom --config ~/.config/qtile/picom.conf &

# picom --experimental-backends &
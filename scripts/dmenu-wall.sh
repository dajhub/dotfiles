#!/bin/sh
#     _____          ___           ___     
#    /  /::\        /  /\         /__/|    
#   /  /:/\:\      /  /::\       |  |:|     ***This script was made by Clay Gomera (Drake)***
#  /  /:/  \:\    /  /:/\:\      |  |:|      - Description: A simple wallpaper changer script
# /__/:/ \__\:|  /  /:/~/:/    __|  |:|      - Dependencies: dmenu, fd, feh
# \  \:\ /  /:/ /__/:/ /:/___ /__/\_|:|____
#  \  \:\  /:/  \  \:\/:::::/ \  \:\/:::::/
#   \  \:\/:/    \  \::/~~~~   \  \::/~~~~ 
#    \  \::/      \  \:\        \  \:\     
#     \__\/        \  \:\        \  \:\    
#                   \__\/         \__\/    
# This is a simple dmenus script to chose wallpapers on the go, using feh and fd. This is still in development


## MAIN VARIABLES AND COMMANDS ##
walldir="$HOME/Pictures/Wallpapers/" # wallpapers folder, change it to yours, make sure that it ends with a /
cd "$walldir" || exit

## SELECT PICTURE FUNCTION ##
selectpic() {
    wallpaper=$(fd --full-path "$walldir" | dmenu -l 10 -b -i -p "Select a wallpaper:")
    if [ "$wallpaper" ]; then
        chosenwall=$wallpaper
    else
        exit 0
    fi
}
selectpic

## WALLPAPER SETTING OPTIONS ##
option1="Fill"
option2="Center"
option3="Tile"
option4="Max"
option5="Scale"
options="$option1\n$option2\n$option3\n$option4\n$option5"

## MAIN ACTION ##
action=$(echo "$options" | dmenu -l 10 -b -i -p "Chose the format:")
case "$action" in
    $option1*)
        feh --bg-fill "$chosenwall";;
    $option2*)
        feh --bg-center "$chosenwall";;
    $option3*)
        feh --bg-tile "$chosenwall";;
    $option4*)
        feh --bg-max "$chosenwall";;
    $option5*)
        feh --bg-scale "$chosenwall";;
esac
exit 0

local gears = require'gears'
local beautiful = require'beautiful'
local awful = require'awful'
require'awful.autofocus'
require'errors' -- Error handling

-- Theme
beautiful.init(require'theme')

-- Bling
local bling = require("bling")

-- Keys
require'keys'

-- Buttons
require'buttons'

-- Client only: {keys, buttons, rules, signals}
require'client'

-- Layouts
awful.layout.layouts = {
    awful.layout.suit.tile,
    awful.layout.suit.floating,
    awful.layout.suit.max,
    bling.layout.centered,
}
require'layout'

-- Init
awful.spawn.with_shell([[
    ~/.config/awesome/desktop.sh
    ~/.config/awesome/v4l2.sh
    picom --config ~/.config/picom/picom.conf &
    nitrogen --restore &
    /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
    -- blueman-applet &
    nm-applet &
    thunar --daemon &
    xset r rate 460 35 &
    setxkbmap -model pc105 -layout gb & 
    xset s 300 5 &
    xss-lock -n /usr/lib/xsecurelock/dimmer -l -- ~/.config/awesome/xsecurelock.sh &
]])

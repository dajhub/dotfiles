# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


# Autostart
import os
import subprocess
from libqtile import hook

##### STARTUP PROGRAMS #####

@hook.subscribe.startup_once
def start_once():
	home = os.path.expanduser("~")
	subprocess.call([home + "/.config/qtile/autostart.sh"])

#
#@hook.subscribe.startup_once
#def autostart():
#    home = os.path.expanduser('~')
    #subprocess.Popen([home + '/.config/qtile/autostart.sh'])
 #   subprocess.Popen([home + '/.config/qtile/brightness.sh'])


mod = "mod4"
alt = "mod1"
terminal = "alacritty" # original: guess_terminal()

#############################################
############ SHORTCUTS ######################
#############################################

keys = [
# Applications    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([alt], "space", lazy.spawn("rofi -combi-modi drun -font 'Noto Sans 11' -show combi")),
    Key([alt], "b", lazy.spawn("firefox")),
    Key([alt], "n", lazy.spawn("thunar")),
    Key([alt], "s", lazy.spawn("code")),
    
# Lock Screen
    #Key([mod],"l", lazy.spawn("betterlockscreen -l")),

##################################################
######### MEDIA & BRIGHTNESS CONTROLS ############
##################################################
# Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

# Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 1%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 1%-")),

# Nightlight
    #Key([mod], "n", lazy.spawn("redshift -P -O 5000")),
    #Key([mod, "shift"], "n", lazy.spawn("redshift -x")),

    

    # Switch between windows in current stack pane
###################################################
################  SWITCH LAYOUT ###################
###################################################


# Switch between windows
    Key([mod], "Tab", lazy.layout.down(), desc="Move focus down"),
    Key([mod, "shift"], "Tab", lazy.layout.up(), desc="Move focus up"),


# Move windows up or down in Monadtall/Layout-Tall
    Key([mod], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod], "Up", lazy.layout.shuffle_up(), desc="Move window up"),


# Window controls - change focus & grow/shrink windows
    Key([mod], "j", lazy.layout.down(), desc='Move focus down in current stack pane'),
    Key([mod], "k", lazy.layout.up(), desc='Move focus up in current stack pane'),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc='Move windows down in current stack'),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc='Move windows up in current stack'),
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod], "n", lazy.layout.normalize(), desc='normalize window size ratios'),
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),

    	

# Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]


###################################################
####################   LAYOUTS ####################
###################################################

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width":1,
"margin":3,
"border_focus": "A3BE8C",
"border_normal":"81a1c1"}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme),
]

###################################################
##############  WIDGETS & SCREENS #################
###################################################

widget_defaults = dict(
    font='sans',
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/Pictures/wallpapers/conifer-sapling.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale = 0.7,
                    padding = 5
                ),

                widget.GroupBox(
                    font="SF Pro Display",
                    fontsize=12,
                    highlight_method="line", # could also be 'block'
                    #highlight_color="2e3440",
                    highlight_color = ['#202020', '#343434'],
                    rounded=False,
                    padding_x=5,
                    padding_y=5,
                    active="#ffffff",
                    inactive="#959595",
                    this_current_screen_border="5e81ac",
                    urgent_border="bf616a",
                    disable_drag=True
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.Prompt(
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="38FC55"
                ),
                widget.TextBox(
                    text=" ",
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="88c0d0"
                ),
                widget.WindowName(
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="88c0d0",
                    max_chars=70
                ),
                widget.Systray(),
#                widget.TextBox(
#                    text="",
#                    font="SF Pro Display",
#                    fontsize=13,
#                    foreground="bf616a"
#                 ),
#                widget.CPU(
#                    font="SF Pro Display",
#                    fontsize=13,
#                    foreground="eceff4",
#                    format="CPU {load_percent}%"
#                ),
                    widget.TextBox(
                    text="    ⟳",
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="d08770"
                ),

                widget.CheckUpdates(
                    distro = "Arch_checkupdates",
                    display_format = "{updates} Updates",
                    no_update_string = '0 Updates',
                    restart_indicator = 'Checking...',
                    font="SF Pro Display",
                    fontsize=13,
                    #foreground = "88c0d0",
                    colour_have_updates = "d08770",
                    #colour_no_updates = "d08770",
                    update_interval = 3000
                 ),

                widget.TextBox(
                    text="    ",
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="a3be8c"
                ),
                widget.Memory(
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="eceff4",
                    format="{MemUsed: } /{MemTotal: } MB"
                ),
                widget.TextBox(
                    text="    ",
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="88c0d0"
                ),
                widget.PulseVolume(
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="eceff4"
                ),
                widget.Battery(
                    font="SF Pro Display",
                    fontsize=13,
                    charge_char='     ',
                    discharge_char="     ",
                    full_char='     ',
                    format="{char} {percent:2.0%}",
                    foreground="eceff4"
                ),
                widget.TextBox(
                    text="     ",
                    font="SF Pro Display",
                    fontsize=13,
                    foreground="b48ead"
                ),
                widget.Clock(
                    font="SF Pro Display",
                    fontsize=13,
                    format="%a  %d %b | %H : %M",
                    foreground="eceff4"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                )
            ],
            28,
            background = "#2e3440",
            opacity = 1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

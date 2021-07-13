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
mod1 = "control"
terminal = "alacritty" # original: guess_terminal()

#############################################
############### COLORS ######################
#############################################
dracula = [
   "#282a36",  # 0  Background
   "#44475a",  # 1  current line/lighter_black
   "#f8f8f2",  # 2  foreground
   "#6272a4",  # 3  comment/dark_grey
   "#8be9fd",  # 4  cyan
   "#50fa7b",  # 5  green
   "#bd93f9",  # 6  purple
   "#ffb86c",  # 7  orange  
   "#f1fa8c",  # 8  yellow
   "#ff5555",  # 9  red
   "#ffffff",  # 10 white 
   "#6272a4",  # 11 bluish -- dracula
   "#4A4A4A",  # 12 grey
   "#A1A1A1",  # 13 light-grey
]

onedark = [
   "#282c34", # 0 background
   "#3f444a", # 1 bg-alt
   "#bbc2cf", # 2 foreground
   "#5B6268", # 3 dark grey / comments
   "#46d9ff", # 4 cyan
   "#98be65", # 5 green 
   "#da8548", # 6 orange 
   "#c678dd", # 7 magenta
   "#a9a1e1", # 8 violet
   "#ff6c6b", # 9 red 
   "#ecbe7b", # 10 yellow 
   "#ffffff", # 11 white
   "#4A4A4A", # 12 grey
   "#A1A1A1", # 13 light-grey
      ]

palenight = [
  "#292D3E", # 0 background
  "#242837", # 1 bg-alt
  "#EEFFFF", # 2 foreground
  "#676E95", # 3 dark grey / comments
  "#80cbc4", # 4 cyan
  "#c3e88d", # 5 green 
  "#f78c6c", # 6 orange 
  "#c792ea", # 7 magenta
  "#bb80b3", # 8 violet
  "#ff5370", # 9 red 
  "#ffcb6b", # 10 yellow 
  "#ffffff", # 11 white
  "#4A4A4A", # 12 grey
  "#A1A1A1", # 13 light-grey
     ]

gruvbox = [
  "#282828", # 0 background /dark hard
  "#242837", # 1 bg-alt
  "#d5c4a1", # 2 foreground / light 2 / for text
  "#676E95", # 3 dark grey / comments
  "#80cbc4", # 4 cyan
  "#c3e88d", # 5 green 
  "#f78c6c", # 6 bright_orange
  "#c792ea", # 7 magenta
  "#bb80b3", # 8 violet
  "#ff5370", # 9 red 
  "#ffcb6b", # 10 yellow 
  "#ffffff", # 11 white
  "#4A4A4A", # 12 grey
  "#A1A1A1", # 13 light-grey
     ]

nord = [
  "#2e3440", # 0 background / POLAR JET - changed
  "#242837", # 1 bg-alt
  "#88b3b3", # 2 foreground / FROST AQUA / for text
  "#676E95", # 3 dark grey / comments
  "#eceff4", # 4 SNOWSTORM SMOKE - changd
  "#a3be8c", # 5 AURORA GREEN - changed 
  "#f78c6c", # 6 orange 
  "#a78ea2", # 7 AURORA PURPLE - changed
  "#76a9a0", # 8 FROST TEAL
  "#ff5370", # 9 AURORA RED - change
  "#ffcb6b", # 10 yellow 
  "#ffffff", # 11 white
  "#4A4A4A", # 12 grey
  "#A1A1A1", # 13 light-grey
     ]

color = dracula


#############################################
# SHORTCUTS 
#############################################

keys = [
# Applications    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Key([alt], "space", lazy.spawn("rofi -combi-modi drun -font 'Noto Sans 11' -show combi")),
    Key([alt], "b", lazy.spawn("vivaldi-stable")),
    Key([alt], "n", lazy.spawn("nemo")),
    Key([alt], "c", lazy.spawn("code")),
    Key([alt], "s", lazy.spawn("simplenote")),
    
# Lock Screen
    #Key([mod],"l", lazy.spawn("betterlockscreen -l")),

# Rofi scripts
    Key([alt], "space", lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget."),
    Key([alt], "Tab", lazy.spawn("rofi -show window -kb-accept-entry '!Alt-Tab,!Alt+Alt_L' -kb-row-down 'Alt+Tab'"),
        desc="Switch between windows"),
    #Key([mod], "v", lazy.spawn("bwmenu"),
    #    desc="Launch password manager"),
    #Key([mod], "p", lazy.spawn(powermenu),
    #    desc="Launch power menu"),

# Rotate through workspaces
    Key([mod1], "Tab", lazy.screen.next_group()),
    Key([mod1, "shift" ], "Tab", lazy.screen.prev_group()),


##################################################
# MEDIA & BRIGHTNESS CONTROLS 
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

    

###################################################
# SWITCH BETWEEN WINDOWS IN CURRENT STACK PANE
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
# LAYOUTS 
###################################################

groups = [
	Group("1", label=""),
	Group("2", label=""),
	Group("3", label=""),
	Group("4", label=""),
	Group("5", label=""),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod4 + shift + number of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([alt, "shift"], i.name, lazy.window.togroup(i.name),
             desc="move focused window to group {}".format(i.name)),
    ])

#####
# Use below when numbering wanted for workspaces instead of circles (as above)
#####

#groups = [Group(i) for i in "12345"]
#
#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + letter of group = move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#        #     desc="move focused window to group {}".format(i.name)),
#    ])

layout_theme = {"border_width":1,
"margin":3,
"border_focus": color[6],
"border_normal":color[12]}

layouts = [
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(**layout_theme),
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
# WIDGETS & SCREENS 
###################################################

widget_defaults = dict(
    font="FiraCode Nerd Font Medium",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()


#####
# Use below when using numbers for workspaces and comment out above
#####

#widget_defaults = dict(
#    font='sans',
#    fontsize=10,
#    padding=3,
#)
#extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper='~/Pictures/wallpapers/space-station.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                # GroupBox
                widget.Spacer(10),
                widget.GroupBox(
                    fontsize=14,
                    padding=3,
                    block_highlight_text_color=color[6],
                    active=color[11],
                    inactive=color[12],
                    borderwidth=0,
                ),
                widget.Spacer(10),

                # Layout
                widget.TextBox(
                    text="", padding=6, fontsize=14, foreground=color[13]
                ),
                widget.CurrentLayout(
                    foreground=color[13], font="Ubuntu regular", fontsize=12),
                widget.Spacer(10),

                # WindowName
                # widget.WindowName(
                #     format="|{state} {name}", max_chars=80, foreground=colors["white"]
                # ),
                # widget.TextBox(text="|", fontsize=16,
                #                foreground=colors["white"]),
                #widget.TaskList(foreground=color[11], icon_size=20, padding=5,
                #                font="FiraCode Nerd Font", fontsize=14, borderwidth=0,
                #                markup_focused='<span weight="bold">{}</span>'),
            ######
            #    widget.CurrentLayoutIcon(
            #        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            #        scale = 0.7,
            #        padding = 5
            #    ),
#
            #    widget.GroupBox(
            #        font="Ubuntu Regular",
            #        fontsize=12,
            #        highlight_method="line", # could also be 'block'
            #        #highlight_color="2e3440",
            #        highlight_color = ['#202020', '#343434'],
            #        rounded=False,
            #        padding_x=5,
            #        padding_y=5,
            #        active="#ffffff",
            #        inactive="#959595",
            #        this_current_screen_border="5e81ac",
            #        urgent_border=color[9],
            #        disable_drag=True
            #    ),
            #    widget.Sep(
            #        linewidth=0,
            #        padding=10
            #    ),
            #    widget.Prompt(
            #        font="Ubuntu regular",
            #        fontsize=12,
            #        foreground=color[5]
            #    ),
                widget.TextBox(
                    text=">> ",
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[2]
                ),
                widget.WindowName(
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[2],
                    max_chars=70
                ),
                widget.Systray(),
#                widget.TextBox(
#                    text="",
#                    font="Ubuntu regular",
#                    fontsize=12,
#                    foreground="bf616a"
#                 ),
#                widget.CPU(
#                    font="Ubuntu regular",
#                    fontsize=12,
#                    foreground="eceff4",
#                    format="CPU {load_percent}%"
#                ),
                    widget.TextBox(
                    text="    ⟳",
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[6]
                ),

                widget.CheckUpdates(
                    distro = "Arch_checkupdates",
                    display_format = "{updates} Updates",
                    no_update_string = '0 Updates',
                    restart_indicator = 'Checking...',
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground = color[2],
                    colour_have_updates = color[9],
                    colour_no_updates = color[2],
                    update_interval = 3000
                 ),

                widget.TextBox(
                    text="    ",
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[5]
                ),
                widget.Memory(
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[2],
                    format="{MemUsed: } /{MemTotal: } MB"
                ),
                widget.TextBox(
                    text="    ",
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[11]
                ),
                widget.PulseVolume(
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[2]
                ),
                widget.Battery(
                    font="Ubuntu regular",
                    fontsize=12,
                    charge_char='     ',
                    discharge_char="     ",
                    full_char='     ',
                    format="{char} {percent:2.0%}",
                    foreground=color[2]
                ),
                widget.TextBox(
                    text="     ",
                    font="Ubuntu regular",
                    fontsize=12,
                    foreground=color[7]
                ),
                widget.Clock(
                    font="Ubuntu regular",
                    fontsize=12,
                    format="%a  %d %b | %H : %M",
                    foreground=color[2]
                ),
                widget.Sep(
                    linewidth=0,
                    padding=10
                )
            ],
            28,
            background = color[0],
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

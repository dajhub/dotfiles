local awful = require'awful'
local beautiful = require'beautiful'

awful.rules.rules = {
    -- All clients will match this rule.
    { rule = { },
      properties = { border_width = beautiful.border_width,
                     border_color = beautiful.border_normal,
                     focus = awful.client.focus.filter,
                     raise = true,
                     keys = require'client.keys',
                     buttons = require'client.buttons',
                     screen = awful.screen.preferred,
                     placement = awful.placement.no_overlap+awful.placement.no_offscreen
     }
    },

    -- Floating clients.
    { rule_any = {
        instance = {
          "DTA",  -- Firefox addon DownThemAll.
          "copyq",  -- Includes session name in class.
          "pinentry",
        },
        class = {
          "Arandr",
          "Blueman-manager",
          "Gpick",
          "Kruler",
          "MessageWin",  -- kalarm.
          "Sxiv",
          "Tor Browser", -- Needs a fixed window size to avoid fingerprinting by screen size.
          "Wpa_gui",
          "veromix",
          "xtightvncviewer"},

        -- Note that the name property shown in xprop might be set slightly after creation of the client
        -- and the name shown there might not match defined rules here.
        name = {
          "Event Tester",  -- xev.
        },
        role = {
          "AlarmWindow",  -- Thunderbird's calendar.
          "ConfigManager",  -- Thunderbird's about:config.
          "pop-up",       -- e.g. Google Chrome's (detached) Developer Tools.
        }
      }, properties = { floating = true }},

    -- Add titlebars to normal clients and dialogs
    { rule_any = {type = { "normal", "dialog" }
      }, properties = { titlebars_enabled = false }
    },

    --{ names =  { "  ", "  ", "  ", "  ", "  " },
    --  layout = { lo[1], lo[1], lo[1], lo[1], lo[3] },
    --},
    --{ names =  { "  ", "  ", "  ", "  ", " 漣" },
    --  layout = { lo[2], lo[1], lo[1], lo[1], lo[1] },
    --},

    -- Set Firefox to always map on the tag named "2" on screen 1.
    -- { rule = { class = "Firefox" },
    --   properties = { screen = 1, tag = "2" } },
    
    -- Brave
    --{ rule = { class = "Brave" },
    --  properties = { screen = 1, tag = "  " } },
    
    -- Element
    { rule = { class = "Element" },
      properties = { screen = 1, tag = "  " } },

    -- GoLand
    { rule = { class = "jetbrains-goland" },
      properties = { screen = 2, tag = "  " } },

    -- Hypnotix
    { rule = { class = "Hypnotix.py" },
      properties = { screen = 1, tag = "  " } },

    -- Lxappearance
    { rule = { class = "Lxappearance" },
      properties = { screen = 2, tag = " 漣" } },
    
    -- Nitrogen
    { rule = { class = "Nitrogen" },
      properties = { screen = 2, tag = " 漣" } },

    -- Pavucontrol
    { rule = { class = "Pavucontrol" },
      properties = { screen = 2, tag = " 漣" } },
    
    -- Ristretto
    { rule = { class = "Ristretto" },
      properties = { screen = 1, tag = "  " } },

    -- Rofi
    { rule = { name = "rofi" },
      properties = { floating = true, titlebars_enabled = false, placement = awful.placement.centered } },
    
    -- Seahorse
    { rule = { class = "Seahorse" },
      properties = { screen = 2, tag = " 漣" } },

    -- Signal
    { rule = { class = "Signal" },
      properties = { screen = 1, tag = "  " } },

    -- Slack
    { rule = { class = "Slack" },
      properties = { screen = 1, tag = "  " } },

    -- Thunar
    --{ rule = { class = "Thunar" },
    --  properties = { screen = 1, tag = "  ", placement = awful.placement.centered } },
}

-- Normally we'd do this with a rule, but Spotify doesn't set its class or name
-- until after it starts up, so we need to catch that signal.
client.connect_signal("property::class", function(c)
    if c.class == "Spotify" then
        -- Move the Spotify instance to "misc" tag on this screen
        --local t = awful.tag.find_by_name(awful.screen.focused(), "misc")
        local t = awful.tag.find_by_name(awful.screen[0], "  ")
        c:move_to_tag(t)
    end
end)
client.connect_signal("property::name", function(c)
    if string.match (c.name, "Calendar | Microsoft Teams") then
        -- Move the Microsft Teams Chromium instance to "chat" tag on this screen
        --local t = awful.tag.find_by_name(awful.screen.focused(), "misc")
        local t = awful.tag.find_by_name(awful.screen[0], "  ")
        c:move_to_tag(t)
    end
end)
client.connect_signal("property::class", function(c)
    if c.class == "jetbrains-pycharm-ce" then
        -- Move jetbrains pycharm instance to "dev" tag on this screen
        --local t = awful.tag.find_by_name(awful.screen.focused(), "misc")
        local t = awful.tag.find_by_name(awful.screen[1], "  ")
        c:move_to_tag(t)
    end
end)

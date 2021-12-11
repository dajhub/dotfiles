local awful = require("awful")
local wibox = require("wibox")
local beautiful = require'beautiful'
local watch = require("awful.widget.watch")

local HOME_DIR = os.getenv("HOME")
local ICONS_DIR = HOME_DIR .. '/.local/share/icons/Tela-dark/24/panel/'

local vpn_widget = wibox.widget {
    {
        --image = ICONS_DIR .. 'cryptfolder-closed-light.svg',
        id = 'icon',
        widget = wibox.widget.textbox
    },
    {
        id = 'vpn_name_text',
        --font = 'Noto Sans Medium 8',
        widget = wibox.widget.textbox
    },
    layout = wibox.layout.fixed.horizontal,
    set_vpn_name = function(self, new_vpn_name)
        if new_vpn_name == '' then
            new_vpn_name = 'no vpn'
            --self:get_children_by_id('icon')[1]:set_image(ICONS_DIR .. 'cryptfolder-open-light.svg')
            --self:get_children_by_id('vpn_name_text')[1]:set_text(tostring(new_vpn_name))
            self:get_children_by_id('icon')[1]:set_markup('<span color="'..beautiful.clr.red..'" font="'..beautiful.icon_font..'"> </span>')
            self:get_children_by_id('vpn_name_text')[1]:set_markup('<span color="'..beautiful.clr.red..'" font="'..beautiful.widget_font..'"> '..new_vpn_name..'</span>')
        else
            --self:get_children_by_id('icon')[1]:set_image(ICONS_DIR .. 'cryptfolder-closed-light.svg')
            --self:get_children_by_id('vpn_name_text')[1]:set_text(tostring(new_vpn_name))
            self:get_children_by_id('icon')[1]:set_markup('<span color="'..beautiful.clr.green..'" font="'..beautiful.icon_font..'"> </span>')
            self:get_children_by_id('vpn_name_text')[1]:set_markup('<span color="'..beautiful.clr.green..'" font="'..beautiful.widget_font..'"> '..new_vpn_name..'</span>')
        end
    end
}

local function worker(user_args)

    local args = user_args or {}
    local timeout = args.timeout or 1

    local update_widget = function(widget, stdout)
        
        local vpn_name_stdout = stdout

        widget:set_vpn_name(vpn_name_stdout)
    end

    local nmcli = "nmcli connection show --active | grep wireguard | cut -d \' \' -f1"

    watch(string.format([[bash -c "%s"]], nmcli), timeout, update_widget, vpn_widget)

    -- Add mouse control
    -- - left click - switch vpn profile 
    vpn_widget:connect_signal("button::press", function(_, _, _, button)
        if (button == 1) then
            awful.spawn("switchvpn", false) -- left click
        end
    end)

    return vpn_widget
end

return setmetatable(vpn_widget, { __call = function(_, ...) return worker(...) end })

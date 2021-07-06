[module/updates-arch]
type = custom/script
exec = "arch_updates -s"
tail = true
format = <label>
format-prefix = " "
click-right = "arch_updates -u&"
click-left = "arch_updates -q&"
click-middle = "arch_updates -c&"
scroll-up = "arch_updates -n&"

from monitorcontrol import get_monitors

source_hdmi = "COMPOSITE1"
source_vga = "ANALOG1"

for monitor in get_monitors():
    with monitor:
        source = monitor.get_input_source()
        if source.name == source_hdmi:
            print("Set VGA")
            monitor.set_input_source(source_vga)
        else:
            print("Set HDMI")
            monitor.set_input_source(source_hdmi)
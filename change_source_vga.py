from monitorcontrol import get_monitors

source_vga = "ANALOG1"

for monitor in get_monitors():
    with monitor:
        source = monitor.get_input_source()
        if source.name != source_vga:
            print("Set VGA")
            monitor.set_input_source(source_vga)
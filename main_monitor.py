from monitorcontrol import get_monitors

monitors_default = [{"id": "65539", "source": "COMPOSITE1"},{"id": "65537", "source": "COMPOSITE1"}]

for monitor in get_monitors():
    with monitor:
        print("Contrast:",monitor.get_contrast())
        print("Input Source:",monitor.get_input_source())
        print("Luminance:",monitor.get_luminance())
        print("Power Mod:",monitor.get_power_mode())
        print("VPC Capabilities:",monitor.get_vcp_capabilities())

for monitor in get_monitors():
    with monitor:
        print(monitor.set_input_source("COMPOSITE1"))
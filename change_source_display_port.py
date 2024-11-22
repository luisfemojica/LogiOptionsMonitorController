from monitorcontrol import get_monitors

source_dp = "DP1"

for monitor in get_monitors():
    with monitor:
        source = monitor.get_input_source()
        if source.name != source_dp:
            print("Set DP")
            monitor.set_input_source(source_dp)
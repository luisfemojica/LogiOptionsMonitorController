#https://pypi.org/project/monitorcontrol/
#https://monitorcontrol.readthedocs.io/en/latest/index.html
#py -3.8 -m pip install monitorcontrol

import subprocess, json
from monitorcontrol import get_monitors

program_init = True
source_init = ""
source_hdmi = "COMPOSITE1"
source_vga = "ANALOG1"
device_status = False
device_status_value = False

dev_node_status_connected = 25174026
dev_node_status_disconnected = 58728458

print("Inicia Programa")
out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Device_DevNodeStatus' } | ConvertTo-Json}\"")
j = json.loads(out)
dev_node_status_value = int(j['Data'])

if dev_node_status_value == dev_node_status_connected:
    device_status = True
else:
    device_status = False

if program_init == True and device_status == True:
    print("Device is connected")
    device_status_value = True
    source_init = source_hdmi
    for monitor in get_monitors():
        with monitor:
            source = monitor.get_input_source()
            if source.name != source_hdmi:
                print("Set HDMI")
                monitor.set_input_source(source_hdmi)
elif program_init == True and device_status == False:
    print("Device is disconnected")
    device_status_value = False
    source_init = source_vga
    for monitor in get_monitors():
        with monitor:
            source = monitor.get_input_source()
            if source.name != source_vga:
                print("Set VGA")
                monitor.set_input_source(source_vga)

print('device_status_value',device_status_value)
print('source_init',source_init)

while True:
    out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Device_DevNodeStatus' } | ConvertTo-Json}\"")
    j = json.loads(out)
    dev_node_status_value = int(j['Data'])

    if dev_node_status_value == dev_node_status_connected:
        device_status = True
    else:
        device_status = False
    
    if device_status != device_status_value:
        if device_status == True:
            print("Device is connected")
            device_status_value = True
            for monitor in get_monitors():
                with monitor:
                    source = monitor.get_input_source()
                    if source.name != source_hdmi:
                        print("Set HDMI")
                        monitor.set_input_source(source_hdmi)
        elif device_status == False:
            print("Device is disconnected")
            device_status_value = False
            for monitor in get_monitors():
                with monitor:
                    source = monitor.get_input_source()
                    if source.name != source_vga:
                        print("Set VGA")
                        monitor.set_input_source(source_vga)
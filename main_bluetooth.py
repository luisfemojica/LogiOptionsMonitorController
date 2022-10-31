
import subprocess, json

is_init = False
device_id = '{83DA6326-97A6-4088-9453-A1923F573B29}'
device_name = 'MX Master 3S'
dev_node_status_keyname = 'DEVPKEY_Device_DevNodeStatus'
bluetooth_device_flags_keyname = 'DEVPKEY_Bluetooth_DeviceFlags'

dev_node_status_value = 0
dev_node_status_connected = 25174026
dev_node_status_disconnected = 58728458

bluetooth_device_flags_value = 0
bluetooth_device_flags_connected = 299077671
bluetooth_device_flags_disconnected = 282300423

device_status_connected = True
device_status_disconnected = False
device_status_value = False

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Device_DevNodeStatus' } | ConvertTo-Json}\"")
j = json.loads(out)
dev_node_status_value = j['Data']

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Bluetooth_DeviceFlags' } | ConvertTo-Json}\"")
j = json.loads(out)
bluetooth_device_flags_value = j['Data']

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^{83DA6326-97A6-4088-9453-A1923F573B29}' -and $_.Type -eq 17 } | ConvertTo-Json}\"")
j = json.loads(out)
device_status = j[1]['Data']

print("Device Status: " + str(device_status))
print("DevNodeStatus: " + str(dev_node_status_value))
print("BluetoothDeviceFlags: " + str(bluetooth_device_flags_value))

# print(out)
# for dev in j:
#     print(dev)
#     print(j)

    #print(dev['Status'], dev['Class'], dev['FriendlyName'], dev['InstanceId'] )

    # Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId | ConvertTo-Json
    # Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }
    # Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^BTH' }
    # Get-PnpDevice -PresentOnly | Select-Object Status,Class,FriendlyName,InstanceId | Where-Object { $_.InstanceId -match '^BTH' }
    # Get-PnpDevice -PresentOnly | Select-Object Status,Class,FriendlyName,InstanceId | Where-Object { $_.InstanceId -match '^BTH' } | ConvertTo-Json 
    # Get-ChildItem -Path HKLM:\SYSTEM\ControlSet001\Services\DeviceAssociationService\State\Store\ | Select-String -Pattern Bluetooth
    # Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty
    # Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | ConvertTo-Json 

    # Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Device_DevNodeStatus' } | ConvertTo-Json 
    # Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^{83DA6326-97A6-4088-9453-A1923F573B29}' -and $_.Type -eq 17 } | ConvertTo-Json
    # Get-PnpDevice -class Bluetooth -FriendlyName 'MX Master 3S' | Get-PnpDeviceProperty | Where-Object { $_.KeyName -match '^DEVPKEY_Bluetooth_DeviceFlags' } | ConvertTo-Json 

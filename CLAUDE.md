# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

A Windows Python daemon that monitors Bluetooth connection state of a Logitech MX Master 3S mouse and automatically switches Samsung monitor input sources via DDC/CI (Display Data Channel):
- Mouse **connected** → monitors switch to HDMI (`COMPOSITE1`)
- Mouse **disconnected** → monitors switch to VGA (`ANALOG1`)

This solves a KVM-like scenario where two PCs share the same monitors, mouse, and keyboard.

## Running the main daemon

```bat
main.bat
```
Or directly:
```powershell
"C:\Users\fe_mo\AppData\Local\Programs\Python\Python311\python.exe" main.py
```

## One-shot input source scripts

```bat
change_source_hdmi.bat    # Force all monitors to HDMI
change_source_vga.bat     # Force all monitors to VGA
change_source.bat         # Toggle between HDMI and VGA
```
Python equivalents: `change_source_hdmi.py`, `change_source_vga.py`, `change_source.py`, `change_source_display_port.py`.

## Install dependency

```
pip install monitorcontrol
```

## Architecture

### Bluetooth detection (`main.py`)
Uses `subprocess` to call PowerShell's `Get-PnpDevice` and reads `DEVPKEY_Device_DevNodeStatus` as a raw integer:
- `25174026` → connected
- `58728458` → disconnected

The main loop polls this value continuously (no sleep delay) and compares against the previous state to detect transitions.

### Input source constants (Samsung monitors)
The `InputSource` enum in `monitorcontrol/monitorcontrol.py` maps DDC/CI VCP values to names. The Samsung monitors in this setup use non-obvious mappings:
- `COMPOSITE1` (0x05) = the physical HDMI port
- `ANALOG1` (0x01) = the physical VGA port
- `DP1` (0x0F) = the physical DisplayPort

### Local `monitorcontrol/` package
A vendored/local copy of the [monitorcontrol](https://pypi.org/project/monitorcontrol/) library. The `Monitor` class in `monitorcontrol/monitorcontrol.py` wraps a VCP (Virtual Control Panel) backend:
- Windows backend: `monitorcontrol/vcp/vcp_windows.py` — uses `ctypes` with `PhysicalMonitorEnumerationAPI`
- Linux backend: `monitorcontrol/vcp/vcp_linux.py`
- VCP codes defined in `monitorcontrol/vcp/vcp_codes.py`

All `Monitor` methods must be called inside a `with monitor:` context manager.

### Reference files (`*.txt`, `main_ejemplo_bluetooth.py`, `main_ejemplo_monitor.py`)
Scratch/reference files kept for historical context. The `.txt` files mirror the `.py` files they are named after. `main_ejemplo_bluetooth.py` contains PowerShell commands explored during development for reading Bluetooth device properties.

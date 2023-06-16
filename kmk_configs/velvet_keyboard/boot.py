import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

from kb import KMKKeyboard
from kmk.scanners import DiodeOrientation

# If this key is held during boot, don't run the code which hides the storage and disables serial
# This will use the first row/col pin. Feel free to change it if you want it to be another pin
col = digitalio.DigitalInOut(KMKKeyboard.col_pins[0])
row = digitalio.DigitalInOut(KMKKeyboard.row_pins[0])

if KMKKeyboard.diode_orientation == DiodeOrientation.COLUMNS:
    col.switch_to_output(value=True)
    row.switch_to_input(pull=digitalio.Pull.DOWN)
else:
    col.switch_to_input(pull=digitalio.Pull.DOWN)
    row.switch_to_output(value=True)

if not row.value:
    usb_cdc.disable()
    usb_midi.disable()
    storage.disable_usb_drive()
    usb_hid.enable((usb_hid.Device.KEYBOARD), boot_device=1)

row.deinit()
col.deinit()

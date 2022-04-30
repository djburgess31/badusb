import usb_hid
import pwmio
from board import LED
import time

time.sleep(3.0)

led = pwmio.PWMOut(LED, frequency=5000, duty_cycle=0)
keyboard = usb_hid.Device.KEYBOARD

keycodes = [0x11,0x08,0x19,0x08,0x15,0x2C,0x0A,0x12,0x11,0x11,0x04,0x2C,0x0A,0x0C,0x19,0x08,0x2C,0x1C,0x12,0x18,0x2C,0x18,0x13]

led_duty_cycle=300
for keycode in keycodes:
    report = bytearray(8)
    report[2] = keycode
    keyboard.send_report(report)
    keyboard.send_report(bytearray(8))
led.duty_cycle=0

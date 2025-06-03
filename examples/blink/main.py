# Blinky for OHS2025 Badge
# Toggles Blue/Green LEDs
# Created by beau@nubcore.dk
# Revised: 31.05.2025 12:34

from machine import Pin
from time import sleep_ms
import neopixel

np = neopixel.NeoPixel(Pin(20), 2)

while 1:
 np[0] = (0, 20, 0)
 np[1] = (0, 0, 20)
 np.write()
 sleep_ms(300)
 np[0] = (0, 0, 20)
 np[1] = (0, 20, 0)
 np.write()
 sleep_ms(300)

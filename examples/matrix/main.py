# Blinky for OHS2025 Badge
# Toggles Blue/Green LEDs
# Created by beau@nubcore.dk
# Revised: 31.05.2025 12:34

from machine import Pin
from time import sleep_ms
import neopixel

# todo: change to const
PIXELS_PIN = 20
MATRIX_PIN = 5
PIXELS_COUNT = 2
MATRIX_COUNT = 16
BLINK_DELAY = 333


np = neopixel.NeoPixel(Pin(PIXELS_PIN), PIXELS_COUNT)
grid = neopixel.NeoPixel(Pin(MATRIX_PIN), MATRIX_COUNT)

pos = 0

def cycle():
 global pos
 grid.fill((0,0,0))
 grid[pos] = (20, 0, 0)
 grid.write()
 pos = pos + 1
 if pos >= MATRIX_COUNT:
  pos = 0
 sleep_ms(100)

while 1:
 np[0] = (0, 20, 0)
 np[1] = (0, 0, 20)
 np.write()
 sleep_ms(100)
 np[0] = (0, 0, 20)
 np[1] = (0, 20, 0)
 np.write()
 sleep_ms(100)

 while 1:
  cycle()

 grid.fill((5, 0, 0))
 grid.write()
 sleep_ms(500)
 grid.fill((0, 5, 0))
 grid.write()
 sleep_ms(500)
 grid.fill((0, 0, 5))
 grid.write()
 sleep_ms(300)

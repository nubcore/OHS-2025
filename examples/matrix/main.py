# Blinky for OHS2025 Badge
# Toggles Blue/Green LEDs
# Created by beau@nubcore.dk
# Revised: 06.03.2025 23:29

from machine import Pin
from time import sleep_ms
import neopixel
import random

# todo: change to const
PIXELS_PIN = 20
MATRIX_PIN = 5
PIXELS_COUNT = 2
MATRIX_COUNT = 16

np = neopixel.NeoPixel(Pin(PIXELS_PIN), PIXELS_COUNT)
grid = neopixel.NeoPixel(Pin(MATRIX_PIN), MATRIX_COUNT)

np.fill((0,0,0))
grid.fill((0,0,0))
sleep_ms(100)

pos = 0

def cycle(delay=20):
 global pos
 grid.fill((0,0,0))
 grid[pos] = (20, 0, 0)
 grid.write()
 pos = pos + 1
 if pos >= MATRIX_COUNT:
  pos = 0
 sleep_ms(delay)

def rgb_test(pixels, delay=100):
 pixels.fill((0, 0, 0))
 pixels.write()
 sleep_ms(delay)
 pixels.fill((5, 0, 0))
 pixels.write()
 sleep_ms(delay)
 pixels.fill((0, 5, 0))
 pixels.write()
 sleep_ms(delay)
 pixels.fill((0, 0, 5))
 pixels.write()

def r():
 return max(random.randint(0,32)-20, 0)

def r3():
 return (r(),r(),r())

def sparkle():
 grid[random.randint(0,MATRIX_COUNT-1)] = r3()
 grid.write()
 np[random.randint(0,PIXELS_COUNT-1)] = r3()
 np.write()

# Initialization dance
for x in range(32):
 cycle()

for y in range(3):
 rgb_test(np, 20)

for x in range(3):
 rgb_test(grid)

# GO GO SPARKLEz
while 1:
 sparkle()

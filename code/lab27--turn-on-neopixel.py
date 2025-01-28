import time
import board
import digitalio
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.20, auto_write=False)

while True:
  # set color red on NeoPixel and turn it on
  color = (255, 0, 0)
  dot.fill(color)
  dot.show()
  time.sleep(1)
  # turn off neopixel, i.e. show black
  color = (0, 0, 0)
  dot.fill(color)
  dot.show()
  time.sleep(1)

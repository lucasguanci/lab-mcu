# Lab 2.4 - toggle onboard LED 
# toggle onboard LED with pushbutton, 
# using internal pull-up resistor
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D6)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
  if switch.value:
    led.value = False
  else:
    led.value = True

  time.sleep(0.01)

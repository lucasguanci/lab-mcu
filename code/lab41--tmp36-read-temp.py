# Lab 4.1 - TMP36 
# reading voltage signal from an analog pin
# and trasforming it into celsius degrees
import board
import analogio
import time

pin_t = analogio.AnalogIn(board.A1)

def getTemperature(pin):
    v = (pin.value * 3.3) / 65536
    t = (v - 0.53) / 0.0112
    return [pin.value, v, t]

while True:
    temp = getTemperature(pin_t)
    print("value: {}, V: {}, T: {:.1f}".format(temp[0], temp[1], temp[2]))
    time.sleep(1)

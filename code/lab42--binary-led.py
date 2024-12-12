# Lab 4.2 - for loop
# generare un numero casuale tra 0 e 31,
# convertirlo in binario e visualizzarlo
# utilizzando 5 LEDs
import board
import digitalio
import time
import random

pin = [ x for x in range(5) ]
pin[0] = digitalio.DigitalInOut(board.D5)
pin[1] = digitalio.DigitalInOut(board.D6)
pin[2] = digitalio.DigitalInOut(board.D9)
pin[3] = digitalio.DigitalInOut(board.D10)
pin[4] = digitalio.DigitalInOut(board.D11)

for i in range(len(pin)):
    pin[i].direction = digitalio.Direction.OUTPUT
    pin[i].value = False

def padding(b):
    # add leading zeros (i.e. padding)
    # to the binary number
    if ( len(b)<7 ):
        splitted = b.split('0b')
        diff = 5-len(splitted[1])
        zeroes = ''
        for i in range(diff):
            zeroes += '0'
        lista = ['0b',zeroes,splitted[1]]
        b = ''.join(lista)
    return(b)

while True:
    # turn off all LEDs
    for i in range(len(pin)):
        pin[i].value = False
    # n è un numero tra 0 e 31
    n = random.randint(0,31)
    # string representation of the binary number,
    # i.e.  '0b....'
    b = bin(n)
    # add leading zeros, if necessary
    b = padding(b)
    for i in range(len(b)):
        # start from the 3rd character to skip over '0b'
        if ( i>1 ):
            if ( b[i] == '1' ):
                pin[6-int(i)].value = True
    time.sleep(10)

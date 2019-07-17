# Zhi Li 2019.07.01
# Blink pin0

import time
from machine import Pin
led=Pin(0,Pin.OUT)        #create LED object from pin0,Set Pin0 to output

while True:
  led.value(1)            #Set led turn on
  time.sleep(0.5)
  led.value(0)            #Set led turn off
  time.sleep(0.5)



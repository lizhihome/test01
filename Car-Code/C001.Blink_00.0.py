
# Zhi Li 2019.07.01
# Turn on LED on Pin18

from machine import Pin
import time

led=Pin(18,Pin.OUT)        #create LED object from pin0,Set Pin0 to output

led.value(1)            #Set led turn on
time.sleep(0.5)
led.value(0)            #Set led turn off
time.sleep(0.5)






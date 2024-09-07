from machine import Pin
import time

led = Pin(28, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if button.value():
        led.value(1)
    else:
        led.value(0)
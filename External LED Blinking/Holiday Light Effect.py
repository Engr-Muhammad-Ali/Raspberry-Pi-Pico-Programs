import machine
import utime

green = machine.Pin(22, machine.Pin.OUT)
red = machine.Pin(26, machine.Pin.OUT)
blue = machine.Pin(27, machine.Pin.OUT)
white = machine.Pin(28, machine.Pin.OUT)


delay = 0.05

while True:
    
    red.value(1)
    green.value(0)
    utime.sleep(delay)
    
    green.value(1)
    red.value(0)
    utime.sleep(delay)
    
    blue.value(1)
    green.value(0)
    utime.sleep(delay)
    
    white.value(1)
    blue.value(0)
    utime.sleep(delay)
    
    blue.value(1)
    white.value(0)
    utime.sleep(delay)
    
    green.value(1)
    blue.value(0)
    utime.sleep(delay)
    
    
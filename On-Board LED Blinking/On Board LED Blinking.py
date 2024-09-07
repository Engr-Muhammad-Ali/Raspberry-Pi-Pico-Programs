import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)
LED = machine.Pin(28, machine.Pin.OUT)

while True:
    
    led.value(1)
    LED.value(0)
    utime.sleep(1)
    
    led.value(0)
    LED.value(1)
    utime.sleep(1)
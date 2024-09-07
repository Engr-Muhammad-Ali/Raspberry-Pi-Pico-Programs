from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

delay = 1

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    
    while echo.value() == 1:
        signalon = utime.ticks_us()
      
    timepassed = signalon - signaloff
    return timepassed

while True:
    measured_time = distance()
    time = measured_time / 1000
    distance_cm = (measured_time * 0.0343) / 2
    
    lcd.move_to(0, 0)
    lcd.putstr("Time: " + "{:.4f} ms".format(time))
    
    lcd.move_to(0, 1)
    lcd.putstr("Distance:" + "{:.0f} cm".format(distance_cm))
    
    utime.sleep(delay)
    lcd.clear()

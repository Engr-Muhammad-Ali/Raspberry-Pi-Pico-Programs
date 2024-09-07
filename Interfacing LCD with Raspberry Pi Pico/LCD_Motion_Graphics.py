from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

delay = 0.1
message = "Muhammad Ali GD"

while True:
    
    for pos in range(4, -1, -1):
        lcd.move_to(pos, 1)
        lcd.putstr(message)
        utime.sleep(delay)
        lcd.clear()

    for pos in range(15, -1, -1):
        lcd.move_to(pos, 0)
        lcd.putstr(message)
        utime.sleep(delay)
        lcd.clear()

    for pos in range(15, 4, -1):
        lcd.move_to(pos, 1)
        lcd.putstr(message)
        utime.sleep(delay)
        lcd.clear()
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

delay = 1

TempSensor = machine.ADC(4)
conversion_factor = 3.3 / 65535

while True:
    
    voltage = TempSensor.read_u16() * conversion_factor
    temperature = 27 - (voltage - 0.706) / 0.001721
    
    lcd.move_to(0, 0)
    lcd.putstr("Pin Value: " + "{:.0f}".format(TempSensor.read_u16()))

    lcd.move_to(0, 1)
    lcd.putstr("V: " + "{:.0f}V".format(voltage) + " Temp:" + "{:.0f} *C".format(temperature))
    
    utime.sleep(delay)
    lcd.clear()

from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
import utime

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

delay = 1

Value = machine.ADC(26)
conversion_factor = 5/65535

while True:
    
  reading = Value.read_u16()
  data = reading * conversion_factor
  
  lcd.move_to(0,0)
  lcd.putstr("Pin Value: " + "{:.2f}".format(reading))
  
  lcd.move_to(0,1)
  lcd.putstr("Result: " + "{:.4f} V".format(data))
  
  utime.sleep(delay)
  lcd.clear()
  
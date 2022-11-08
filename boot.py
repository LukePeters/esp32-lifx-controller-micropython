from machine import Pin, SoftI2C
import ssd1306
import gfx

i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
graphics = gfx.GFX(128, 64, display.pixel)

DISPLAY_LINE_HEIGHT = 10
DISPLAY_MAX_LINES = 6

BUILTIN_LED = Pin(2, Pin.OUT)
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for monochromatic character LCD on Raspberry Pi"""
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# This demo is only for a single line display but need ot set to 2 lines due to 0x40 offset at char 8
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D21)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

# Turn backlight on and off a few times
for _ in range(5):
   lcd.backlight = True
   time.sleep(0.5)
   lcd.backlight = False
   time.sleep(0.5)
# Print message
lcd.message = "Hello Out There!"
# Wait 5s
time.sleep(5)
lcd.clear()
# Print message right to left
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello Backwards!"
# Wait 5s
time.sleep(5)
# Return text direction to left to right
lcd.text_direction = lcd.LEFT_TO_RIGHT

# Display cursor
lcd.clear()
lcd.cursor = True
lcd.message = "Cursor!"
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor! "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!  "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!   "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!    "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!     "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!      "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!       "
# Wait 1s
time.sleep(0.5)
lcd.message = "Cursor!        "
# Wait 1s
time.sleep(0.5)


# Display blinking cursor
lcd.clear()
lcd.blink = True
lcd.message = "Blinky Cursor!"
# Wait 5s
time.sleep(5)
lcd.blink = False
lcd.clear()
# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg
# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()
lcd.message = "All Done, Cya!"
# Turn backlight off
lcd.backlight = False
time.sleep(2)

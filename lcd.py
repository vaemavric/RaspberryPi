#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_16x2.py
#  16x2 LCD Test Script
#
# Author : Matt Hawkins
# Date   : 06/04/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def main():
  # Main program block

  GPIO.setup(8, GPIO.OUT)  # E
  GPIO.setup(7, GPIO.OUT) # RS
  GPIO.setup(25, GPIO.OUT) # DB4
  GPIO.setup(24, GPIO.OUT) # DB5
  GPIO.setup(23, GPIO.OUT) # DB6
  GPIO.setup(18, GPIO.OUT) # DB7


  # Initialise display
  lcd_init()

  while True:

    # Send some test
    lcd_string("Rasbperry Pi",0x80)
    lcd_string("16x2 LCD Test",0xC0)

    time.sleep(3) # 3 second delay

    # Send some text
    lcd_string("1234567890123456",0x80)
    lcd_string("abcdefghijklmnop",0xC0)



    time.sleep(3) # 3 second delay

    # Send some text
    lcd_string("RaspberryPi-spy",0x80)
    lcd_string(".co.uk",0xC0)

    time.sleep(3)

    # Send some text
    lcd_string("Follow me on",0x80)
    lcd_string("Twitter @RPiSpy",0xC0)

    time.sleep(3)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,False) # 110011 Initialise
  lcd_byte(0x32,False) # 110010 Initialise
  lcd_byte(0x06,False) # 000110 Cursor move direction
  lcd_byte(0x0C,False) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,False) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,False) # 000001 Clear display
  time.sleep(0.0005)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(7, mode) # RS

  # High bits
  GPIO.output(25, False)
  GPIO.output(24, False)
  GPIO.output(23, False)
  GPIO.output(18, False)
  if bits&0x10==0x10:
    GPIO.output(25, True)
  if bits&0x20==0x20:
    GPIO.output(24, True)
  if bits&0x40==0x40:
    GPIO.output(23, True)
  if bits&0x80==0x80:
    GPIO.output(18, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(25, False)
  GPIO.output(24, False)
  GPIO.output(23, False)
  GPIO.output(18, False)
  if bits&0x01==0x01:
    GPIO.output(25, True)
  if bits&0x02==0x02:
    GPIO.output(24, True)
  if bits&0x04==0x04:
    GPIO.output(23, True)
  if bits&0x08==0x08:
    GPIO.output(18, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(0.0005)
  GPIO.output(8, True)
  time.sleep(0.0005)
  GPIO.output(8, False)
  time.sleep(0.0005)

def lcd_string(message,line):
  # Send string to display




  message = message.ljust(16," ")

  lcd_byte(line, False)

  for i in range(16):
    lcd_byte(ord(message[i]),True)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
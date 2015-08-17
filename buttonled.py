# Raspberry Pi Basic input/output control
#
# Author : Vaemavric
# Date : 12/08/2015
# 

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#A function to set the desired pin to input or output
def setupPin(pinNo, COM):
 if(COM == 'in'):
  GPIO.setup(pinNo, GPIO.IN)
 elif(COM == 'out'):
  GPIO.setup(pinNo, GPIO.OUT)
 else:
  print ('COM can only be \"in\" or \"out\" ')

#A function to blink an led on and off
def blinking(pinNo, period):
 GPIO.output(pinNo, True)
 time.sleep(period)
 GPIO.output(pinNo, False)
 time.sleep(period)

prev_input = False
#A function to return whether a button has been pushed
def buttonPush(pinNo):
 global prev_input
 input = GPIO.input(pinNo)
 if((not prev_input) and (input)):
  pressed = True
 else:
  pressed = False
 time.sleep(0.05) 
 prev_input = input
 return pressed

#final function to clear settings
def clear():
 GPIO.cleanup()
 quit() 

setupPin(17, 'out') 
setupPin(4, 'in')
GPIO.output(17, False)
LEDoff = True
try:
 while True:
  if (buttonPush(4)):
   if (LEDoff):
    GPIO.output(17, True)
    LEDoff = False
   elif((not LEDoff)):
    GPIO.output(17, False)
    LEDoff = True 
except KeyboardInterrupt:
 clear()


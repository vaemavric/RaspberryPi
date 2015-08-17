import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pinNo = 17
GPIO.setup(pinNo, GPIO.IN)
prev_input = 0
try:
 while True:
  input = GPIO.input(pinNo)
  if((not prev_input) and (input)):
   print("Button Pressed")
  prev_input = input
  time.sleep(0.05)
except KeyboardInterrupt:
 GPIO.cleanup()

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def setupPin(pinNo, com):
	if(com == 'in'):
		GPIO.setup(pinNo, GPIO.IN)
	elif(com == 'out'):
		GPIO.setup(pinNo, GPIO.OUT)
		GPIO.output(17, False)
	else:
		pass
def clear():
	GPIO.cleanup()
	quit()
def toggle(pinP, pinL):
	prevInput = 0
	state = False
	while True:
		input = GPIO.input(pinP)
		print 'input= {} prevInput = {}'.format(input, prevInput)
		if ((not prevInput) and input):
			print "In"
			if(state == True):
				state = False 
				GPIO.output(pinL, False)
			elif(state == False):
				GPIO.output(pinL, True)
				state = True
			else:
				pass
		prevInput = GPIO.input(pinP)
		time.sleep(0.1)
		

try:
	states = {4:'in', 17:'out'}
	for i in states:
		setupPin(i, states[i])
	toggle(4, 17)
except:
	clear()
	

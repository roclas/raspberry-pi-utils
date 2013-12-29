#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

#waittime=1.0/4302 #remotes key-1 frequency
waittime=1.0/40
pin=11 

def main():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	# Set Pin X on the GPIO header to act as an output
	GPIO.setup(pin,GPIO.OUT)
	# This loop runs forever and flashes the LED
	while True:
		GPIO.output(pin,GPIO.HIGH)
		#print "se enciende el led"
		time.sleep(waittime)

		GPIO.output(pin,GPIO.LOW)
		#print "se apaga el led"
		time.sleep(waittime)

try:
      main()
except: 
      print "error happened"
	

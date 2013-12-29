#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

tiempo=2.0
pin=11 

def main():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	# Set Pin X on the GPIO header to act as an output
	GPIO.setup(pin,GPIO.OUT)
	# This loop runs forever and flashes the LED
	while True:
		GPIO.output(pin,GPIO.HIGH)
		print "se enciende el led"
		time.sleep(tiempo)

		GPIO.output(pin,GPIO.LOW)
		print "se apaga el led"
		time.sleep(tiempo)

try:
      main()
except: 
      print "error happened"
	

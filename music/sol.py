#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

tiempo=1/1536.0

def main():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	# Set Pin 5 on the GPIO header to act as an output
	GPIO.setup(5,GPIO.OUT)
	# This loop runs forever and flashes the LED
	while True:
		GPIO.output(5,GPIO.HIGH)
		print "se enciende el led"
		# Wait for 2 seconds
		time.sleep(tiempo)
		GPIO.output(5,GPIO.LOW)
		print "se apaga el led"
		time.sleep(tiempo)

try:
      main()
except: 
      print "error happened"
	

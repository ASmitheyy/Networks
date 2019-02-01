import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

while True:
	GPIO.output(17, GPIO.HIGH)
	print("Red LED ON")
	GPIO.output(12, GPIO.LOW)
	print("Yellow LED OFF")
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(12,GPIO.HIGH)
	print("Red LED OFF")
	print("Yellow Led ON")
	time.sleep(1)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for x in range(26):
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, GPIO.LOW)
	x += 1


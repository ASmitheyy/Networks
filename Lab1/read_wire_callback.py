import time
import RPi.GPIO as GPIO
import os
import math

num_bits = 8

def result_byte():
	result_byte.my_byte += 1 << line_break.counter

result_byte.my_byte = 0 

def hold_bytes():
	hold_bytes.message.append(result_byte.my_byte)

hold_bytes.message = bytearray()

def store_bytes():
	char=bytes(result_byte.my_byte)
	hold_bytes.message.extend(char)

def determine_number():
	total = 0
	if (result_byte.my_byte != 0):
		store_bytes()

def line_break():
	line_break.counter += 1

line_break.counter = 0

def poll_data():
	result = GPIO.input(21)
	if result:
		result_byte()
		line_break()
	else:
		line_break()

	if (line_break.counter > 7):
		line_break.counter = 0
		hold_bytes()
		print_string()
		result_byte.my_byte = 0

def print_string():
	print("Recieved code")

def print_message():
	for my_byte in hold_bytes.message:
		print(" - {:08b} - {:}".format(my_byte, chr(my_byte)))

def make_byte():
	make_byte.byte = bytes(result_byte.my_byte)



def my_callback(channel1):
	if GPIO.input(channel1) == 0:
		poll_data()
	still_running.done = True
	new_print = True

def still_running():
	still_running.done = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.IN)

GPIO.add_event_detect(22, GPIO.BOTH, callback=my_callback)

print("RUNNING")

#I did this because i didnt think of opening another session and accessing the pi that way
os.system("python3 encoding.py")

new_print = True

while True:
	print("still running")
	if (still_running.done == False and new_print):
		print_message()
		new_print = False
	else:
		still_running.done = False
		time.sleep(3)


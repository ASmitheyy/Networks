import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

bits_to_encode = 8
message = 'Hello Dr. Craven.'
clock_time = .01

byte_array = bytearray(message,'UTF-8')



def mystring():
	mystring.string = [0,0,0,0,0,0,0,0]
mystring()
def print_string():
	print("Sending:")
	print(''.join(str(x) for x in mystring.string))


for my_byte in byte_array:


	for bit_pos in range(bits_to_encode):
		GPIO.output(17,GPIO.HIGH)
		bit = 1 << bit_pos & my_byte
		if bit != 0:
			bit_value = 1
			GPIO.output(12,GPIO.HIGH)
		else:
			bit_value = 0
			GPIO.output(12,GPIO.LOW)
		time.sleep(clock_time)
		GPIO.output(17,GPIO.LOW)
		time.sleep(clock_time)
		mystring.string[bit_pos] = bit_value
	print_string()

	#print("Bit position {:2} is {} which is worth {:2}".format(bit_pos,bit_value,bit))



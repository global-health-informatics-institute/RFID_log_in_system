#Importing modules 

import RPi.GPIO as GPIO
from mfrc522 import SimpleMRFC522
import os
import sys

#Initializing SimpleMRFC522() function
reader = SimpleMRFC522()

#Defining Auth_Keys

Auth_keys =[464528273323, 458964803305]

#Reading the Card's id and text with reader.read()
try:
	id, text = reader.read()

#Cleaning the GPIO pins for other communications
finally:
	GPIO.cleanup()

#conditions if Auth_keys
if id == 464528273323:
	print(Welcome, text)
	os.system('/sbin/logsave')
	
elif id==458964803305:
	
	print(Welcome, text)
	os.system('/sbin/logsave')

#if conditions not met
else:
	os.system('/sbin/reboot')
	
	
#importing modules

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#Initializing reader variable 
reader =  SimpleMFRC522()

try:
    #input as New data
	text = input ('New data:')
	
	#prompt a user to place the closer to RFID-RC522 module
    print ("Now place your tag to write")
	
	#writing the data on the card
    reader.write(text)
	
	#feedback to confirm that the card has been written
    print (""Written")
    
#cleaning the GPIO pins to be available for other communications	
finally:
    GPIO.cleanup()

#importing modules
 
import RPi.GPIO as GPIO
fom mfrc522 import SimpleMFRC522

#Initializing reader variable
reader = SimpleMFRC522()

	
try:
    #readinging the id and text
	id, text = reader.read()
	
    #printing the id
	print(id)
	
    #print the text
	print (text)

#cleaning the GPIO pins to be available for other communications    
finally:
    GPIO.cleanup()

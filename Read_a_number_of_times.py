##importing modules
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

##Initializing SimpleMRFC522() function
reader = SimpleMFRC522()

##Looping
try:
	while True:
		print("Hold a tag near the reader")
		
		##Reading the Card's id and text with reader.read()
		id, text = reader.read()
		
		##print the ID and the text
		print("ID:%s\nText:%s"(id,text))
		
		##sleep the reading for 5 seconds
		sleep(5)
		
##Exceptionof the KeyboardInterrupt
except KeyboardInterrupt:

#Cleaning the GPIO pins for other communications
	GPIO.cleanup()
	
## raise
	raise
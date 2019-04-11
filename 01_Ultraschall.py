import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig =  
echo = 

print("Messung startet")

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try: 
	while True:
		gpio.output(trig, False)
		
		time.sleep(0.5)
		
		gpio.output(trig, True)
		time.sleep(0.00001)
		gpio.output(trig, False)
		
		while gpio.input(echo) == 0:	# Nach Senden des Signals über trig springt der Input (echo) kurz auf LOW
			start = time.time()
		
		while gpio.input(echo) == 1:	# Solange kein reflektiertes Signal zurückkommt ist Input (echo) HIGH
			stop = time.time()
			
		vergangeneZeit = stop-start
		
		entfernung = round(vergangeneZeit*34000/2, 2)
		
		print(entfernung)

except KeyboardInterrupt:
	gpio.cleanup()


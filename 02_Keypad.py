import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

matrix = [["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["*", "0", "#", "D"]]

spalte = [, , , ]
zeile = [, , , ]

for j in range(4):
	gpio.setup(spalte[j], gpio.OUT)
	gpio.output(spalte[j], 1)
	gpio.setup(zeile[j], gpio.IN, pull_up_down=gpio.PUD_UP)
	
def keypad():
	while True:
		for j in range (4):
			gpio.output(spalte[j], 0)
			for i in range(4):
				if gpio.input(zeile[i]) == 0:
					benutzerEingabe = matrix[i][j]
					while gpio.input(zeile[i]) == 0:
						pass
					return benutzerEingabe
			gpio.output(spalte[j], 1)
	return False
try:
	while True:
		print(keypad())
		time.sleep(0.2)

except KeyboardInterrupt:
	gpio.cleanup()

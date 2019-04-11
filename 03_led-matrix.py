import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219

# cascaded: Anzahl an Matrizen, block_orientation: Rotation der Ausrichtung
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0)  

virtual = viewport(device, width=200, height=100)

try:
	while True:
		with canvas(virtual) as draw:
	    		draw.text((0, 3), "    Temperatur: 20°C  ", fill="white")

		for offset in range(135):
	    		virtual.set_position((offset, 4))
	    		time.sleep(0.07)
except:
	print("Fehler aufgetreten.")


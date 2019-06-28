from ev3dev.ev3 import *

class SensorLum:
    def __init__(self):
        self.cl = ColorSensor()
        self.cl.mode='COL-COLOR'

    def getColor(self):
        colors=('unknown','black','blue','green','yellow','red','white','brown')
        return (colors[self.cl.value()])


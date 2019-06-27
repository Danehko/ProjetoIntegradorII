#!/usr/bin/env python3

from ev3dev.ev3 import *
from time   import sleep

class SensorLum:

	def __init__(self):
		self.cl = ColorSensor()
		self.cl.mode='COL-COLOR'


	def getColor(self):
		colors=('unknown','black','blue','green','yellow','red','white','brown')
		return (colors[self.cl.value()])






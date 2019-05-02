#!/usr/bin/env python3
from itertools import chain
import codecs
import collections
import copy
import random
import struct
import sys
import socket
from robo import *
from SensorLum import *
from enum import Enum

class Coordenadas:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.eixo = 0

    def enviarCoordenadas(self):
        return self.posx +':'+ self.posy +':'+ self.eixo

    def virarEixo(self, dir):
        if(self.eixo == 0):
            self.eixo = 1
            return true
        elif(self.eixo == 1):
            self.eixo = 0
            return true
        return false

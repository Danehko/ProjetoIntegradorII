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
    def __init__(self,posx,posy,ref):
        self.posx = posx
        self.posy = posy
        self.referencia = ref

    def enviarCoordenadas(self):
        return (posx,posy)

    def trocandoPos(self, dir):
        if(dir=='frente'):
            if(self.referencia=='N'):
                self.posx = self.posx + 1
            elif(self.referencia=='S'):
                self.posx = self.posx - 1
            elif (self.referencia == 'L'):
                self.posy = self.posy + 1
            elif (self.referencia == 'O'):
                self.posy = self.posy - 1
        elif(dir=='retornar'):
            if (self.referencia == 'N'):
                self.posx = self.posx - 1
            elif (self.referencia == 'S'):
                self.posx = self.posx + 1
            elif (self.referencia == 'L'):
                self.posy = self.posy - 1
            elif (self.referencia == 'O'):
                self.posy = self.posy + 1
        elif (dir == 'direita'):
            if (self.referencia == 'N'):
                self.posy = self.posy + 1
                self.referencia = 'L'
            elif (self.referencia == 'S'):
                self.posy = self.posy - 1
                self.referencia = 'O'
            elif (self.referencia == 'L'):
                self.posx = self.posx - 1
                self.referencia = 'S'
            elif (self.referencia == 'O'):
                self.posx = self.posx + 1
                self.referencia = 'N'
        elif (dir == 'esquerda'):
            if (self.referencia == 'N'):
                self.posy = self.posy - 1
                self.referencia = 'O'
            elif (self.referencia == 'S'):
                self.posy = self.posy + 1
                self.referencia = 'L'
            elif (self.referencia == 'L'):
                self.posx = self.posx + 1
                self.referencia = 'N'
            elif (self.referencia == 'O'):
                self.posx = self.posx - 1
                self.referencia = 'S'
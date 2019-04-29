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

class sr:
    def __init__(self):
        self.robot = Robo()
        self.MAC = self.mac()
        self.posx = 0
        self.posy = 0
        self.eixo = 0
        self.pausa = 0
        self.inicio = 0
        self.modoDeJogo = 0
        self.listaDeCacas
        self.listaDeCompetidores

    def mac(self):
        dados = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        aux = ''
        cont = 0
        while (cont < 12):
            aux = aux + random.choice(dados);
            cont = cont + 1
        return aux

    def obstaculo(self):

    def autenticar(self, server_adress='', port=int(5683)):

    def frente(self):
        robot.setManual("frente")
        return true
    def esquerda(self):
        robot.setManual("esquerda")
        return true
    def direita(self):
        robot.setManual("direita")
        return true
    def tras(self):
        robot.setManual("retornar")
        return true
    def seguirEstrategia(self):

    def enviarLocalizacao(self, server_adress='', port=int(5683)):

    def confirmarCaca(self, server_adress='', port=int(5683)):

    def recebendoInfo(self, server_adress='', port=int(5683)):


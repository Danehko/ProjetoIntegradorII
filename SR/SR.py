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
from Mapa import *
from SensorLum import *
from enum import Enum


class sr:
    def __init__(self):
        self.robot = Robo() #cria um robo
        self.MAC = '1a2b3c4d5e6f' #identificação unica do Robo
        self.coordenadas = Coordenadas()
        self.pausa = 0 # se pausa for igual a 1 o jogo é pausado
        self.inicio = 0 # se inicio for igual 1 o jogo começou
        self.modoDeJogo = 0 # mododeJogo igual a 0 para modo autonomo e 1 para modo manual

    #def mac(self):
    #    dados = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    #    aux = ''
    #    cont = 0
    #    while (cont < 12):
    #        aux = aux + random.choice(dados);
    #        cont = cont + 1
    #    return aux

    def frente(self):
        if((self.pausa==0) and (self.modoDeJogo==1) and (self.inicio==1)):
            robot.setManual("frente")
            return true
        return false

    def esquerda(self):
        if ((self.pausa == 0) and (self.modoDeJogo == 1) and (self.inicio == 1)):
            robot.setManual("esquerda")
            return true
        return false

    def direita(self):
        if ((self.pausa == 0) and (self.modoDeJogo == 1) and (self.inicio == 1)):
            robot.setManual("direita")
            return true
        return false

    def tras(self):
        if ((self.pausa == 0) and (self.modoDeJogo == 1) and (self.inicio == 1)):
            robot.setManual("retornar")
            return true
        return false

    #def autenticar(self, server_adress='', port=int(5683)):

    #def seguirEstrategia(self):

    #def enviarLocalizacao(self, server_adress='', port=int(5683)):

    #def confirmarCaca(self, server_adress='', port=int(5683)):

    #def recebendoInfo(self, server_adress='', port=int(5683)):


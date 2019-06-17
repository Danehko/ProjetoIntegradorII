#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq
import sys
from threading import Thread

class Recebe_SS(Thread):
    def __init__(self,partida):
        super().__init__()
        self.partida = partida
        self.movendo = 'nao'
        context = zmq.Context()
        self.s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.142" #String
        PORT = sys.argv[2] if len(sys.argv) > 2 else "60000" #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.connect(p)  # connect to the server
        self.s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages

    def run(self):
        self._recebe()

    def _recebe(self):
        dados = self.s.recv()  # receive a message
        print(dados.decode())
        dados = dados.decode()
        self._tratando(dados)
               
    def _tratando(self, mensagem):
        dados = mensagem[0]
        dados = dados.split(':')
        if(dados[0] == '0'):
            print('Autenticado')
        elif(dados[0] == '1'): #
            print('Nao autenticado')
        elif(dados[0] == '2'): #
            self.partida.receberMapa(mensagem[0][2:len(mensagem[0])])
            self.partida.inicio()
        elif (dados[0] == '3'): #
            self.movendo = dados[1]
        elif (dados[0] == '4'): #
            self.partida.receber(mensagem[0][2:len(mensagem[0])])
        elif (dados[0] == '5'): #
            self.partida.pause()
        elif (dados[0] == '6'): #
            self.partida.inicio()
        elif (dados[0] == '7'): #
            print(dados[1])

    def isMovendo(self):
        return self.movendo


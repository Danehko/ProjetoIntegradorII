#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq
import sys
from threading import Thread

class Recebe_SS(Thread):
    def __init__(self,ip,port,partida):
        super().__init__()
        self.ip = ip
        self.port = port
        self.partida = partida
        self.movendo = 'nao'

    def run(self):
        self._recebe()

    def _recebe(self):
        context = zmq.Context()
        s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = sys.argv[1] if len(sys.argv) > 1 else str(self.ip) #String
        PORT = sys.argv[2] if len(sys.argv) > 2 else str(self.port) #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        s.connect(p)  # connect to the server
        s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
        for i in range(5):  # Five iterations
            dados = s.recv()  # receive a message
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


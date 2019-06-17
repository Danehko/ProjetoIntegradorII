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
        print(mensagem)
        dados = mensagem.split(':')
        if(dados[1] == '0'):
            print('Não Autenticado')
        elif(dados[1] == '1'): #
            print('Autenticado')
        elif(dados[1] == '2'): #
            self.partida.receberMapa(dados[2:len(dados)])
            self.partida.inicio()
            print('rato')
        elif (dados[1] == '3'): #
            self.movendo = dados[2]
        elif (dados[1] == '4'): #
            self.partida.receber(dados[2:len(dados)])
            print('gato')
        elif (dados[1] == '5'): #
            self.partida.pause()
        elif (dados[1] == '6'): #
            self.partida.inicio()
        elif (dados[1] == '7'): #
            print(dados[1])

    def isMovendo(self):
        return self.movendo


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, sys
from threading import Thread

class Recebe_SR(Thread):
    def __init__(self, partida):
        super().__init__()
        self._connect = False
        self.partida = partida
        self.confirmar = 0
        context = zmq.Context()
        self.s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.125" #String
        PORT = sys.argv[2] if len(sys.argv) > 2 else "50000" #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.connect(p)  # connect to the server
        self.s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
	self.id = ''
        self.coord = ''

    def run(self):
        self._recebe()
      
    def _recebe(self):
        while(True):
            dados = self.s.recv()  # receive a message
            self._tratando(dados.decode())

    def _tratando(self, mensagem):
        print(mensagem)
        dados = mensagem.split(':')
        if(dados[1] == '0'):
            tupla = dados[2].split(',')
            add = (int(tupla[0]),int(tupla[1]))
            self.partida._localizacaoRobo = []
            self.partida._localizacaoRobo.append(add)
        elif(dados[1] == '1'): # valida
            tupla = dados[2].split(',')
            add = (int(tupla[0]),int(tupla[1]))
            self.partida._localizacaoRobo = []
            self.partida._localizacaoRobo.append(add)
            if add in self.partida._listaDeTesouro:
                self.partida._listaDeTesouro.remove(add)
                print('Tesouro Encontrado')
                print(len(self.partida._listaDeTesouro))
        elif(dados[1] == '2'):
            self.id = dados[2]
            pos = dados[3].split(',')
            self.coord = (int(pos[0]),int(pos[1]))
            self._connect = True
            self.partida._localizacaoRobo.append(self.coord)

    def isConnect(self):
        return self._connect

    def isConfirmar(self):
        return self.confirmar


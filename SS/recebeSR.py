#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, sys
from threading import Thread

class Recebe_SR(Thread):
    def __init__(self, partida, comunica):
        super().__init__()
        self._connect = False
        self.partida = partida
        self.confirmar = 0
        context = zmq.Context()
        self.s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = "192.168.1.125" #String
        PORT = "50000" #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.connect(p)  # connect to the server
        self.s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
        self.id = ''
        self.coord = ''
        self.comunica = comunica

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
            self.coord  = (int(tupla[0]),int(tupla[1]))
            self.comunica.try_move(self.coord )

        elif(dados[1] == '1'): # valida
            dados = mensagem.split(':')
            tupla = dados[2].split(',')
            self.coord  = (int(tupla[0]),int(tupla[1]))
            print('kiko')
            print(self.partida._listaDeTesouro)
            lista = []
            lista.append(int(tupla[0]))
            lista.append(int(tupla[1]))
            print(lista)
            if lista  in self.partida._listaDeTesouro:
                print('Tesouro Encontrado')
                self.comunica.get_flag(self.coord)
        elif(dados[1] == '2'):
            self.id = dados[2]
            pos = dados[3].split(',')
            self.coord = (int(pos[0]),int(pos[1]))
            self._connect = True

    def isConnect(self):
        return self._connect

    def isConfirmar(self):
        return self.confirmar


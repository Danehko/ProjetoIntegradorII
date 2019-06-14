#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, sys
from threading import Thread

class Recebe_SR(Thread):
    def __init__(self,ip,port,partida):
        super().__init__()
        self.ip = ip
        self.port = port
        self._connect = False
        self.partida = partida

    def run(self):
        self._recebe()
      
    def _recebe(self):
        context = zmq.Context()
        s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = sys.argv[1] if len(sys.argv) > 1 else self.ip #String
        PORT = sys.argv[2] if len(sys.argv) > 2 else self.porta #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        s.connect(p)  # connect to the server
        s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
        dados = s.recv()  # receive a message
        self._tratando(dados)

    def _tratando(self, mensagem):
        dados = mensagem[0]
        dados = dados.split(':')
        if(dados[0] == '0'):
            tupla = (int(dados[1]),int(dados[2]))
            self.partida._localizacaoRobo = []
            self.partida._localizacaoRobo.append(tupla)
        elif(dados[0] == '1'):
            tupla = (int(dados[1]),int(dados[2]))
            self.partida._localizacaoRobo = []
            self.partida._localizacaoRobo.append(tupla)
            if tupla in self.partida._listaDeTesouro:
                self.partida._listaDeTesouro.remove(tupla)
        elif(dados[0] == '2'):
            id = dados[1]
            pos = dados[2].split(',')
            coord = (int(pos[0]),int(pos[1]))
            self._connect = True
            self.partida._localizacaoRobo.append(coord)

    def isConnect(self):
        return self._connect
                        
'''    
0:posx:posy
1:posx:posy

2:id:0,0



0:Enviar atualização

1:Validar caça

2:
'''




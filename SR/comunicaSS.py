#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, time

class Comunica_SS:
    def __init__(self):
        context = zmq.Context()
        self.s = context.socket(zmq.PUB)  # create a publisher socket
        HOST = "*"
        PORT = "50000"
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.bind(p)  # bind socket to the address

    def conectar(self, nome, posicao):
        msg = '2:' + nome + ':' + str(posicao[0]) + ',' + str(posicao[1])
        self.envia(msg)
        
    def atualizarPos(self,posicao):
        msg = '0:' + str(posicao[0]) + ',' + str(posicao[1])
        self.envia(msg)
        
    def validarTesouro(self,posicao):
        msg = '1:' + str(posicao[0]) + ',' + str(posicao[1])
        self.envia(msg)

    def envia(self, msg):
        print(msg)
        time.sleep(1)
        self.s.send(msg.encode())


'''
 '''


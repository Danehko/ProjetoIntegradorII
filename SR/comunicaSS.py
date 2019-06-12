#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq

class Comunica_SS:
    def __init__(self, porta):
        self.port = porta
        
    def conectar(self, nome, posicao):
        msg = '2:' + nome + ':' + posicao[0] + ':' + posicao[1]
        
    def atualizarPos(self,posicao):
        msg = '0:' + posicao[0] + ',' + posicao[1]

        
    def validarTesouro(self,posicao):
        msg = '1:' + posicao[0] + ',' + posicao[1]

    def envia(self, msg):
        context = zmq.Context()
        s = context.socket(zmq.PUB)  # create a publisher socket

        HOST = "*"
        PORT = self.port #String

        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        s.bind(p)  # bind socket to the address

        s.send(msg.encode())


'''
 '''


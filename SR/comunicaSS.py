#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq

class Comunica_SS:
    def __init__(self, ip, porta):
        self.ip = ip
        self.port = porta
        
    def conectar(self, nome, posicao):
        msg = '2:' + nome + ':' + str(posicao[0]) + ':' + str(posicao[1])
        self.envia(msg)
        
    def atualizarPos(self,posicao):
        msg = '0:' + str(posicao[0]) + ',' + str(posicao[1])
        self.envia(msg)
        
    def validarTesouro(self,posicao):
        msg = '1:' + str(posicao[0]) + ',' + str(posicao[1])
        self.envia(msg)

    def envia(self, msg):
        context = zmq.Context()
        s = context.socket(zmq.PUB)  # create a publisher socket

        HOST = str(self.ip)
        PORT = str(self.port) #String

        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        s.bind(p)  # bind socket to the address

        s.send(msg.encode())


'''
 '''


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, sys

class Recebe_SS:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
      
    def _recebe(self):
        context = zmq.Context()
        s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = sys.argv[1] if len(sys.argv) > 1 else self.ip #String
        PORT = sys.argv[2] if len(sys.argv) > 2 else self.porta #String
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
        if(dados[0] == '0'): #

        elif(dados[0] == '1'): #

        elif(dados[0] == '2'): #

        elif (dados[0] == '3'): #

        elif (dados[0] == '4'): #

        elif (dados[0] == '5'): #

        elif (dados[0] == '6'): #

        elif (dados[0] == '7'): #


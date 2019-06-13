#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq

class Comunica_SR:

    def __init__(self, ipSR, portaSR):
        self.ipSR = ipSR
        self.portSR = portaSR

    def naoAutenticar(self):
        msg = '0:NOK'
        self.envia(msg)

    def autenticar(self):
        msg = '1:OK'
        self.envia(msg)

    def iniciarPartida(self,msgInicio): # Modo de uso,numero de caças, numero de competidores + cor do Robô, numero de caças, Localização das caças
        msg = '2:' + msgInicio
        self.envia(msg)

    def movimentarManual(self, direcao):
        msg = '3:' + direcao
        self.envia(msg)

    def receberAtualização(self,atualizacao):  # numero de caça + localização das caça, numero de competidores + localização de competidores
        msg = '4:' + atualizacao
        self.envia(msg)

    def pausarContinuar(self):
        msg = '5:pausar'
        self.envia(msg)

    def terminarPartida(self):
        msg = '6:Partida Encerrada'
        self.envia(msg)

    def declararVencedor(self, vencedor):
        msg = '7:' + vencedor
        self.envia(msg)

    def envia(self,msg):
        context = zmq.Context()
        s = context.socket(zmq.PUB)  # create a publisher socket

        HOST = "*"
        PORT = "50009"

        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        s.bind(p)  # bind socket to the address

        s.send(msg.encode())

'''
- Autentiticar	        SS	SR	Identificação do SS + "|" + mensagem "autenticado"
- Pausar/continuar	    SS	SR	mensagem de pausa ou continua
- Iniciar partida	    SS	SR	
- Movimentar manual	    SS	SR	Direção .
- Receber atualização	SS	SR	
- Terminar partida	    SS	SR	mensagem de fim de jogo
- Declarar Vencedor	    SS	SR	Vencedor
'''





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zmq, time

class Comunica_SR:
    def __init__(self):
        context = zmq.Context()
        self.s = context.socket(zmq.PUB)  # create a publisher socket
        HOST = "192.168.1.142"
        self.ip = HOST
        PORT = "60000"
        self.porta = PORT
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.bind(p)  # bind socket to the address

    def naoAutenticar(self):
        msg = ':0:NOK'
        self.envia(msg)

    def autenticar(self):
        msg = ':1:OK'
        self.envia(msg)

    def iniciarPartida(self,msgInicio): # Modo de uso,numero de caças, numero de competidores + cor do Robô, numero de caças, Localização das caças
        msg = ':2:' + msgInicio
        self.envia(msg)

    def movimentarManual(self, direcao):
        msg = ':3:' + direcao
        self.envia(msg)

    def receberAtualização(self,atualizacao):  # numero de caça + localização das caça, numero de competidores + localização de competidores
        msg = ':4:' + atualizacao
        self.envia(msg)

    def pausarContinuar(self):
        msg = ':5:pausar'
        self.envia(msg)

    def terminarPartida(self):
        msg = ':6:Partida Encerrada'
        self.envia(msg)

    def declararVencedor(self, vencedor):
        msg = ':7:vencedor'
        self.envia(msg)

    def confirmarTesouro(self):
        msg = ':8'
        self.envia(msg)

    def naoConfirmarTesouro(self):
        msg = ':9'
        self.envia(msg)

    def envia(self,msg):
        time.sleep(2)
        msg = str("TIME ")+msg
        self.s.send(msg.encode())


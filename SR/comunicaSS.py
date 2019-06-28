import zmq
import time

class Comunica_SS:
    def __init__(self):
        context = zmq.Context()
        self.s = context.socket(zmq.PUB)  # create a publisher socket
        HOST = "192.168.1.125"
        PORT = "50000"
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.bind(p)  # bind socket to the address

    def conectar(self, nome, posx, posy):
        msg = ':2:' + nome + ':' + str(posx) + ',' + str(posy)
        self.envia(msg)
        
    def atualizar(self, posx, posy):
        msg = ':0:' + str(posx) + ',' + str(posy)
        self.envia(msg)
        
    def validar(self, posx, posy):
        msg = ':1:' + str(posx) + ',' + str(posy)
        self.envia(msg)

    def envia(self, msg):
        time.sleep(2)
        msg = str("STATUS ")+msg
        self.s.send(msg.encode())




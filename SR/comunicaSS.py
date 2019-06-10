import socket

class Comunica_SS:
    def __init__(self, ipSS, portaSS):
        self.ipSS = ipSS
        self.portSS = portaSS
        self.saida = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def conectar(self, nome, posx, posy):
        msg = '2:' + nome + ':' + posx + ':' + posy
        msg = msg.encode()
        self.saida.sendto(msg, (self.ipSS, self.portSS))
        
    def atualizarPos(self,posicao):
        msg = '0:' + posicao[0] + ',' + posicao[1]
        msg = msg.encode()
        self.saida.sendto(msg, (self.ipSS, self.portSS))
        
    def validarTesouro(self,posicao):
        msg = '1:' + posicao[0] + ',' + posicao[1]
        msg = msg.encode()
        self.saida.sendto(msg, (self.ipSS, self.portSS))

import socket

class Comunica_SR:

    def __init__(self, ipSR, portaSR, partida):
        self.ipSR = ipSR
        self.portSR = portaSR
        self.saida = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.partida = partida    

    def autenticar(self):
        msg = 'OK'
        msg = msg.encode()
        self.saida.sendto(msg, (self.ipSR, self.portSR))
        
    def naoAutenticar(self):
        msg = 'NOK'
        msg = msg.encode()
        self.saida.sendto(msg, (self.ipSR, self.portSR))
        
    def movimentarManual(self, direcao):
        msg = direcao.encode()
        self.saida.sendto(msg, (self.ipSR, self.portSR))         
'''
- Autentiticar	SS	SR	Identificação do SS + "|" + mensagem "autenticado"
Receber atualização	SS	SR	numero de caça + localização das caça, numero de competidores + localização de competidores
- Movimentar manual	SS	SR	Direção .
Iniciar partida	SS	SR	Modo de uso,numero de caças, numero de competidores + cor do Robô, numero de caças, Localização das caças
Pausar/continuar	SS	SR	mensagem de pausa ou continua
Terminar partida	SS	SR	mensagem de fim de jogo
Declarar Vencedor	SS	SR	Vencedor
self.saida.sendto(msg, (self.ipSS, self.portSS))
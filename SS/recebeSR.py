import socket
from threading import Thread

class Recebe_SR (Thread):

    def __init__(self, ipSR, portaSR):
        super().__init__()
        self.ip = "0.0.0.0"
        self.port = 6000
        self.ipSR = ipSR
        self.portSR = portaSR
        self._conectar()
   
    def _conectar(self):
        self.entrada = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.entrada.bind((self.ip,self.port))
        self.sr, self.sr_addres = self.entrada.accept()
      
    def _recebe(self):
        self.laco = True
        while(self.laco):
            try:
                mensagem = self.sr.recv(1024).decode()
                self.tratando(mensagem)
            except Exception as e:
                print(e)
               
    def run(self):
        self.recebe()
               
    def _tratando(self, mensagem):
        dados = mensagem[0]
        dados = dados.split(':')
        if(dados[0] == '0'):
            tupla = (int(dados[1]),int(dados[2]))
        elif(dados[0] == '1'):
            tupla = (int(dados[1]),int(dados[2]))
        elif(dados[0] == '2'):
            id = dados[1]
            pos = dados[2].split(',')
            coord = (int(pos[0]),int(pos[1]))   
                        
'''    
0:posx:posy
1:posx:posy

2:id:0,0



0:Enviar atualização

1:Validar caça

2:
'''
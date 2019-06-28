import zmq
from threading import Thread

class Recebe_SS(Thread):
    def __init__(self,partida):
        super().__init__()
        context = zmq.Context()
        self.s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = "192.168.1.142" #String
        PORT = "60000" #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.connect(p)  # connect to the server
        self.s.setsockopt(zmq.SUBSCRIBE, b"STATUS")  # subscribe to TIME messages
        self.partida = partida
        self.movendo = 'nao'
        self.continua = False
        
    def run(self):
        self.recebe()

    def recebe(self):
        while(True):
        	self.tratando(self.s.recv().decode())
               
    def tratando(self, mensagem):
        print(mensagem)
        dados = mensagem.split(':')
        if(dados[1] == '0'):
            print('Não Autenticado')
        elif(dados[1] == '1'):
            print('Autenticado')
        elif(dados[1] == '2'):
            nn = dados[2:len(dados)]
            nm = ':'
            mensg = nm.join(nn)
            self.partida.receber(mensg)
            self.partida.inicio()
        elif (dados[1] == '3'):
            self.movendo = dados[2]
            print(self.movendo)
        elif (dados[1] == '4'):
            nn = dados[2:len(dados)]
            nm = ':'
            mensg = nm.join(nn)
            self.partida.receber(mensg)
        elif (dados[1] == '5'):
            self.partida.pause()
        elif (dados[1] == '6'):
            self.partida.inicio()
        elif (dados[1] == '7'):
            print(dados[1])
        elif (dados[1] == '8'):
            print('Tesouro confirmado')
            self.continua = True
        elif (dados[1] == '9'):
            print('Tesouro não confirmado')
            self.continua = True

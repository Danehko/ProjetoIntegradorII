import zmq
from threading import Thread

class Recebe_SR(Thread):
    def __init__(self, partida, comunica):
        super().__init__()
        context = zmq.Context()
        self.s = context.socket(zmq.SUB)  # create a subscriber socket
        HOST = "192.168.1.125" #String
        PORT = "50000" #String
        p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
        self.s.connect(p)  # connect to the server
        self.s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME messages
        self.comunica = comunica
        self.partida = partida
        self.connect = False
        self.id = ''
        self.posx = 0
        self.posy = 0

    def run(self):
        self._recebe()

    def _recebe(self):
        while(True):
            self._tratando(self.s.recv().decode())

    def _tratando(self, mensagem):
        print(mensagem)
        dados = mensagem.split(':')
        if(dados[1] == '0'):
            tupla = dados[2].split(',')
            self.posx = int(tupla[0])
            self.posy = int(tupla[1])
            self.comunica.try_move((self.posx,self.posy))
        elif(dados[1] == '1'): # valida
            tupla = dados[2].split(',')
            self.posx = int(tupla[0])
            self.posy = int(tupla[1])
            lista = ((self.posx,self.posy))
            print(lista)
            if lista in self.partida.listaDeTesouro: #verificar aqui
                print('Tesouro Encontrado')
                self.comunica.get_flag((self.posx,self.posy))
        elif(dados[1] == '2'):
            self.id = dados[2]
            tupla = dados[3].split(',')
            self.posx = int(tupla[0])
            self.posy = int(tupla[1])
            self.connect = True

    def isConnect(self):
        return self.connect


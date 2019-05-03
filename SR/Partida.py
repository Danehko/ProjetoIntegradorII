class Partida:
    _listaDeTesouro
    _localizacaoRobo
    def __init__(self):
        self._listaDeTesouro = []        # lista com a localização das caças
        self._localizacaoRobo = []       # lista com a localização dos robos
        self.pausa = 0                   # se pausa for igual a 1 o jogo é pausado
        self.inicio = 0                  # se inicio for igual 1 o jogo começou

    def pause(self):
        if(self.pausa==0):
            self.pausa = 1
        elif(self.pausa==1):
            self.pausa = 0

    def inicio(self):
        if (self.inicio == 0):
            self.inicio = 1
        elif (self.inicio == 1):
            self.inicio = 0

    def addTesouro(self, posx, posy):
        self._listaDeTesouro.append((posx,posy))

    def addLocRobo(self, posx, posy):
        self._localizacaoRobo.append((posx, posy))

    def removerTesouro(self, posx, posy):
        self._listaDeTesouro.remove((posx,posy))

    def removerRobo(self, posx, posy):
        self._localizacaoRobo.remove((posx,posy))
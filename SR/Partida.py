class Partida:
    def __init__(self):
        self.modoDeUso = 0
        self._listaDeTesouro = []        # lista com a localização das caças
        self._localizacaoRobo = []       # lista com a localização dos robos
        self.pausa = 0                   # se pausa for igual a 1 o jogo é pausado
        self.inicio = 0                 # se inicio for igual 1 o jogo começou
        self.tam = 7

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

    def atualizarMapa(self, tam, _listates, _listaloc, inicio, pausa):
        self._listaDeTesouro = _listates
        self._localizacaoRobo = _listaloc
        self.inicio = inicio
        self.pausa = pausa
        
    def informarMapa(self):
        retorno = str(len(self._listaDeTesouro))
        cont = 0
        while(cont != len(self._listaDeTesouro)):
            retorno = retorno + ':' + str(self._listaDeTesouro[cont][0]) + ',' + str(self._listaDeTesouro[cont][1])
            cont = cont + 1
        retorno = retorno + ':' + str(len(self._localizacaoRobo))
        cont = 0
        while(cont != len(self._localizacaoRobo)):
            retorno = retorno + ':' + str(self._localizacaoRobo[cont][0]) + ',' + str(self._localizacaoRobo[cont][1])
            cont = cont + 1
        retorno = retorno + ':' + str(self.equipe1) + ':' + str(self.equipe2) + ':' + str(self.inicio)
        return retorno

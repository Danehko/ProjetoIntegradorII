class Partida:
    def __init__(self):
        self.modoDeUso = 0
        self._listaDeTesouro = []        # lista com a localização das caças
        self._localizacaoRobo = []       # lista com a localização dos robos
        self.pausa = 0                   # se pausa for igual a 1 o jogo é pausado
        self.status = 0                 # se inicio for igual 1 o jogo começou
        self.tam = 7

    def pause(self):
        if(self.pausa==0):
            self.pausa = 1
        elif(self.pausa==1):
            self.pausa = 0

    def inicio(self):
        if (self.status == 0):
            self.status = 1
        elif (self.status == 1):
            self.status = 0

    def atualizarMapa(self, tam, _listates, _listaloc, inicio, pausa):
        self._listaDeTesouro = _listates
        self._localizacaoRobo = _listaloc
        self.status = inicio
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
        return retorno

    def informar(self):
        retorno = str(self.modoDeUso) + ':'
        retorno = retorno + str(len(self._listaDeTesouro))
        cont = 0
        while(cont != len(self._listaDeTesouro)):
            retorno = retorno + ':' + str(self._listaDeTesouro[cont][0]) + ',' + str(self._listaDeTesouro[cont][1])
            cont = cont + 1
        retorno = retorno + ':' + str(len(self._localizacaoRobo))
        cont = 0
        while(cont != len(self._localizacaoRobo)):
            retorno = retorno + ':' + str(self._localizacaoRobo[cont][0]) + ',' + str(self._localizacaoRobo[cont][1])
            cont = cont + 1
        return retorno

    def receber(self,dados):
        self._listaDeTesouro = []
        self._localizacaoRobo = []
        dados = dados.split(':')
        contPos = int(dados[0])
        cont = 1
        while (contPos != (cont-1)):
            print(cont)
            pos = dados[cont]
            self._listaDeTesouro.append(pos)
            cont = cont + 1
        contRobo = int(dados[cont])
        cont = cont + 1
        while (cont != len(dados)):
            pos = dados[cont]
            self._localizacaoRobo.append(pos)
            cont = cont + 1

    def receberMapa(self,dados):
        self._listaDeTesouro = []
        self._localizacaoRobo = []
        dados = dados.split(':')
        self.modoDeUso = int(dados[0])
        contPos = int(dados[1])
        cont = 2
        while (contPos != (cont - 2)):
            pos = dados[cont]
            self._listaDeTesouro.append(pos)
            cont = cont + 1
        contRobo = int(dados[cont])
        cont = cont + 1
        while (cont != len(dados)):
            pos = dados[cont]
            self._localizacaoRobo.append(pos)
            cont = cont + 1

    def isInicio(self):
        return self.status

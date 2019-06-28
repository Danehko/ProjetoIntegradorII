class Partida:
    def __init__(self):
        self.modoDeJogo = 0
        self.listaDeTesouro = []        # lista com a localização das caças
        self.localizacaoRobo = []       # lista com a localização dos robos
        self.pausa = 0                   # se pausa for igual a 1 o jogo é pausado
        self.partidaIniciada = 0                 # se inicio for igual 1 o jogo começou

    def zerar(self):
        self.listaDeTesouro = []      
        self.pausa = 0                   
        self.status = 0 

    def pause(self):
        if (self.pausa == 0):
            self.pausa = 1
        elif (self.pausa == 1):
            self.pausa = 0

    def inicio(self):
        if (self.partidaIniciada == 0):
            self.partidaIniciada = 1
        elif (self.partidaIniciada == 1):
            self.partidaIniciada = 0

    def informar(self):
        retorno = str(self.modoDeJogo) + ':'
        retorno = retorno + str(len(self.listaDeTesouro))
        cont = 0
        while(cont != len(self.listaDeTesouro)):
            retorno = retorno + ':' + str(self.listaDeTesouro[cont][0]) + ',' + str(self.listaDeTesouro[cont][1])
            cont = cont + 1
        retorno = retorno + ':' + str(len(self.localizacaoRobo))
        cont = 0
        while(cont != len(self.localizacaoRobo)):
            retorno = retorno + ':' + str(self.localizacaoRobo[cont][0]) + ',' + str(self.localizacaoRobo[cont][1])
            cont = cont + 1
        return retorno

    def receber(self,dados):
        dados = dados.split(':')
        self.modoDeJogo = int(dados[0])
        contPos = int(dados[1])
        cont = 2
        self.listaDeTesouro = []
        while (contPos != (cont - 2)):
            pos = dados[cont]
            pos = pos.split(',')
            self.listaDeTesouro.append((int(pos[0]),int(pos[1])))
            cont = cont + 1
        cont = cont + 1
        self.localizacaoRobo = []
        while (cont != len(dados)):
            pos = dados[cont]
            pos = pos.split(',')
            self.localizacaoRobo.append((int(pos[0]),int(pos[1])))
            cont = cont + 1

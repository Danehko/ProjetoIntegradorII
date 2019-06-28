import random

from recebeSR import *
from Partida import *
from comunicaSR import *

print('Sistema Supervisorio - Iniciado')
print('Bem vindo')

partida = Partida()
envia = Comunica_SR()
recebe = Recebe_SR(partida)
recebe.start()

while(not recebe.isConnect()):
    pass
envia.autenticar()

condicao = True
while(condicao):
    aux = input('Digite 1 para Criar Partida \nDigite 2 para sair\n')
    if(aux == '1'):
        tesouro = int(input('Digite o numero de Tesouros:\n'))
        tipo = int(input('Voce deseja sortear os tessouros? digite (1) ou digite (2) para informar a localização dos tessouros?'))
        if(tipo==1):
            contador = 0
            while (tesouro != contador):
                x = random.randrange(7)
                y = random.randrange(7)
                if (((x, y) in partida._listaDeTesouro) == False):
                    partida._listaDeTesouro.append((x, y))
                    contador = contador + 1
        elif(tipo==2):
            contador = 0
            while (tesouro != contador):
                print('Digite a posicao do tesouro ' + str(contador + 1) + ' de ' + str(tesouro))
                x = int(input('Por favor insira a coordenada x:'))
                y = int(input('Por favor insira a coordenada y:'))
                if (((x, y) in partida._listaDeTesouro) == False):
                    partida._listaDeTesouro.append((x, y))
                    contador = contador + 1
                else:
                    print('Tesouro ja adicionado')

        atualizacao = partida.informarMapa()
        envia.receberAtualização(atualizacao)
        condicao2 = True
        adonis = int(input('Digite 1 para modo manual e 2 para modo autonomo'))
        while(condicao2):
            resp = int(input('Digite 1 para iniciar a partida '))
            if(resp == 1):
                condicao2 = False
        if(adonis==1):
            partida.modoDeUso = 1
            inicio = partida.informar()
            envia.iniciarPartida(inicio)
            partida.inicio()
            while(partida.isInicio()==1):
                print('Tesouro')
                cont0 = 0
                while(cont0 != len(partida._listaDeTesouro)):
                        auxiliar = partida._listaDeTesouro[cont0]
                        print('Localizada  em ' + str(auxiliar[0]) + ',' + str(auxiliar[1]) )
                        cont0 = cont0 + 1
                print('Modo Manual')
                print('1 - Frente')
                print('2 - Retornar')
                print('3 - Direita')
                print('4 - Esquerda')
                print('5 - Validar Tesouro')
                msg = int(input('Insira o número da opção desejada'))
                resp = ''
                if(msg == 1):
                    resp = 'Frente'
                    envia.movimentarManual(resp)
                elif(msg == 2):
                    resp = 'Retornar'
                    envia.movimentarManual(resp)
                elif(msg == 3):
                    resp = 'Direita'
                    envia.movimentarManual(resp)
                elif(msg == 4):
                    resp = 'Esquerda'
                    envia.movimentarManual(resp)
                elif(msg == 5):
                    cont1 = 0
                    print('Lista de Tesouros')
                    while(cont1 != len(partida._listaDeTesouro)):
                        auxiliar = partida._listaDeTesouro[cont1]
                        print(str((cont1 + 1)) + ' - localizada  em ' + str(auxiliar[0]) + ',' + str(auxiliar[1]) )
                        cont1 = cont1 + 1
                    remover = int(input('insira o numero da caça que deseja ser validado'))
                    remover = remover - 1
                    if(remover < len(partida._listaDeTesouro)):
                        lixo = partida._listaDeTesouro.pop(remover)
                        if(len(partida._listaDeTesouro)==0):
                            partida.inicio()
                            partida.zerar()
                    else:
                        print('Tesouro inexistente')
        elif(adonis==2):
            partida.modoDeUso = 2
            inicio = partida.informar()
            envia.iniciarPartida(inicio)
            partida.inicio()
            while(partida.isInicio()==1):
                atualizacao = partida.informarMapa()
                if(len(partida._listaDeTesouro)!=0):
                    envia.receberAtualização(atualizacao)
                else:
                    adonis = 0
                    envia.terminarPartida()
                    partida.inicio()
    elif(aux == '2'):
       condicao = False
       recebe.join()



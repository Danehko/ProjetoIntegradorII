import random

from SS.recebeSR import *
from SR.Partida import *
from SS.comunicaSR import *

print('Sistema Supervisorio - Iniciado')
print('Bem vindo')

ip = input('Digite o ip do Sistema Supervisorio\n')
porta = int(input('Digite a porta de recepcao do Sistema Supervisorio:\n'))

ipSR = input('Digite o ip do Robo:\n')
portaSR = int(input('Digite a porta de recepcao do Robo:\n'))

#ipSA = input('Digite o ip do Sistema Arbitrario:\n')
#portaSA = int(input('Digite a porta de recepcao do Sistema Arbitrario:\n'))

partida = Partida()
recebe = Recebe_SR(ip,porta,partida)
envia = Comunica_SR(ipSR,portaSR)

recebe.start()

while(not recebe.isConnect()):
    pass
envia.autenticar()

condicao = True
while(condicao):
    aux = input('Digite 1 para Criar Partida \nDigite 2 para sair\n')
    if(aux == '1'):
        tesouro = int(input('Digite o numero de Tesouros:\n'))
        tipo = int(input('Voce deseja sortear(digite 1) ou escolher(digite 2) aonde ficaram os tessouros?'))
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
                print('Digite a posicao do tesouro' + str(contador + 1) + ' de ' + str(tesouro))
                x = int(input('Por favor insira a coordenada x:'))
                y = int(input('Por favor insira a coordenada y:'))
                if (((x, y) in partida._listaDeTesouro) == False):
                    partida._listaDeTesouro.append((x, y))
                    contador = contador + 1
                else:
                    print('Tesouro ja adicionado')

        condicao2 = True
        adonis = int(input('Digite 1 para modo manual e 2 para modo autonomo'))
        if(adonis==1):
            partida.modoDeUso = 1
        elif():
            partida.modoDeUso = 2
        atualizacao = partida.informarMapa()
        envia.receberAtualização(atualizacao)
        while(condicao2):
            resp = int(input('Digite 1 para iniciar a partida '))
            if(resp == 1):
                condicao2 = False
        inicio = partida.informar()
        partida.inicio()
        envia.iniciarPartida()
        if(adonis==1):
            while(partida.isInicio()==1):
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
                    print('Funcao não implementa - SA')
        elif(adonis==2):
            while(partida.isInicio()==1):
                atualizacao = partida.informarMapa()
                envia.receberAtualização(atualizacao)


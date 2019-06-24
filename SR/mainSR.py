#!/usr/bin/env python3
from robo import *
from recebeSS import *
from comunicaSS import *
from Partida import *
import sys

argumentos = sys.argv[0:] 

#argv1=nome
#argv2=posx
#argv3=posy
#argv4=orientação

#print('Robo - Iniciado')
#print('Bem vindo')
#nome = input('Digite o nome do Robo:\n')
nome = argumentos[1]
#print('Lembrando que o mapa do jogo e quadrado (7x7), portanto e somente aceito 0-6')
#print('Por favor insira a localizacao do Robo')
#posx = int(input('Eixo x:'))
#posy = int(input('Eixo y:'))
#orien = input('Digite a orientacao do Robo \n (N) - Norte \n (S) - Sul \n (L) - Leste \n (O) - Oeste \n' )
robot = Robo('outA', 'outD', 200, argumentos[2],argumentos[3],argumentos[4])

partida = Partida()
comunica = Comunica_SS()
recebe = Recebe_SS(partida)

recebe.start()
comunica.conectar(nome,robot.coordenadas.enviarCoordenadas())
while(True):
    while(partida.isInicio() == 0):
        pass
    while(partida.isInicio() == 1):
        while(partida.pausa== 1):
            pass
        if(partida.modoDeUso == 1):
            mover = recebe.isMovendo()
            print(mover)
            if(mover=='Frente'):
                robot.setFrente()
                print('indo pra frente')
                recebe.movendo = 'nao'
            elif(mover=='Retornar'):
                robot.setRetornar()
                print('indo pra tras')
                recebe.movendo = 'nao'
            elif(mover=='Esquerda'):
                robot.setEsquerda()
                print('indo pra esquerda')
                recebe.movendo = 'nao'
            elif(mover=='Direita'):
                robot.setDireita()
                print('indo pra direita')
                recebe.movendo = 'nao'
            elif(mover=='nao'):
                pass
        elif(partida.modoDeUso == 2):
            robot.auto(partida._listaDeTesouro)
            if(robot.enviar==1):
                comunica.atualizarPos(robot.coordenadas.enviarCoordenadas())
                robot.enviar = 0
            elif(robot.enviar==2):
                comunica.validarTesouro(robot.coordenadas.enviarCoordenadas())
                robot.enviar = 0


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

nome = argumentos[1]
robot = Robo('outA', 'outD', 200, int(argumentos[2]),int(argumentos[3]),argumentos[4])
partida = Partida()
comunica = Comunica_SS()
recebe = Recebe_SS(partida)
recebe.start()
posx, posy = robot.coordenadas.enviarCoordenadas()
comunica.conectar(nome, posx, posy)
while(True):
    while(partida.partidaIniciada == 0):
        pass
    while(partida.partidaIniciada == 1):
        while(partida.pausa== 1):
            if(recebe.continua==True):
                partida.pause()
        if(partida.modoDeJogo == 1):
            mover = recebe.movendo
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
        elif(partida.modoDeJogo == 2):
            if(len(partida.listaDeTesouro)>0):
                robot.auto(partida.listaDeTesouro)
                if(robot.enviar==1):
                    posx, posy = robot.coordenadas.enviarCoordenadas()
                    comunica.atualizar(posx, posy)
                    robot.enviar = 0
                elif(robot.enviar==2):
                    posx, posy = robot.coordenadas.enviarCoordenadas()
                    comunica.validar(posx, posy)
                    robot.enviar = 0
                    partida.pause


#!/usr/bin/env python3
from robo import *
from recebeSS import *
from comunicaSS import *

print('Robo - Iniciado')
print('Bem vindo')
versao = input('Se o SS ja foi implementado digite (True) caso contrario digite (False)\n')
nome = input('Digite o nome do Robo:\n')

print('Lembrando que o mapa do jogo e quadrado (7x7), portanto e somente aceito 0-6')
print('Por favor insira a localizacao do Robo')
posx = int(input('Eixo x:'))
posy = int(input('Eixo y:'))
orien = input('Digite a orientacao do Robo \n (N) - Norte \n (S) - Sul \n (L) - Leste \n (O) - Oeste \n' )
robot = Robo('outA', 'outD', 200 , posx, posy, orien)

if(versao == 'False'):
    modo = int(input('Digite 1 para modo munual ou 2 para modo autonomo\n'))
    if(modo==1):
        direcao = ''
        while (direcao != "exit"):
            direcao = input('Entre com a direcao que deseja movimentar o robo:\n (a) para frente.\n (b) para tras.\n (c) para esquerda.\n (d) para direita.\n')
            if direcao == 'a':
                robot.setFrente()
                print('indo pra frente')
            elif direcao == 'b':
                robot.setRetornar()
                print('indo pra tras')
            elif direcao == 'c':
                robot.setEsquerda()
                print('indo pra esquerda')
            elif direcao == 'd':
                robot.setDireita()
                print('indo pra direita')
    elif(modo==2):
        _loc = []
        opcao = int(input('Digite 1 para seguir somente um comando ou 2 para n\n'))
        if(opcao==1):
            print('Ir para')
            x=int(input('x:'))
            y=int(input('y:'))
            _loc.append((x,y))
            robot.auto(_loc)
        elif(opcao==2):
            seq = int(input('Digite o numero de repeticoes\n'))
            cont = 0
            while(seq!=cont):
                print('Movimento numero '+str(cont+1)+' de '+str(seq))
                x = int(input('Por favor insira a coordenada x:'))
                y = int(input('Por favor insira a coordenada y:'))
                _loc.append((x,y))
                cont = cont + 1
            robot.auto(_loc)


if(versao == 'True'):
    ip = input('Digite o ip do Robo:\n')
    porta = int(input('Digite a porta de conexao:\n'))
    ipSS = input('Digite o ip do Sistema Supervisor:\n')
    portaSS = int(input('Digite a porta de conexão do Sistema Supervisor:\n'))

    comunicaSS = Comunica_SS()
    comunicaSS.conectar(ip, porta)

    recebe = RecebeSS()
    recebe.start()
    #msg = ''
    #while(msg != 'Partida encerrada'):
    #    msg = recebeSS.start()


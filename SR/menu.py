#!/usr/bin/env python3
from robo import *

print('Bem vindo')
print('Lembrando que o mapa do jogo e quadrado (10x10), portanto e somente aceito 0-9')
print('Por favor insira a localizacao do Robo')
posx = int(input('Eixo x:'))
posy = int(input('Eixo y:'))
modo = int(input('Digite 1 para modo munual ou 2 para modo autonomo\n'))
direcao = ''
robot = Robo('outA', 'outD', 200,0,0,'N')

if(modo==1):
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

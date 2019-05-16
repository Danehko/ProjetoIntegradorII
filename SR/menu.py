#!/usr/bin/env python3
from robo import *

print('Bem vindo')
print('Lembrando aue o mapa do jogo é quadrado (10x10), portanto é somente aceito 0-9')
print('Por favor insira a localização do Robô')
posx = int(input('Eixo x:'))
posy = int(input('Eixo y:'))
modo = int(input('Digite 1 para modo munual ou dois para modo autonomo'))
if(modo==1):
	direcao = ''
	robot = Robo('outA', 'outD', 200,0,0,'N')

	while (direcao != "exit"):
		direcao = input('Entre com a direcao que deseja movimentar o robo:\n A para frente.\n B para tras.\n C para esquerda.\n D para direita.\n')

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
	opcao = int(input('Digite 1 para seguir somente um comando ou 2 para n'))
	if(opcao==1):
		print('Ir para')
		x=int(input('x:'))
		y=int(input('x:'))
		_loc.append((x,y))
	elif(opcao==2):
		seq = int(input('Digite o número de repetições'))
		cont = 0
		while(seq!=cont):
			print('Movimento numero '+str(cont)+' de '+str(seq))
			x = int(input('Por favor insira a coordenada x:'))
			y = int(input('Por favor insira a coordenada y:'))
			_loc.append((x,y))


#!/usr/bin/env python3
from robo import *


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


#!/usr/bin/env python3
from robo import *


direcao = input("Bem Vindo(a)! Entre com a direção que deseja movimentar o robô:\-A para frente.\-B para trás.\-C para esquerda.\-D para direita.")
robot = Robo()


while (direcao != "exit"):
	direcao = input("Entre com a direção que deseja movimentar o robô:\-A para frente.\-B para trás.\-C para esquerda.\-D para direita.")

	if direcao == 'a':
		robot.setManual("frente")
		print('indo pra frente')
	elif direcao == 'b':
		robot.setManual("retornar")
		print('indo pra trás')
	elif direcao == 'c':
		robot.setManual("esquerda")
		print('indo pra esquerda')
	elif direcao == 'd':
		robot.setManual("direita")
		print('indo pra direita')


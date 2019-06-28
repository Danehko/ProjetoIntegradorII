from recebeSR import *
from Partida import *
from comunicaSR import *
from Comunica_SA import *
import sys

argumentos = sys.argv[0:]

print('Sistema Supervisorio - Iniciado')
print('Bem vindo')

partida = Partida()
envia = Comunica_SR()
comunica = Comunica_SA('8888', argumentos[1], envia, partida)
recebe = Recebe_SR(partida, comunica)
recebe.start()

while(not recebe.isConnect()):
    pass
comunica.run()
comunica.login(recebe.id,(recebe.posx, recebe.posy))
envia.autenticar()
condicao = True
while(condicao):
    if((partida.partidaIniciada == 1) and (partida.modoDeJogo == 1)):
        while(partida.partidaIniciada==1):
            print('Tesouro')
            cont0 = 0
            while(cont0 != len(partida.listaDeTesouro)):
                auxiliar = partida.listaDeTesouro[cont0]
                print('Localizada  em ' + str(auxiliar[0]) + ',' + str(auxiliar[1]) )
                cont0 = cont0 + 1
            print('Modo Manual')
            print('1 - Frente')
            print('2 - Retornar')
            print('3 - Direita')
            print('4 - Esquerda')
            print('5 - Validar Tesouro')
            msg = int(input('Insira o número da opção desejada: \n'))
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
                while(cont1 != len(partida.listaDeTesouro)):
                    auxiliar = partida.listaDeTesouro[cont1]
                    print(str((cont1 + 1)) + ' - localizada  em ' + str(auxiliar[0]) + ',' + str(auxiliar[1]) )
                    cont1 = cont1 + 1
                remover = int(input('insira o numero da caça que deseja ser validado: \n'))
                remover = remover - 1
                if(remover < len(partida.listaDeTesouro)):
                    lixo = partida.listaDeTesouro.pop(remover)
                    comunica.get_flag(lixo)
                    if(len(partida.listaDeTesouro)==0):
                        partida.inicio()
                        partida.zerar()
                else:
                    print('Tesouro inexistente')
    elif(partida.partidaIniciada==1 and partida.modoDeJogo == 2):
        inicio = partida.informar()
        envia.iniciarPartida(inicio)
        while(partida.partidaIniciada == 1):
            atualizacao = partida.informarMapa()
            if(len(partida.listaDeTesouro)!=0):
                envia.receberAtualizacao(atualizacao)
            else:
                pass

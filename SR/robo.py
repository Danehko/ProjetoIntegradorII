#!/usr/bin/env pynthon3
from ev3dev.ev3 import *
from Coordenadas import *
from time import sleep

class Robo:

    def __init__(self,motorA,motorB,velocidade,posx,posy,ref):
        self.MAC = '1a2b3c4d5e6f'  # identificação unica do Robo
        self.coordenadas = Coordenadas(posx,posy,ref)
        self.modoDeJogo = 0  # mododeJogo igual a 0 para modo autonomo e 1 para modo manual
        self.velocidade = velocidade
        self.l = LargeMotor(motorA)
        self.r = LargeMotor(motorB)
        self.cl = ColorSensor()
        self.colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')

    def setVol(self):
        return self.velocidade

    def setFrente(self):
        self.cl.mode = 'COL-COLOR'
        if self.colors[self.cl.value()] == "green" or self.colors[self.cl.value()] == "yellow" or self.colors[
            self.cl.value()] == "blue":
            while self.colors[self.cl.value()] == "green" or self.colors[self.cl.value()] == "yellow" or \
                    self.colors[
                        self.cl.value()] == "blue":
                self.r.run_forever(speed_sp=self.velocidade)
                self.l.run_forever(speed_sp=self.velocidade)
            else:
                self.setParar()
                ## Colocar o resto do codico no else

        if self.colors[self.cl.value()] == "unknown":
            while self.colors[self.cl.value()] != "black":
                self.r.run_forever(speed_sp=self.velocidade)

        while self.colors[self.cl.value()] != "green":
            while self.colors[self.cl.value()] == "black":
                self.r.run_forever(speed_sp=self.velocidade / 2)
                self.l.run_forever(speed_sp=self.velocidade)

            while self.colors[self.cl.value()] == "white":
                self.r.run_forever(speed_sp=self.velocidade)
                self.l.run_forever(speed_sp=self.velocidade / 2)

            if self.colors[self.cl.value()] == "yellow":
                self.l.run_forever(speed_sp=self.velocidade)
                self.r.run_forever(speed_sp=self.velocidade)
                sleep(0.1)
                break

            if self.colors[self.cl.value()] == "blue":
                self.l.run_forever(speed_sp=self.velocidade)
                self.r.run_forever(speed_sp=self.velocidade)
                sleep(0.1)
                break

        else:
            self.l.run_forever(speed_sp=self.velocidade)
            self.r.run_forever(speed_sp=self.velocidade)
            sleep(0.1)

        self.setParar()

    def setEsquerda(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.r.run_forever(speed_sp=self.velocidade)
            self.l.run_forever(speed_sp=self.velocidade * 0)
        else:
            self.l.stop(stop_action="hold")

        while self.colors[self.cl.value()] == "black":
            self.r.run_forever(speed_sp=self.velocidade)

        while self.colors[self.cl.value()] != "black":
            self.r.run_forever(speed_sp=self.velocidade)

        else:
            self.r.run_forever(speed_sp=self.velocidade)

        # self.setParar()

        self.setFrente()

        #self.cl.mode = 'COL-COLOR'
        #while self.colors[self.cl.value()] != "black":
        #   self.l.run_forever(speed_sp=-self.velocidade / 2)
        #    self.r.run_forever(speed_sp=self.velocidade)

        #else:
            # sleep(0.1)
        #    self.setParar()

        # else:
        # sleep(0.1)
        # self.setParar()

        #self.setParar()

        #self.setFrente()

    def setDireita(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.l.run_forever(speed_sp=self.velocidade)
            self.r.run_forever(speed_sp=self.velocidade/2)
        else:
            self.r.stop(stop_action="hold")

        while self.colors[self.cl.value()] == "black":
            self.l.run_forever(speed_sp=self.velocidade)

        while self.colors[self.cl.value()] != "black":
            self.l.run_forever(speed_sp=self.velocidade)

        else:
            self.l.run_forever(speed_sp=self.velocidade)

        #self.setParar()

        self.setFrente()

    def setRetornar(self):
        self.cl.mode = 'COL-COLOR'
        while self.colors[self.cl.value()] == "green":
            self.l.run_forever(speed_sp=-self.velocidade)
        # self.r.run_forever(speed_sp=-self.velocidade/2)

        # sleep(0.1)
        # self.setParar()

        while self.colors[self.cl.value()] == "black":
            #			self.r.run_forever(speed_sp=self.velocidade)
            self.l.run_forever(speed_sp=-self.velocidade)

        while self.colors[self.cl.value()] != "black":
            # self.setParar()
            self.l.run_forever(speed_sp=-self.velocidade)

        self.setParar()
        self.setFrente()

    def setVelocidade(self, setV):
        self.velocidade = setV

    def setParar(self):
        self.r.stop(stop_action="hold")
        self.l.stop(stop_action="hold")

    def auto(self,_lista):
        while(len(_lista)!=0):
            print(len(_lista))
            x,y = _lista.pop(0)
            xablau = True
            aux1 = abs(self.coordenadas.posx - x)
            aux2 = abs(self.coordenadas.posy - y)
            if(aux1<aux2):
                while(xablau):
                    print(self.coordenadas.posx, self.coordenadas.posy)
                    if((self.coordenadas.posx == x) and (self.coordenadas.posy == y)):
                        xablau = False
                    elif(self.coordenadas.posx > x):
                        if(self.coordenadas.referencia == 'N'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posx < x):
                        if(self.coordenadas.referencia == 'N'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posy > y):
                        if(self.coordenadas.referencia == 'N'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posy < y):
                        if(self.coordenadas.referencia == 'N'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
            else:
                while(xablau):
                    print(self.coordenadas.posx, self.coordenadas.posy)
                    if((self.coordenadas.posx == x) and (self.coordenadas.posy == y)):
                        xablau = False
                    elif(self.coordenadas.posy > y):
                        if(self.coordenadas.referencia == 'N'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posy < y):
                        if(self.coordenadas.referencia == 'N'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posx > x):
                        if(self.coordenadas.referencia == 'N'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                    elif(self.coordenadas.posx < x):
                        if(self.coordenadas.referencia == 'N'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direita')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'S'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'L'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                            print(self.coordenadas.enviarCoordenadas())
                        elif(self.coordenadas.referencia == 'O'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                            print(self.coordenadas.enviarCoordenadas())


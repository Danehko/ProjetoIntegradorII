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
        self.colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red' 'white', 'brown')

    def auto(self,_lista):
        while(len(_lista)!=0):
            x,y = _lista.pop(0)
            aux1 = self.coordenadas.posx - x
            if(aux1<0):
                aux1= aux1 * (-1)
            aux2 = self.coordenadas.posy - y
            if(aux2<0):
                aux2= aux2 * (-1)
            if(aux1<aux2):
                while((self.coordenadas.posx!=x)and(self.coordenadas.posy!=y)):
                    if(self.coordenadas.posx > x):
                        if (self.referencia == 'N'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'S'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'L'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'O'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                    elif(self.coordenadas.posx < x):
                        if (self.referencia == 'N'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'S'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'L'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'O'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                    elif (self.coordenadas.posy > y):
                        if (self.referencia == 'N'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'S'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'L'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'O'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                    elif (self.coordenadas.posy < y):
                        if (self.referencia == 'N'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'S'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'L'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'O'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
            else:
                while ((self.coordenadas.posx != x) and (self.coordenadas.posy != y)):
                    if (self.coordenadas.posy > y):
                        if (self.referencia == 'N'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'S'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'L'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'O'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                    elif (self.coordenadas.posy < y):
                        if (self.referencia == 'N'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'S'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'L'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'O'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                    elif (self.coordenadas.posx < x):
                        if (self.referencia == 'N'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'S'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'L'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
                        elif (self.referencia == 'O'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                    elif (self.coordenadas.posx > x):
                        if (self.referencia == 'N'):
                            self.setRetornar()
                            self.coordenadas.trocandoPos('retornar')
                        elif (self.referencia == 'S'):
                            self.setFrente()
                            self.coordenadas.trocandoPos('frente')
                        elif (self.referencia == 'L'):
                            self.setEsquerda()
                            self.coordenadas.trocandoPos('esquerda')
                        elif (self.referencia == 'O'):
                            self.setDireita()
                            self.coordenadas.trocandoPos('direits')
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
            self.r.run_forever(speed_sp=self.velocidade / 2)
        else:
            self.r.stop(stop_action="hold")

        while self.colors[self.cl.value()] == "black":
            self.l.run_forever(speed_sp=self.velocidade)

        while self.colors[self.cl.value()] != "black":
            self.l.run_forever(speed_sp=self.velocidade)

        else:
            self.l.run_forever(speed_sp=self.velocidade)

        # self.setParar()

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

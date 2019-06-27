class Coordenadas:
    def __init__(self,posx,posy,ref):
        self.posx = posx
        self.posy = posy
        self.referencia = ref
        self.proximoRef = 'SR'
        self.habilitarTroca = 0

    def enviarCoordenadas(self):
        return (self.posx,self.posy)

    def trocarPosicao(self, x, y):
        if(self.habilitarTroca == 1):
            self.posx = x
            self.posy = y
            self.referencia = self.proximoRef
            self.proximoRef = 'SR'
            self.habilitarTroca = 0

    def trocandoPos(self, dir):
        if(dir=='frente'):
            if(self.referencia=='N'):
                self.proximoRef = self.referencia
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
            elif(self.referencia=='S'):
                self.proximoRef = self.referencia
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.referencia == 'L'):
                self.proximoRef = self.referencia
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.referencia == 'O'):
                self.proximoRef = self.referencia
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
        elif(dir=='retornar'):
            if (self.referencia == 'N'):
                self.proximoRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.referencia == 'S'):
                self.proximoRef = 'N'
                self.habilitarTroca = 1                
                return(self.posx, (self.posy + 1))
            elif (self.referencia == 'L'):
                self.proximoRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.referencia == 'O'):
                self.proximoRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
        elif (dir == 'direita'):
            if (self.referencia == 'N'):
                self.proximoRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.referencia == 'S'):
                self.proximoRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.referencia == 'L'):
                self.proximoRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))
            elif (self.referencia == 'O'):
                self.proximoRef = 'N'
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
        elif (dir == 'esquerda'):
            if (self.referencia == 'N'):
                self.proximoRef = 'O'
                self.habilitarTroca = 1
                return((self.posx - 1), self.posy)
            elif (self.referencia == 'S'):
                self.proximoRef = 'L'
                self.habilitarTroca = 1
                return((self.posx + 1), self.posy)
            elif (self.referencia == 'L'):
                self.proximoRef = 'N'
                self.habilitarTroca = 1
                return(self.posx, (self.posy + 1))
            elif (self.referencia == 'O'):
                self.proximoRef = 'S'
                self.habilitarTroca = 1
                return(self.posx, (self.posy - 1))

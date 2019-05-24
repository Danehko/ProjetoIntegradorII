print('Sistema Supervisorio - Iniciado')
print('Bem vindo')
#versao = input('Se o SA ja foi implementado digite (True) caso contrario digite (False)\n')
versao = False

ip = input('Digite o ip do Sistema Supervisorio\n')
porta = int(input('Digite a porta de conexão:\n'))

ipSA = input('Digite o ip do Sistema Arbitrario:\n')
portaSA = int(input('Digite a porta de conexão do Sistema Arbitrario:\n'))

#recebeSR.start()


ex = Supervisor(ip, porta, ipSA, portaSA)
ex.conectarSupervisor()
print('Esperando Dados')
msg = ''
ex.recebendo()
ex.ajustarRobo()
while(msg != 'Partida encerrada'):
    teste = ex.recebendo()
    if(teste=='exit'):
        msg = 'Partida encerrada'
    else:
        msg = ex.mover()
ex.encerrar()
print('Partida encerrada')


def ajuda(com):
    help(comando)


#Programa Principal

comando = ''
while True:
    comando = str(input('Digite o comando: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
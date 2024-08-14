def leiaInt(msg):
    while True:
        try:
            n =int(input(msg))
        except(TypeError, ValueError):
            print('\033[31mERRO!\033[m Digite um valor inteiro válido')
        except(KeyboardInterrupt):
            print('\033[031mEntrada  de dados interrompida pelo usuário\033[m')
            return 0
            continue
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except(TypeError, ValueError):
            print('\033[31mERRO!\033[m Digite um valor real válido')
        except(KeyboardInterrupt):
            print('\033[031mEntrada  de dados interrompida pelo usuário\033[m')
            return 0
            continue
        else:
            return n2

#Programa principal
        
n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número Real: ')

print(f'Você digitou o número inteiro {n}')
print(f'Você digitou o número real {n2}')



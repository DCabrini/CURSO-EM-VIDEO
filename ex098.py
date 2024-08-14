from time import sleep

def contador(inicio,fim,passo):
    print('=-'*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for n in range(inicio,fim+1,passo):
            print(n, end=' ', flush =True)
            sleep(0.5)
        print('Fim')
    else:
        for n in range(inicio,fim-1,(-1)*passo):
            print(n, end=' ', flush= True)
            sleep(0.5)
        print('Fim')
    if passo < 0:
        for n in range(inicio,fim-1,passo):
            print(n, end=' ', flush =True)
            sleep(0.5)
        print('Fim')     


contador(1, 10, 1)
contador(10, 0, 2)
print('~'*20)
print('Agora é sua vez de pesonalizar.')
inicio = int(input('Ínicio: '))
fim =int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
    
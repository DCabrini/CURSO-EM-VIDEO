from random import randint
from time import sleep



def sorteio(lista): 
     for i in range(0, 5):
        lista.append(randint(0, 10))

def somapar(valores):
    soma = 0
    for n in valores:
        if n %2 ==0:
            soma += n    
    print(soma)

lista = list()
sorteio(lista)
print(lista)
somapar(lista)

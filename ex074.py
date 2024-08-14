from random import randint

n1  = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)
n4 = randint(1,10)
tupla = (n1, n2, n3, n4)
print(f'Os números listados foram {tupla}')
print(f'O maior valor sorteado é {max(tupla)}')
print(f'O menor valor sorteado é {min(tupla)}')
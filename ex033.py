n1 = int(input('Digite o primieto valor: '))
n2 = int(input('Digite o segundo Valor: '))
n3 = int(input('Digite o segndo valor: '))
menor  = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor  = n3

# Verificando o maior  
maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'Maior = {maior}\nMenor = {menor}')
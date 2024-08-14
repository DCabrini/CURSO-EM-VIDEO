n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1, n2, n3, n4)
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O valor trêsa apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor três não foi digitado')
print('Os numeros para são:',end='')
for n in tupla:
    if n %2 ==0:
        print(n,end=' ')




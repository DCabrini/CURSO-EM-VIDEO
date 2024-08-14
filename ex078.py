lista = list()
maior = posmaior = menor= posmenor = 0
for n in range(0,5):
    lista.append(int(input(f'Digite um valor par a posição {n}:')))
    
    if n == 0:
        menor = maior = lista[n]
    else:
        if lista[n] > maior:
           maior = lista[n]
           posmaior = n
        if menor > lista[n]:
           menor = lista[n]
           posmenor = n

print(f'Você digitou os seguintes valores  {lista}')
print(f'O maior valor é {maior} e estão nas pocições', end =' ')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}', end='...')
print()
print(f'O menor valor é {menor} e está na posição', end=' ')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos}', end='...')

           
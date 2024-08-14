lista =  list()
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Qual o nome da pessoa? ')))
    temp.append(int(input('Qual o peso da pessoa? ')))
    if len(lista) == 0:
        maior = menor = temp[1]
        maiornome = menornome =temp[0]
    else:
        if temp[1] > maior:
            maior = temp[1]
            maiornome = temp[0]
        elif temp[1] < menor:
            menor = temp[1]
            menornome = temp[0]
    lista.append(temp[:])
    temp.clear()
    perg = ' '
    while perg not in 'NS':
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break
print(lista)
print(f'A pessoa mais pesada é {maiornome} com peso de {maior}')
print(f'A pessoa mais leve é {menornome} com peso de {menor}')

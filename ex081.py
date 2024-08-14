lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    per = ' '
    perg = str(input('Dseja continuar? [S/N]: ')).upper().strip()[0]
    while perg not in 'NS':
        perg = str(input('Desja continuar? [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break
lista.sort(reverse=True)
print(f'Vlaores digirado foram - {lista}')
print(f'Foram digitados o total de {cont} números')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 NÃO está na lista.')
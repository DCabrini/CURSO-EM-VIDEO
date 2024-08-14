lista = []
while True:
    n = (int(input(f'Digite um valor: ')))
    if n in lista:
        print('Valor Duplicado! Não irei adicionar')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso')
    perg = ' '
    perg = str(input('Desja continuar? [S/N]: ')).upper().strip()[0]
    while perg not in 'NS':
        perg = str(input('Desja continuar? [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break
print(f'Voce digitou os valores {lista}')
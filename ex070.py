total = cont = barato =  0
while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto em R$ '))
    total += preco
    if preco > 1000:
        cont += 1
    if cont == 1:
        barato == preco
    else:
        if preco < barato:
            nome = nome
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if perg == 'N':
        break
print(f'O Total gasto é R${total}')
print(f'{cont} custam mais de R$1000')
print(f'{nome} é o produto mais barato')
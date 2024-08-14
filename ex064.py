

perg = ''
soma = 0
cont = 0
while perg != 'N':
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor =  n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    perg = str(input('Deseja continuar [S/N]? ')).upper()
    
print(f'A média entre os {cont} valore é de {(soma)/cont}')
print(f'O maior valor digitado é {maior}\nO menor valor digitado é {menor}')
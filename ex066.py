n = int(input('Digite um valor inteiro: '))
cont  = soma = 0

while True:
    soma += n
    cont += 1
    print('-'*30)
    print('Digite 999 para parar.')
    print('-'*30)
    n = int(input('Digite um valor: '))
    if n == 999:
        break
print(f'Foram digitados {cont} valores\nA soma é de {soma}')
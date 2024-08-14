n1  = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opc = ''

while opc != '5':
    print('''Opções:
      [1] - Soma
      [2] - Multiplicação
      [3] - Maior
      [4] - Novos Números
      [5] - Sair do Programa''')
    opc = str(input('Digite e opção desejada: '))
    if opc == '1':
        res = n1 + n2
        print(f'soma é {res}')
    elif opc == '2':
        res = n1*n2
        print(f'Multiplicação é {res}')
    elif opc == '3':
        if n1 > n2:
            maior = n1
            menor  = n2
        else:
            maior = n2
            menor = n1
        print(f'O maior {maior}\nMenor é {menor}')
    elif opc== '4':
        n1  = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('Fim')

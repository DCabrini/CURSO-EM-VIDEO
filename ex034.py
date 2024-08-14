s = float(input('Digite o salário do funcionário R$'))

if s > 1250:
    print(f'Seu novo salário é {s*1.1}')
else:
    print(f'Seu novo salário é de {s*1.15}')
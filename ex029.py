v = float(input('Qual a velocidade do carro? '))

if v > 80:
    print(f'Carro acima da velocidade permitida!\nMulta a ser paga é de R${(v-80)*7}')
else:
    print('Velocidade permitida.\nBoa Viagem!')
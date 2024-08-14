d = float(input('Qual a distância (Km) da viagem? '))

if d > 200:
    print(f'O valor da passagem é de R${d*0.45}')
else:
    print(f'O valor da passagem é de R${d*0.50}')
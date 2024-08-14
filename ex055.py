maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Qual o peso da pessoa {i}: '))
    if i == 1:
        menor = maior = peso
    elif i > 1:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg\nO menor peso é {menor}kg')
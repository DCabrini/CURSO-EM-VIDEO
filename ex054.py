from datetime import date
ano = int(date.today().strftime('%Y'))

menor = 0
maior = 0
for i in range(1,8):
    p = int(input(f'Qual o ano de nascimento da pessoa {i}? '))
    if (ano - p )>= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade')
print(f'{menor} pessoas não menores de idade')
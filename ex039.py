from datetime import date

nasc = int(input('Qual o ano de nascimento? '))
hoje = int(date.today().strftime("%Y"))

if (hoje - nasc) < 18:
    print(f'Vai alistar em {hoje - nasc} anos')
elif (hoje - (nasc + 18)) == 0:
    print('Deve alistar esse ano.')
elif (hoje - nasc) > 18:
    print(f'Alistameno atrasado em {hoje - (nasc +18)} anos.')

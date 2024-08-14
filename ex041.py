from datetime import date
nasc = int(input('Qual a data de nascimento do atleta? '))
ano = int(date.today().strftime('%Y'))

if (ano - nasc) <=9:
    print(f'Atleta de {ano-nasc} anos\nCategoria: MIRIM')
elif 9 <(ano - nasc) <= 14:
    print(f'Atleta de {ano - nasc} anos\nCategoria: INFANTIL')
elif 14 < (ano - nasc) <= 19:
    print(f'Atleta de {ano - nasc} anos\nCategoria: JUNIOR')
elif 19 < (ano - nasc) <= 20:
    print(f'Atleta de {ano - nasc} anos\nCategoria: SÊNIOR')
elif (ano - nasc) > 20:
    print(f'Atleta de {ano - nasc} anos\nCategoria: MASTER')
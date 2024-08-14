peso = float(input('Qual o peso do paciente [Kg]: '))
altura = float(input('Digite a altura do pasciente [m]: '))
imc = peso/((altura)**2)

if imc < 18.5:
    print(f'IMC = {imc:.1f} - Abaixo do Peso')
elif 18.5 < imc <= 25:
    print(f'IMC = {imc:.1f} - Peso Ideal')
elif 25 < imc <= 30:
    print(f'IMC = {imc:.1f} - SOBREPESO')
elif 30 < imc <= 40:
    print(f'IMC = {imc:.1f} - OBESIDADE')
elif imc > 40:
    print(f'IMC = {imc:.1f} - Obesidade Mórbida')
r1 = float(input('Digite o valor da priemira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} formam um triangulo.')
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isósceles')
    elif r1 != r2 != r3:
        print('Triângulo Escaleno')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO formam um triangulo.')
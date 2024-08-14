n = int(input('Quer ver a tabuada de qual valor? '))
cont = 1

while True:
    while cont <=10:
        print(f'{cont:2} X {n} = {n*cont:2}')
        cont += 1
    n = int(input('Quer ver a tabuada de qual valor (valores negativos encerra o programa)? '))
    cont = 1
    if n < 0:
        break
print('Fim')

n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
if cont ==2:
    print(f'{n} é primo')
else:
    print(f'{n} NÃO é primo')
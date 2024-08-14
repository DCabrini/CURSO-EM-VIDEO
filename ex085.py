lista = [[], []]

for n in range(0, 7):
    numero = int(input(f'Digite o {n+1} número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
#lista.append(pares)
#lista.append(impares)
lista[0].sort()
lista[1].sort()
print(f'Os números pare digitado foram {lista[0]}')
print(f'Os números impares digitados foram {lista[1]}')

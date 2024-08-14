lista = list()

for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0:
        lista.append(valor)
        print('Valor adicionado no final da lista.')
    elif valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
            pos += 1

print(lista)
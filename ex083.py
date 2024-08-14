n = str(input('Digite sua expressão: '))
lista = list()
for i in range(0, len(n)):
    lista.append(n[i])
if lista.count('(') == lista.count(')'):
    print('Sua expressão é valida.')
else:
    print('Sua expressão está errada.')
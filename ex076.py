lista = ('Borracha', 1.50, 'Lápis', 1.00, 'Caneta', 3, 'Caderno', 25.00)

for mat in range(0, len(lista)):
        if mat % 2 ==0:
            print(f'{lista[mat]:.<30}',end=' ')
        else:
            print(f'{lista[mat]}')
    
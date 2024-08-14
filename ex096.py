def area(l, c):
    area = l*c
    print(f'A área de um terreno de {l} x {c} é de {area}m²')

print('Controle de Terrenos')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l,c)
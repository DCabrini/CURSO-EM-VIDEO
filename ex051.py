r  = int(input('Digite a razão da PA: '))
a1 = int(input('Digite o primeiro termo da PA: '))


for i in range(a1, ((a1+(10 - 1)*r)+r) ,r):
        print(f'{i}', end=" - ")
print('ACABOU')
        
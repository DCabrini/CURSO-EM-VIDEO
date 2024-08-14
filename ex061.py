p = int(input('Digite o primeiro termo da PA: '))
r  = int(input('Digite a razão da PA: '))
cont = 0
res = 0
per = 0
while cont < 10:
    res += r
    cont += 1
    print(f'{res}',end=" - ")

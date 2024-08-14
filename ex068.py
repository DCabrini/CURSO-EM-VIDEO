from random import randint

pn = randint(0, 11)
gn = int(input('Diga uma valor: '))
es = str(input('Você quer par ou impar [P/I]: ')).upper()
nv = 0
while True:
    if (pn+gn) % 2 == 0 and es == 'P' or (pn+gn) % 2 !=0 and es == 'I':
        nv += 1
        print(pn+gn)
    elif (pn+gn) % 2 !=0 and es == 'P' or (pn+gn) % 2 == 0 and es == 'I':
        print('O jogo acabou')
        break
    pn = randint(0, 11)
    gn = int(input('Diga uma valor: '))
    es = str(input('Você quer par ou impar [P/I]: ')).upper().strip()
print(f'Voc^venceu {nv} seguidas')

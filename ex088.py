from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos quer fazer? '))
cont = 0
tot =1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 61)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(jogos)

                
                


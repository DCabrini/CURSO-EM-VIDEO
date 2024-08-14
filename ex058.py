from random import randint
pcn = randint(1,11)
print(pcn)
gn = int(input('Qual o número o PC está pensando? '))
cont = 1
while gn != pcn:
    gn = int(input('Numro errado. Tenten novamente: '))
    cont += 1
print(f'Você Venceu! O númro é {pcn}.\nVocê precisou de {cont} tentativas para ganhar.')
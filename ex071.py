print('-'*30)
print('DC Bank')
print('-'*30)
saque = int(input('Quanto deseja sacar? R$'))
total = saque
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced =1
        totalced = 0
        if total ==0:
            break
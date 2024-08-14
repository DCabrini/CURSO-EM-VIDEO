k = float(input('Quantos quilometros foram percorrigos? '))
d = int(input('Quantos dias de aluguel? '))
print(f'O carro percorreu {k}km em {d} dias.\nO valor a ser pago é de R${(0.15*k)+(d*60):.2f}')
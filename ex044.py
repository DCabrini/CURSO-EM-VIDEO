p = float(input('Qual o preço do produto? '))
print('Forma de Pagamanto\n')
print('''[1] - À vista dinheiro/cheque: 10% de deconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até duas vezes no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros\n''')

opc = int(input('Qual a forma de pagamento? '))

if opc == 1:
    print(f'Forma de pagamento 1\nPreço a pagar R${p*0.90:.2f}')
elif opc == 2:
    print(f'Forma de pagamento 2\nPreço a pagar R${p*0.95:.2f}')
elif opc == 3:
    print(f'Forma de pagamento 3\nPreço a pagar R${p:.2f}')
elif opc == 4:
    print(f'Forma de pagamento 1\nPreço a pagar R${p*1.20:.2f}')
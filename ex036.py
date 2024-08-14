vc = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = float(input('Quantos anos de pagamento? '))
pret = vc/(12*anos)
print(f'Valor da éstação é de R${pret:.2f}')
if pret > (0.30*sal):
    print('Empretimo negado')
else:
    print('Emprestimo concedido')
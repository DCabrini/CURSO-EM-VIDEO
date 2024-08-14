n = int(input('Digite um número: '))
print('''\nEscolha uma opção para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL\n''')
opc = int(input('Qual opção deseja? '))

if opc == 1:
    print(f'{n} convertido para BINÀRIO é = {bin(n)[2:]}')
elif opc == 2:
    print(f'{n} convertido para OCTAL é = {oct(n)[2:]}')
elif opc == 3:
    print(f'{n} convertido para HEXADECIMAL é = {hex(n)[2:]}')
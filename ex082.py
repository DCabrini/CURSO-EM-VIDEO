alllist = list()

while True:
    alllist.append(int(input('Digite um valor inteiro? ')))

    perg = ' '
    perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while perg not in 'NS':
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break
print(f'Todos os valores digitados foram - {alllist}')
parlist = []
imparlist = []
for i in range(0, len(alllist)):
    if alllist[i]% 2 == 0:
        parlist.append(alllist[i])
    else:
        imparlist.append(alllist[i])
print(f'Os valores pares digitado forma - {parlist}')
print(f'Os valores impares digitados foram - {imparlist}')
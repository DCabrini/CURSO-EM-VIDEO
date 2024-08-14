

contida = conthome = contmulh =  0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Qual o sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        contida +=1
    if sexo == 'M':
        conthome += 1
    if sexo == 'F' and idade < 20:
        contmulh +=1
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if perg  == 'N':
        break
print(f'Número de pessoas com mais de 18 anos = {contida}')
print(f'Número de homens cadastrados = {conthome}')
print(f'Número de mulhers menores de 20 anos = {contmulh}')
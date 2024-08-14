
media = 0
hmv = 0
cont = 0
for i in range(1, 5):
    nome = str(input(f'Qual o nome da {i} pessoa: ')).strip()
    idade = int(input(f'Qual a idade da {i} pessoa: '))
    sexo = str(input(f'Qual o sexo da {i} pessoa [M/F]: ')).upper().strip()
    media += idade
    if sexo =='M' and hmv < idade:
        hmv = idade
    if sexo =='F' and idade < 20:
        cont += 1        
        
print(f'A Média das idades é {media/4}')
print(f'A idade do homem mais velho é de {hmv} anos')
print(f'{cont} mulheres tem menos de 20')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1 + n2)/2 >= 7:
    print(f'\nMédia de {(n1 + n2)/2}\n\nAluno APROVADO!')
elif 5 <= (n1 + n2)/2 < 7:
    print(f'\nMédia de {(n1 + n2)/2}\n\nAluno em RECUPERAÇÂO!')
elif (n1+n2)/2 < 5:
    print(f'\nMédia de {(n1 + n2)/2}\n\nAluno REPROVADO')
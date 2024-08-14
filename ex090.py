dados = {}
dados["nome"] = str(input('Qual o nome do aluno? '))
dados["media"] = float(input('Qual a média do aluno? '))
print(dados)
print(f'Nome é {dados["nome"]}')
print(f'Média é {dados["media"]}')

if dados["media"] >= 7:
    print('Situação é Aprovado')
else:
    print('Situação é Reprovado')
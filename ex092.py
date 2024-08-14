from datetime import date

dados = {}

while True:
    dados["nome"] = str(input('Nome: '))
    nasc = int(input('Ano de nascimento? '))
    hoje = int(date.today().strftime("%Y"))
    dados["idade"] = hoje - nasc
    ctps = int(input('Carteira de Trabalho (0 = não tem): '))
    if ctps == 0:
        dados["ctps"] = ctps
        break
    else:
        dados["ctps"] = ctps
        dados["contratação"] = int(input('Ano de contratação: '))
        dados["salário"] = int(input('Salário R$: '))
        dados["aposentadoria"] = dados["idade"] + (dados["contratação"] + 35) - hoje
        break

print(dados)
print()
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
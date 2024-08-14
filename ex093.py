dados = {}
listgols = []
soma =0
dados["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for n in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {n+1}: '))
    listgols.append(gols)
    soma += gols
dados["gols"] = listgols[:]
dados["total"] = soma
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')


for i, v in enumerate(dados["gols"]):
    print(f'Na partida {i+1} fez {v} gols')

dados = {}
listgols = []
lista = list()

while True:
    listgols.clear()
    soma = 0
    dados["nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for n in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {n+1}: '))
        listgols.append(gols)
        soma += gols
    dados["gols"] = listgols[:]
    dados["total"] = soma
    lista.append(dados.copy())
    while True:
        perg = str(input('Deseja continura? [S/N]: ')).upper().strip()[0]
        if perg in 'NS':
            break
        print('ERRO! = Responda apenas S ou N')
    if perg == 'N':
        break
print(lista)
#print(dados)
for i, c in enumerate(lista):
    print(f'{i:>4}', end=' ')
    for v in c.values():
        print(f' {v}', end=' ')
    print()


while True:
    
    while True:
        mostra = int(input('Mostrar dados de qual jogador? '))
        if mostra > len(lista):
            print('ERRO! - Jogador não encontrado digite um número válido.')
        if mostra <= len(lista):
            print(f'Levantamento do Jogador {lista[mostra]["nome"]}')
            for i, v in enumerate(lista[mostra]["gols"]):
                print(f'Na partida {i+1} fez {v} gols')       
        break
    while True:
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if perg in 'NS':
            break
        print('ERRO! - Digite apenas S ou N')
    if perg == 'N':
        break

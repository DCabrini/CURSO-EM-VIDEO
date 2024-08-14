lista = list()
name = list()
notas = list()
#n = 0


while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a nota1 do aluno: '))
    nota2 = float(input('Digite a nota2 do aluno: '))
    name.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    name.append(notas[:])
    lista.append(name[:])
    name.clear()
    notas.clear()
    perg = ' '
    while perg not in "NS":
        perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break

print('N°',end=' ')
print('Aluno',end=' ')
print('Média')
for i in range(0, len(lista)):
    n = 0
    print(f'{i:<3}', end ='')
    for h in range(0, 2):
        if h % 2 == 0:
            pessoa = lista[i][h]
            print(f'{pessoa}', end=' ')
        if h % 2 != 0:
            for j in range(0, 2):
                n += lista[i][h][j]
            print(f'{n/2:<3}')


while True:
    escolha = int(input('Mostrar nota de qual aluno? '))
    print(lista[escolha][1])
    mostra = ' '
    while mostra not in 'SN':
        mostra = str(input('Deseja mostrar mais alguma nota? [S/N]: ')).upper().strip()[0]
    if mostra == 'N':
        break
print('Encerrado')

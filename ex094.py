lista = list()
listaF = []
dados = {}
cont = media = 0
while True:
    dados["nome"] = str(input('Nome: '))
    while True:
        dados["sexo"] = str(input('Qual o sexo [M/F]: ')).upper()
        if dados["sexo"] in 'MF':
            break
        print('Erro - Digite M ou F')
    dados["idade"] = int(input('Idade: '))
    lista.append(dados.copy())
    cont += 1
    media += dados["idade"]
    if dados["sexo"] == 'F':
        listaF.append(dados["nome"])
    perg = ' '
    while perg not in 'NS':
        perg = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if perg == 'N':
        break

print(lista)
print(listaF)
print(cont)
print(media/cont)
for i in lista:
    if i["idade"] >= (media/cont):
        print(i["nome"], ende=' - ')

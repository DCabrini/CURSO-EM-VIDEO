from utilidadescev import moeda

n = float(input('Digite um valor em R$: R$'))
#print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
#print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
pormais = int(input('Quanto deseja aumentar? '))
#print(f'Aumentando {pormais}%, temos {moeda.aumentar(n,pormais, True)}')
pormenos = int(input('Quanto deseja diminuir? '))
#print(f'Reduzindo em {pormenos}%, temos {moeda.diminuir(n, pormenos, True)}')
moeda.resumo(n, pormais, pormenos)
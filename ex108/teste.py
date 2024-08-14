import moeda

n = float(input('Digite um valor em R$: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
pormais = int(input('Quanto deseja aumentar? '))
print(f'Aumentando {pormais}%, temos {moeda.moeda(moeda.aumentar(n,pormais))}')
pormenos = int(input('Quanto deseja diminuir? '))
print(f'Reduzindo em {pormenos}%, temos {moeda.moeda(moeda.diminuir(n, pormenos))}')
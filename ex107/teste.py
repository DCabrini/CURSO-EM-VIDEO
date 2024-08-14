from ex107 import moeda

n = float(input('Digite um valor em R$: R$'))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
pormais = int(input('Quanto deseja aumentar? '))
print(f'Aumentando {pormais}, temos {moeda.aumentar(n,pormais)}')
pormenos = int(input('Quanto deseja diminuir? '))
print(f'Reduzindo em {pormenos}, temos {moeda.diminuir(n, pormenos)}')
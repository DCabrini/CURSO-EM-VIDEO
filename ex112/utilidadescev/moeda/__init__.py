def aumentar(v=0, por=0, formato=False):
    final = v*(1+(por/100))
    return final if formato is False else moeda(final)


def diminuir(v=0, por=0, formato=False):
    final = v*(1-(por/100))
    return final if formato is False else moeda(final)

def dobro(v=0, formato=False):
    final = 2*v
    return final if formato is False else moeda(final)

def metade(v=0, formato=False):
    final = v/2
    return final if formato is False else moeda(final)

def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')

def resumo(v = 0 , taxaa = 10, taxar = 10 ):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado {moeda(v)}')
    print(f'O dobro do perço é {dobro(v, True)}')
    print(f'Metade do preço é {metade(v, True)}')
    print(f'Com um aumento de {taxaa}% o valor é de {aumentar(v, taxaa, True)}')
    print(f'Com uma redução de {taxar}% o valor é de {diminuir(v, taxar, True)}')
    print('-'*30)

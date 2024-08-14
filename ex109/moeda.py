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
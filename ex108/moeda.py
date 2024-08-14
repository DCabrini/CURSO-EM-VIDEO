def aumentar(v=0, por=0):
    final = v*(1+(por/100))
    return final


def diminuir(v=0, por=0):
    final = v*(1-(por/100))
    return final

def dobro(v=0):
    final = 2*v
    return final

def metade(v=0):
    final = v/2
    return final

def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
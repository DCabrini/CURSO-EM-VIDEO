tupla = ('carro',  'moto', 'onibus', 'labreta', 'aviao', 'foguete')

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ',end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end = ' ')
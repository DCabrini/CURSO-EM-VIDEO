def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! \"{entrada}\" Preço invalido!')
        else:
            valido =True
            return float(entrada)
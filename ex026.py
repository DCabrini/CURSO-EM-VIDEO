frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letre "a" aparece {frase.count("a")}')
print(f'A letra "a" aparece pela primeira vez na posição {frase.find("a")}' )
print(f'A letra "a" aprece pela última vez na posição {frase.rfind("a")}')
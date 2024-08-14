frase = str(input('Digite uma frase: ')).lower().strip()

palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print(junto, inverso)
    print('É palindromo')
else:
    print('Não é palindromo')
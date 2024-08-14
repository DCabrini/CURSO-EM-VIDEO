import random

nc = random.randint(0,6)

nu = int(input('DIgite um número inteiro entre 0 e 5: '))

if nu == nc:
    print(f'O computador pensou em {nc}\n{nu} = {nc}\nParabéns você gangou!')
else:
    print(f'O computador pensou em {nc}\n{nu} ≠ {nc}\nSinto muito, você perdeu!')
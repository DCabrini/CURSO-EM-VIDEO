import random
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print('Opções de jogo')
print('''- pedra
- papel
- tesoura''')
eu = str(input('O que você escolhe? ')).strip().lower()

if pc == eu:
    print('Jogo empatado\nNinguem venceu')
elif (pc == 'pedra' and eu == 'tesoura') or (pc == 'tesoura' and eu == 'papel') or (pc == 'papel' and eu  == 'pedra'):
    print(f'Você PERDEU\nPC escolheu {pc} e Você escolheu {eu}')
elif (eu == 'pedra' and pc == 'tesoura') or (eu == 'tesoura' and pc == 'papel') or (eu == 'papel' and pc  == 'pedra'):
    print(f'Você ***VENCEU***\nPC escolheu {pc} e Você escolheu {eu}')
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaterc = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Digite o valor na pocição {l+1} {c+1}: '))
        if matrix[l][c] % 2== 0:
            soma += matrix[l][c]
        if c == 2:
            somaterc += matrix[l][c]
        if l == 1 and c == 0:
            maior = matrix[l][c]
        if l == 1 and c > 0:
            if maior < matrix[l][c]:
                maior = matrix[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matrix[l][c]:^5}',end='')
    print()
print(f'Soma dos valores pares é {soma}')
print(f'A soma dos elementos da terceira coluna é {somaterc}')
print(f'O maior valor da segunda linha é {maior}')


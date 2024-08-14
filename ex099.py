from time import sleep

def maior(*valores):
    print('~~ Analisando valores ~~')
    maior = 0
    for n in range(0, len(valores)):
        print(valores[n], end=' ', flush=True)
        sleep(0.5)
        if n == 0:
            maior = valores[n]
        else:
            if valores[n] > maior:
                maior = valores[n]
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {maior}')



maior(2,5,26,8,12,4)
maior(2,9,45)
maior()
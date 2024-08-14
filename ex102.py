
def fatorial(n, show=True):
    f = 1
    if show ==True:
        while n > 0:
            f *= n
            n -= 1
            print(f'{n} x ', end=" ")
        print(f'= {f}')
    elif show == False:
        while n > 0:
            f *= n
            n -= 1
        return print(f)
        


#print(show)
#n = int(input('Digite o valor: '))
#show = bool(input('Indique verdadeiro ou falso: '))
fatorial(5, False)

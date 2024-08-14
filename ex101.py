from datetime import date

def voto(n):
    hoje = int(date.today().strftime("%Y"))
    if 18 <= (hoje - nasc) < 65:
        return print(f'Com {(hoje - nasc)} anos: VOTO OBRIGATÓRIO')
    elif (hoje - nasc) < 16:
        return print(f'Com {(hoje - nasc)} anos: NÃO VOTA')
    elif (hoje - nasc) > 65 or 16 <= (hoje - nasc) < 18:
        return print(f'Com {(hoje - nasc)} anos: VOTO OPCIONAL')


nasc = int(input('Ano de nascimento? '))
#hoje = int(date.today().strftime("%Y"))
#print(hoje)
voto(nasc)
classi = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba','América-MG')
print(classi)
print('='*50)
print(f'Os cinco preiros colocados são {classi[:5]}')
print('='*50)
print(f'Os quatro últimos colocados são {classi[-4:]}')
print('='*50)
print(f'Os times em ordem alfabética:\n{sorted(classi)}')
print('='*50)
for pos, time in enumerate(classi):
    if time == 'São Paulo':
        print(f'O São Paulo está na posição {pos+1}')
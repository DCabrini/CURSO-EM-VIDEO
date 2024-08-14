s  = str(input('Digite o sexo da pesoa [M/F]: ')).upper().strip()[0]

while s not in "MF":
    s  = str(input('Dados invalidos, Digite seu sexo: ')).upper().strip()[0]
print(s)





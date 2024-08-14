tupla = ('zero','um','dois','três', 'quatro','cinco','seis','sete','oito','nove','dex','onze','douze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input("Digite um número entre zero e vinte: "))

while n not in range(0, len(tupla)):
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {tupla[n]}')
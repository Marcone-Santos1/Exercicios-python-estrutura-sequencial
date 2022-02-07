'''

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''

base = float(input('Sabendo que um quadrado tem seus lados de mesma medida, Digite apenas o valor de um de seus lados: '))
altura = base
pi = 3.14159265359

area = base * altura

print('A área do quadrado é: {} * {}  = {}'.format(base, altura, area))

print('O dobro da area é:', area * 2)
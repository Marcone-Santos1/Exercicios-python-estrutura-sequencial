# https://wiki.python.org.br/EstruturaSequencial
'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

n1 = int(input('Digite um número interio: '))
n2 = int(input('Digite outro número interio: '))
n3 = float(input('Digite um número real: '))

s_n1 = n1 * 2
m_n2 = n2 / 2

s_triplo_n1 = n1 * 3

exponenciacao = n3 ** 3

produto = s_n1 * m_n2
print(produto)

soma = s_triplo_n1 + n3
print(soma)

print(exponenciacao)


print ('Soma:', ((2*n1) * (n2/2)))
print ('Produto:', (3 * n1) + n3)
print ('Cubo:', n3**3)
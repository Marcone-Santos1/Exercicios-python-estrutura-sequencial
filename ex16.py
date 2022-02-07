'''

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 ltros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

# area = float(input('Qual a area que deve ser pintada em m²? '))
area = altura * largura

litros = area / 3

preco_lata_de_tinta = 80
litros_lata = 18 
latas = litros / litros_lata
total = latas * preco_lata_de_tinta


print (f'Você usara {litros:.2f} e isso equivale a {latas:.2f} latas de tinta. O preco total é de: R$ {total:.2f}')


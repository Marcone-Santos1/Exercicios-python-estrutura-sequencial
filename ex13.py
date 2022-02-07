'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

'''

sexo = input('Digite 1 - Homem \nDigite 2 - Mulher \nQual a sua aescolha? ')

h = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

peso_ideal_homem = (72.7 * h) - 58
peso_ideal_mulher = (62.1 * h) - 44.7


'''if sexo == '1':
    print((72.7 * h) - 58)

else:
    print((62.1 * h) - 44.7)
'''

if sexo == '1':
    print((72.7 * h) - 58)

    if peso < peso_ideal_homem:
            print('Abaixo do peso ideal!')
    elif peso == peso_ideal_homem:
        print('Dentro do peso ideal!')
    else:
        print('Acima do peso ideal!')
    print (f'{peso:.2f} / {peso_ideal_homem:.2f}')

else:
    print((62.1 * h) - 44.7)
    
    if peso < peso_ideal_mulher:
            print('Abaixo do peso ideal!')
    elif peso == peso_ideal_mulher:
        print('Dentro do peso ideal!')
    else:
        print('Acima do peso ideal!')
    print (f'{peso:.2f} / {peso_ideal_mulher:.2f}')
    

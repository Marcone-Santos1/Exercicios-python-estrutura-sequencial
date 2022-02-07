'''

Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)

'''

fahrenheit = float(input('Digite a temperatura em Fahrenheit, ou seja, de 20F à 120F: '))

c = 5

celcius = c * ((fahrenheit - 32)) / 9

print(f'A conversão de {fahrenheit}ºF para Celcius fica: {celcius:.2f}ºC')

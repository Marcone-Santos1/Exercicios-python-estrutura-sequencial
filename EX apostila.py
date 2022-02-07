

# print as palavras entre o  dois pontos
a = "Um elefante incomoda muita gente"

print(a[3:21])

# print a frase com tudo em maiusculo e sem espaço
oi = str(input('Oi, Digite uma frase: '))

print(oi.strip().upper())


# Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z   =  (𝑥2+ 𝑦2)(𝑥−𝑦)2  

x = int(input('Digite um número: '))
y = int(input('Digite um numero: '))

z = ((x ** 2) + (y ** 2)) / ((x - y) ** 2)

print(f'{z:.2}')

# reajuste salarial

salario = int(input('Digite seu salário: '))

reajuste = salario * (35 / 100)

novo_salario =  salario + reajuste

print(novo_salario)
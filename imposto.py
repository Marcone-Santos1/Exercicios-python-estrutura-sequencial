salario = float(input("Escreva quanto é o seu salário: "))

deve_pagar_imposto = 1200

if salario >= deve_pagar_imposto:
    print('deve pagar imposto')
elif salario < deve_pagar_imposto:
    print('não deve pagar imposto')
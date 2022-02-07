materia1 = float(input("Digite sua nota 1: "))
materia2 = float(input("Digite sua nota 2: "))
materia3 = float(input("Digite sua nota 3: "))

média_minima = 7

média = (materia1 + materia2 + materia3) / 3

if média >= média_minima:
    print(f"aprovado com a {média:.2f}")

elif média < média_minima:
    print(f"reprovado com a {média:.2f}")
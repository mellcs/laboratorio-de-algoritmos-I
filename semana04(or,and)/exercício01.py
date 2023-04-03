nome = input("Insira seu nome:")
salario = float(input("Insira seu salário:"))
tempo = float(input("Insira a quantos anos você trabalha na empresa:"))

if tempo >=5 and salario <=2000:
    print("Parabéns", nome, "você receberá um aumento de 10%!")
else:
    print("Parabéns", nome, "você receberá um aumento de 5%!")


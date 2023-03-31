salario = float(input("Insira seu salário:"))

if salario <1500:
    salario = salario + 200
elif salario == 1500:
    salario = salario + 150
else:
    salario = salario +100

print("Seu novo salário é: R$", salario)

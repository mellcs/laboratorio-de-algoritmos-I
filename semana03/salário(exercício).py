salario = 35.00

horas = float(input("Insira suas horas trabalhadas:"))

totalMensal = (salario * horas)
print("Seu salário esse mês será:", totalMensal)

if totalMensal < 1000:
    totalMensal + 300
    print("Parabéns, você recebeu um acréscimo de R$300,00 e seu salário atual é de:", totalMensal + 300)
else:
    print("Parabéns, seu salário atual é de:", totalMensal)
# Aumento de 65%
valorFabrica = float(input("Digite o valor original:"))

#valorfinal = valorFabrica * 1.65
#valorfinal = (valorFabrica * 165) / 100

valorFinal = (valorFabrica * 0.65) + valorFabrica

print ("O novo valor será: ", valorFinal)

#Desconto de 65%
valorAtual = float(input("Valor atual do produto: "))
#valorFinal = valorAtual * 0.35
valorFinal = valorAtual - (valorAtual * 0.65)
#valorFinal = (valorAtual * 35) / 100

print("O valor final será: " , valorFinal)
quantidadeMorangos = float(input("Digite a quantidade (em Kg) de morangos comprados: "))
quantidadeMacas = float(input("Digite a quantidade (em Kg) de maçãs compradas: "))

if quantidadeMorangos <= 5:
    valorMorangos = quantidadeMorangos * 2.50
else:
    valorMorangos = quantidadeMorangos * 2.20

if quantidadeMacas <= 5:
    valorMacas = quantidadeMacas * 1.80
else:
    valorMacas = quantidadeMacas * 1.50

valorTotal = valorMorangos + valorMacas

if quantidadeMorangos + quantidadeMacas > 8 or valorTotal > 25.00:
    valorTotal = valorTotal * 0.9


print("O valor total a ser pago é R$", valorTotal)

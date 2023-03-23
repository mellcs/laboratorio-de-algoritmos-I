qtdMelao = int(input("Quantidade de melões:"))

totalCompra = qtdMelao *8.79
print("Valor total:", totalCompra)

if totalCompra >= 60:
    valorComDesconto = totalCompra * 0.9
    print("Valor com desconto: R$", valorComDesconto)
else:
    valorSemDesconto = totalCompra * 1.1
    print("Valor sem desconto: R$", valorComDesconto)
if valorComDesconto >= 60:
    print("Você recebeu um desconto!")

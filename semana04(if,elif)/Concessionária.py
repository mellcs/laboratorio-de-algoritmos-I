valorCarro = float(input("Digite o valor do auto:"))

print("1 - Pagamento a vista.")
print("2 - Pagamento em 12x.")
print("3 - Pagamento em 24x.")
print("4 - Pagamento em 36x.")
opcao = int(input("Digite a opção:"))

if opcao == 1:
    valorAtualizado = valorCarro * 0.96
    print("Valor do carro: R$", valorCarro)
    print("Valor com desconto: R$", valorAtualizado)
elif opcao == 2:
    valorAtualizado = valorCarro * 1.02
    valorParcela = valorAtualizado/12
    print("Valor do carro: R$", valorCarro)
    print("Valor com juros: R$", valorAtualizado)
    print("Valor parcela: R$", valorParcela)
elif opcao == 3:
    valorAtualizado = valorCarro * 1.07
    valorParcela = valorAtualizado/24
    print("Valor do carro: R$", valorCarro)
    print("Valor com juros: R$", valorAtualizado)
    print("Valor da parcela: R$", valorParcela)
elif opcao == 4:
    valorAtualizado = valorCarro * 1.15
    valorParcela = valorAtualizado/36
    print("Valor do carro: R$", valorCarro)
    print("Valor com juros: R$", valorAtualizado)
    print("Valor da parcela: R$", valorParcela)
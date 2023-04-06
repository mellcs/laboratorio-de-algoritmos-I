caixa = float(input("Valor em caixa:"))

opcao = 0 
while opcao != 4:
    print("1-R ealizar venda.")
    print("2- Retirar dinheiro.")
    print("3- Dinheiro em caixa.")
    print("4- Sair.")
    opcao = int(input("Opção:"))

    if opcao == 1:
        venda = float(input("Valor da venda:"))
        caixa = caixa + venda
    elif opcao == 2:
        retirada = float(input("Valor da retirada:"))
        if caixa >= retirada:
            caixa = caixa - retirada
        else:
            print("Valor insuficiente!")
    elif opcao == 3:
        print("Valor em caixa:", caixa)
    elif opcao == 4:
        print("Volte sempre na loja do 100tinho!")
    else:
        print("Opção inválida!")


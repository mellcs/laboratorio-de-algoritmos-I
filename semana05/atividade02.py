saldo = float(input("Insira seu saldo atual:"))

opcao = 0 
while opcao != 4:
    print("1 - Sacar.")
    print("2 - Depositar.")
    print("3 - Saldo.")
    print("4 - Sair.")
    opcao = int(input("Opção:"))

    if opcao == 2:
        deposito = float(input("Valor do deposito:"))
        saldo = saldo + deposito
    elif opcao == 1:
        saque = float(input("Valor do saque:"))
        if saldo >= saque:
            saldo = saldo - saque
        else:
            print("Valor insuficiente!")
    elif opcao == 3:
        print("Valor disponível:", saldo)
    elif opcao == 4:
        print("Obrigado por usar o nosso banco!")
    else:
        print("Opção inválida!")
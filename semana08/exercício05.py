saldo = 0

def mostrar_menu():
    print("Bem-vindo ao Banco XYZ!")
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")

def sacar(saldo):
    valor = float(input("Digite o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print("Saque de R$", saldo, "realizado com sucesso.")

def depositar(saldo):
    valor = float(input("Digite o valor do depósito: "))
    saldo += valor
    print("Depósito de R$", saldo, "realizado com sucesso.")

def mostrar_saldo(saldo):
    print(f"Seu saldo atual é de R$", saldo)

mostrar_menu()

opcao = 0
while opcao != 4:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        sacar(saldo)
    elif opcao == 2:
        depositar(saldo)
    elif opcao == 3:
        mostrar_saldo(saldo)
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
    else:
        print("Opção inválida. Por favor, tente novamente.")

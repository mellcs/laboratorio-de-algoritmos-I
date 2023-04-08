alturatotal = 0
idadetotal = 0
pessoas = 0
opcao = 0

while opcao != 3:
    print("Menu:")
    print("1 - Cadastrar pessoa.")
    print("2 - Ver médias de altura e idade.")
    print("3 - Sair.")

    opcao = int(input("Insira sua opção:"))

    if opcao == 1:
        altura = float(input("Insira sua altura:"))
        idade = int(input("Insira sua idade:"))
        alturatotal += altura
        idadetotal += idade
        pessoas += 1
        print("Pessoa cadastrada com sucesso!")
    elif opcao == 2:
        if pessoas == 0:
            print("Nenhuma pessoa cadastrada. Cadastre alguém para começar.")
        else:
            mediaaltura = alturatotal / pessoas
            mediaidade = idadetotal / pessoas
            print("Média parcial de altura:", mediaaltura, "m.")
            print("Média parcial de idade:", mediaidade , "anos.")
    elif opcao == 3:
        print("Obrigado pela preferência. Volte sempre!")
    else:
        print("Opção inválida. Insira uma opção válida.")





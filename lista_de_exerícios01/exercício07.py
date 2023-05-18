def realizar_pesquisa():
    revista_a = 0
    revista_b = 0
    revista_c = 0
    total_pessoas = 0

    while total_pessoas < 20:
        opcao = input("Qual jornal você considera mais lido? (A, B ou C): ").upper()
        if opcao == 'A':
            revista_a += 1
            total_pessoas += 1
        elif opcao == 'B':
            revista_b += 1
            total_pessoas += 1
        elif opcao == 'C':
            revista_c += 1
            total_pessoas += 1
        else:
            print("Opção inválida. Por favor, escolha entre A, B ou C.")

    porcentagem_a = (revista_a / 20) * 100
    porcentagem_b = (revista_b / 20) * 100
    porcentagem_c = (revista_c / 20) * 100

    if porcentagem_a <= porcentagem_b and porcentagem_a <= porcentagem_c:
        menor = porcentagem_a
        if porcentagem_b <= porcentagem_c:
            meio = porcentagem_b
            maior = porcentagem_c
        else:
            meio = porcentagem_c
            maior = porcentagem_b
    elif porcentagem_b <= porcentagem_a and porcentagem_b <= porcentagem_c:
        menor = porcentagem_b
        if porcentagem_a <= porcentagem_c:
            meio = porcentagem_a
            maior = porcentagem_c
        else:
            meio = porcentagem_c
            maior = porcentagem_a
    else:
        menor = porcentagem_c
        if porcentagem_a <= porcentagem_b:
            meio = porcentagem_a
            maior = porcentagem_b
        else:
            meio = porcentagem_b
            maior = porcentagem_a

    print("As porcentagens são:")
    print("-", menor)
    print("-", meio)
    print("-", maior)


def main():
    realizar_pesquisa()


if __name__ == "__main__":
    main()

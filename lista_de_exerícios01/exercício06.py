def pesquisa():
    sim1 = 0
    nao1 = 0
    contador = 0

    while contador < 20:
        resposta = input("Você gostou do produto?: ").strip().lower()
        if resposta == "sim":
            sim1 += 1
            contador += 1
        elif resposta == "não" or resposta == "nao":
            nao1 += 1
            contador += 1
        else:
            print("Insira uma resposta válida.")

    return sim1, nao1

def main():
    sim1, nao1 = pesquisa()

    print("O número de pessoas que gostou é:", sim1)
    print("O número de pessoas que não gostou é:", nao1)


main()
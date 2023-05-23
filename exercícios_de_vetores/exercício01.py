def preencher_vetor():
    vetor = []
    for i in range(8):
        numero = int(input("Insira um número inteiro: "))
        vetor.append(numero)
    return vetor

def contar_maior_que_30(vetor):
    contador = 0
    soma = 0
    for numero in vetor:
        if numero > 30:
            contador += 1
            soma += numero
    return contador, soma

def somar_vetor(vetor):
    soma = sum(vetor)
    return soma

def main():
    vetor = preencher_vetor()

    print("Valores do vetor:", vetor)

    contador_maior_30, soma_maior_30 = contar_maior_que_30(vetor)
    print("Quantidade de números maiores que 30:", contador_maior_30)
    print("Soma dos números maiores que 30:", soma_maior_30)

    soma_total = somar_vetor(vetor)
    print("Soma de todos os números do vetor:", soma_total)

main()

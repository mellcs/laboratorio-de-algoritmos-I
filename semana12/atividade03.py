def criar_array():
    numeros = []
    contador = 0

    while contador < 5:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
        contador += 1

    return numeros

def encontrar_maior_menor(numeros):
    if not numeros:
        return None, None, None, None

    maior = menor = numeros[0]
    posicao_maior = posicao_menor = 0

    for i in range(1, len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
            posicao_maior = i
        if numeros[i] < menor:
            menor = numeros[i]
            posicao_menor = i

    return maior, menor, posicao_maior, posicao_menor

def main():
    numeros = criar_array()
    maior, menor, posicao_maior, posicao_menor = encontrar_maior_menor(numeros)

    if maior is None:
        print("Nenhum número foi digitado.")
    else:
        print("Maior número:", maior)
        print("Posição do maior número:", posicao_maior)
        print("Menor número:", menor)
        print("Posição do menor número:", posicao_menor)

main()
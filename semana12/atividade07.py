import random

def criar_array():
    array = []
    contador = 0

    while contador < 10:
        numero = random.random() * 50 + 1
        numero = int(numero)
        array.append(numero)
        contador += 1

    return array

def contar_pares_impares(array):
    pares = 0
    impares = 0

    for numero in array:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

def main():
    array = criar_array()
    pares, impares = contar_pares_impares(array)
    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)

main()

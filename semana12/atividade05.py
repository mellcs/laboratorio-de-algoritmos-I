import random

def criar_array():
    array = []
    contador = 0

    while contador < 10:
        numero = random.randint(1, 100)
        array.append(numero)
        contador += 1

    return array

def exibir_pares(array):
    for numero in array:
        if numero % 2 == 0:
            print(numero)

def main():
    array = criar_array()
    exibir_pares(array)

main()

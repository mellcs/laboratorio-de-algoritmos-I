def criar_array(tamanho):
    array = []
    contador = 0

    while contador < tamanho:
        numero = int(input("Digite um número inteiro: "))
        array.append(numero)
        contador += 1

    return array

def tamanho_array(array):
    contador = 0
    for _ in array:
        contador += 1

    return contador

def somar_arrays(array1, array2):
    tamanho = tamanho_array(array1)
    if tamanho_array(array2) < tamanho:
        tamanho = tamanho_array(array2)

    array_soma = []

    for i in range(tamanho):
        soma = array1[i] + array2[i]
        array_soma.append(soma)

    return array_soma

def main():
    tamanho = int(input("Digite o tamanho dos arrays: "))
    array1 = criar_array(tamanho)
    array2 = criar_array(tamanho)
    array_soma = somar_arrays(array1, array2)

    print("Array 1:", array1)
    print("Array 2:", array2)
    print("Soma dos arrays:", array_soma)

main()
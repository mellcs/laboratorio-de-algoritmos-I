def criar_array():
    array = []
    contador = 0

    while contador < 5:
        numero = int(input("Digite um número: "))
        array.append(numero)
        contador += 1

    return array

def verificar_numero(array, numero):
    for valor in array:
        if valor == numero:
            return "O número está presente no array."

    return "O número não está presente no array."

def main():
    array = criar_array()
    numero = int(input("Digite um número para verificar: "))
    resultado = verificar_numero(array, numero)
    print(resultado)

main()

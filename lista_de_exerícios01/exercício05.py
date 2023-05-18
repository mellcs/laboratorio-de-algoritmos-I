def somar_naturais(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

def main():
    numero = int(input("Insira um número:"))
    resultado = somar_naturais(numero)
    print(resultado)  


main()
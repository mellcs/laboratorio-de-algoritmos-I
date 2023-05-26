#Escreva um programa que solicita ao usuário que insira 5 números inteiros e armazene-os em um array. Em seguida, calcule e exiba a soma e a média dos números.

#solicitação, limitação de 5 números, armazenamento em lista
def solicitacao(lista):

    for x in range (0,5):
        numero = int(input("Insira um número:"))
        lista.append(numero)
    return lista

#importante vvvvv
def somatorio(lista):
    soma = 0
    for x in range (0,5):
        soma = soma + lista[x]
    return soma

#amostra, cálculo da soma
def main():
    lista=[]
    lista = solicitacao(lista) 
    print(lista)
    #soma = 0
    #numero = int(input("Insira um número:"))
   # media = soma / 5
  
    resposta = somatorio(lista)
    print("A soma dos números é:", resposta)
    media = resposta / 5
    print("A média dos números é:", media)
main()
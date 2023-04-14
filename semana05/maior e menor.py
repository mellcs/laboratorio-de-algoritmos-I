idade = int(input("Digite uma idade:"))
maior = idade
menor = idade

contador = 0
while contador <14:
    idade = int(input("Digite uma idade:"))

    if maior < idade:
        maior = idade
    elif menor > idade:
        menor = idade
        
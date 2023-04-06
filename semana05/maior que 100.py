numero = 0
maioresque100 = 0

while numero != -1:
    numero = int(input("Digite um número:"))
    if numero > 100:
        maioresque100 = maioresque100 + 1

print("Total de valores maiores que 100:", maioresque100)
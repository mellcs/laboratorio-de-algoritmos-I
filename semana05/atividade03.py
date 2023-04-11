contador = 0
numero = 1

while numero != 0:
    numero = float(input("Digite um número, ou digite 0 para sair: "))
    if numero == 10:
        contador += 1

print("Você digitou o número 10", contador, "vezes.")
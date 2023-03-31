valorUm = float(input("Insira o primeiro valor:"))
valorDois = float(input("Insira o segundo valor:"))

print("Somar.")
print("Subtrair.")
print("Multiplicar.")
print("Dividir.")

operacao = input("Digite a operação:")

if operacao == "Somar":
    resultado = valorUm+valorDois
    print("O resultado será:", resultado)

elif operacao == "Subtrair":
    resultado = valorUm-valorDois
    print("O resultado é:", resultado)

elif operacao == "Multiplicar":
    resultado = valorUm*valorDois
    print("O resultado é:", resultado)

else:
    resultado = valorUm/valorDois
    print("o resultado é:", resultado)
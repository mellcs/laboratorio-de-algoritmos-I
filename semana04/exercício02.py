valor = float(input("Insira o valor da peça:"))

print("1 - Á vista.")
print("2 - Em 2x")
print("3 - Em 3x")

opcao = int(input("Digite a opção:"))

if opcao == 1:
    print("O valor da peça será de:", valor)

elif opcao == 2:
    parcela2 = valor / 2
    print("O valor de cada parcela será de:", parcela2)

else:
    parcela3 = valor / 3
    print("O valor de cada parcela será de:", parcela3)
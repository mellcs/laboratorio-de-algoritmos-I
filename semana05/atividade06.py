maiores_dezoito = 0

for i in range(10):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if idade >= 18:
        maiores_dezoito += 1

print(f"A quantidade de pessoas com idade maior ou igual a 18 anos é: {maiores_dezoito}")

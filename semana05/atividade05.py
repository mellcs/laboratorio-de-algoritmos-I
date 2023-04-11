soma_salarios = 0
maior_idade = 0
menor_idade = 999
mulheres_salario_ate_100 = 0

for i in range(1, 11):
    print(f"Digite os dados da {i}ª pessoa:")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ")
    salario = float(input("Salário: "))
    print("-------------------------------")

    soma_salarios += salario

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade:
        menor_idade = idade

    if sexo == "F" and salario <= 100:
        mulheres_salario_ate_100 += 1

media_salarios = soma_salarios / 10

print(f"Média de salário do grupo: R${media_salarios:.2f}")
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Menor idade do grupo: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$100,00: {mulheres_salario_ate_100}")

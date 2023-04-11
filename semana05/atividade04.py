idades = []
pesos = []
maiores_de_idade = 0
entre_10_e_30 = 0

for i in range(7):
    idade = int(input("Digite a idade da pessoa {} : ".format(i+1)))
    peso = float(input("Digite o peso da pessoa {} : ".format(i+1)))
    idades.append(idade)
    pesos.append(peso)
    
    if idade >= 18:
        maiores_de_idade += 1
    
    if 10 <= idade <= 30:
        entre_10_e_30 += 1

media_idades = sum(idades) / len(idades)
percentual_entre_10_e_30 = (entre_10_e_30 / len(idades)) * 100

print("Média das idades: {:.2f}".format(media_idades))
print("Pessoas maiores de idade: {}".format(maiores_de_idade))
print("Porcentagem de pessoas entre 10 e 30 anos: {:.2f}%".format(percentual_entre_10_e_30))


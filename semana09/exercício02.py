def ler_idades():
    idades = []
    for i in range(7):
        idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
        idades.append(idade)
    return idades

def calcular_media(idades):
    total = sum(idades)
    media = total / len(idades)
    return media

def contar_maiores(idades):
    count = 0
    for idade in idades:
        if idade >= 18:
            count += 1
    return count

def calcular_porcentagem(idades):
    count = 0
    for idade in idades:
        if 10 <= idade <= 30:
            count += 1
    porcentagem = (count / len(idades)) * 100
    return porcentagem

idades = ler_idades()
media = calcular_media(idades)
maiores = contar_maiores(idades)
porcentagem = calcular_porcentagem(idades)

print("A média das idades é: {:.2f}".format(media))
print("Quantidade de pessoas maiores de idade: {}".format(maiores))
print("Porcentagem de pessoas com idade entre 10 e 30 anos: {:.2f}%".format(porcentagem))

#eu fiz essa em aula com o senhor, mas na hora que salvei na sala acabou não copiando e colando esse exercício, e sim o primeiro. Aí eu fiquei triste e pedi pro chat fazer esse :D

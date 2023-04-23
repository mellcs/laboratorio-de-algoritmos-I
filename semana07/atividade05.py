# inicializa as variáveis
maior_idade = 0
mulheres_18_35_vcl = 0
olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0
loiros = 0
castanhos = 0
pretos = 0
homens = 0
mulheres = 0

# loop para entrevistar 15 pessoas
for i in range(15):
    # perguntas
    sexo = input("Informe o sexo (M/F): ")
    cor_olhos = input("Informe a cor dos olhos (A/V/C): ")
    cor_cabelos = input("Informe a cor dos cabelos (L/C/P): ")
    idade = int(input("Informe a idade: "))

    # verifica a maior idade
    if idade > maior_idade:
        maior_idade = idade
    
    # verifica a quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos loiros
    if sexo == "F" and 18 <= idade <= 35 and cor_olhos == "V" and cor_cabelos == "L":
        mulheres_18_35_vcl += 1
    
    # conta a quantidade de pessoas com cada cor de olhos e cabelos
    if cor_olhos == "A":
        olhos_azuis += 1
    elif cor_olhos == "V":
        olhos_verdes += 1
    else:
        olhos_castanhos += 1
    
    if cor_cabelos == "L":
        loiros += 1
    elif cor_cabelos == "C":
        castanhos += 1
    else:
        pretos += 1
    
    # conta a quantidade de homens e mulheres
    if sexo == "M":
        homens += 1
    else:
        mulheres += 1

# calcula as porcentagens
total_pessoas = olhos_azuis + olhos_verdes + olhos_castanhos
porcentagem_olhos_azuis = (olhos_azuis / total_pessoas) * 100
porcentagem_olhos_verdes = (olhos_verdes / total_pessoas) * 100
porcentagem_olhos_castanhos = (olhos_castanhos / total_pessoas) * 100

total_cabelos = loiros + castanhos + pretos
porcentagem_loiros = (loiros / total_cabelos) * 100
porcentagem_castanhos = (castanhos / total_cabelos) * 100
porcentagem_pretos = (pretos / total_cabelos) * 100

porcentagem_homens = (homens / 15) * 100
porcentagem_mulheres = (mulheres / 15) * 100

# exibe as respostas
print("Maior idade:", maior_idade)
print("Mulheres entre 18 e 35 anos, olhos verdes e cabelos loiros:", mulheres_18_35_vcl)
print("Porcentagem de olhos azuis:", porcentagem_olhos_azuis)
print("Porcentagem de olhos verdes:", porcentagem_olhos_verdes)
print("Porcentagem de olhos castanhos:", porcentagem_olhos_castanhos)
print("Porcentagem de cabelos loiros:", porcentagem_loiros)
print("Porcentagem de cabelos castanhos:", porcentagem_castanhos)
print("Porcentagem de cabelos pretos:", porcentagem_pretos)
print("Porcentagem de pessoas do sexo feminino:", porcentagem_mulheres)
print("Porcentagem de pessoas do sexo masculino:", porcentagem_homens)
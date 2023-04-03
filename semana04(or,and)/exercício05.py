print("Responda com 'sim' ou 'nao' as seguintes perguntas:")
telefonou = input("Telefonou para a vítima? ")
esteve = input("Esteve no local do crime? ")
mora = input("Mora perto da vítima? ")
devia = input("Devia para a vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")

respostas_positivas = 0
if telefonou == "sim":
    respostas_positivas += 1
if esteve == "sim":
    respostas_positivas += 1
if mora == "sim":
    respostas_positivas += 1
if devia == "sim":
    respostas_positivas += 1
if trabalhou == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é suspeito do crime. Não saia da cidade.")
elif respostas_positivas in (3, 4):
    print("Você é cúmplice do crime. Não saia da cidade e contate um advogado.")
elif respostas_positivas == 5:
    print("Você é o(a) assassino(a)! A polícia está a caminho!")
else:
    print("Você é inocente do crime. Obrigado pela cooperação.")
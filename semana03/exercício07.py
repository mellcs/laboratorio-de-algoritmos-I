altura = float(input("Insira sua altura:"))
sexo = input("Insira seu sexo:")

masculino = (72.7*altura) - 58
feminino = (62.1*altura) - 44.7

if sexo != feminino:
    print("Seu peso ideal será de:", masculino)

else:
    print("Seu peso ideal será de:", feminino)

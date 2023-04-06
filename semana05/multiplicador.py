numero = int(input("Digite um valor para calcular a tabuada:"))
multiplicador = 1
roberto = int(input("Você deseja a tabuada multiplicada por 1 até:"))

while multiplicador <= roberto:
    resultado = numero * multiplicador
    print("-", resultado)
    multiplicador = multiplicador + 1
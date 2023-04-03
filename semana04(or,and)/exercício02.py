lado1 = float(input("Insira a medida do primeiro lado:"))
lado2 = float(input("Insira a medida do segundo lado:"))
lado3 = float(input("Insira a medida do terceiro lado:"))

#trianguloequilatero = lado1 == lado2 == lado3
#trianguloisoceles = quaisquer 2 lados iguais
#triangulo escaleno = todos os lados diferentes

if lado1 == lado2 == lado3:
    print("É um triângulo equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um triângulo isóceles!")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("É um triângulo escaleno!")
else:
    print("Não é um triângulo!")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 % 2 == 1:
    num1 += 1

while num1 <= num2:
    print(num1)
    num1 += 2
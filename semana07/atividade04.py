impar = 0
par = 0
zero = 0

for numero in range (1,11):
    numero = int(input("Insira um número:"))
    if numero % 2 != 0:
        impar = impar + 1
    elif numero % 2 == 0:
        par = par + 1
    else:
        zero = zero + 1
print("A quantidade de números pares é:", par, ", de ímpares é:", impar, ", e de zeros é:", zero)
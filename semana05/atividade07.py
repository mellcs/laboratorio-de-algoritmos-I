qtd_numeros = 10
qtd_entre_30_e_90 = 0

for i in range(qtd_numeros):
    numero = float(input("Digite um número: "))
    if numero >= 30 and numero <= 90:
        qtd_entre_30_e_90 += 1

print("Quantidade de números entre 30 e 90: ", qtd_entre_30_e_90)
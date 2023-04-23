opinioes = []
for i in range(20):
    op = input(f"Opinião da pessoa {i+1} (A, B ou C): ")
    opinioes.append(op)

# contagem das opiniões
a = b = c = 0
for op in opinioes:
    if op == 'A':
        a += 1
    elif op == 'B':
        b += 1
    elif op == 'C':
        c += 1

# cálculo das porcentagens
total = a + b + c
porc_a = a / total * 100
porc_b = b / total * 100
porc_c = c / total * 100

# ordenação das porcentagens
if porc_a <= porc_b and porc_a <= porc_c:
    menor = porc_a
    if porc_b <= porc_c:
        meio = porc_b
        maior = porc_c
    else:
        meio = porc_c
        maior = porc_b
elif porc_b <= porc_a and porc_b <= porc_c:
    menor = porc_b
    if porc_a <= porc_c:
        meio = porc_a
        maior = porc_c
    else:
        meio = porc_c
        maior = porc_a
else:
    menor = porc_c
    if porc_a <= porc_b:
        meio = porc_a
        maior = porc_b
    else:
        meio = porc_b
        maior = porc_a

print("As porcentagens são:", maior, meio, menor)
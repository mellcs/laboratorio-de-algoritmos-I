A = 0
B = 0
C = 0

for pessoal in range (1,21):
    option =  input("Qual jornal você lê? (A, B, e C)").upper()
    if option == "A":
        A = A += 1
    elif option == "B":
        B = B += 1
    elif option == "C":
        C = C += 1
    else:
        print("Insira uma opção válida.")
total = A + B + C
porcentagemA = (A / total) * 100
porcentagemB = (B / total) * 100
porcentagemC = (C / total) * 100

if porcentagemA <= porcentagemB and porcentagemA <= porcentagemC:
    menor = porcentagemA
    if porcentagemC <= porcentagemC:
        meio = porcentagemB
        maior = porcentagemC
    else:
        meio = porcentagemC
        maior = porcentagemB
elif porcentagemB <= porcentagemA and porcentagemB <= porcentagemC:
    menor = porcentagemB
    if porcentagemA <= porcentagemC:
        meio = porcentagemA
        maior = porcentagemC
    else:
        meio = porcentagemC
        maior = porcentagemA
else:
    menor = porcentagemC
    if porcentagemA <= porcentagemB:
        meio = porcentagemA
        maior = porcentagemB
    else:
        meio = porcentagemB
        maior = porcentagemA

print("As porcentagens são:", maior, meio, menor)
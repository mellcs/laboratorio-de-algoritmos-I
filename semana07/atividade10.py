ramos = int(input("Digite o número de ramos da árvore de Natal: "))

for i in range(1, ramos+1):
    for j in range(i):
        print("*", end="")
    print()

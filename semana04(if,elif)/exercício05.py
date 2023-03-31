print("Qual tipo de carteira de motorista você possui?")

print("A")
print("B")
print("C")
print("D")
print("E")

alternativa = input("Selecione uma alternativa:").upper()

if alternativa == "A":
    print("Você pode dirigir motos e triciclos!")
elif alternativa == "B":
    print("Você pode dirigir carros de passeio!")
elif alternativa == "C":
    print("Você pode dirigir veículos de carga!")
elif alternativa == "D":
    print("Você pode dirigir veículos com +8 passageiros!")
else:
    print("Você pode dirigir veículos com unidade acoplada!")
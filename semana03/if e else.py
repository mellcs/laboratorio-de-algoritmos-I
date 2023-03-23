n1 = float(input("Digite a nota da prova:"))
n2 = float(input("Digite a nota dos exercícios:"))

media = (n1*0.8) + (n2*0.2)

if media >= 7:
    print("Você está aprovado com média:" ,media, "!")
    print("Até o próximo semestre!")
else:
    print("Você está reprovado com media:" ,media, "!")
    print("Infelizmente, até o próximo semestre.")

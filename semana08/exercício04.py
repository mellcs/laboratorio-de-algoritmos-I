# ler 5 notas , fazer a média e diga se está aprovado (>= 7), recuperação ( 4<= e < 7) ou reprovado (< 4). usar três funções.

def aprovado():
    print("Você foi aprovado!")

def recuperação():
    print("Você está em recuperação.")

def reprovado():
    print("Você foi reprovado.")
    
def main():
    media = 0
    
    for n in range (0,5):
        nota = float(input("Digite a nota:"))
        media = media + nota
    media = media / 5

    if media >= 7:
        aprovado()
    elif media <= 4 and media <7:
        recuperação()
    elif media < 4:
        reprovado()

main()
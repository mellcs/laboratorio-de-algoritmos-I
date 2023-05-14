def receber_preferencias():
    elevadores = {'A': 0, 'B': 0, 'C': 0}
    for i in range(10):
        elevador = input("Qual elevador você mais utiliza? (A, B ou C): ")
        if elevador in elevadores:
            elevadores[elevador] += 1
        else:
            print("Elevador inválido. Tente novamente.")
            return receber_preferencias()
    return elevadores

def calcular_porcentagem(elevadores, total_pessoas):
    porcentagens = {}
    for elevador, total in elevadores.items():
        porcentagem = total * 100 / total_pessoas
        porcentagens[elevador] = porcentagem
    return porcentagens

def main():
    preferencias = receber_preferencias()
    total_pessoas = sum(preferencias.values())

    print("Total de pessoas por elevador:")
    for elevador, total in preferencias.items():
        porcentagens = calcular_porcentagem(preferencias, total_pessoas)
        print("Elevador", elevador + ":", total, "pessoas (" + str(porcentagens[elevador]) + "%)")

main()

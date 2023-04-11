# Inicializando as variáveis com zero
total_elevador_A = 0
total_elevador_B = 0
total_elevador_C = 0

# Loop para obter as respostas dos moradores
for i in range(10):
    elevador_usado = input("Qual elevador você utiliza com mais frequência? (A, B ou C): ")
    if elevador_usado == "A":
        total_elevador_A += 1
    elif elevador_usado == "B":
        total_elevador_B += 1
    elif elevador_usado == "C":
        total_elevador_C += 1
    else:
        print("Opção inválida. Digite A, B ou C.")

# Calculando o total de pessoas que usam cada elevador
total_geral = total_elevador_A + total_elevador_B + total_elevador_C

# Mostrando os resultados
print("Total de pessoas que usam o elevador A:", total_elevador_A, "({:.2f}% do total)".format((total_elevador_A/total_geral)*100))
print("Total de pessoas que usam o elevador B:", total_elevador_B, "({:.2f}% do total)".format((total_elevador_B/total_geral)*100))
print("Total de pessoas que usam o elevador C:", total_elevador_C, "({:.2f}% do total)".format((total_elevador_C/total_geral)*100))
def contadores():
    contador_1 = 0
    contador_2 = 0
    
    while contador_1 <= 10:
        numero = int(input("Insira um número:"))
        if numero > 100:
            contador_2 = contador_2 + 1
        contador_1 = contador_1 + 1
    return contador_2

def main():
    resultado = contadores()
    print ("Existem", resultado, "números maiores que 100.")
    
main()

#o input fica dentro do while nesse caso.
#precisa de return pq o processo se repete e é uma soma
#fazer resultado = x é sempre bom
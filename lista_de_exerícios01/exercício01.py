def soma (n1, n2):
    resultado = n1 + n2
    return resultado
    
def main ():
    n1 = int(input("Insira um número:"))
    n2 = int(input("Insira outro número:"))
    resultado = soma(n1, n2)
    print("-", resultado)
    
main()
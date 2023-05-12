#perguntar o valor, mostrar em decímetros, centímetros e milímetros.



def decimetro(numero):
    print(numero*10)
    
def centimetro(numero):
    print(numero*100)
    
def milimetro(numero):
    print(numero*1000)
    
def main():
    numero = int(input("Insira um número:"))
    decimetro(numero)
    centimetro(numero)
    milimetro(numero)
    
main()
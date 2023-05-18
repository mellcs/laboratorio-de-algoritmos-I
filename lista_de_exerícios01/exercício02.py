def verificacao(numero):
    if numero % 2 != 0:
        print("Ele é primo.")
    elif numero == 2:
        print("Ele é primo.")
    else:
        print("Ele não é primo.")
    
def main():
    numero = int(input("Insira um número para saber se ele é primo:"))
    if numero % 2 != 0:
        print("Ele é primo.")
    elif numero == 2:
        print("Ele é primo.")
    else:
        print("Ele não é primo.")

main()
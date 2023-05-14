maior = 0
menor = 0
soma_total = 0 
quantidade_mulheres = 0
idade = 0
sexo = 0
salario = 0


def maior_e_menor(idade):
    menor = maior = idade
    if maior < idade:
        maior = idade
    elif menor > idade:
        menor = idade
    
def media(soma_total):
    print(soma_total/10)
    
def mulheres(quantidade_mulheres, sexo):
    if sexo == "M" and salario <= 100:
        quantidade_mulheres = quantidade_mulheres + 1
        
def main():
    soma_total = 0
    quantidade_mulheres = 0
    maior = 0
    menor = 0
    idade = 0
    sexo = 0
    idade = int(input("Insira sua idade:"))
    sexo = input("Insira seu sexo:").upper()
    salario = float(input("Insira seu salário:"))
    soma_total = soma_total + salario
    print("A média salarial é:")
    media(soma_total)
    maior_e_menor(idade)
    mulheres(quantidade_mulheres, sexo)
    
main()
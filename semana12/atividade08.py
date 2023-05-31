def inserir_item(array):
    numero = int(input("Digite um número par para inserir: "))
    if numero % 2 == 0:
        array.append(numero)
        print("Número inserido com sucesso!")
    else:
        print("Erro: Apenas números pares são permitidos.")

def listar_itens(array):
    print("Itens no array:")
    for numero in array:
        print(numero)

def retirar_item(array):
    numero = int(input("Digite o número par que deseja retirar: "))
    found = False
    i = 0
    while i < len(array):
        if array[i] == numero:
            found = True
            array = array[:i] + array[i+1:]
            print("Número removido com sucesso!")
            break
        i += 1
    if not found:
        print("Erro: O número não está presente no array.")
    return array

def retirar_todos_itens(array):
    array = []
    print("Todos os itens foram removidos.")
    return array

def main():
    array = []

    while True:
        print("\nMENU:")
        print("1 - Inserir item")
        print("2 - Listar itens")
        print("3 - Retirar item")
        print("4 - Retirar todos os itens")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            inserir_item(array)
        elif opcao == 2:
            listar_itens(array)
        elif opcao == 3:
            array = retirar_item(array)
        elif opcao == 4:
            array = retirar_todos_itens(array)
        elif opcao == 5:
            print("Encerrando o programa...")
            return
        else:
            print("Opção inválida. Tente novamente.")

main()

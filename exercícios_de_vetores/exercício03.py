def inserir_item(vetor):
    item = input("Insira um item: ")
    vetor.append(item)
    print("Item inserido com sucesso!")

def retirar_item(vetor):
    if len(vetor) == 0:
        print("O vetor está vazio.")
        return
    indice = int(input("Insira o índice do item a ser removido: "))
    if indice < 0 or indice >= len(vetor):
        print("Índice inválido.")
        return
    item_removido = vetor.pop(indice)
    print("Item removido:", item_removido)

def listar_itens(vetor):
    if len(vetor) == 0:
        print("O vetor está vazio.")
    else:
        print("Itens no vetor:")
        for i in range(len(vetor)):
            print(i, "-", vetor[i])

def main():
    vetor = []
    opcao = 0
    while opcao != 4:
        print("\nMenu:")
        print("1 - Inserir item")
        print("2 - Retirar item")
        print("3 - Listar itens")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            inserir_item(vetor)
        elif opcao == 2:
            retirar_item(vetor)
        elif opcao == 3:
            listar_itens(vetor)
        elif opcao == 4:
            print("Encerrando o programa...")
        else:
            print("Opção inválida.")

main()

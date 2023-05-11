def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo += imposto
    return custo

# Exemplo de uso da função
taxa = 10  # 10% de imposto sobre vendas
preco_item = 100  # Custo do item antes do imposto

preco_final = somaImposto(taxa, preco_item)
print("O preço final do item, incluindo imposto, é de R$", preco_final)
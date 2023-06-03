print("Sistema de Vendas")
print("------------------------")
"""
banco de dados
"""
estoque = 10

produto = input('Digite o produto: ')
quantidade = int(input('Digite a quantidade: '))
precoDeVenda = float(input("Digite o preco de venda:"))

valorTotal = quantidade * precoDeVenda

print("Produto: ", produto)
print("Quantidade: ", quantidade)
print("Preco: ", precoDeVenda)
print("Valor Total da Venda: ", valorTotal)

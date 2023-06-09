print ("Sistema de Vendas")
print ("------------------------")
#banco de dados
estoque = 10
estoqueMin = 3
       
produto = input ('Digite o produto: ')
quantidade = int (input ('Digite a quantidade: '))
precoDeVenda = float (input ("Digite o preco de venda:"))

if quantidade>=estoque:
# 80 = 8 x 10
       valorTotal = quantidade * precoDeVenda
       print = estoque - quantidade
       # 2 < 3
       if estoque<estoqueMin:
           print ("estoque minimo atingido")
       print ("valor total da venda: " , valorTotal)
       

else:
    print ("Sem estoque para atender pedido")

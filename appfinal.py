import funcoesapp

iniciar = funcoesapp.iniciarfuncoes()

categoria = str(input('Digite o nome:'))
produto = str(input('Digite o produto:'))
cor = str(input('Digite a cor:'))
precocompra = float(input('Digite o preço de compra:'))
precovenda = float(input('Digite o preço de venda:'))
estoque = int(input('Digite a quantidade comprada:'))

iniciar.cadastroprodutos(categoria, produto, cor,
                         precocompra, precovenda, estoque)

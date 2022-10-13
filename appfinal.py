import funcoesapp 

iniciar = funcoesapp.iniciarfuncoes()

categoria = input('Digite o nome:')
produto = input('Digite o produto:')
cor = '5' 
precocompra = '4'
precovenda = '9' 
estoque = 5

iniciar.cadastroprodutos(categoria, produto, cor, precocompra, precovenda, estoque)


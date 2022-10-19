import pandas as pd
import addexcelmult


class iniciarfuncoes():

    def __init__(self):
        self.address = 'dados.xlsx'

    def cadastrarusuario(self, nome, email, telefone, cpf, endereco):  # Cadastro de usuarios
        self.nomeplanilha = 'CadastroUsuario'
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        df_usuario = pd.DataFrame({"Nome": [self.nome],
                                   "Email": [self.email],
                                   "Telefone": [self.telefone],
                                   "Cpf": [self.cpf],
                                   "Endereco": [self.endereco]})

        addexcelmult.addusuarioexcel(
            df_usuario, addexcelmult.lerplanilha(self.nomeplanilha))
        return

    # Cadastro de Produtos
    def cadastroprodutos(self, categoria, produto, cor, precocompra, precovenda, estoque):
        self.nomeplanilha = 'CadastroProduto'
        self.categoria = categoria
        self.produto = produto
        self.cor = cor
        self.precocompra = precocompra
        self.precovenda = precovenda
        self.estoque = estoque
        df_produto = pd.DataFrame({"id": [addexcelmult.gerarcodigoproduto()],
                                   "categoria": [self.categoria],
                                   "produto": [self.produto],
                                   "cor": [self.cor],
                                   "precocompra": [self.precocompra],
                                   "precovenda": [self.precovenda],
                                   "estoque": [self.estoque]})  # Tranformando os dados para um formato legível no excel

        addexcelmult.addprodutoexcel(
            df_produto, addexcelmult.lerplanilha(self.nomeplanilha))
        return

    def cadastrarvenda(self, categoria, produto, cor, qtd_vendida):
        self.nomeplanilha = 'Vendas'
        self.categoria = categoria
        self.produto = produto
        self.cor = cor
        self.qtd_vendida = qtd_vendida

        df_venda = pd.DataFrame({"categoria": [self.categoria],
                                 "produto": [self.produto],
                                 "cor": [self.cor],
                                 "qtd_venda": [self.qtd_vendida]}
                                )

        addexcelmult.cadastrarvenda(
            df_venda, addexcelmult.lerplanilha(self.nomeplanilha))
        return

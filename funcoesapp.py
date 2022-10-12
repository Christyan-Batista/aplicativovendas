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
                           "Email":[self.email],
                           "Telefone": [self.telefone],
                           "Cpf": [self.cpf],
                           "Endereco":[self.endereco]})

        
        addexcelmult.addusuarioexcel(df_usuario, addexcelmult.lerplanilha(self.nomeplanilha))

    def cadastroprodutos(self, categoria, produto, cor, precocompra, precovenda, estoque):  #Cadastro de Produtos
        self.nomeplanilha = 'CadastroProduto'
        self.categoria = categoria
        self.produto = produto
        self.cor = cor
        self.precocompra = precocompra
        self.precovenda = precovenda
        self.estoque = estoque
        df_produto = pd.DataFrame({"categoria": [self.categoria],
                                   "produto": [self.produto],
                                   "cor": [self.cor],
                                   "precocompra": [self.precocompra],
                                   "precovenda": [self.precovenda],
                                   "estoque": [self.estoque]})  #Tranformando os dados para um formato legível no excel
    

        addexcelmult.addprodutoexcel(df_produto, addexcelmult.lerplanilha(self.nomeplanilha))
        return


    def cadastrarvenda(self, categoria, produto, cor, qtd_vendida):
        self.nomeplanilha = 'CadastroVenda'
        self.categoria = categoria
        self.produto = produto
        self.cor = cor
        self.qtd_vendida = qtd_vendida

        df_venda = pd.DataFrame({"categoria": [self.categoria],
                                 "produto":[self.produto],
                                 "cor":[self.cor],
                                 "qtd_venda": [self.qtd_vendida]}
                                 )

        df_excelprod = pd.read_excel(self.address, sheet_name=self.nomeplanilha)

        addexcelmult.cadastrarvenda(df_venda, df_excelprod)
        


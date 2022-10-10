import pandas as pd
import addexcelmult

class iniciarfuncoes():

    def __init__(self):
        self.address = 'dados.xlsx'


    def cadastrarusuario(self, nome, email, telefone, cpf, endereco):
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
        df_excel = pd.read_excel(self.adress, sheet_name="CadastroUsuario")
        adicionarcadastro = pd.concat([df_excel, df], ignore_index=True)
        adicionarcadastro.to_excel(self.adress,sheet_name='CadastroUsuario', index=False)


    def cadastroprodutos(self, categoria, produto, cor, precocompra, precovenda):
        self.categoria = categoria
        self.produto = produto
        self.cor = cor
        self.precocompra = precocompra
        self.precovenda = precovenda
        df_produto = pd.DataFrame({"categoria": [self.categoria],
                                   "produto": [self.produto],
                                   "cor": [self.cor],
                                   "precocompra": [self.precocompra],
                                   "precovenda": [self.precovenda]})  #Tranformando os dados para um formato legível no excel
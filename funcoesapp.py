import pandas as pd
import addexcelmult

class iniciarfuncoes():

    def __init__(self):
        self.adress = "dados.xlsx"


    def cadastrarusuario(self, nome, email, telefone, cpf, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        df = pd.DataFrame({"Nome": [self.nome], 
                           "Email":[self.email],
                           "Telefone": [self.telefone],
                           "Cpf": [self.cpf],
                           "Endereco":[self.endereco]})
        df_excel = pd.read_excel(self.adress, sheet_name="CadastroUsuario")
        
        addexcelmult.addusuarioexcel(df, df_excel, self.adress)

        print(df)
        return

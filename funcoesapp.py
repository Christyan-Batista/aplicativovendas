import pandas as pd

class iniciarfuncoes():

    def __init__(self):
        self.adress = "dados.xlsx"


    def cadastrarusuario(self, nome, email, telefone, cpf, endereco):
        self.nome = name
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
        adicionarcadastro = pd.concat([df_excel, df], ignore_index=True)
        adicionarcadastro.to_excel(self.adress,sheet_name='CadastroUsuario', index=False)

        print(df)
        return

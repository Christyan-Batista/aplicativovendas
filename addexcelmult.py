import pandas as pd

arquivo_xml = 'dados.xlsx'

def addusuarioexcel(df, df_excel):  #Função que insere uma nova linha na planilha com o novo usuario
    resultado_concat = pd.concat([df_excel, df])

    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        resultado_concat.to_excel(writer, sheet_name='CadastroUsuario', index=False)
    return


def addprodutoexcel(df_prod, df_excel):  #Função que insere uma nova linha na planilha com o novo produto
    resultado_conc = pd.concat([df_excel, df_prod])
    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        resultado_conc.to_excel(writer, sheet_name='CadastroProduto', index=False)
    return


def cadastrarvenda(df_venda, df_excel_venda):
    resultado_concat = pd.concat([df_excel_venda, df_venda])
    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        resultado_concat.to_excel(writer, sheet_name='Vendas', index=False) #Adicionando a venda a folha de venda
    return


def lerplanilha(stringplanilha):  #Funcão que lê a planilha e retorna para determinado fim
    ler = pd.read_excel(arquivo_xml, sheet_name=stringplanilha)
    return ler


def gerarcodigoproduto():
    print()
    print()



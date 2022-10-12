import pandas as pd

arquivo_xml = 'dados.xlsx'

def addusuarioexcel(df, df_excel):  #Função que insere uma nova linha na planilha com o novo usuario
    resultado_concat = pd.concat([df_excel, df])

    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        resultado_concat.to_excel(writer, sheet_name='CadastroUsuario', index=False)
    return


def addprodutoexcel(df_prod, df_excel):  #Função que insere uma nova linha na planilha com o novo produto
    resultado_concat = pd.concat([df_excel, df_prod])
    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        resultado_concat.to_excel(writer, sheet_name='CadastroProduto', index=False)
    return



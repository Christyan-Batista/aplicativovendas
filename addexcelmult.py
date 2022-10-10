import pandas as pd

def addusuarioexcel(df, df_excel, arquivo_xml):
    resultado_concat = pd.concat([df_excel, df])
    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace ') as writer:
        resultado_concat.to_excel(writer, sheet_name='CadastroUsuario')
    return

def addprodutoexcel():
    print()
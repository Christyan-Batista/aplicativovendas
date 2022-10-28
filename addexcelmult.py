import pandas as pd
from random import randint

arquivo_xml = 'dados.xlsx'


# Função que insere uma nova linha na planilha com o novo usuario
def addusuarioexcel(df, df_excel):
    
    planilha_usuario, f_ou_v = verificausuario(df)
    
    if f_ou_v:
        escrever_excel(planilha_usuario, 'CadastroUsuario')

    else:
        resultado_concat = pd.concat([df_excel, df])
        escrever_excel(resultado_concat, 'CadastroUsuario')

    return


# Função que insere uma nova linha na planilha com o novo produto
def addprodutoexcel(df_prod, df_excel):
    # Como a função verificaplanilha recebe 3 return, preciso passar 3 variáveis para os valores serem atribuidos.
    df_prod, verifica, num = verificaplanilha(df_prod)
    if verifica:  # É verdadeiro se o confirma for 1, logo, ele soma com o valor já existente de estoque
        df_excel['estoque'][num] = df_prod['estoque']
        # Apenas substitui linha existente no excel

        escrever_excel(df_excel, 'CadastroProduto')

    else:
        resultado_conc = pd.concat([df_excel, df_prod])
        # Adiciona uma nova linha comn o mesmo id
        escrever_excel(resultado_conc, 'CadastroProduto')

    return


def cadastrarvenda(df_venda, df_excel_venda):
    resultado_concat = pd.concat([df_excel_venda, df_venda])

    escrever_excel(resultado_concat, 'Vendas')

    return


def lerplanilha(stringplanilha):  # Funcão que lê a planilha e retorna para determinado fim
    ler = pd.read_excel(arquivo_xml, sheet_name=stringplanilha)
    return ler


# Função que verifica condições de estoque e precocompra / precovenda
def verificaplanilha(df_produto):
    confirma = None
    ler = lerplanilha('CadastroProduto')
    # Laço para verificar as linhas da planilha de acordo com cada categoria atribuiada a "c"
    for num, c in enumerate(ler['categoria']):

        if df_produto['categoria'][0] == c:
            # iloc é uma função do pandas para retornar uma linha específica de um DataFrame. OBS: RETORNA UMA TUPLA
            verificar = ler.iloc[num]

            # Os 4 if's abaixo garantem que o que eu estou cadastrando é igual a linha que a função verificar leu!
            if verificar[0] == df_produto['categoria'][0]:
                if verificar[1] == df_produto['produto'][0]:
                    if verificar[2] == df_produto['cor'][0]:
                        if verificar[3] == df_produto['precocompra'][0] and verificar[4] == df_produto['precovenda'][0]:
                            # Ele soma com o valor já existente de estoque
                            df_produto['estoque'][0] += ler['estoque'][num]
                            confirma = 1
                            break
                        else:
                            # Atribui o valor id de um id já existente
                            df_produto['id'][0] = ler['id'][num]
                            confirma = 0
                            break

    # Se confirma = 1, o estoque foi mudado. Se confirma = 0, deve-se adicionar uma nova linha e manter o id existente
    # Num retorna a linha que eu estou trabalhando
    return df_produto, confirma, num


def gerarcodigoproduto():
    gerarId = randint(1000, 9999)

    try:
        lerId = pd.read_excel(arquivo_xml, sheet_name='CadastroProduto')['id']
    except:
        return gerarId

    while True:
        if gerarId in lerId:
            gerarId = randint(1000, 9999)
        else:
            break

    return gerarId


def verificausuario(df_usuario):
    planilha_usuario = lerplanilha('CadastroUsuario') #retorna a planilha do excel
    f_ou_v = False

    for num, c in enumerate(planilha_usuario['Cpf']): #laço para ler as colunas dos cpf's
        
        if c == df_usuario['Cpf'][0]:
            f_ou_v = True
            planilha_usuario['Email'][num] = df_usuario['Email'][0]
            planilha_usuario['Telefone'][num] = df_usuario['Telefone'][0]
            planilha_usuario['Endereco'][num] = df_usuario['Endereco'][0]

        else:
            f_ou_v = False
    
    return planilha_usuario, f_ou_v


def escrever_excel(valorescrito, nome_planilha):
    with pd.ExcelWriter(arquivo_xml, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        valorescrito.to_excel(writer, sheet_name=nome_planilha, index=False)
    return
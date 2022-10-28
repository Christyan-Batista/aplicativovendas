import funcoesapp
import PySimpleGUI as sg

class aplicacao():
    
    def __init__(self):
        self.janela_menu = self.janela_principal()
        self.janela_usuario = None
        self.janela_venda = None
        self.janela_produto = None

        self.inicializar_lib = funcoesapp.iniciarfuncoes()

        while True:
            self.janela, self.evento, self.valor = sg.read_all_windows()

            if self.evento == sg.WIN_CLOSED:
                self.janela.close()
                if self.janela == self.janela_usuario:
                    self.janela_usuario = None
                if self.janela == self.janela_venda:
                    self.janela_venda = None
                if self.janela == self.janela_produto:
                    self.janela_produto = None
                if self.janela == self.janela_menu:
                    break
            
            if self.janela == self.janela_menu and self.evento == 'Usuario':
                self.janela_usuario = self.janela_cad_usuario()

            if self.janela == self.janela_usuario and self.evento == 'cadastrar':
                self.inicializar_lib.cadastrarusuario(str(self.valor['nome']),
                                                      str(self.valor['email']),
                                                      str(self.valor['telefone']),
                                                      str(self.valor['cpf']),
                                                      str(self.valor['endereço']),)

            if self.janela == self.janela_menu and self.evento == 'Produto':
                self.janela_produto = self.janela_cad_produto()
            
            if self.janela == self.janela_produto and self.evento == 'cadastrar':
                self.inicializar_lib.cadastroprodutos(str(self.valor['categoria']),
                                                      str(self.valor['produto']),
                                                      str(self.valor['cor']),
                                                      float(self.valor['precocompra']),
                                                      float(self.valor['precovenda']),
                                                      int(self.valor['estoque']),)

            if self.janela == self.janela_menu and self.evento == 'Vendas':
                self.janela_venda = self.janela_cad_vendas()
            
            if self.janela == self.janela_venda and self.evento == 'cadastrar':
                self.inicializar_lib.cadastrarvenda(str(self.valor['categoria']),
                                                      str(self.valor['produto']),
                                                      str(self.valor['cor']),
                                                      int(self.valor['quantidade']),
                                                      float(self.valor['precovenda']),
                                                      str(self.valor['data']),)


    def janela_principal(self):
        self.layout_menu =  [[sg.Button('Cadastrar Usuario',expand_x=True,size=(0,2),key='Usuario')],
                             [sg.Button('Cadastrar Produto', expand_x=True,size=(0,2), key='Produto')],
                             [sg.Button('Cadastrar Venda', expand_x=True,size=(0,2), key='Vendas')]
                            ]

        return sg.Window('Aplicativo Vendas', self.layout_menu, resizable=True, size=(300, 200), 
                        background_color='black', finalize=True)

    
    def janela_cad_usuario(self):

        self.layout_coluna_usuario1 = [[sg.Text('Nome', background_color='black')],
                                      [sg.Text('Email',background_color='black')],
                                      [sg.Text('Telefone',background_color='black')],
                                      [sg.Text('CPF',background_color='black')],
                                      [sg.Text('Endereço',background_color='black')]
                                     ]
        
        self.layout_coluna_usuario2 = [[sg.Input(key='nome')],
                                       [sg.Input(key='email')],
                                       [sg.Input(key='telefone')],
                                       [sg.Input(key='cpf')],
                                       [sg.Input(key='endereço')]
                                      ]

        self.layout_usuario = [
                               [sg.Column(self.layout_coluna_usuario1, background_color='black'), 
                                sg.Column(self.layout_coluna_usuario2,background_color='black')],
                                [sg.Button('Cadastrar', key='cadastrar')]]

        return sg.Window('Cadastrar Usuario', self.layout_usuario, resizable=True, size=(450, 200), 
                        background_color='black', finalize=True)



    def janela_cad_produto(self):

        self.layout_coluna_usuario3 = [[sg.Text('Categoria', background_color='black')],
                                      [sg.Text('Produto',background_color='black')],
                                      [sg.Text('Cor',background_color='black')],
                                      [sg.Text('Preço Compra',background_color='black')],
                                      [sg.Text('Preço Venda',background_color='black')],
                                      [sg.Text('Estoque',background_color='black')]
                                     ]
        
        self.layout_coluna_usuario4 = [[sg.Input(key='categoria')],
                                       [sg.Input(key='produto')],
                                       [sg.Input(key='cor')],
                                       [sg.Input(key='precocompra')],
                                       [sg.Input(key='precovenda')],
                                       [sg.Input(key='estoque')]
                                      ]

        self.layout_usuario2 = [
                               [sg.Column(self.layout_coluna_usuario3, background_color='black'), 
                                sg.Column(self.layout_coluna_usuario4,background_color='black')],
                                [sg.Button('Cadastrar', key='cadastrar')]]

        return sg.Window('Cadastrar Produto', self.layout_usuario2, resizable=True, size=(450, 200), 
                        background_color='black', finalize=True)


    def janela_cad_vendas(self):

        self.layout_coluna_usuario5 = [[sg.Text('Categoria', background_color='black')],
                                      [sg.Text('Produto',background_color='black')],
                                      [sg.Text('Cor',background_color='black')],
                                      [sg.Text('Quantidade',background_color='black')],
                                      [sg.Text('Preço Venda',background_color='black')],
                                      [sg.Text('Data (DD/MM/AAAA)',background_color='black')],
                                     ]
        
        self.layout_coluna_usuario6 = [[sg.Input(key='categoria')],
                                       [sg.Input(key='produto')],
                                       [sg.Input(key='cor')],
                                       [sg.Input(key='quantidade')],
                                       [sg.Input(key='precovenda')],
                                       [sg.Input(key='data')]
                                      ]

        self.layout_usuario3 = [
                               [sg.Column(self.layout_coluna_usuario5, background_color='black'), 
                                sg.Column(self.layout_coluna_usuario6,background_color='black')],
                                [sg.Button('Cadastrar', key='cadastrar')]]

        return sg.Window('Cadastrar Venda', self.layout_usuario3, resizable=True, size=(450, 200), 
                        background_color='black', finalize=True)

iniciar = aplicacao()
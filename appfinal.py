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
                self.inicializar_lib.cadastrarusuario(self.valor['nome'],
                                                      self.valor['email'],
                                                      self.valor['telefone'],
                                                      self.valor['cpf'],
                                                      self.valor['endereço'])


    def janela_principal(self):
        self.layout_menu =  [[sg.Button('Cadastrar Usuario',expand_x=True,size=(0,2),key='Usuario')],
                             [sg.Button('Cadastrar Produto', expand_x=True,size=(0,2), key='Produto')],
                             [sg.Button('Cadastrar Venda', expand_x=True,size=(0,2), key='Vendas')]
                            ]

        return sg.Window('Aplicativo Vendas', self.layout_menu, resizable=True, size=(300, 200), 
                        background_color='black', finalize=True)

    
    def janela_cad_usuario(self):

        self.layout_coluna_usuario1 = [[sg.Text('Nome', background_color='black')],
                                      [sg.Text('Email')],
                                      [sg.Text('Telefone')],
                                      [sg.Text('CPF')],
                                      [sg.Text('Endereço')]
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

iniciar = aplicacao()
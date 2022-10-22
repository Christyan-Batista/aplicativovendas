import funcoesapp

iniciar = funcoesapp.iniciarfuncoes()

usuario = str(input('Nome:'))
cpf = str(input('Cpf:'))
email = str(input('Email:'))
tel = str(input('Telefone:'))
endereco = str(input('Endereco:'))

iniciar.cadastrarusuario(usuario, email, tel, cpf, endereco)

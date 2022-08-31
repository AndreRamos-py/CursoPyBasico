usuario_tt = 'Fulano'
senha_tt = '12345f'

usuario = input('Qual é o seu usuário? ')
senha = input('Qual é a sua senha? ')

if usuario == usuario_tt and senha == senha_tt:
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorretos.')

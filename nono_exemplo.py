"""
LOGIN SIMPLES
"""

usuario_correto = "admin"
senha_correta = "1234"

while True:
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Usuário ou senha incorretos! Tente novamente.")
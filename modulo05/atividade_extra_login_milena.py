# Dicionário com usuários e senhas
usuarios = {

    "admin": "1234",

    "milena": "senha123",

    "joao": "abc123"
}


# Função para validar login
def validar_login(usuario, senha):

    if usuario in usuarios and usuarios[usuario] == senha:

        return True

    else:

        return False


# Sistema de login
print("=== LOGIN ===")

usuario = input("Usuário: ")

senha = input("Senha: ")


# Verificação
if validar_login(usuario, senha):

    print("Login realizado com sucesso!")

else:

    print("Usuário ou senha incorretos.")
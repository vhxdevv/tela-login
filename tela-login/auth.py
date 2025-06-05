import json

def autenticar_usuario(usuario, senha):
    try:
        with open('users.json', 'r') as arquivo:
            usuarios = json.load(arquivo)
        return usuarios.get(usuario) == senha
    except FileNotFoundError:
        return False
    
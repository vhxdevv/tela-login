import json

def carregar_usuario():
    try:
        with open("user.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def cadastrar_usuario(novo_usuario, nova_senha):
    usuarios = carregar_usuario()

    if novo_usuario in usuarios:
        return False #Ja existe
    else:
        usuarios[novo_usuario] = nova_senha
        with open("users.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        return True #Cadastro feito
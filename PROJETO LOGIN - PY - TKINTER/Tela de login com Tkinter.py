#Tela de login com Tkinter

import customtkinter

#Janela principal
app = customtkinter.CTk()
app.title("Tela de Login")
app.geometry("400x300")

#Cria um rotulo(Label) para o titulo
rotulo_titulo = customtkinter.CTkLabel(app, text=("Login"), font=("Arial", 16))
rotulo_titulo.pack(pady=20)   #define espaçamento

#Campo de entrada do usuario
entrada_usuario = customtkinter.CTkEntry(app, placeholder_text=("Nome do Usuario"))
entrada_usuario.pack(pady=10)

#Campo de entrada da senha
entrada_senha = customtkinter.CTkEntry(app, placeholder_text=("Senha"), show="*")
entrada_senha.pack(pady=10)

#Botão para o login
botao_login = customtkinter.CTkButton(app, text=("Fazer login"), command=lambda: login_action(entrada_usuario.get(), entrada_senha.get()))
botao_login.pack(pady=20)

#Função para Botão de login
def login_action(usuario, senha):
    print(f"Nome de usuário: {usuario}, Senha: {senha}")
    if usuario == "usuario" and senha == "senha":
        print("Login efetuado com sucesso!")
    else:
        print("Usuario ou senha incorretos")


app.mainloop()
 
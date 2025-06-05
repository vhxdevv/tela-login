import customtkinter
from auth import autenticar_usuario # type: ignore

def criar_interface():
    app = customtkinter.CTk()
    app.title("Tela de Login")
    app.geometry("400x300")

    def login_action():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if autenticar_usuario(usuario, senha):
            rotulo_mensagem.configure(text="Login efetuado com sucesso!", text_color="green")
        else:
            rotulo_mensagem.configure(text="Usuário ou senha incorretos", text_color="red")

    rotulo_titulo = customtkinter.CTkLabel(app, text="Login", font=("Arial", 16))
    rotulo_titulo.pack(pady=20)

    entrada_usuario = customtkinter.CTkEntry(app, placeholder_text="Nome do Usuário")
    entrada_usuario.pack(pady=10)

    entrada_senha = customtkinter.CTkEntry(app, placeholder_text="Senha", show="*")
    entrada_senha.pack(pady=10)

    botao_login = customtkinter.CTkButton(app, text="Fazer login", command=login_action)
    botao_login.pack(pady=20)

    rotulo_mensagem = customtkinter.CTkLabel(app, text="")
    rotulo_mensagem.pack()

    app.mainloop()

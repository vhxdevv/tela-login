import customtkinter
from auth import autenticar_usuario # type: ignore

def criar_interface():
    app = customtkinter.CTk()
    app.title("Tela de Login")
    app.geometry("400x300")
    app.configure(fg_color="#1e1e1e")

    def login_action():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if autenticar_usuario(usuario, senha):
            rotulo_mensagem.configure(text="Login efetuado com sucesso!", text_color="green")
        else:
            rotulo_mensagem.configure(text="Usuário ou senha incorretos", text_color="red")

    # Frame com contorno arredondado
    frame_login = customtkinter.CTkFrame(app, corner_radius=20, fg_color="#1e1e1e", width=350, height=400)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")  # centraliza na janela

    rotulo_titulo = customtkinter.CTkLabel(app, text="Faça Login na sua conta", font=("OpenSans_Condensed-Italic", 20), text_color="white")
    rotulo_titulo.pack(pady=20)

    entrada_usuario = customtkinter.CTkEntry(app, placeholder_text="Nome do Usuário", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_usuario.pack(pady=5)

    entrada_senha = customtkinter.CTkEntry(app, placeholder_text="Senha", show="*", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_senha.pack(pady=10)

    esqueceu_senha = customtkinter.CTkLabel(app, text="Esqueceu a senha?", font=("OpenSans_Condensed-Italic", 10),text_color="#327058", cursor="hand2")
    esqueceu_senha.pack(pady=(3, 10))
    esqueceu_senha.bind("<Button-1>", lambda e: print("Recuperação de senha"))


    botao_login = customtkinter.CTkButton(app, text="Fazer login", fg_color="#00BE75", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12), command=login_action)
    botao_login.pack(pady=(15, 15))

    rotulo_mensagem = customtkinter.CTkLabel(app, text="")
    rotulo_mensagem.pack()

    app.mainloop()

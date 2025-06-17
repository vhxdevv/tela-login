import customtkinter
from users_py import cadastrar_usuario # type: ignore

def tela_registro():
    reg = customtkinter.CTk()
    reg.title("Tela de registro")
    reg.geometry("300x300")
    reg.configure(fg_color="#1e1e1e")

    def registrar():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuario == "" or senha == "":
            rotulo_mensagem.configure(text= "Preencha todos os campos!", text_color="red")
        else:
            sucesso = cadastrar_usuario(usuario, senha)
            if sucesso:
               rotulo_mensagem.configure(text= "Registro feito com sucesso!", text_color="green")
            else:
                rotulo_mensagem.configure(text= "Usuario ja existe!", text_color="red")

    rotulo_titulo = customtkinter.CTkLabel(reg, text="Faça seu registro", font=("OpenSans_Condensed-Italic", 20), text_color="white")
    rotulo_titulo.pack(pady=10)

    entrada_usuario = customtkinter.CTkEntry(reg, placeholder_text="Digite um nome de usuario", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_usuario.pack(pady=10)

    entrada_senha = customtkinter.CTkEntry(reg, placeholder_text="Digite a senha", show="*", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_senha.pack(pady=10)

    botao_registro = customtkinter.CTkButton(reg, text="Registrar-se", fg_color="#00BE75", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12), command=registrar)
    botao_registro.pack(pady=20)

    rotulo_mensagem = customtkinter.CTkLabel(reg, text="")
    rotulo_mensagem.pack()

    reg.mainloop()
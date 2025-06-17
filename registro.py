import customtkinter

def register_action():
    reg = customtkinter.CTk()
    reg.title("Tela de registro")
    reg.geometry("300x250")
    reg.configure(fg_color="#1e1e1e")

    def registrar():
        rotulo_mensagem.configure(text="Conta registrada com sucesso!", text_color="green")

    rotulo_titulo = customtkinter.CTkLabel(reg, text="Faça seu registro", font=("OpenSans_Condensed-Italic", 20), text_color="white")
    rotulo_titulo.pack(pady=10)

    entrada_email = customtkinter.CTkEntry(reg, placeholder_text="Digite um nome de usuario", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_email.pack(pady=10)

    entrada_senha = customtkinter.CTkEntry(reg, placeholder_text="Digite a senha", show="*", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    entrada_senha.pack(pady=10)

    botao_registro = customtkinter.CTkButton(reg, text="Registrar-se", fg_color="#00BE75", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12), command=registrar)
    botao_registro.pack(pady=20)

    rotulo_mensagem = customtkinter.CTkLabel(reg, text="")
    rotulo_mensagem.pack()

    reg.mainloop()
import customtkinter
import json


def carregar_usuario():
    try:
        with open("users.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def salvar_usuarios(usuarios):
    with open('users.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def esq_senha():
    esq = customtkinter.CTk()
    esq.title("Esqueceu a senha")
    esq.geometry("350x300")
    esq.configure(fg_color="#1e1e1e")

    usuarios = carregar_usuario()

    frame = customtkinter.CTkFrame(esq, fg_color="transparent")
    frame.pack(pady=20)

    rotulo_esq = customtkinter.CTkLabel(frame, text="Digite seu usuário!", font=("OpenSans_Condensed-Italic", 20), text_color="white")
    rotulo_esq.grid(row=0, column=0, pady=10)

    ent_usuario = customtkinter.CTkEntry(frame, placeholder_text="Usuário", fg_color="#272727", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
    ent_usuario.grid(row=1, column=0, pady=10)

    mensagem = customtkinter.CTkLabel(frame, text="", text_color="white")
    mensagem.grid(row=3, column=0, pady=10)

    ent_nova_senha = None

    def verificar_usuario():
        nonlocal ent_nova_senha

        usuario = ent_usuario.get()

        if usuario in usuarios:
            rotulo_esq.configure(text="Digite sua nova senha!")

            if not ent_nova_senha:
                ent_nova_senha = customtkinter.CTkEntry(frame, placeholder_text="Nova senha", fg_color="#272727", show="*", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12))
                ent_nova_senha.grid(row=2, column=0, pady=10)

            botao_esq.configure(text="Alterar Senha", command=alterar_senha)
            mensagem.configure(text="")
        else:
            mensagem.configure(text="Usuário não encontrado!", text_color="red")

    def alterar_senha():
        nova_senha = ent_nova_senha.get()

        if nova_senha.strip() == "":
            mensagem.configure(text="Senha não pode ser vazia!", text_color="red")
            return

        usuarios[ent_usuario.get()] = nova_senha
        salvar_usuarios(usuarios)

        mensagem.configure(text="Senha alterada com sucesso!", text_color="green")
        esq.after(2000, esq.destroy)

    botao_esq = customtkinter.CTkButton(frame, text="Confirmar", fg_color="#00BE75", width=220, height=30, corner_radius=10, font=("OpenSans_Condensed-Italic", 12), command=verificar_usuario)
    botao_esq.grid(row=4, column=0, pady=15)

    esq.mainloop()

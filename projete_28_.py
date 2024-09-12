import tkinter as tk
from tkinter import messagebox
import datetime as dt
import hashlib
import google.generativeai as genai

# Lista global de cadastros
lista_cadastros = []

# Lista global de matérias
lista_materias = []

# Lista global de resumos
lista_resumos = []


def criar_cadastro():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    if not nome or not email or not senha or not confirmar_senha:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas são diferentes")
        return

    # Hash da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Colocando data e hora no cadastro
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

    # Adicionando cadastro à lista
    cadastros = len(lista_cadastros) + 1
    cadastros_str = f"cadastro-{cadastros}"
    lista_cadastros.append((cadastros_str, nome, email, senha_hash, data_criacao))

    # Salvar informações no arquivo
    salvar_cadastro_no_arquivo(nome, email, senha_hash, data_criacao)

    # Limpar tudo depois de cadastrar
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)

    # Mensagem de sucesso
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Fecha a janela de cadastro e abre a janela inicial
    janela_cadastro.destroy()
    criar_janela_login()

def salvar_cadastro_no_arquivo(nome, email, senha_hash, tempo):
    # Salvar informações no arquivo
    with open('arquivos_salvos.txt', 'a') as arquivo:  # Mudar para 'a' para adicionar ao final
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Senha (hash): {senha_hash}\n")
        arquivo.write(f"Data e Hora: {tempo}\n")
        arquivo.write("="*40 + "\n")  # Linha separadora para melhor leitura

def criar_janela_cadastro():
    global entry_nome, entry_email, entry_senha, entry_confirmar_senha, janela_cadastro
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro de Usuário")

    tk.Label(janela_cadastro, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.pack(pady=5)

    tk.Label(janela_cadastro, text="Email:").pack(pady=5)
    entry_email = tk.Entry(janela_cadastro)
    entry_email.pack(pady=5)

    tk.Label(janela_cadastro, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.pack(pady=5)

    tk.Label(janela_cadastro, text="Confirmar Senha:").pack(pady=5)
    entry_confirmar_senha = tk.Entry(janela_cadastro, show="*")
    entry_confirmar_senha.pack(pady=5)

    tk.Button(janela_cadastro, text="Cadastrar", command=criar_cadastro).pack(pady=20)

    janela_cadastro.mainloop()


def fazer_login():
    email = entry_email_login.get()
    senha = entry_senha_login.get()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    for cadastro in lista_cadastros:
        if cadastro[2] == email and cadastro[3] == senha_hash:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            janela_login.destroy()
            criar_janela_inicial()
            return

    messagebox.showerror("Erro", "Email ou senha incorretos")

def criar_janela_login():
    global entry_email_login, entry_senha_login, janela_login

    janela_login = tk.Toplevel()
    janela_login.title('Login')

    label_email = tk.Label(janela_login, text="Email")
    label_email.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_email_login = tk.Entry(janela_login)
    entry_email_login.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_senha = tk.Label(janela_login, text="Senha")
    label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha_login = tk.Entry(janela_login, show='*')
    entry_senha_login.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_login = tk.Button(janela_login, text="Fazer login", command=fazer_login)
    botao_login.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_login.transient(janela_principal)
    janela_login.grab_set()
    janela_principal.wait_window(janela_login)

def criar_materia():
    titulo = entry_materia.get()
    corpo = entry_texto.get()

    if not titulo or not corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    # Salvar matéria na lista de matérias
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")
    lista_materias.append((titulo, corpo, data_criacao))

    messagebox.showinfo("Sucesso", "Matéria criada com sucesso!")
    janela_materia.destroy()

def criar_janela_materia():
    global entry_materia, entry_texto, janela_materia

    janela_materia = tk.Toplevel()
    janela_materia.title('Criar Matéria')

    label_materia = tk.Label(janela_materia, text="Título da matéria")
    label_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_materia = tk.Entry(janela_materia)
    entry_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_texto = tk.Label(janela_materia, text="Corpo da matéria")
    label_texto.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_texto = tk.Entry(janela_materia)
    entry_texto.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_materia = tk.Button(janela_materia, text="Criar Matéria", command=criar_materia)
    botao_materia.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_materia.transient(janela_inicial)
    janela_materia.grab_set()
    janela_inicial.wait_window(janela_materia)

def acessar_materia():
    if not lista_materias:
        messagebox.showinfo("Informação", "Nenhuma matéria disponível")
        return

    janela_acessar_materia = tk.Toplevel()
    janela_acessar_materia.title('Acessar Matéria')

    for i, materia in enumerate(lista_materias, start=1):
        titulo, corpo, data = materia
        tk.Label(janela_acessar_materia, text=f"Matéria {i}").pack()
        tk.Label(janela_acessar_materia, text=f"Título: {titulo}").pack()
        tk.Label(janela_acessar_materia, text=f"Data: {data}").pack()
        tk.Label(janela_acessar_materia, text=f"Corpo: {corpo}").pack()
        tk.Label(janela_acessar_materia, text="").pack()  # Espaçamento

        # Botão para editar a matéria
        botao_editar = tk.Button(janela_acessar_materia, text="Editar",          command=lambda i=i: criar_janela_editar_materia(i))
        botao_editar.pack(padx=10, pady=5, fill=tk.BOTH)

        # Botão para deletar a matéria
        botao_deletar = tk.Button(janela_acessar_materia,                        text="Deletar", command=lambda i=i: deletar_materia(i))
        botao_deletar.pack(padx=10, pady=5, fill=tk.BOTH)

def deletar_materia(index):
    if messagebox.askyesno("Confirmar", "Você tem certeza de que deseja deletar esta matéria?"):
        lista_materias.pop(index - 1)  # Remove a matéria da lista
        messagebox.showinfo("Sucesso", "Matéria deletada com sucesso!")
        janela_acessar_materia.destroy()  # Fecha a janela de acesso à matéria
        
def criar_janela_editar_materia(index):
    global entry_editar_materia, entry_editar_texto, janela_editar_materia

    janela_editar_materia = tk.Toplevel()
    janela_editar_materia.title('Editar Matéria')

    titulo, corpo, _ = lista_materias[index - 1]

    label_editar_materia = tk.Label(janela_editar_materia, text="Título da matéria")
    label_editar_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_editar_materia = tk.Entry(janela_editar_materia)
    entry_editar_materia.insert(0, titulo)
    entry_editar_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_editar_texto = tk.Label(janela_editar_materia, text="Corpo da matéria")
    label_editar_texto.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_editar_texto = tk.Entry(janela_editar_materia)
    entry_editar_texto.insert(0, corpo)
    entry_editar_texto.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_editar = tk.Button(janela_editar_materia, text="Salvar Alterações", command=lambda: editar_materia(index))
    botao_editar.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_editar_materia.transient(janela_inicial)
    janela_editar_materia.grab_set()
    janela_inicial.wait_window(janela_editar_materia)

def editar_materia(index):
    novo_titulo = entry_editar_materia.get()
    novo_corpo = entry_editar_texto.get()

    if not novo_titulo or not novo_corpo:
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    lista_materias[index - 1] = (novo_titulo, novo_corpo, lista_materias[index - 1][2])

    messagebox.showinfo("Sucesso", "Matéria editada com sucesso!")
    janela_editar_materia.destroy()

def criar_janela_inicial():
    global janela_inicial

    janela_inicial = tk.Toplevel()
    janela_inicial.title('Bem-vindo(a)')

    botao_criar_materia = tk.Button(janela_inicial, text="Criar matéria", command=criar_janela_materia)
    botao_criar_materia.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_acessar_materia = tk.Button(janela_inicial, text="Acessar matérias", command=acessar_materia)
    botao_acessar_materia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_acessar_IA = tk.Button(janela_inicial, text="Acessar IA", command=criar_janela_IA)
    botao_acessar_IA.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_sair = tk.Button(janela_inicial, text="Sair", command=janela_inicial.destroy)
    botao_sair.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

def fazer_pergunta():
    model = genai.GenerativeModel('gemini-pro')

    GOOGLE_API_KEY=userdata.get('AIzaSyCQrLB1H6vCvfA-y_if_SoyKrwv3qC4aBM')
    genai.configure(api_key=GOOGLE_API_KEY)


def criar_janela_IA():
    global entry_pergunta, janela_IA

    janela_IA = tk.Toplevel()
    janela_IA.title('Inteligência Artificial')

    label_ia = tk.Label(janela_IA, text="Faça uma pergunta à IA")
    label_ia.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    entry_pergunta = tk.Entry(janela_IA)
    entry_pergunta.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    botao_perguntar = tk.Button(janela_IA, text="Perguntar", command=fazer_pergunta)
    botao_perguntar.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_IA.transient(janela_inicial)
    janela_IA.grab_set()
    janela_inicial.wait_window(janela_IA)


def iniciar_aplicacao():
    global janela_principal

    janela_principal = tk.Tk()
    janela_principal.title(' koala Helper ')

    label_bemvindo = tk.Label(janela_principal, text="Bem-vindo ao koala Helper")
    label_bemvindo.pack(padx=10, pady=10)

    botao_cadastrar = tk.Button(janela_principal, text="Cadastrar", command=criar_janela_cadastro)
    botao_cadastrar.pack(padx=10, pady=10, fill=tk.BOTH)

    botao_login = tk.Button(janela_principal, text="Login", command=criar_janela_login)
    botao_login.pack(padx=10, pady=10, fill=tk.BOTH)

    janela_principal.mainloop()

# Iniciar a aplicação
iniciar_aplicacao()
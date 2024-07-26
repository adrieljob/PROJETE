import tkinter as tk
from tkinter import messagebox
import datetime as dt
import hashlib

# Lista global de cadastros
lista_cadastros = []

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

    # hash da senha
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Colocando data e hora no cadastro
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

    # Adicionando cadastro à lista
    cadastros = len(lista_cadastros) + 1
    cadastros_str = f"cadastro-{cadastros}"
    lista_cadastros.append((cadastros_str, nome, email, senha_hash, data_criacao))

    # Limpar tudo depois de cadastrar
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)

    # caixinha bonitinha pra mostrar que o cadastro foi realizado com sucesso
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Fecha a janela de cadastro e abre a janela inicial
    janela_cadastro.destroy()
    criar_janela_inicial()

def criar_janela_cadastro():
    global entry_nome, entry_email, entry_senha, entry_confirmar_senha, janela_cadastro

    janela_cadastro = tk.Toplevel()  # Cria uma janela secundária
    janela_cadastro.title('Cadastro')

    # Nome de usuário
    label_nome = tk.Label(janela_cadastro, text="Nome de usuário")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Email
    label_email = tk.Label(janela_cadastro, text="Email")
    label_email.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_email = tk.Entry(janela_cadastro)
    entry_email.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Senha
    label_senha = tk.Label(janela_cadastro, text="Senha")
    label_senha.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha = tk.Entry(janela_cadastro, show='*')
    entry_senha.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Confirmar senha
    label_confirmar_senha = tk.Label(janela_cadastro, text="Confirmar senha")
    label_confirmar_senha.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_confirmar_senha = tk.Entry(janela_cadastro, show='*')
    entry_confirmar_senha.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    # Botão para cadastrar
    botao_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", command=criar_cadastro)
    botao_cadastrar.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    janela_cadastro.transient(janela_principal)  # Faz a janela de cadastro modal
    janela_cadastro.grab_set()  # Captura eventos na janela de cadastro
    janela_principal.wait_window(janela_cadastro)  # Espera a janela de cadastro ser fechada

def criar_janela_login():
    janela_login = tk.Toplevel()
    janela_login.title('Login')

    # lógica da janela de login (Kaio)
    botao_login = tk.Button(janela_login, text="Fazer login", command=fazer_login)
    botao_login.pack(padx=20, pady=20)

def criar_janela_materia():
    janela_materia = tk.Toplevel()
    janela_materia.title('Criar Matéria')

    # lógica da janela de criar matéria (fazendo em projete_6_.py)
    botao_materia = tk.Button(janela_materia, text="Criar Matéria", command=criar_materia)
    botao_materia.pack(padx=20, pady=20)

def criar_janela_acessar_materia():
    janela_acessar_materia = tk.Toplevel()
    janela_acessar_materia.title('Acessar Matéria')

    # lógica da janela de acessar matéria
    botao_acessar_materia = tk.Button(janela_acessar_materia, text="Acessar Matéria", command=acessar_materia)
    botao_acessar_materia.pack(padx=20, pady=20)

def criar_janela_cronometro():
    janela_cronometro = tk.Toplevel()
    janela_cronometro.title('Cronômetro')

    # lógica da janela do cronômetro
    botao_cronometro = tk.Button(janela_cronometro, text="Criar Cronômetro", command=criar_cronometro)
    botao_cronometro.pack(padx=20, pady=20)

def criar_janela_inicial():
    global janela_inicial

    janela_inicial = tk.Toplevel()
    janela_inicial.title('Inicial')

    # botao pra criar materia
    botao_materia = tk.Button(janela_inicial, text="Abrir Criar Matéria", command=criar_janela_materia)
    botao_materia.pack(padx=20, pady=20)

    # botao pra acessar materia
    botao_acessar_materia = tk.Button(janela_inicial, text="Abrir Acessar Matéria", command=criar_janela_acessar_materia)
    botao_acessar_materia.pack(padx=20, pady=20)

    # botao pra acessar cronometro
    botao_cronometro = tk.Button(janela_inicial, text="Abrir Cronômetro", command=criar_janela_cronometro)
    botao_cronometro.pack(padx=20, pady=20)

    janela_inicial.transient(janela_principal)
    janela_inicial.grab_set()
    janela_principal.wait_window(janela_inicial)

def criar_janela_principal():
    global janela_principal

    janela_principal = tk.Tk()
    janela_principal.title('Principal')

    # botao pra fazer login
    botao_login = tk.Button(janela_principal, text="Abrir Login", command=criar_janela_login)
    botao_login.pack(padx=20, pady=20)

    # botao pra fazer cadastro
    botao_cadastro = tk.Button(janela_principal, text="Abrir Cadastro", command=criar_janela_cadastro)
    botao_cadastro.pack(padx=20, pady=20)

    janela_principal.mainloop()

# Inicia o programa abrindo a janela principal
criar_janela_principal()

# Exibe a lista de cadastros após o fechamento da janela principal
print(lista_cadastros)

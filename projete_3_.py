#para usar as labels, entry e outras coisas
import tkinter as tk
from tkinter import ttk
#para colocar a data
import datetime as dt
#para comparaçao das senhas
import tkinter.messagebox as tkmb
import hashlib

janela_cadastro = tk.Tk()
#definir o tamanho da janela aqui tem o tamanho da tela do celular la do figma
#janela_cadastro.geometry("353x852")

lista_cadastros = []

#funçao para criar cadastro
def criar_cadastro():
   #pegando as informações que o usuario inseriu
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    #checa se todos os campos te algo escrito se sim retorna sim se nao mostra erro
    if not nome or not email or not senha or not confirmar_senha:
        print("Preencha todos os campos")

    #checa se as senhas sao iguais se sim retorna sim se nao mostra erro
    if senha != confirmar_senha:
             print("As senhas são diferentes")
    

    #colocando data e hora no cadastro
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    
    #mostrando a lista de cadastros 
    cadastros = len(lista_cadastros)+1
    cadastros_str = "cadastro-{}".format(cadastros)
    lista_cadastros.append((cadastros_str,nome,email,senha,confirmar_senha,data_criacao))

#nome da janela
janela_cadastro.title( 'cadastro' )
#nome de usualrio
#mostrar para o usuario oq ele deve inserir 
label_nome = tk.Label(text="Nome de usuario")
label_nome.grid(row=1, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)
#caixa de texto para ele inserir oq pediu la em cima 
entry_nome = tk.Entry()
entry_nome.grid(row=2, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

#email
#mostrar para o usuario oq ele deve inserir 
label_email = tk.Label(text="Email")
label_email.grid(row=3, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)
#caixa de texto para ele inserir oq pediu la em cima 
entry_email = tk.Entry()
entry_email.grid(row=4, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

#senhapediu l
#mostrar para o usuario oq ele deve inserir 
label_senha = tk.Label(text="Senha")
label_senha.grid(row=5, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)
#caixa de texto para ele inserir oq a em cima 
#show='*' hash para proteger a senha
entry_senha = tk.Entry(show='*')
entry_senha.grid(row=6, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

#confirmar senha
#mostrar para o usuario oq ele deve inserir 
label_confirmar_senha = tk.Label(text="Confirmar senha")
label_confirmar_senha.grid(row=7, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)
#caixa de texto para ele inserir oq pediu la em cima 
#show='*' hash para proteger a confirmaçao senha
entry_confirmar_senha = tk.Entry(show='*')
entry_confirmar_senha.grid(row=8, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

#botao para cadstrar

botao_cadastrar = tk.Button(text="Cadastrar", command=criar_cadastro)
botao_cadastrar.grid(row=9, column=0, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

janela_cadastro.mainloop()

print(lista_cadastros)

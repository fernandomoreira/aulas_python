
import tkinter as tk
from tkinter import messagebox

def adicionar_item():
    codigo = entry_codigo.get()
    descricao = entry_descricao.get()
    fabricante = entry_fabricante.get()
    preco = entry_preco.get()
    
    if not codigo or not descricao or not fabricante or not preco:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    
    with open("estoque_versao2.txt", "a") as arquivo:
        arquivo.write(f"{codigo},{descricao},{fabricante},{preco}\n")
    
    messagebox.showinfo("Sucesso", "Item adicionado.")
    limpar_campos()
    listar_estoque()

def listar_estoque():
    listbox.delete(0, tk.END)
    try:
        with open("estoque_versao2.txt", "r") as arquivo:
            for linha in arquivo:
                listbox.insert(tk.END, linha.strip())
    except FileNotFoundError:
        open("estoque_versao2.txt", "w").close()

def alterar_item():
    selecionado = listbox.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um item para alterar.")
        return
    
    codigo_novo = entry_codigo.get()
    descricao_nova = entry_descricao.get()
    fabricante_novo = entry_fabricante.get()
    preco_novo = entry_preco.get()
    
    if not codigo_novo or not descricao_nova or not fabricante_novo or not preco_novo:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    item_selecionado = listbox.get(selecionado)
    codigo_antigo = item_selecionado.split(",")[0]

    with open("estoque_versao2.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("estoque_versao2.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo_antigo:
                arquivo.write(f"{codigo_novo},{descricao_nova},{fabricante_novo},{preco_novo}\n")
            else:
                arquivo.write(linha)
    
    messagebox.showinfo("Sucesso", "Item alterado.")
    limpar_campos()
    listar_estoque()

def remover_item():
    selecionado = listbox.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um item para remover.")
        return
    
    item_selecionado = listbox.get(selecionado)
    codigo_remover = item_selecionado.split(",")[0]

    with open("estoque_versao2.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("estoque_versao2.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != codigo_remover:
                arquivo.write(linha)
    
    messagebox.showinfo("Sucesso", "Item removido.")
    limpar_campos()
    listar_estoque()

def limpar_campos():
    entry_codigo.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_fabricante.delete(0, tk.END)
    entry_preco.delete(0, tk.END)

def carregar_item(event):
    selecionado = listbox.curselection()
    if not selecionado:
        return
    item = listbox.get(selecionado).split(",")
    entry_codigo.delete(0, tk.END)
    entry_codigo.insert(0, item[0])
    entry_descricao.delete(0, tk.END)
    entry_descricao.insert(0, item[1])
    entry_fabricante.delete(0, tk.END)
    entry_fabricante.insert(0, item[2])
    entry_preco.delete(0, tk.END)
    entry_preco.insert(0, item[3])

# Interface gráfica
janela = tk.Tk()
janela.title("Estoque de Informática")

tk.Label(janela, text="Código:").grid(row=0, column=0)
entry_codigo = tk.Entry(janela)
entry_codigo.grid(row=0, column=1)

tk.Label(janela, text="Descrição:").grid(row=1, column=0)
entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=1, column=1)

tk.Label(janela, text="Fabricante:").grid(row=2, column=0)
entry_fabricante = tk.Entry(janela)
entry_fabricante.grid(row=2, column=1)

tk.Label(janela, text="Preço:").grid(row=3, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=3, column=1)

tk.Button(janela, text="Adicionar", command=adicionar_item).grid(row=4, column=0)
tk.Button(janela, text="Alterar", command=alterar_item).grid(row=4, column=1)
tk.Button(janela, text="Remover", command=remover_item).grid(row=5, column=0)
tk.Button(janela, text="Limpar", command=limpar_campos).grid(row=5, column=1)

listbox = tk.Listbox(janela, width=50)
listbox.grid(row=6, column=0, columnspan=2)
listbox.bind("<<ListboxSelect>>", carregar_item)

listar_estoque()
janela.mainloop()

import tkinter as tk
import operacoes

def gravar():
    operacoes.gravar_sensor(codigo.get(), nome.get(), valor.get())

def buscar():
    dados = operacoes.buscar_sensor(codigo.get())
    if dados:
        nome.delete(0, tk.END)
        valor.delete(0, tk.END)
        nome.insert(0, dados[1])
        valor.insert(0, dados[2])

def alterar():
    operacoes.alterar_sensor(codigo.get(), nome.get(), valor.get())

def excluir():
    operacoes.excluir_sensor(codigo.get())

# Janela
janela = tk.Tk()
janela.title("Sensores")

tk.Label(janela, text="Código").grid(row=0, column=0)
codigo = tk.Entry(janela)
codigo.grid(row=0, column=1)

tk.Label(janela, text="Nome").grid(row=1, column=0)
nome = tk.Entry(janela)
nome.grid(row=1, column=1)

tk.Label(janela, text="Valor").grid(row=2, column=0)
valor = tk.Entry(janela)
valor.grid(row=2, column=1)

tk.Button(janela, text="Gravar", command=gravar).grid(row=3, column=0)
tk.Button(janela, text="Buscar", command=buscar).grid(row=3, column=1)
tk.Button(janela, text="Alterar", command=alterar).grid(row=4, column=0)
tk.Button(janela, text="Excluir", command=excluir).grid(row=4, column=1)

janela.mainloop()

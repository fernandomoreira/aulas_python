#Gravando em um arquivo
"""
arquivo = open ("numeros.txt", "w")
for linha in range (1,100):
    arquivo.write(f"{linha}\n")
arquivo.close()


#lendo dados do arquivo
arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()


#Criar Arquivos para CRUD
#abre arquivo no modo escrita
with open ("dados.txt", "w") as arquivo:
    arquivo.write("João\n")

#abre um arquivo no modo leitura
with open ("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())#mostra o conteudo sem pular linhas (ignora o \n)"


#Alteração-Modificação dos dados

#lê os dados
with open ("dados.txt", "r")as arquivo:
    linhas = arquivo.readlines()
# Modifica o nome "João" para "Maria"
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "João":
            arquivo.write("Maria")
        else:
            arquivo.write(linha)
"""
#remover dados
#Lê dados
with open ("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
#escreve os dados diferentes de Maria
with open ("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "Maria":
            arquivo.write(linha)








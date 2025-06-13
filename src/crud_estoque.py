
def adicionar_item():
    codigo = input("Código: ")
    descricao = input("Descrição: ")
    fabricante = input("Fabricante: ")
    preco = input("Preço: ")
    
    with open("estoque.txt", "a") as arquivo:
        arquivo.write(f"{codigo},{descricao},{fabricante},{preco}\n")
    print("Item adicionado.")

def listar_estoque():
    with open("estoque.txt", "r") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",") #strip()remove as quebras e split, separa os campos por virgula
            print(f"Código: {item[0]} | Descrição: {item[1]} | Fabricante: {item[2]} | Preço: R${item[3]}")

def alterar_item():
    codigo_alvo = input("Digite o código do item a alterar: ")
    
    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo_alvo:
                print("Digite os novos dados:")
                novo_codigo = input("Novo Código: ")
                nova_desc = input("Nova Descrição: ")
                novo_fabricante = input("Novo Fabricante: ")
                novo_preco = input("Novo Preço: ")
                arquivo.write(f"{novo_codigo},{nova_desc},{novo_fabricante},{novo_preco}\n")
            else:
                arquivo.write(linha)
    print("Item alterado.")

def remover_item():
    codigo_alvo = input("Digite o código do item a remover: ")
    
    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != codigo_alvo:
                arquivo.write(linha)
    
    print("Item removido.")

def menu():
    while True:
        print("\n--- MENU ESTOQUE ---")
        print("1 - Adicionar item")
        print("2 - Listar estoque")
        print("3 - Alterar item")
        print("4 - Remover item")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            listar_estoque()
        elif opcao == "3":
            alterar_item()
        elif opcao == "4":
            remover_item()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

menu()

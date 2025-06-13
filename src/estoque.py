ARQUIVO = "estoque.txt"


def carregar():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return [linha.strip().split(",") for linha in arquivo]
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando novo estoque...")
        return []


def salvar(produtos):
    with open(ARQUIVO, "w") as arquivo:
        for p in produtos:
            arquivo.write(",".join(p) + "\n")


def adicionar():
    print("\nNovo Produto:")
    codigo = input("Código: ")
    descricao = input("Descrição: ")
    fabricante = input("Fabricante: ")
    preco = input("Preço: ")

    produtos = carregar()
    produtos.append([codigo, descricao, fabricante, preco])
    salvar(produtos)
    print("Produto adicionado!")


def listar():
    produtos = carregar()
    print("\nEstoque:")
    for p in produtos:
        print(f"{p[0]} - {p[1]} ({p[2]}) R${p[3]}")


def atualizar():
    codigo = input("\nCódigo do produto: ")
    produtos = carregar()

    for p in produtos:
        if p[0] == codigo:
            p[1] = input(f"Nova descrição ({p[1]}): ") or p[1]
            p[2] = input(f"Novo fabricante ({p[2]}): ") or p[2]
            p[3] = input(f"Novo preço ({p[3]}): ") or p[3]
            salvar(produtos)
            print("Produto atualizado!")
            return

    print("Produto não encontrado!")


def remover():
    codigo = input("\nCódigo do produto: ")
    produtos = carregar()
    novos = [p for p in produtos if p[0] != codigo]

    if len(novos) < len(produtos):
        salvar(novos)
        print("Produto removido!")
    else:
        print("Produto não encontrado!")


def menu():
    while True:
        print("\nMENU:")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Sair")

        op = input("Opção: ")

        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "3":
            atualizar()
        elif op == "4":
            remover()
        elif op == "5":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
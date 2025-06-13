# Nome do arquivo onde os produtos serão armazenados
NOME_ARQUIVO_ESTOQUE = "estoque.txt"


def carregar_produtos_do_arquivo():
    """Carrega todos os produtos do arquivo para uma lista"""
    try:
        with open(NOME_ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
            lista_de_produtos = []
            for linha in arquivo:
                codigo, descricao, fabricante, preco = linha.strip().split(",")
                lista_de_produtos.append([codigo, descricao, fabricante, preco])
            return lista_de_produtos
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Iniciando com estoque vazio.")
        return []
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")
        return []


def salvar_produtos_no_arquivo(lista_de_produtos):
    """Salva a lista completa de produtos no arquivo"""
    try:
        with open(NOME_ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
            for produto in lista_de_produtos:
                linha = ",".join(produto) + "\n"
                arquivo.write(linha)
    except Exception as erro:
        print(f"Erro ao salvar o arquivo: {erro}")


def cadastrar_novo_produto():
    """Adiciona um novo produto ao estoque"""
    print("\n╔══════════════════════════╗")
    print("║  CADASTRO DE NOVO PRODUTO  ║")
    print("╚══════════════════════════╝")

    codigo = input("Código do produto (ex: 001): ").strip()
    descricao = input("Descrição (ex: Mouse sem fio): ").strip()
    fabricante = input("Fabricante (ex: Logitech): ").strip()
    preco = input("Preço (ex: 125.90): ").strip()

    lista_produtos = carregar_produtos_do_arquivo()
    lista_produtos.append([codigo, descricao, fabricante, preco])
    salvar_produtos_no_arquivo(lista_produtos)

    print(f"\n✅ Produto {descricao} cadastrado com sucesso!")


def exibir_todos_produtos():
    """Mostra todos os produtos do estoque formatados"""
    lista_produtos = carregar_produtos_do_arquivo()

    print("\n📋 LISTA COMPLETA DE PRODUTOS")
    print("=" * 60)
    print(f"{'CÓDIGO':<10} {'DESCRIÇÃO':<25} {'FABRICANTE':<15} {'PREÇO':>10}")
    print("-" * 60)

    if not lista_produtos:
        print("Nenhum produto cadastrado no estoque.")
    else:
        for produto in lista_produtos:
            print(f"{produto[0]:<10} {produto[1]:<25} {produto[2]:<15} R$ {produto[3]:>7}")
    print("=" * 60)


def atualizar_dados_produto():
    """Permite editar os dados de um produto existente"""
    print("\n🔄 ATUALIZAR PRODUTO")
    codigo_busca = input("Digite o código do produto que deseja atualizar: ").strip()

    lista_produtos = carregar_produtos_do_arquivo()
    produto_encontrado = False

    for produto in lista_produtos:
        if produto[0] == codigo_busca:
            produto_encontrado = True
            print(f"\nEditando produto: {produto[1]}")
            print("[Deixe em branco para manter o valor atual]")

            produto[1] = input(f"Nova descrição ({produto[1]}): ") or produto[1]
            produto[2] = input(f"Novo fabricante ({produto[2]}): ") or produto[2]
            novo_preco = input(f"Novo preço (R${produto[3]}): ")
            produto[3] = novo_preco if novo_preco else produto[3]

            salvar_produtos_no_arquivo(lista_produtos)
            print("\n✅ Produto atualizado com sucesso!")
            break

    if not produto_encontrado:
        print("\n❌ Produto não encontrado!")


def remover_produto_do_estoque():
    """Remove um produto do estoque pelo código"""
    print("\n❌ REMOVER PRODUTO")
    codigo_busca = input("Digite o código do produto a ser removido: ").strip()

    lista_produtos = carregar_produtos_do_arquivo()
    nova_lista_produtos = [produto for produto in lista_produtos if produto[0] != codigo_busca]

    if len(nova_lista_produtos) < len(lista_produtos):
        salvar_produtos_no_arquivo(nova_lista_produtos)
        print("\n✅ Produto removido com sucesso!")
    else:
        print("\n❌ Produto não encontrado!")


# Menu interativo principal
def mostrar_menu_principal():
    """Exibe o menu e gerencia as opções"""
    while True:
        print("\n" + "=" * 50)
        print("🏪 SISTEMA DE ESTOQUE - LOJA DE INFORMÁTICA")
        print("=" * 50)
        print("1. 📝 Cadastrar novo produto")
        print("2. 📋 Listar todos os produtos")
        print("3. 🔄 Atualizar produto existente")
        print("4. ❌ Remover produto")
        print("5. 🚪 Sair do sistema")
        print("=" * 50)

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar_novo_produto()
        elif opcao == "2":
            exibir_todos_produtos()
        elif opcao == "3":
            atualizar_dados_produto()
        elif opcao == "4":
            remover_produto_do_estoque()
        elif opcao == "5":
            print("\nObrigado por usar nosso sistema! Até logo! 👋")
            break
        else:
            print("\n⚠️ Opção inválida! Por favor, escolha de 1 a 5.")


# Inicia o sistema
mostrar_menu_principal()
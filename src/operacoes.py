ARQUIVO = "sensoriamento.txt"

def gravar_sensor(cod, nome, val):
    with open(ARQUIVO, "a") as f:
        f.write(f"{cod},{nome},{val}\n")

def buscar_sensor(cod):
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                c, n, v = linha.strip().split(",")
                if c == cod:
                    return c, n, v
    except:
        return None

def alterar_sensor(cod, nome, val):
    linhas = []
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                c, _, _ = linha.strip().split(",")
                if c == cod:
                    linhas.append(f"{cod},{nome},{val}\n")
                else:
                    linhas.append(linha)
        with open(ARQUIVO, "w") as f:
            f.writelines(linhas)
    except:
        pass

def excluir_sensor(cod):
    linhas = []
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                c, _, _ = linha.strip().split(",")
                if c != cod:
                    linhas.append(linha)
        with open(ARQUIVO, "w") as f:
            f.writelines(linhas)
    except:
        pass

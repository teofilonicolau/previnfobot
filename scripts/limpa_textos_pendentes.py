import os

PASTA_ORIGEM = "dados/textos_pendentes"
PASTA_DESTINO = "dados/textos_revisados"

RUÍDOS = ["####", "…..", "~~~", "@@@", "¯¯¯", "|||", ">>>", "“”"]

os.makedirs(PASTA_DESTINO, exist_ok=True)

def linha_valida(linha):
    return not any(r in linha for r in RUÍDOS) and linha.strip()

def limpar_arquivo(nome_arquivo):
    caminho_origem = os.path.join(PASTA_ORIGEM, nome_arquivo)
    caminho_destino = os.path.join(PASTA_DESTINO, nome_arquivo)

    with open(caminho_origem, "r", encoding="utf-8", errors="ignore") as f:
        linhas = f.readlines()

    linhas_limpas = [linha for linha in linhas if linha_valida(linha)]

    with open(caminho_destino, "w", encoding="utf-8") as f:
        f.writelines(linhas_limpas)

    print(f"✅ Limpo: {nome_arquivo} ({len(linhas_limpas)} linhas mantidas)")

def main():
    arquivos = [a for a in os.listdir(PASTA_ORIGEM) if a.endswith(".txt")]
    for arquivo in arquivos:
        limpar_arquivo(arquivo)

    print(f"\n🧼 Todos arquivos limpos salvos em: {PASTA_DESTINO}/")

if __name__ == "__main__":
    main()

import os
import csv
from datetime import datetime

PASTA_TXT = "dados/textos_limpos"
CAMINHO_CSV = "relatorios/resumo_arquivos.csv"

os.makedirs("relatorios", exist_ok=True)

def analisar_arquivo(caminho_txt):
    with open(caminho_txt, "r", encoding="utf-8", errors="ignore") as f:
        conteudo = f.read()
        num_caracteres = len(conteudo)
        num_palavras = len(conteudo.split())
    tamanho_kb = round(os.path.getsize(caminho_txt) / 1024, 2)
    ultima_mod = datetime.fromtimestamp(os.path.getmtime(caminho_txt)).strftime("%Y-%m-%d %H:%M:%S")
    return num_caracteres, num_palavras, tamanho_kb, ultima_mod

def main():
    linhas = []
    for raiz, _, arquivos in os.walk(PASTA_TXT):
        for nome in arquivos:
            if nome.endswith(".txt"):
                caminho = os.path.join(raiz, nome)
                caracteres, palavras, tamanho_kb, data_mod = analisar_arquivo(caminho)
                linhas.append([
                    nome,
                    caminho,
                    caracteres,
                    palavras,
                    tamanho_kb,
                    data_mod
                ])

    with open(CAMINHO_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["arquivo", "caminho", "caracteres", "palavras", "tamanho_kb", "data_modificacao"])
        writer.writerows(linhas)

    print(f"✅ Relatório gerado com sucesso: {CAMINHO_CSV}")

if __name__ == "__main__":
    main()
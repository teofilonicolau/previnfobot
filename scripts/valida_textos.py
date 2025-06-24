import os
import csv

PASTA_TXT = "dados/textos_limpos"
RELATORIO_CSV = "relatorios/extracoes_com_erro.csv"

# Critérios de validação
MIN_CARACTERES = 100
MIN_PALAVRAS = 20
RUÍDOS = ["####", "…..", "~~~", "@@@", "¯¯¯", "|||", ">>>", "“”"]

os.makedirs("relatorios", exist_ok=True)

def possui_ruido(conteudo):
    return any(r in conteudo for r in RUÍDOS)

def analisar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
        conteudo = f.read()
        num_caracteres = len(conteudo)
        num_palavras = len(conteudo.split())
        ruido = possui_ruido(conteudo)
    return num_caracteres, num_palavras, ruido

def main():
    linhas_suspeitas = []

    for raiz, _, arquivos in os.walk(PASTA_TXT):
        for nome in arquivos:
            if nome.endswith(".txt"):
                caminho = os.path.join(raiz, nome)
                caracteres, palavras, tem_ruido = analisar_arquivo(caminho)

                if caracteres < MIN_CARACTERES or palavras < MIN_PALAVRAS or tem_ruido:
                    motivo = []
                    if caracteres < MIN_CARACTERES: motivo.append("poucos caracteres")
                    if palavras < MIN_PALAVRAS: motivo.append("poucas palavras")
                    if tem_ruido: motivo.append("ruído textual")
                    linhas_suspeitas.append([nome, caminho, caracteres, palavras, ", ".join(motivo)])

    with open(RELATORIO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["arquivo", "caminho", "caracteres", "palavras", "motivo"])
        writer.writerows(linhas_suspeitas)

    print(f"🔍 {len(linhas_suspeitas)} arquivos suspeitos listados em: {RELATORIO_CSV}")

if __name__ == "__main__":
    main()


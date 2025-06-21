import pdfplumber
import os

PASTA_PDFS = "../../dados/pdfs/"
PASTA_SAIDA = "../../dados/textos/"

os.makedirs(PASTA_SAIDA, exist_ok=True)

for nome_arquivo in os.listdir(PASTA_PDFS):
    if nome_arquivo.endswith(".pdf"):
        caminho_pdf = os.path.join(PASTA_PDFS, nome_arquivo)
        texto_total = ''
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_total += texto + '\n'
        base_nome = nome_arquivo.replace('.pdf', '.txt')
        caminho_saida = os.path.join(PASTA_SAIDA, base_nome)
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(texto_total)
        print(f"Texto extraído de {nome_arquivo}")
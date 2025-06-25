import os
import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image
from tqdm import tqdm

# Caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Pastas do projeto
PASTA_ORIGEM = "dados/fontes_extra"
PASTA_DESTINO = "dados/textos_limpos"
os.makedirs(PASTA_DESTINO, exist_ok=True)

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

def extrair_texto_docx(caminho_docx):
    doc = docx.Document(caminho_docx)
    return "\n".join([p.text for p in doc.paragraphs])

def extrair_texto_imagem(caminho_img):
    imagem = Image.open(caminho_img)
    return pytesseract.image_to_string(imagem, lang='por')

def limpar_texto(texto):
    return '\n'.join([linha.strip() for linha in texto.splitlines() if linha.strip()])

def salvar_texto(texto, nome_base, indice):
    nome_arquivo = f"{indice:03}_{nome_base}.txt"
    caminho = os.path.join(PASTA_DESTINO, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto)

def main():
    indice = 1
    for raiz, _, arquivos in os.walk(PASTA_ORIGEM):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            ext = nome.lower().split(".")[-1]
            nome_base = os.path.splitext(nome)[0].replace(" ", "_")

            try:
                if ext == "pdf":
                    texto = extrair_texto_pdf(caminho)
                elif ext == "docx":
                    texto = extrair_texto_docx(caminho)
                elif ext in ["png", "jpg", "jpeg"]:
                    texto = extrair_texto_imagem(caminho)
                else:
                    print(f"❌ Tipo não suportado: {nome}")
                    continue

                texto_limpo = limpar_texto(texto)
                salvar_texto(texto_limpo, nome_base, indice)
                indice += 1
            except Exception as e:
                print(f"⚠️ Erro ao processar {nome}: {e}")

if __name__ == "__main__":
    main()

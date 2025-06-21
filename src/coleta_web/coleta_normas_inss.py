import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re
from unidecode import unidecode

# 🚩 URL da página principal com as normas
URL_BASE = "https://www.gov.br"
PAGINA_INICIAL = "https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/normas-interativas-2"

# 📁 Caminho absoluto para salvar os arquivos de texto extraídos
PASTA_SAIDA = Path(__file__).resolve().parents[2] / "dados" / "textos"
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

# 🔍 Baixar HTML da página principal (⚠️ verify=False: provisório até resolver SSL)
try:
    resposta = requests.get(PAGINA_INICIAL, verify=False)  # ← AVISO: remover verify=False depois!
    resposta.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"❌ Falha ao acessar a página principal: {e}")
    exit(1)

sopa = BeautifulSoup(resposta.text, "html.parser")

# 🧩 Diagnóstico: exibe as primeiras tags <a> para ajudar no debug se vierem 0 links
# print(sopa.prettify()[:1000])  # Descomente se quiser inspecionar manualmente

# 🧷 Selecionar links das normas (pode ser ajustado conforme estrutura do site)
links = sopa.select("a.external-link")

print(f"🔗 Encontrados {len(links)} links de normas. Iniciando download...\n")

if not links:
    print("⚠️ Nenhum link foi encontrado. A estrutura da página pode ter mudado.")
    exit(1)

# ⛏️ Processar cada link individualmente
for link in links:
    titulo = link.get_text(strip=True)
    href = link.get("href")
    if not href:
        continue
    if not href.startswith("http"):
        href = URL_BASE + href

    try:
        # ⚠️ verify=False: manter enquanto resolver problema de certificado
        conteudo_resposta = requests.get(href, timeout=20, verify=False)
        conteudo_resposta.raise_for_status()
        conteudo_sopa = BeautifulSoup(conteudo_resposta.text, "html.parser")
        texto_extraido = conteudo_sopa.get_text(separator="\n")

        # 🔤 Gerar nome de arquivo limpo
        nome_arquivo = unidecode(titulo.lower())
        nome_arquivo = re.sub(r"[^\w\s-]", "", nome_arquivo).replace(" ", "_")
        caminho_arquivo = PASTA_SAIDA / f"{nome_arquivo}.txt"

        # 💾 Salvar conteúdo em arquivo .txt
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(texto_extraido)

        print(f"✅ Salvo: {caminho_arquivo.name}")

    except Exception as e:
        print(f"⚠️ Erro ao acessar {href}: {e}")

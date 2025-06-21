from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pathlib import Path
import time
import re
from unidecode import unidecode

# Caminho do chromedriver
caminho_driver = Path(__file__).resolve().parents[2] / "drivers" / "chromedriver.exe"

# Pasta onde serão salvos os textos
PASTA_SAIDA = Path(__file__).resolve().parents[2] / "dados" / "textos"
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

# Palavras-chave para filtrar normas específicas
PALAVRAS_CHAVE = ["instrução normativa", "128/2022", "portaria", "manual técnico", "comunicado"]

# Configuração do navegador
options = Options()
# options.add_argument("--headless")  # Ative quando estiver testado
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(str(caminho_driver)), options=options)

try:
    print("🌐 Acessando a página de normas...")
    driver.get("https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/normas-interativas-2")
    time.sleep(5)

    # Localiza o menu lateral com os links relevantes
    menu = driver.find_element(By.CSS_SELECTOR, "ul.submenu.navTree.navTreeLevel1")
    links = menu.find_elements(By.TAG_NAME, "a")
    print(f"🔎 Analisando {len(links)} links do menu lateral...\n")

    for link in links:
        texto_link = link.text.strip().lower()
        href = link.get_attribute("href")

        if href and any(palavra in texto_link for palavra in PALAVRAS_CHAVE):
            print(f"🔗 Coletando: {link.text.strip()}")
            driver.get(href)
            time.sleep(4)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            texto = soup.get_text(separator="\n")

            nome_arquivo = unidecode(link.text.lower())
            nome_arquivo = re.sub(r"[^\w\s-]", "", nome_arquivo).replace(" ", "_")
            caminho = PASTA_SAIDA / f"{nome_arquivo}.txt"

            with open(caminho, "w", encoding="utf-8") as f:
                f.write(texto)

            print(f"✅ Salvo: {caminho.name}\n")

finally:
    driver.quit()
    print("📦 Coleta finalizada com sucesso.")

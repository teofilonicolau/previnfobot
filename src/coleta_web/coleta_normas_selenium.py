from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pathlib import Path
import time
import re
from unidecode import unidecode

# === CONFIGURAÇÕES GERAIS ===
URL = "https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/normas-interativas-2"
PALAVRAS_CHAVE = []  # ← Deixe vazio para coletar tudo, ou adicione termos como ["instrução normativa", "128/2022"]
HEADLESS = True
TIMEOUT = 60
CHROMEDRIVER = Path(__file__).resolve().parents[2] / "drivers" / "chromedriver.exe"
PASTA_SAIDA = Path(__file__).resolve().parents[2] / "dados" / "textos"
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

# === CONFIGURAÇÃO DO NAVEGADOR ===
options = Options()
if HEADLESS:
    options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(str(CHROMEDRIVER)), options=options)
driver.set_page_load_timeout(TIMEOUT)

try:
    print("🌐 Acessando página de normas do INSS...")
    driver.get(URL)
    time.sleep(5)

    # SELETOR CONFIÁVEL DO MENU LATERAL
    menu = driver.find_element(By.CSS_SELECTOR, "ul.submenu.navTree.navTreeLevel1")
    links = menu.find_elements(By.TAG_NAME, "a")
    print(f"📎 {len(links)} links detectados no menu lateral.\n")

    for i, link in enumerate(links):
        try:
            titulo = link.text.strip()
            href = link.get_attribute("href")
        except Exception:
            continue  # pula se o link estiver quebrado

        if not href or (PALAVRAS_CHAVE and not any(p in titulo.lower() for p in PALAVRAS_CHAVE)):
            continue

        nome_arquivo = unidecode(titulo.lower())
        nome_arquivo = re.sub(r"[^\w\s-]", "", nome_arquivo).replace(" ", "_")
        caminho = PASTA_SAIDA / f"{nome_arquivo}.txt"
        if caminho.exists():
            print(f"⚠️ Já existe: {caminho.name}, pulando...\n")
            continue

        print(f"🔗 Coletando ({i+1}/{len(links)}): {titulo}")
        driver.get(href)
        time.sleep(4)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        texto = soup.get_text(separator="\n")

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto)

        print(f"✅ Salvo: {caminho.name}\n")

        # Volta para a página inicial para processar o próximo link
        driver.get(URL)
        time.sleep(3)
        menu = driver.find_element(By.CSS_SELECTOR, "ul.submenu.navTree.navTreeLevel1")
        links = menu.find_elements(By.TAG_NAME, "a")

finally:
    driver.quit()
    print("📦 Coleta finalizada com sucesso.")

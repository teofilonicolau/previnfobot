import os
import re
import pandas as pd
from collections import Counter

# Biblioteca opcional: remove palavras comuns como "de", "e", "a"
try:
    from nltk.corpus import stopwords
    nltk_stopwords = set(stopwords.words("portuguese"))
except:
    nltk_stopwords = set()

CAMINHO = "dados/textos_limpos/"
SAIDA_CSV = "relatorios/termos_frequentes.csv"

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"\W+", " ", texto)  # Remove símbolos e pontuação
    return texto

def analisar_termos():
    todas_as_palavras = []

    for arquivo in os.listdir(CAMINHO):
        if arquivo.endswith(".txt"):
            with open(os.path.join(CAMINHO, arquivo), "r", encoding="utf-8") as f:
                conteudo = limpar_texto(f.read())
                palavras = conteudo.split()
                palavras_filtradas = [
                    p for p in palavras if p not in nltk_stopwords and len(p) > 2
                ]
                todas_as_palavras.extend(palavras_filtradas)

    contagem = Counter(todas_as_palavras).most_common(30)

    print("\n🔝 Top 30 termos mais frequentes nos textos limpos:")
    for palavra, freq in contagem:
        print(f"{palavra:<20} {freq}")

    # Exporta para CSV
    df = pd.DataFrame(contagem, columns=["Termo", "Frequência"])
    os.makedirs(os.path.dirname(SAIDA_CSV), exist_ok=True)
    df.to_csv(SAIDA_CSV, index=False, encoding="utf-8")
    print(f"\n📁 Exportado para: {SAIDA_CSV}")

if __name__ == "__main__":
    analisar_termos()

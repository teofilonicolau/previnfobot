import os
import re
import pandas as pd
import streamlit as st
from collections import Counter

try:
    from nltk.corpus import stopwords
    nltk_stopwords = set(stopwords.words("portuguese"))
except:
    nltk_stopwords = set()

CAMINHO = "dados/textos_limpos/"

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"\W+", " ", texto)
    return texto

def contar_termos():
    todas_as_palavras = []

    for arquivo in os.listdir(CAMINHO):
        if arquivo.endswith(".txt"):
            with open(os.path.join(CAMINHO, arquivo), encoding="utf-8") as f:
                palavras = limpar_texto(f.read()).split()
                palavras_filtradas = [p for p in palavras if p not in nltk_stopwords and len(p) > 2]
                todas_as_palavras.extend(palavras_filtradas)

    return Counter(todas_as_palavras).most_common(50)

st.title("📊 Análise Léxica da Base Jurídica")
termos = contar_termos()

df = pd.DataFrame(termos, columns=["Termo", "Frequência"])
st.bar_chart(df.set_index("Termo"))

st.download_button("📁 Baixar como CSV", data=df.to_csv(index=False), file_name="frequencia_termos.csv", mime="text/csv")

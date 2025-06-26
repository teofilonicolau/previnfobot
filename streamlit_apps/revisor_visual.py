import streamlit as st
import os
import csv
from datetime import datetime
import shutil
import re
import webbrowser

# ✅ Função de validação automática do texto limpo
def validar_texto_limpo(texto):
    erros = []

    if re.search(r"[^\w\s.,;:!?()-]", texto):
        erros.append("Caracteres estranhos encontrados")

    if "###" in texto or "..." in texto:
        erros.append("Ruído de marcação ou pontuação excessiva")

    if not texto.strip():
        erros.append("Texto vazio ou só com espaços")

    aprovado = len(erros) == 0
    return {"aprovado": aprovado, "erros": erros}

# 🔄 Função auxiliar para registrar a decisão
def salvar_decisao(nome_arquivo, decisao):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOG_REVISÃO = "relatorios/log_revisoes.csv"
    novo = not os.path.exists(LOG_REVISÃO)
    with open(LOG_REVISÃO, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if novo:
            writer.writerow(["arquivo", "data_hora", "decisao"])
        writer.writerow([nome_arquivo, now, decisao])

# 🗂️ Configuração de pastas
PASTA_ORIGEM = "dados/textos_pendentes"
PASTA_LIMPA = "dados/textos_revisados"
PASTA_APROVADO = "dados/textos_limpos"
PASTA_DESCARTADO = "dados/textos_descartados"

# Criação das pastas, se necessário
for pasta in [PASTA_APROVADO, PASTA_DESCARTADO, "relatorios"]:
    os.makedirs(pasta, exist_ok=True)

st.set_page_config(layout="wide")
st.title("🔎 Revisor Visual de Textos - Previnfobot")

# Lista de arquivos
arquivos = sorted([f for f in os.listdir(PASTA_ORIGEM) if f.endswith(".txt")])

if not arquivos:
    st.success("✅ Nenhum texto pendente. Tudo revisado!")
    st.stop()

arquivo_selecionado = st.selectbox("📄 Escolha um arquivo para comparar:", arquivos)

# Caminhos dos arquivos selecionados
caminho_original = os.path.join(PASTA_ORIGEM, arquivo_selecionado)
caminho_limpo = os.path.join(PASTA_LIMPA, arquivo_selecionado)

# Colunas lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟥 Texto Original com Ruído")
    with open(caminho_original, "r", encoding="utf-8", errors="ignore") as f:
        texto_original = f.read()
    st.text_area("Conteúdo original", texto_original, height=600, key="orig")

with col2:
    st.subheader("🟩 Texto Após Limpeza")
    if os.path.exists(caminho_limpo):
        with open(caminho_limpo, "r", encoding="utf-8") as f:
            texto_limpo = f.read()
        st.text_area("Conteúdo limpo", texto_limpo, height=600, key="limpo")
    else:
        st.error("🚫 Arquivo limpo não encontrado.")
        st.stop()

# 🔍 Validação automática
resultado = validar_texto_limpo(texto_limpo)

if resultado["aprovado"]:
    st.success("✅ Texto limpo validado com sucesso!")
else:
    st.error("⚠️ Problemas detectados no texto limpo:")
    for erro in resultado["erros"]:
        st.markdown(f"- {erro}")

# Decisões
col_a, col_b = st.columns(2)

with col_a:
    if resultado["aprovado"]:
        if st.button("✅ Aceitar e mover para textos_limpos/"):
            shutil.move(caminho_limpo, os.path.join(PASTA_APROVADO, arquivo_selecionado))
            os.remove(caminho_original)
            salvar_decisao(arquivo_selecionado, "aceito")
            st.success("🎉 Texto aceito e movido com sucesso!")
            st.experimental_rerun()
    else:
        st.info("⛔ Corrija os erros antes de aceitar este texto.")

with col_b:
    if st.button("🗑️ Recusar e mover para textos_descartados/"):
        shutil.move(caminho_original, os.path.join(PASTA_DESCARTADO, arquivo_selecionado))
        if os.path.exists(caminho_limpo):
            os.remove(caminho_limpo)
        salvar_decisao(arquivo_selecionado, "descartado")
        st.warning("🚮 Texto descartado.")
        st.experimental_rerun()

# 🔁 Acesso rápido ao Painel Central
with st.expander("🧩 Gerenciar processamento"):
    st.markdown("Você também pode abrir o Painel Central de Execução a partir daqui.")
    if st.button("🎛️ Ir para Painel de Execução"):
        webbrowser.open_new_tab("http://localhost:8501")

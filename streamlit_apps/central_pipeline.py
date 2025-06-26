import streamlit as st
import subprocess
import os

st.set_page_config(page_title="🧩 Painel Central - Previnfobot", layout="wide")
st.title("🧠 Painel Central de Execução – Previnfobot")

def rodar_comando(titulo, comando):
    st.markdown(f"### 🔹 {titulo}")
    with st.status("Executando...", expanded=True) as status:
        with st.spinner(f"Rodando: `{comando}`"):
            try:
                resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
                st.code(resultado.stdout)
                if resultado.stderr:
                    st.error(resultado.stderr)
                status.update(label="✅ Concluído", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Erro ao executar: {e}")
                status.update(label="❌ Falhou", state="error", expanded=True)

# Botões
if st.button("🚀 Executar TUDO (pipeline completa)"):
    rodar_comando("Pipeline Geral", "python executa_tudo.py")

st.divider()
col1, col2 = st.columns(2)

with col1:
    if st.button("🧼 Limpar textos pendentes"):
        rodar_comando("Limpando textos", "python scripts/limpa_textos_pendentes.py")

    if st.button("📝 Validar textos limpos"):
        rodar_comando("Validação automática", "python scripts/valida_textos.py")

with col2:
    if st.button("📤 Extrair e limpar arquivos (.doc, .pdf, .png)"):
        rodar_comando("Extração e pré-processamento", "python scripts/extrai_e_limpa_drive.py")

    if st.button("📊 Gerar relatório final"):
        rodar_comando("Geração de relatório CSV", "python scripts/gera_relatorio_csv.py")

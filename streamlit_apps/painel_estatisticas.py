import streamlit as st
import pandas as pd
import plotly.express as px
import webbrowser

st.set_page_config(page_title="Painel de Estatísticas", layout="wide")

st.title("📈 Painel de Revisões - Previnfobot")

try:
    df = pd.read_csv("relatorios/log_revisoes.csv")
    df["data_hora"] = pd.to_datetime(df["data_hora"])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total por decisão")
        st.plotly_chart(px.histogram(df, x="decisao", color="decisao", barmode="group"))

    with col2:
        st.subheader("Evolução ao longo do tempo")
        df["data"] = df["data_hora"].dt.date
        st.plotly_chart(px.histogram(df, x="data", color="decisao"))

    # 🔁 Acesso ao Painel Central
    with st.expander("🧩 Gerenciar processamento"):
        st.markdown("Você pode acessar o Painel Central para executar etapas da pipeline:")
        if st.button("🎛️ Ir para Painel de Execução"):
            webbrowser.open_new_tab("http://localhost:8501")

except FileNotFoundError:
    st.warning("Arquivo de log não encontrado. Faça revisões primeiro.")

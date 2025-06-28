# 🗺️ Roadmap de Evolução – PrevInfoBot

Este arquivo documenta, em ciclos, todas as entregas, objetivos e melhorias do projeto.

---

## ✅ Ciclo 1 — Estrutura Inicial

- Criação das pastas: `src/`, `dados/`, `scripts/`, `streamlit_apps/`, `tests/`
- Instalação das bibliotecas principais (LangChain, OpenAI, FAISS, etc.)
- Organização do `.gitignore`, ambiente virtual (`venv/`) e dependências

---

## ✅ Ciclo 2 — Coleta e Extração

- Scraper com Selenium (`coleta_web.py`)
- Conversão `.doc` → `.docx` e OCR com `pytesseract`
- Pipeline de limpeza (`limpa_textos_pendentes.py`)
- Scripts robustos com logs e suporte a reprocessamento

---

## ✅ Ciclo 3 — Validação e Revisão

- Revisor visual em Streamlit (`revisor_visual.py`)
- Botões "Aceitar" e "Recusar" com log automático em `.csv`
- Validador de ruídos (`validar_texto_limpo`)
- Painel de estatísticas interativo

---

## ✅ Ciclo 4 — Integração com IA

- Indexador com FAISS (`indexa_com_faiss.py`)
- Busca e geração de respostas com IA (`pergunta_ao_robo.py`)  
  ↳ *Movido para `app/api/` e renomeado como `router.py`*
- Integração RAG concluída

---

## ✅ Ciclo 5 — API e Automação

- Criação de endpoint FastAPI: `/consultar`
- Pipeline centralizadora em Streamlit (`central_pipeline.py`)
- Automação com scripts `.bat`
- Testes automatizados com Pytest
- Cobertura de testes: **68%**

---

## 📌 Em Progresso

- Exportação de relatórios em `.pdf`
- CI/CD com GitHub Actions
- Expansão do domínio para **Direito do Consumidor**

---

🧱 *Cada bloco bem colocado fortalece a base da inteligência jurídica.*

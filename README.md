# PrevInfoBot

Um robô jurídico baseado em RAG (Retrieval-Augmented Generation) que lê PDFs jurídicos, extrai os textos, limpa, fragmenta e indexa os dados para fornecer respostas inteligentes usando modelos de linguagem natural.

---

## ✔️ Etapas concluídas

### 1. Estrutura de Diretórios
Organizamos o projeto com pastas para separar funções:
- `dados/pdfs/`: Armazena os PDFs originais
- `dados/textos/`: Receberá os textos extraídos
- `src/`: Contém scripts separados por etapa: extração, limpeza, fragmentação e indexação

### 2. Criação do Ambiente Virtual
Criamos um ambiente virtual (`venv/`) no nível raiz do projeto para isolar as bibliotecas e manter o projeto organizado e compatível com diferentes ambientes.

### 3. Arquivos principais criados
Foram criados os arquivos:
- `requirements.txt`: Para listar todas as dependências do projeto
- `README.md`: Instruções e explicações
- `main.py`: Ponto de entrada para o fluxo completo do robô

### 4. Instalação das Bibliotecas Essenciais
Instalamos as bibliotecas listadas abaixo, com suas finalidades:

| Biblioteca        | Função principal                                    |
|-------------------|-----------------------------------------------------|
| `langchain`       | Estrutura para o pipeline de RAG e integração LLM   |
| `openai`          | Integração com modelos da OpenAI                    |
| `pdfplumber`      | Extração de texto de arquivos PDF                   |
| `pytesseract`     | OCR para PDFs que contêm imagens (texto escaneado) |
| `Pillow`          | Manipulação de imagens usada pelo pytesseract      |
| `faiss-cpu`       | Indexação vetorial para busca semântica eficiente  |
| `python-dotenv`   | Leitura de variáveis de ambiente (.env)            |
| `unidecode`       | Remoção de acentos e normalização de texto         |

### 5. Extração de Texto dos PDFs
Implementamos o primeiro script, que percorre os PDFs e extrai o texto para arquivos `.txt`. Isso prepara os dados brutos para o fluxo de pré-processamento.

---

## ▶️ Próximo passo
Iniciaremos o processo de limpeza dos textos extraídos — eliminando ruídos, caracteres especiais e formatando o conteúdo para análise semântica.

---

## 💡 Observação
O projeto está sendo conduzido com didatismo extremo, passo a passo, para garantir total entendimento de cada etapa técnica e conceitual.lvar com Codificação → UTF-8.

---


extrurtura:

## Árvore do Projeto PrevInfoBot

```
previnfobot/
│
├── dados/                     # Armazena dados brutos e processados
│   ├── pdfs/                  # Coloque aqui seus arquivos PDF originais
│   └── textos/                # (criaremos depois para armazenar os .txt extraídos)
│
├── src/                       # Todo o código fonte do projeto
│   ├── extracao/              # Scripts para extrair texto dos PDFs
│   │   └── extrai_texto.py    # Script (a ser criado) para extrair texto
│   ├── limpeza/               # Scripts para limpar e normalizar textos
│   ├── fragmentacao/          # Scripts para dividir textos em chunks
│   ├── indexacao/             # Scripts para indexador vetorial (FAISS, etc)
│   └── main.py                # Script principal para orquestrar o processo
│
├── requirements.txt           # Lista de dependências do projeto
└── README.md                  # Instruções e documentação do projeto
```

---

## Dica: Onde criar cada coisa

- **Pasta do Projeto:**  
  Onde você preferir (ex: em `Documentos/Projetos/`).

### - **dados/**:

| Dentro de `previnfobot/`. |
|---|


### - **pdfs/**:

| Dentro de `dados/`. |
|---|


    Coloque seus PDFs aqui assim que começar.

### - **textos/**:

| Dentro de `dados/` (só crie depois do script de extração, não precisa criar agora). |
|---|



### - **src/**:

| Dentro de `previnfobot/`. |
|---|



### - **extracao/**:

| Dentro de `src/`. |
|---|


    - `extrai_texto.py`: arquivo que você irá criar nessa pasta, quando formos para extração.

### - **limpeza/**, **fragmentacao/**, **indexacao/**:

| Também dentro de `src/` (deixe vazias por enquanto). |
|---|



---

## **Resumo Visual**

```
SeuComputador/
└── local-que-voce-preferir/
    └── previnfobot/
        ├── dados/
        │   └── pdfs/
        └── src/
            ├── extracao/
            ├── limpeza/
            ├── fragmentacao/
            ├── indexacao/
```

## Segundo dia:

## ✅ O que foi feito hoje

### 1. **Reestruturação do Coletor com Selenium**
Criamos um novo scraper robusto com as seguintes melhorias:
- Navegação em modo headless (sem abrir janela)
- Seletores de menu lateral atualizados (`ul.submenu.navTree.navTreeLevel1`)
- Coleta completa ou filtrada por palavras-chave (`PALAVRAS_CHAVE`)
- Evita duplicatas (não sobrescreve `.txt` já existentes)
- Arquivos salvos com nomes limpos e em UTF-8

> Script localizado em: `src/coleta_web/coleta_normas_selenium.py`

---

### 2. **Correção do erro `StaleElementReferenceException`**
Implementamos uma lógica que captura o texto e o link de cada norma antes da navegação (`driver.get()`), e reabre a página inicial após cada extração para garantir estabilidade na coleta.

---

### 3. **Coletas armazenadas automaticamente**
Cada norma é salva em:
```
dados/textos/{nome-da-norma}.txt
```

---
	
## 📍 Próximos passos

- Executar o script de limpeza dos textos (`src/limpeza/limpa_textos.py`) para gerar arquivos limpos em `dados/textos_limpos/`
- Expandir o scraping para outras fontes jurídicas (Planalto, STJ, DOU, sites com modelos de petição etc.)
- Fragmentar o conteúdo e indexar com FAISS
- Conectar à LangChain para perguntas em linguagem natural

---




## Terceiro dia

# 📚 Previnfobot – Pipeline de Extração Inteligente

Este projeto realiza a extração, limpeza e preparação de documentos jurídicos (em `.pdf`, `.docx`, `.png`, entre outros), com foco em **organização eficiente e automação escalável** para futura indexação e integração com IA.

---

## ✅ O que foi feito hoje

### 1. **Correção de leitura de subpastas**
O script `extrai_e_limpa_drive.py` foi atualizado para **percorrer pastas recursivamente**, permitindo manter os documentos organizados por módulo, tema ou tipo, sem perder leitura.

### 2. **Tratamento de arquivos com falha**
Arquivos `.doc` (Word antigo) não eram suportados por `python-docx`. Optamos por:

- 📂 Criar um script (`converte_doc_para_docx.py`) que **automatiza a conversão de `.doc` para `.docx`** usando o Word do Windows
- ✔️ Implementar proteção contra travamentos e logs estruturados
- 📄 Para arquivos corrompidos ou não conversíveis, convertemos **manualmente para `.pdf` via Google Docs** como solução alternativa compatível

### 3. **Renomeador inteligente**
Criamos o `renomeador_doc_inteligente.py`, que:

- Localiza arquivos `.doc` com nomes ou caminhos problemáticos
- Gera cópias com nomes curtos e seguros (`doc_001_xyz.doc`)
- Organiza em uma pasta `dados/fontes_convertiveis/` para facilitar o processo

### 4. **Extração validada**
Rodamos com sucesso o `extrai_e_limpa_drive.py`, confirmando a extração dos textos em `.txt` para:
```
dados/textos_limpos/
```
Todos os arquivos `.pdf`, `.docx`, e imagens processadas com OCR foram transformados em texto limpo, pronto para uso com IA.

---

## 🎯 Por que fizemos isso hoje

- Garantir que **nenhum arquivo importante fosse perdido** por problemas de formato ou nome
- Ter um pipeline confiável, limpo e rastreável (com logs e relatórios)
- Preparar o terreno para a próxima etapa: **indexação vetorial com LangChain + FAISS**
- Evitar o retrabalho manual e criar uma estrutura **modular, escalável e automatizada**

---

## 🔜 Próximos passos sugeridos

- [ ] Criar índice vetorial dos textos com FAISS
- [ ] Integrar com LangChain para consultas semânticas
- [ ] Adicionar interface web ou API (FastAPI)

---

_Construído com consistência, estratégia e propósito. Bora transformar o jurídico com código! ⚖️💻_

# 📄 Revisor Visual de Textos - Previnfobot

Este aplicativo Streamlit foi desenvolvido para facilitar a revisão humana de textos processados pelo Previnfobot, permitindo comparações visuais entre arquivos originais (com ruído) e textos limpos.

---

## ✅ Funcionalidades Implementadas

### 🔍 1. Visualização lado a lado
- Mostra o **texto original com ruído** e o **texto limpo** de forma comparativa, usando duas colunas.
- Facilita a revisão humana e permite tomar decisões rapidamente.

### ✅ 2. Botão "Aceitar"
- Move o texto limpo da pasta `dados/textos_revisados` para `dados/textos_limpos`.
- Remove o texto original da pasta de pendentes.
- Registra a decisão em um log CSV com data/hora e nome do arquivo.

### 🗑️ 3. Botão "Recusar"
- Move o texto original para `dados/textos_descartados`.
- Remove o texto limpo, se existir.
- Também registra a decisão no log.

### 🗂️ 4. Estrutura de Pastas Automatizada
- Cria automaticamente as pastas `textos_limpos`, `textos_descartados` e `relatorios` se não existirem.

### 🧠 5. Log de Revisões
- As decisões são salvas em `relatorios/log_revisoes.csv` no seguinte formato:
  ```
  arquivo,data_hora,decisao
  exemplo.txt,2025-06-24 16:12:00,aceito
  ```

### ⚡ 6. Script de inicialização
- Criamos um `.bat` que ativa o ambiente virtual e roda o Streamlit com apenas um clique no atalho de desktop.

---

## 💡 Por que implementamos isso?

- **Agilidade**: revisar dezenas de textos manualmente era inviável sem interface visual.
- **Rastreabilidade**: o log garante que todas as decisões sejam registradas.
- **Produtividade**: agora o projeto tem um fluxo revisional claro, profissional e escalável.
- **Pronto para crescer**: já estamos preparando terreno para dashboards e análises dos dados revisados.

---

## 🔧 Como executar

1. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Instale as dependências:

   ```bash
   pip install streamlit
   ```

3. Execute com:

   ```bash
   streamlit run streamlit_apps/revisor_visual.py
   ```

---

## 🚀 Próximos passos sugeridos

- Criar um **painel de estatísticas** com dados do `log_revisoes.csv`
- Adicionar filtros por datas, status, nome de arquivos
- Implementar validação automatizada de texto limpo

---

# 📘 README – Sessão de Implementação com Teófilo (25 de Junho de 2025)

Este documento resume todas as implementações, melhorias e decisões que desenvolvemos hoje no projeto **Previnfobot**, com foco na automação da revisão de textos, melhoria da rastreabilidade e usabilidade da aplicação. 🔍🤖

---

## ✅ O que implementamos hoje

### 🔧 1. Revisão e ajuste do `.gitignore`
- Corrigimos o uso de `*.txt` (que excluía arquivos importantes) e passamos a ignorar apenas pastas dinâmicas específicas:  
  `dados/textos_pendentes/`, `dados/textos_revisados/` etc.
- Resultado: **controle mais seguro sobre o que entra no Git** e garantia de que arquivos realmente úteis são versionados.

---

### 📂 2. Recuperação de branch e commits perdidos
- Identificamos que os arquivos “sumiram” porque estavam em uma branch paralela.
- Usamos `git checkout extracao-textual`, validamos os arquivos, e fizemos `git push origin extracao-textual` seguido de um **pull request e merge** para `main`.
- Resultado: **código recuperado e unido com segurança à linha principal de desenvolvimento**.

---

### 📊 3. Criação do `painel_estatisticas.py`
- Interface Streamlit que mostra:
  - Quantidade de textos aceitos vs. descartados
  - Evolução temporal das decisões
- Permite uma **análise visual e interativa da produtividade** do revisor.

---

### 🧪 4. Validação automática da limpeza textual
- Adicionamos a função `validar_texto_limpo()` ao `revisor_visual.py`
  - Detecta ruído visual (como `...`, `###`, símbolos estranhos)
  - Impede o aceite de textos sem qualidade mínima
- Resultado: **garantia de consistência dos dados aprovados**

---

### 👁️ 5. Atualização do `revisor_visual.py`
- Interface de comparação entre original e limpo
- Decisões de aceitar ou recusar
- Registro em `log_revisoes.csv`
- ✅ Inclusão do botão para abrir o painel de execução (`central_pipeline.py`) diretamente

---

### 🧩 6. Criação do Painel Central – `central_pipeline.py`
- Interface Streamlit com botões para executar:
  - limpeza
  - extração
  - validação
  - geração de relatório
  - **ou a pipeline completa**
- Resultado: **centralização do controle da aplicação em um único painel**

---

### 🎛️ 7. Botões de acesso cruzado
- No `painel_estatisticas.py` e no `revisor_visual.py`, adicionamos:
  - Um botão `🎛️ Ir para Painel de Execução`
  - Isso abre `http://localhost:8501` se o painel estiver rodando

---

### 🖱️ 8. Criação do `.bat` de acesso rápido
- `inicia_painel_central.bat`:
  - Ativa o ambiente virtual
  - Roda automaticamente o painel `central_pipeline.py`


Com carinho,  
🤖 Desenvolvido com apoio do Copilot e ✊ dedicação de Teófilo


# 🧠 PrevInfoBot – Integração RAG Jurídica Previdenciária

Este repositório contém o pipeline modular do **PrevInfoBot**, um assistente jurídico previdenciário baseado em RAG (Retrieval-Augmented Generation) com GPT-4 + FAISS. Abaixo estão os componentes implementados e testados nesta fase.

---

## ✅ Funcionalidades implementadas

### 1. `indexa_com_faiss.py`
- Local: `src/indexacao/indexa_com_faiss.py`
- Função: carrega `.txt` de `dados/textos_limpos/`, fragmenta em chunks e indexa com FAISS usando embeddings da OpenAI.
- Melhoria: processamento em lotes para evitar erros de memória.
- Dependências: `langchain-openai`, `tiktoken`, `dotenv`.

### 2. `pergunta_ao_robo.py`
- Local: `src/rag_pipeline/pergunta_ao_robo.py`
- Fluxo:
  1. Carrega o índice FAISS
  2. Consulta via similaridade semântica
  3. GPT-4 responde com base no contexto encontrado
- Uso: interface de terminal que recebe a pergunta e retorna resposta estruturada.
- Melhorias:
  - Troca de `.run()` por `.invoke()`
  - Impressão elegante com `resposta["result"]` tratado

---

## ⚒️ Ferramentas utilizadas

| Ferramenta        | Finalidade                              |
|-------------------|------------------------------------------|
| LangChain         | Framework de RAG                         |
| LangChain Community & OpenAI | Conectores e LLMs via GPT-4          |
| FAISS             | Indexador vetorial                       |
| OpenAIEmbeddings  | Vetorização semântica                    |
| Streamlit         | Interface visual do pipeline de revisão  |
| Python `.env`     | Gestão de chaves com segurança           |

---

## 📂 Pastas envolvidas

- `dados/textos_pendentes/`: onde novos `.txt` devem ser colocados
- `scripts/limpa_textos_pendentes.py`: limpeza e padronização dos textos
- `dados/textos_revisados/`: arquivos limpos para revisão
- `streamlit_apps/revisor_visual.py`: permite aceitar ou descartar textos
- `dados/textos_limpos/`: base final que será vetorizada
- `dados/vetores/faiss_index/`: índice final salvo para consulta

---

## 🧪 Exemplo de uso

```bash
# Etapa 1 – Adicionar arquivo novo
→ Salvar em: dados/textos_pendentes/

# Etapa 2 – Limpeza
python scripts/limpa_textos_pendentes.py

# Etapa 3 – Revisão manual (opcional)
python -m streamlit run streamlit_apps/revisor_visual.py

# Etapa 4 – Indexar
python src/indexacao/indexa_com_faiss.py

# Etapa 5 – Perguntar ao robô
python src/rag_pipeline/pergunta_ao_robo.py
```

---

## 📌 Observações

- O `.env` deve conter a variável `OPENAI_API_KEY`
- O arquivo `.env` já está listado no `.gitignore`
- Com base na pergunta feita, o robô responde contextualizadamente
- Respostas sem dados retornam feedback seguro, sem inventar fatos


import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

CAMINHO_TEXTOS = "dados/textos_limpos"
CAMINHO_INDICE = "dados/vetores/faiss_index"

def carregar_textos(caminho):
    documentos = []
    for nome_arquivo in os.listdir(caminho):
        if nome_arquivo.endswith(".txt"):
            loader = TextLoader(os.path.join(caminho, nome_arquivo), encoding="utf-8")
            documentos.extend(loader.load())
    return documentos

def fragmentar_textos(documentos):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documentos)

def indexar_em_lotes(docs_fragmentados, lote_tamanho=20):  # 🔧 Lote reduzido para mais segurança
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    index_geral = None

    total_lotes = len(docs_fragmentados) // lote_tamanho + 1
    print(f"\n📦 Total de lotes: {total_lotes}")

    for i in range(0, len(docs_fragmentados), lote_tamanho):
        lote = docs_fragmentados[i:i + lote_tamanho]
        print(f"🔧 Processando lote {i // lote_tamanho + 1}/{total_lotes}")
        index_parcial = FAISS.from_documents(lote, embeddings)

        if index_geral:
            index_geral.merge_from(index_parcial)
        else:
            index_geral = index_parcial

    os.makedirs(CAMINHO_INDICE, exist_ok=True)
    index_geral.save_local(CAMINHO_INDICE)
    print(f"\n✅ Índice salvo com sucesso em: {CAMINHO_INDICE}")

if __name__ == "__main__":
    print("📥 Carregando textos...")
    docs = carregar_textos(CAMINHO_TEXTOS)
    print(f"✂️ Fragmentando {len(docs)} documentos...")
    fragments = fragmentar_textos(docs)
    print(f"🔎 Indexando {len(fragments)} fragmentos...")
    indexar_em_lotes(fragments)

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()

CAMINHO_INDICE = "dados/vetores/faiss_index"

def carregar_robô_rag(k=4):
    """
    Carrega o índice vetorial FAISS e retorna a cadeia RAG para perguntas jurídicas.
    """
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    faiss_index = FAISS.load_local(
        CAMINHO_INDICE,
        embeddings,
        allow_dangerous_deserialization=True
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(
            model_name="gpt-4",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        chain_type="stuff",
        retriever=faiss_index.as_retriever(search_type="similarity", search_kwargs={"k": k})
    )
    return qa_chain

def responder_pergunta(pergunta: str) -> str:
    """
    Executa o fluxo RAG: busca nos vetores + consulta ao modelo GPT.
    """
    chain = carregar_robô_rag()
    resposta = chain.invoke(pergunta)
    return resposta

if __name__ == "__main__":
    pergunta = input("🔎 Faça sua pergunta jurídica: ")
    resposta = responder_pergunta(pergunta)

    # Tratamento elegante da resposta
    if isinstance(resposta, dict) and "result" in resposta:
        print(f"\n🤖 Resposta:\n{resposta['result']}")
    else:
        print(f"\n🤖 Resposta:\n{resposta}")

import os
import win32com.client
from datetime import datetime

PASTA = "dados/fontes_convertiveis"  # NOVA pasta com nomes curtos
PASTA_LOG = "logs"
CAMINHO_LOG_ERROS = os.path.join(PASTA_LOG, "erros_conversao.txt")

os.makedirs(PASTA_LOG, exist_ok=True)

def log_erro(msg):
    with open(CAMINHO_LOG_ERROS, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def converter_doc_para_docx(caminho_doc):
    word = None
    try:
        if len(caminho_doc) > 255:
            msg = f"[LONGO] {caminho_doc}"
            print(f"⚠️ Caminho longo: {msg}")
            log_erro(msg)
            return

        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(caminho_doc)
        novo_caminho = caminho_doc + "x"
        doc.SaveAs(novo_caminho, FileFormat=16)
        doc.Close()
        print(f"✔️ Convertido: {os.path.basename(caminho_doc)}")
    except Exception as e:
        msg = f"[ERRO] {caminho_doc}: {e}"
        print(f"❌ {msg}")
        log_erro(msg)
    finally:
        try:
            if word:
                word.Quit()
        except Exception as fechar_erro:
            print(f"⚠️ Erro ao fechar o Word: {fechar_erro}")
            log_erro(f"[FALHA AO FECHAR WORD] {caminho_doc}: {fechar_erro}")

def main():
    with open(CAMINHO_LOG_ERROS, "w", encoding="utf-8") as f:
        f.write(f"Relatório de erros - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    print("🔍 Convertendo arquivos da nova pasta renomeada...\n")
    for raiz, _, arquivos in os.walk(PASTA):
        for nome in arquivos:
            if nome.lower().endswith(".doc") and not nome.lower().endswith(".docx"):
                caminho_completo = os.path.join(raiz, nome)
                converter_doc_para_docx(caminho_completo)

    print(f"\n📋 Conversão concluída. Relatório salvo em: {CAMINHO_LOG_ERROS}")

if __name__ == "__main__":
    main()

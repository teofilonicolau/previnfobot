import os
import shutil
from pathlib import Path
from datetime import datetime

ORIGEM = "dados/fontes_extra"
DESTINO = "dados/fontes_convertiveis"
RELATORIO = "logs/renomeados.txt"

os.makedirs(DESTINO, exist_ok=True)
os.makedirs("logs", exist_ok=True)

def nome_simplificado(base, indice):
    nome_curto = base.lower().replace(" ", "_").replace("ç", "c").replace("ã", "a").replace("õ", "o")
    nome_curto = ''.join(c for c in nome_curto if c.isalnum() or c == "_")
    return f"doc_{indice:03}_{nome_curto}.doc"

def main():
    contador = 1
    with open(RELATORIO, "w", encoding="utf-8") as log:
        log.write(f"Relatório de renomeação - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for raiz, _, arquivos in os.walk(ORIGEM):
            for nome in arquivos:
                if nome.lower().endswith(".doc") and not nome.lower().endswith(".docx"):
                    caminho_original = os.path.join(raiz, nome)
                    try:
                        nome_curto = nome_simplificado(Path(nome).stem, contador)
                        caminho_destino = os.path.join(DESTINO, nome_curto)
                        shutil.copy2(caminho_original, caminho_destino)

                        log.write(f"{caminho_original}  →  {caminho_destino}\n")
                        print(f"📂 Copiado e renomeado: {nome_curto}")
                        contador += 1
                    except Exception as e:
                        log.write(f"❌ Falha ao copiar {caminho_original}: {e}\n")

    print(f"\n✅ Renomeação concluída. Verifique o relatório em: {RELATORIO}")

if __name__ == "__main__":
    main()

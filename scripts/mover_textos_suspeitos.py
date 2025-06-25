import os
import shutil
import csv

CSV_ERROS = "relatorios/extracoes_com_erro.csv"
PASTA_ORIGEM = "dados/textos_limpos"
PASTA_DESTINO = "dados/textos_pendentes"

os.makedirs(PASTA_DESTINO, exist_ok=True)

with open(CSV_ERROS, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        nome_arquivo = row["arquivo"]
        origem = os.path.join(PASTA_ORIGEM, nome_arquivo)
        destino = os.path.join(PASTA_DESTINO, nome_arquivo)
        if os.path.exists(origem):
            shutil.move(origem, destino)
            print(f"➡️  Movido: {nome_arquivo}")
        else:
            print(f"⚠️  Não encontrado: {nome_arquivo}")

print("\n✅ Todos arquivos suspeitos foram movidos para dados/textos_pendentes/")

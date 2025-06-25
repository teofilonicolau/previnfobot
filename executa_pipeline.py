import os
import argparse
from datetime import datetime

def run(script, nome_amigavel=""):
    print(f"\n▶️ Executando: {nome_amigavel or script}")
    status = os.system(f"python {script}")
    if status != 0:
        print(f"❌ Erro ao executar {script}")
    return status

def notificar_sucesso(total_erros=0):
    print("\n📬 Simulação de notificação:")
    if total_erros == 0:
        print("✅ Pipeline finalizado com sucesso. Nenhum erro grave encontrado.")
    else:
        print(f"⚠️ Pipeline finalizado com {total_erros} arquivos suspeitos detectados.")
    # Aqui você poderia integrar com um webhook, e-mail, Slack etc.

def main():
    parser = argparse.ArgumentParser(description="Executa o pipeline completo com base na pasta de textos.")
    parser.add_argument("--pasta_textos", default="dados/textos_limpos", help="Pasta onde estão os arquivos .txt")
    args = parser.parse_args()

    print(f"\n🔧 Iniciando pipeline ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"📂 Pasta de entrada: {args.pasta_textos}")

    os.environ["PASTA_TXT"] = args.pasta_textos

    run("scripts/extrai_e_limpa_drive.py", "Extração e limpeza dos arquivos")
    run("scripts/gera_relatorio_csv.py", "Geração de relatório .csv")
    run("scripts/valida_textos.py", "Validação de conteúdo textual")

    # Leitura opcional do número de arquivos com erro
    erro_path = "relatorios/extracoes_com_erro.csv"
    total_erros = 0
    if os.path.exists(erro_path):
        with open(erro_path, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            total_erros = len(linhas) - 1  # cabeçalho

    notificar_sucesso(total_erros)

if __name__ == "__main__":
    main()

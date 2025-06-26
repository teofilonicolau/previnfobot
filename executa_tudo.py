import os
import subprocess

def executar(titulo, comando):
    print(f"\n🔹 {titulo}...")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode == 0:
        print("✅ Sucesso!")
    else:
        print("❌ Falhou!")

if __name__ == "__main__":
    print("🚀 Iniciando pipeline completa do Previnfobot...")

    executar("Limpando textos pendentes", "python scripts/limpa_textos_pendentes.py")
    executar("Executando extração e pré-processamento", "python scripts/extrai_e_limpa_drive.py")
    executar("Validando textos limpos", "python scripts/valida_textos.py")
    executar("Gerando relatórios finais", "python scripts/gera_relatorio_csv.py")

    print("\n🎉 Pipeline finalizada com sucesso!")

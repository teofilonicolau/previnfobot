from pathlib import Path
import re

PASTA_ORIGEM = Path(__file__).resolve().parents[2] / "dados" / "textos"
PASTA_LIMPA = Path(__file__).resolve().parents[2] / "dados" / "textos_limpos"
PASTA_LIMPA.mkdir(parents=True, exist_ok=True)

arquivos = list(PASTA_ORIGEM.glob("*.txt"))

def limpar(texto):
    texto = re.sub(r'[ \t]+', ' ', texto)
    texto = re.sub(r'\n\s*\n', '\n', texto)
    texto = texto.strip()

    linhas = texto.splitlines()
    limpas = []
    for linha in linhas:
        l = linha.strip().lower()
        if l.startswith("ministério") or l.startswith("portaria") or l in ["voltar", "imprimir"]:
            continue
        limpas.append(linha)
    return "\n".join(limpas)

if not arquivos:
    print("Nenhum arquivo .txt encontrado para limpar.")
else:
    for arquivo in arquivos:
        with open(arquivo, "r", encoding="utf-8") as f:
            bruto = f.read()
        limpo = limpar(bruto)
        destino = PASTA_LIMPA / arquivo.name
        with open(destino, "w", encoding="utf-8") as f:
            f.write(limpo)
        print(f"✅ Limpo e salvo em: {destino.name}")

print("🧼 Limpeza concluída.")

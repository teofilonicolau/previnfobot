import re

def limpar_texto(texto: str) -> str:
    texto = re.sub(r"[^\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]", "", texto)  # remove símbolos
    texto = re.sub(r"\s+", " ", texto)  # substitui múltiplos espaços por um só
    return texto.strip()

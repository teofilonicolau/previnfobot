import hashlib

def gerar_hash_sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()

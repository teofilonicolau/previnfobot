from app.services.hash_utils import gerar_hash_sha256

def test_hash_sha256_valido():
    conteudo = "jurisprudência clara e objetiva"
    resultado = gerar_hash_sha256(conteudo)  # agora passa só a string
    assert len(resultado) == 64

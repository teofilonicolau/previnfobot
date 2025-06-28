from app.services.limpeza import limpar_texto

def test_remover_palavras_invalidas():
    texto = "Previdência 📄 é essencial, mas @123 textos vêm com ruídos."
    esperado = "Previdência é essencial mas 123 textos vêm com ruídos"
    assert limpar_texto(texto) == esperado



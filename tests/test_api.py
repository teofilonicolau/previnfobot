from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_consulta_basica():
    resposta = client.post("/consultar", json={"pergunta": "Quais são os requisitos para aposentadoria por idade?"})
    assert resposta.status_code == 200
    assert "resposta" in resposta.json()

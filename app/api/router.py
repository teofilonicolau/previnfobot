# app/api/router.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import responder_pergunta  # sua lógica já criada

router = APIRouter()

class ConsultaRequest(BaseModel):
    pergunta: str

@router.post("/consultar")
def consultar(req: ConsultaRequest):
    resposta = responder_pergunta(req.pergunta)
    return {"resposta": resposta}

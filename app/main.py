# app/main.py

from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="⚖️ Previnfobot API",
    description=(
        "Robô jurídico especializado em Direito Previdenciário, "
        "com integração RAG (GPT + vetores), "
        "pronto para consultas, petições e pareceres automatizados.\n\n"
        "Desenvolvido por  Teófilo Nicolau, com arquitetura modular, "
        "boas práticas e visão de escalabilidade para múltiplos ramos do Direito."
    ),
    version="1.0.0",
    contact={
        "name": "Time Previnfobot",
        "url": "https://github.com/seuusuario/previnfobot-correto",  # ajuste se quiser
        "email": "contato@seudominio.com"
    },
    openapi_tags=[
        {
            "name": "Consultas Jurídicas",
            "description": "Consulta com inteligência artificial baseada em jurisprudência e normas indexadas"
        }
    ]
)

app.include_router(router, tags=["Consultas Jurídicas"])

from fastapi import FastAPI
from .routers import router
from .database import engine
from .database import Base

app = FastAPI()

# Criação das tabelas no banco (caso ainda não existam)
Base.metadata.create_all(bind=engine)

# Inclui as rotas do arquivo routers.py
app.include_router(router)



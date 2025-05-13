from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from datetime import datetime
from .database import Base


# Definindo o modelo de dados
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    disponivel = Column(Boolean, nullable=False)
    categoria = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
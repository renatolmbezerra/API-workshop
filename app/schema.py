# schema.py
from pydantic import BaseModel, PositiveFloat
from typing import Optional
from datetime import datetime

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    disponivel: bool
    categoria: str

class ProdutoCreate(ProdutoBase):
    pass

class ProdutosSchema(ProdutoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[PositiveFloat] = None
    disponivel: Optional[bool] = None
    categoria: Optional[str] = None
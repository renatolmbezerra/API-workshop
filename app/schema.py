from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    disponivel: bool
    categoria: str

    class Config:
        orm_mode = True
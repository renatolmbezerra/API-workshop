from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutoCreate, ProdutosSchema, ProdutoUpdate
from .database import get_session
from .model import Produto

router = APIRouter()


@router.get("/")
def ola_mundo():
    """
    Função que retorna um dicionário com a chave "Ola" e o valor "Mundo".
    :return: Dicionário com a chave "Ola" e o valor "Mundo".
    """
    return {"Olá": "Mundo"}


@router.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_session)):
    """
    Função que retorna uma lista de produtos.
    """
    return db.query(Produto).all() # SELECT * FROM produtos


@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def obter_produto(produto_id: int, db: Session = Depends(get_session)):   
    """
    Função que retorna um produto específico com base no ID.
    :param produto_id: ID do produto a ser retornado.
    :return: Produto correspondente ao ID fornecido.
    """
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto 
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.post("/produtos", response_model=ProdutosSchema)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_session)):
    """
    Função que cria um novo produto.
    :param produto: Produto a ser criado.
    :return: Produto criado.
    """
    novo_produto = Produto(**produto.model_dump())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
def deletar_produto(produto_id: int, db: Session = Depends(get_session)):
    """
    Função que deleta um produto específico com base no ID.
    :param produto_id: ID do produto a ser deletado.
    :return: Produto deletado.
    """
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    
@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_session)):
    """
    Função que atualiza um produto específico com base no ID.
    :param produto_id: ID do produto a ser atualizado.
    :param produto: Produto com os novos dados.
    """
    # Buscar o produto no banco
    produto_db = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto_db is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Atualizar os campos apenas se forem fornecidos
    if produto.nome is not None:
        produto_db.nome = produto.nome
    if produto.descricao is not None:
        produto_db.descricao = produto.descricao
    if produto.preco is not None:
        produto_db.preco = produto.preco
    if produto.disponivel is not None:
        produto_db.disponivel = produto.disponivel
    if produto.categoria is not None:
        produto_db.categoria = produto.categoria

    # Commit da transação e retorno do produto atualizado
    db.commit()
    db.refresh(produto_db)
    return produto_db
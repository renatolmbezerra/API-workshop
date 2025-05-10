from fastapi import FastAPI
from app.schema import ProdutosSchema
from app.data import Produtos

app = FastAPI()
Lista_de_produtos = Produtos()

@app.get("/")
def ola_mundo():
    """
    Função que retorna um dicionário com a chave "Ola" e o valor "Mundo".
    :return: Dicionário com a chave "Ola" e o valor "Mundo".
    """
    return {"Olá": "Mundo"}

@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    """
    Função que retorna uma lista de produtos.
    :return: Lista de produtos.
    """
    return Lista_de_produtos.listar_produtos()


@app.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def obter_produto(produto_id: int):
    """
    Função que retorna um produto específico com base no ID.
    :param produto_id: ID do produto a ser retornado.
    :return: Produto correspondente ao ID fornecido.
    """
    return Lista_de_produtos.obter_produto(produto_id)


@app.post("/produtos", response_model=ProdutosSchema)
def criar_produto(produto: ProdutosSchema):
    """
    Função que cria um novo produto.
    :param produto: Produto a ser criado.
    :return: Produto criado.
    """
    return Lista_de_produtos.criar_produto(produto)

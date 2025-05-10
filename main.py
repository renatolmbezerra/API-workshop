from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone", 
        "descricao": "Smartphone com tela de 6 polegadas e 128GB de armazenamento.",
        "preco": 1999.99,
        "disponivel": True,
        "categoria": "eletronicos",
    },
    {
        "id": 2,
        "nome": "Notebook", 
        "descricao": "Um computador portátil com 16GB de RAM e 512GB de SSD.",
        "preco": 4999.99,
        "disponivel": False,
        "categoria": "eletronicos",
    },
    {
        "id": 3,
        "nome": "Cadeira Gamer", 
        "descricao": "Cadeira ergonômica para jogos com apoio para os braços.",
        "preco": 899.99,
        "disponivel": True,
        "categoria": "moveis",
    },
    {
        "id": 4,
        "nome": "Monitor", 
        "descricao": "Monitor de 27 polegadas com resolução 4K.",
        "preco": 2499.99,
        "disponivel": True,
        "categoria": "eletronicos",
    },
]

@app.get("/")
def ola_mundo():
    """
    Função que retorna um dicionário com a chave "Ola" e o valor "Mundo".
    :return: Dicionário com a chave "Ola" e o valor "Mundo".
    """
    return {"Olá": "Mundo"}

@app.get("/produtos")
def listar_produtos():
    """
    Função que retorna uma lista de produtos.
    :return: Lista de produtos.
    """
    return produtos


@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    """
    Função que retorna um produto específico com base no ID.
    :param produto_id: ID do produto a ser retornado.
    :return: Produto correspondente ao ID fornecido.
    """
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"Status": 404, "erro": "Produto não encontrado"}   
